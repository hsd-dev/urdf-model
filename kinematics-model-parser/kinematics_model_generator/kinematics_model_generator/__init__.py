#!/usr/bin/env python3

import argparse
from bigtree import find, findall, find_attr, list_to_tree, Node, print_tree, tree_to_dict, tree_to_dot
import json
from json import JSONEncoder
from jsonschema import validate
import os
import pyecore
import requests
import ruamel.yaml
from ruamel.yaml.error import YAMLError
import sys
import xml.etree.ElementTree as ET
import yaml

import kinematics_model_generator
from kinematics_model_generator.cli import process_args
from kinematics_model_generator.utils.xml_helper import *
from kinematics_model_generator.kinematics.urdf import *
from kinematics_model_generator.kinematics.component import *

from ament_index_python.packages import get_package_share_directory
import rclpy


# xtext grammar expects specific sequence of features
attr_seq = {'Robot': ['name', 'version', 'link', 'joint'],
            'Component': ['name', 'version', 'category', 'gitRepo', 'group', 'link', 'joint', 'group'],
            'GitRepo': ['distro', 'repo', 'branch', 'package', 'version'],
            'Group': ['name', 'base_link', 'end_link'],
            'Macro': ['name', 'parameters', 'link', 'joint', 'condition'],
            'Block': ['link', 'joint'],
            'Condition': ['param', 'if_', 'unless'],
            'Link': ['name', 'inertial', 'visual', 'collision'],
            'Inertial': ['origin', 'mass', 'inertia'],
            'Visual': ['origin', 'geometry'],
            'Collision': ['origin', 'geometry'],
            'Joint': ['name', 'type', 'parent', 'child', 'origin', 'axis', 'limit']}

# if the EString is defined as rule in xtext, it cannot have quotes
is_rule = {'Joint': ['type'], 'Component': ['category']}


# dump string with double quotes
class quoted(str):
    pass


def quoted_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')


yaml = ruamel.yaml.YAML()
yaml.representer.add_representer(quoted, quoted_presenter)

# PyYAML
# yaml.add_representer(quoted, quoted_presenter)


def insert_component(name, dot_trees, model_dict):
    url = 'http://0.0.0.0:5500/add'

    files = {
        'dot_trees': (None, json.dumps(dot_trees), 'application/json'),
        'model': (None, json.dumps(model_dict), 'application/json')
    }

    r = requests.post('http://0.0.0.0:5500/add', files=files)
    print(f"Status Code: {r.status_code}")


def create_tree(component):
    # prepare tree based on joints

    link_names = []
    for link in component.link:
        link_names.append(link.name)

    joint_data = []
    for joint in component.joint:
        joint_data.append((joint.name, joint.parent.link, joint.child.link))

    # Create a dictionary to store nodes by name for easy access
    nodes_by_name = {}

    # Create nodes for each joint and populate the nodes_by_name dictionary
    for joint_name, parent_name, child_name in joint_data:
        if parent_name not in link_names:
            raise Exception(parent_name + ' parent in joint ' +
                            joint_name + ' does not exist. Not a valid tree')

        if child_name not in link_names:
            raise Exception(child_name + ' child in joint ' +
                            joint_name + ' does not exist. Not a valid tree')

        parent_node = nodes_by_name.get(parent_name, Node(parent_name))
        parent_link = find_link(component, joint.parent.link)
        parent_node.is_rigid = is_link_rigid(parent_link)

        child_node = nodes_by_name.get(child_name, Node(child_name))
        child_link = find_link(component, joint.child.link)
        child_node.is_rigid = is_link_rigid(child_link)

        child_node.parent = parent_node

        nodes_by_name[parent_name] = parent_node
        nodes_by_name[child_name] = child_node

    # Find the root node
    root_node = None
    for node in nodes_by_name.values():
        if not node.parent:
            root_node = node
            break

    return root_node


def find_link(component, link_name):
    for link in component.link:
        if link.name == link_name:
            return link

    return None


def is_link_rigid(link):
    if link and link.inertial:
        return True
    return False


def parse_args(args):
    arg_parser = argparse.ArgumentParser(
        description='Options for kinematics parser')

    # Add the arguments
    arg_parser.add_argument('urdf',
                            type=str,
                            help='URDF file to be parsed')
    arg_parser.add_argument('output',
                            type=str,
                            help='output file in YAML format')

    args = arg_parser.parse_args(args)
    return args.urdf, args.output


