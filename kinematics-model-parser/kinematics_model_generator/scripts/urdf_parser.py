#!/usr/bin/env python3

import argparse
import json
from json import JSONEncoder
from jsonschema import validate
import os
import pyecore
import sys
import xml.etree.ElementTree as ET
import yaml

from kinematics_model_generator.utils.xml_helper import *
from kinematics_model_generator.kinematics.urdf import *
from kinematics_model_generator.kinematics.component import *

from ament_index_python.packages import get_package_share_directory
import rclpy


# xtext grammar expects specific sequence of features
attr_seq = {'Robot': ['name', 'version', 'link', 'joint'],
            'Component': ['name', 'version', 'link', 'joint', 'group'],
            'GitRepo': ['raw_file_url', 'repo', 'package', 'version'],
            'Macro': ['name', 'parameters', 'link', 'joint', 'condition'],
            'Block': ['link', 'joint'],
            'Condition': ['param', 'if_', 'unless'],
            'Link': ['name', 'inertial', 'visual', 'collision'],
            'Inertial': ['origin', 'mass', 'inertia'],
            'Visual': ['origin', 'geometry'],
            'Collision': ['origin', 'geometry'],
            'Joint': ['name', 'type', 'parent', 'child', 'origin', 'axis', 'limit']}

# if the EString is defined as rule in xtext, it cannot have quotes
is_rule = {'Joint': ['type']}


# dump string with double quotes
class quoted(str):
    pass


def quoted_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')


yaml.add_representer(quoted, quoted_presenter)


def insert_component(name, category, raw_file_url, repo,
                     package, version, dot_trees, model_dict):
    url = 'http://127.0.0.1:5000/add'
    component = {
        "name": name,
        "category": category,
        "raw_file_url": raw_file_url,
        "repo": repo,
        "package": package,
        "version": version
    }

    trees = {}
    for name, dot in dot_trees.items():
        trees[name] = dot

    files = {
        'json': (None, json.dumps(component), 'application/json'),
        'dot_trees': (None, json.dumps(trees), 'application/json'),
        'model': (None, json.dumps(model_dict), 'application/json')
    }

    r = requests.post('http://127.0.0.1:5000/add', files=files)
    print(f"Status Code: {r.status_code}")


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


def write_to_file(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()


def conv_str_to_type(elem, name, val_str):
    try:
        val_type = str(elem.eClass.findEStructuralFeature(name).eType)
    except Exception as e:
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
                    attr_set[attr] = attr_elems
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
        model = yaml.safe_load(model_str)
        validate(instance=model, schema=schema)
    except yaml.YAMLError as exc:
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
    component.name = robot.name
    component.version = robot.version
    
    for joint in robot.joint:
        component.joint.append(joint)

    for link in robot.link:
        component.link.append(link)

    return component

def main():
    urdf_file, output_file = parse_args(sys.argv[1:])

    doc = parse(None, urdf_file)
    root, node = get_root_elem(doc.firstChild)
    parse_elem(node, root)

    # 'root' at this point is a populated 'Robot' object that can be used
    # in a python application

    model_str = yaml.dump(eobj_to_dict(
        root), default_flow_style=False, sort_keys=False)

    validate_model(model_str)

    # convert URDF to component model
    # Component model is very similar to URDF,
    # except that it has additional attributes like
    # group (useful for MoveIt!), connection points (useful for composition)
    component = convert_urdf_component(root)
    component_str = yaml.dump(eobj_to_dict(
        component), default_flow_style=False, sort_keys=False)
    write_to_file(output_file, component_str)


if __name__ == "__main__":
    main()
