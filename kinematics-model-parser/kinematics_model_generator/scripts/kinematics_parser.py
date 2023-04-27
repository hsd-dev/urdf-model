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
from kinematics_model_generator.kinematics import *

from ament_index_python.packages import get_package_share_directory
import rclpy


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


# Convert arbitrary EObject to YAML
def eobj_to_dict(eobj):
    model_dict = dict()
    attr_dict = dict()
    # loop over all attributes of the EObject
    for attr in dir(eobj):
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
                    elem_dict = eobj_to_dict(attr_elem)
                    attr_elems.append(list(elem_dict.values())[0])
                attr_set[attr] = attr_elems
                attr_dict.update(attr_set)
            # TODO: this is not generic, won't work for other meta-models
            elif 'kinematics_model_generator.kinematics' in str(type(attr_value)):
                elem_dict = eobj_to_dict(attr_value)
                attr_set = dict()
                attr_set[attr] = list(elem_dict.values())[0]
                attr_dict.update(attr_set)
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
            elem_attr = None
            for attr in parent.eClass.eAttributes:
                if node.tagName == attr._name:
                    elem_attr = attr
                    break
            if not elem_attr:
                for attr in parent.eClass.eReferences:
                    if node.tagName == attr._name:
                        elem_attr = attr
                        break

            elem = elem_attr.eType.__call__()

            for name, value in node.attributes.items():
                setattr(elem, name, value)

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


def main():
    urdf_file, output_file = parse_args(sys.argv[1:])

    doc = parse(None, urdf_file)
    root, node = get_root_elem(doc.firstChild)
    parse_elem(node, root)

    # 'root' at this point is a populated 'Robot' object that can be used 
    # in a python application

    model_str = yaml.dump(eobj_to_dict(root), default_flow_style=False)

    validate_model(model_str)
    write_to_file(output_file, model_str)


if __name__ == "__main__":
    main()