def write_to_file(filename, data):
    with open(filename, 'w') as f:
        yaml.dump(data, f)


def conv_str_to_type(elem, name, val_str):
    try:
        val_type = str(elem.eClass.findEStructuralFeature(name).eType)
    except Exception as e:
        print('EClass ' + elem.eClass.name + ' has no attribute ' + name)
        raise e
    if 'float' in val_type:
        if elem.eGet(name).__class__ == pyecore.valuecontainer.EList:
            val_list = [float(x) for x in val_str.split()]
            return val_list
        return float(val_str)
    elif 'int' in val_type:
        if elem.eGet(name).__class__ == pyecore.valuecontainer.EList:
            val_list = [int(x) for x in val_str.split()]
            return val_list
        return int(val_str)
    elif 'str' in val_type:
        # if the attribute is a rule, return string without quotes
        if elem.eClass.name in is_rule:
            attributes = is_rule[elem.eClass.name]
            if name in attributes:
                return val_str
        return quoted(val_str)
    return val_str


# convert list into flow-style (default is block style)
def FSlist(l):
    from ruamel.yaml.comments import CommentedSeq
    cs = CommentedSeq(l)
    cs.fa.set_flow_style()
    return cs


# Convert arbitrary EObject to YAML
def eobj_to_dict(eobj):
    model_dict = dict()
    attr_dict = dict()
    # loop over all attributes of the EObject
    attributes = None
    if eobj.eClass.name in attr_seq:
        attributes = attr_seq[eobj.eClass.name]
    else:
        attributes = dir(eobj)

    for attr in attributes:
        # get the value of that attribute
        attr_value = eobj.eGet(attr)
        if attr_value is not None:
            if type(attr_value) == pyecore.valuecontainer.EOrderedSet:
                # if the attribute is EOrderedSet,
                # convert it into list of dicts
                attr_set = dict()
                attr_elems = list()
                # loop through each elem of the ordered set
                # and convert it into a dict
                for attr_elem in attr_value:
                    # if type(attr_elem) == pyecore.ecore.EObject:
                    elem_dict = eobj_to_dict(attr_elem)
                    attr_elems.append(list(elem_dict.values())[0])
                    # else:
                    #     attr_elems.append(attr_elem)
                if len(attr_elems) > 0:
                    attr_set[attr] = attr_elems
                    attr_dict.update(attr_set)
            elif type(attr_value) == pyecore.valuecontainer.EList:
                # if the attribute is EList,
                # convert it into list of dicts
                attr_set = dict()
                attr_elems = list()
                # loop through each elem of the ordered set
                # and convert it into a dict
                for attr_elem in attr_value:
                    if type(attr_elem) == pyecore.ecore.EObject:
                        elem_dict = eobj_to_dict(attr_elem)
                        attr_elems.append(list(elem_dict.values())[0])
                    else:
                        attr_elems.append(attr_elem)
                if len(attr_elems) > 0:
                    attr_set[attr] = FSlist(attr_elems)
                    attr_dict.update(attr_set)
            # TODO: this is not generic, won't work for other meta-models
            elif 'kinematics_model_generator.kinematics' in str(type(attr_value)):
                elem_dict = eobj_to_dict(attr_value)
                attr_set = dict()
                attr_set[attr] = list(elem_dict.values())[0]
                attr_dict.update(attr_set)
            else:
                if type(attr_value) == pyecore.ecore.EEnumLiteral:
                    attr_dict[attr] = eobj.eGet(attr).value
                else:
                    attr_dict[attr] = eobj.eGet(attr)

    model_dict[eobj.eClass.__name__.lower()] = attr_dict
    return model_dict


# validates the model against a Json schema
def validate_model(model_str):
    # get Json schema from file
    package_share_directory = get_package_share_directory(
        'kinematics_model_generator')
    schema_path = os.path.join(
        package_share_directory, 'resources', 'kinematics_schema.json')
    schema_file = open(schema_path)
    schema = json.load(schema_file)

    try:
        model = yaml.load(model_str)
        validate(instance=model, schema=schema)
    except YAMLError as exc:
        print(exc.problem)


# parse XML dom object and populate the EObject 'parent'
# This function expects there is a one-to-one mapping between
# the xml document and the meta-model of the EObject
def parse_elem(node, parent):
    node = node.firstChild
    while node:
        next = node.nextSibling

        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            elem = get_eobj_from_attr(parent, node.tagName)

            for name, value in node.attributes.items():
                conv_val = conv_str_to_type(elem, name, value)

                if type(conv_val) == list:
                    elem_at = getattr(elem, name)
                    elem_at.extend(conv_val)
                else:
                    setattr(elem, name, conv_val)

            attr = getattr(parent, node.tagName)
            if type(attr) == pyecore.valuecontainer.EOrderedSet:
                attr.add(elem)
            else:
                setattr(parent, node.tagName, elem)

            parse_elem(node, elem)
        node = next


def get_root_elem(node):
    while node:
        next = node.nextSibling
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            cls = globals()[node.tagName.capitalize()]
            root = cls()

            for name, value in node.attributes.items():
                setattr(root, name, value)

            return root, node

        node = next


def dict_to_eobj(data, eobject):
    for key, value in data.items():
        if isinstance(value, dict):
            if hasattr(eobject, key):
                sub_eobject = get_eobj_from_attr(eobject, key)
                setattr(eobject, key, sub_eobject)
                dict_to_eobj(value, sub_eobject)
        elif isinstance(value, list):
            if hasattr(eobject, key):
                sub_eobject = getattr(eobject, key)
                sub_eobject.extend(value)
        else:
            setattr(eobject, key, value)


def get_eobj_from_attr(eobject, key):
    elem_attr = None
    for attr in eobject.eClass.eAttributes:
        if key == attr._name:
            elem_attr = attr
            break
    if not elem_attr:
        for attr in eobject.eClass.eReferences:
            if key == attr._name:
                elem_attr = attr
                break

    try:
        elem = elem_attr.eType.__call__()
    except Exception as e:
        raise e

    return elem


def convert_urdf_component(robot):
    component = Component()
    component.name = quoted(robot.name)
    component.version = robot.version

    # The following code is unpredictable
    # ---
    # for joint in robot.joint:
    #     component.joint.append(joint)
    # ---
    # the for-loop does not complete for all joint in robot
    # So the temp strategy is to create a dict from eobj
    # and convert is back into a new eobject and then append
    # that to component

    for joint in robot.joint:
        joint_dict = eobj_to_dict(joint)
        j = Joint()
        dict_to_eobj(joint_dict['joint'], j)
        component.joint.append(j)

    for link in robot.link:
        link_dict = eobj_to_dict(link)
        l = Link()
        dict_to_eobj(link_dict['link'], l)
        component.link.append(l)

    return component


def parse_urdf(insput_file_str=None, input_file_name=None, **kwargs):
    # urdf_file, output_file = parse_args(sys.argv[1:])

    doc = parse(insput_file_str, input_file_name)
    root, node = get_root_elem(doc.firstChild)
    parse_elem(node, root)

    # 'root' at this point is a populated 'Robot' object that can be used
    # in a python application

    # convert URDF to component model
    # Component model is very similar to URDF,
    # except that it has additional attributes like
    # group (useful for MoveIt!), connection points (useful for composition)
    component = convert_urdf_component(root)

    gitRepo = GitRepo()
    gitRepo.distro = quoted(kwargs['distro'])
    gitRepo.repo = quoted(kwargs['repo'])
    gitRepo.branch = quoted(kwargs['branch'])
    gitRepo.package = quoted(kwargs['package'])
    gitRepo.version = quoted(kwargs['version'])

    component.gitRepo = gitRepo

    if 'category' in kwargs:
        component.category = kwargs['category']

    component_tree = create_tree(component)
    tree_dict = {}
    try:
        print_tree(component_tree)
        tree_dict[component.name] = tree_to_dict(component_tree)
    except Exception as e:
        print(e)

    component_dict = eobj_to_dict(component)
    write_to_file(kwargs['output'], component_dict)

    if 'push_to_db' in kwargs and kwargs['push_to_db']:
        print('inserting component ' + component.name + ' in ')
        insert_component(component.name,
                        dot_trees=tree_dict,
                        model_dict=component_dict)
