#!/usr/bin/env python3

from bigtree import find, findall, find_attr, list_to_tree, Node, print_tree, tree_to_dict, tree_to_dot
from collections import OrderedDict
import json
import os
import pyecore
import requests
import sys
import xml.dom.minidom
import yaml

import kinematics_model_generator
from kinematics_model_generator import check_deprecated_tag, eval_all, eval_text, grab_property, handle_macro_call
from kinematics_model_generator.kinematics.urdf import *
from kinematics_model_generator.kinematics.xacro import *


# xtext grammar expects specific sequence of features
attr_seq = {'XacroRobot': ['name', 'gitRepo', 'macros', 'configuredMacros'],
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


def is_link_rigid(link):
    if link and link.inertial:
        return True
    return False


def find_link(macro, link_name):
    for link in macro.link:
        if link.name == link_name:
            return link

    return None

# TODO: save as dot file?


def create_tree(macro):
    # prepare tree based on joints

    parent = None
    for joint in macro.joint:
        if parent:
            node = find_attr(parent.root, 'node_name', joint.parent.link)
            parent = node
        else:
            parent = Node(name=joint.parent.link)
            link = find_link(macro, joint.parent.link)
            parent.is_rigid = is_link_rigid(link)
        child = Node(name=joint.child.link)
        link = find_link(macro, joint.child.link)
        child.is_rigid = is_link_rigid(link)

        if not parent:
            raise Exception(joint.parent.link + ' parent in joint ' +
                            joint.name + ' does not exist. Not a valid tree')

        child.parent = parent

    # TODO: Need to check this again
    if not parent:
        return None
    return parent.root


class XacroStr(str):
    def set_keyword(self, keyword=''):
        self.keyword = keyword

    def dump_xtext(self, indent='', level=1):
        return '\n' + indent * level + self.keyword + ' "' + self + '"'


def conv_str_to_type(elem, name, val_str, symbols):
    try:
        val_type = str(elem.eClass.findEStructuralFeature(name).eType)
    except Exception as e:
        print(elem)
        print(name)
        print(val_str)
        raise e
    if 'float' in val_type:
        if elem.eGet(name).__class__ == pyecore.valuecontainer.EList:
            val_list_str = [eval_text(x, symbols) for x in val_str.split()]
            return [float(x) for x in val_list_str]
        return float(eval_text(val_str, symbols))
    elif 'int' in val_type:
        if elem.eGet(name).__class__ == pyecore.valuecontainer.EList:
            val_list_str = [eval_text(x, symbols) for x in val_str.split()]
            return [int(x) for x in val_list_str]
        return int(eval_text(val_str, symbols))
    elif 'str' in val_type:
        # if the attribute is a rule, return string without quotes
        if elem.eClass.name in is_rule:
            attributes = is_rule[elem.eClass.name]
            if name in attributes:
                return val_str
        return quoted(val_str)
    return val_str


def get_xacro_str(ref_name, keyword):
    xacroStr = XacroStr(ref_name)
    xacroStr.set_keyword(keyword)
    return xacroStr


def identify_param_type(elem, p):
    if isinstance(elem, Link) or isinstance(elem, Joint):
        if p in elem.name:
            param = Parameter(
                name=p, type=ParameterType.getEEnumLiteral('String'))
            return param

    if isinstance(elem, Joint):
        if p in elem.parent.link or p in elem.child.link:
            param = Parameter(
                name=p, type=ParameterType.getEEnumLiteral('LinkRef'))
            return param

    return None


def format_ref_link(link, params):
    link = format_name(link)
    link = link.replace('"', '')

    for param in params:
        if link == param.name:
            return link

    return '"' + link + '"'


def format_name(name, symbols=None):
    try:
        name = kinematics_model_generator.unicode(
            kinematics_model_generator.eval_text(name, symbols))
    except Exception as e:
        while '${' in name:
            start = name.rfind('${')
            if start != -1:
                end = name[start:].rfind('}')
                param = name[start+2:start+end]
                name = name[:start] + '"' + param + '"' + name[start+end+1:]

    return name


def grab_properties(node, symbols):
    node = node.firstChild
    while node:
        next = node.nextSibling
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            if node.tagName in ['property', 'xacro:property'] \
                    and check_deprecated_tag(node.tagName):
                grab_property(node, symbols)

        node = next


def handle_macros(parent, node, name, macros):
    # print('I m here: ' + name)
    if name in macros.keys():
        print('MACRO: ' + name)
        node = macros[name].body.firstChild
        while node.nodeType != xml.dom.Node.ELEMENT_NODE:
            node = node.nextSibling

        setattr(parent, node.tagName, get_xacro_str(name, node.tagName))
        return True
    return False

def init_macro_calls(macros, macro_calls):
    config_macros = []

    for macro in macro_calls:
        macro_name = list(macro.keys())[0]
        macro_params = list(macro.values())

        found = False
        for m in macros:
            if m == macro_name:
                found = True
                break

        if not found:
            continue

        config_macro = ConfiguredMacro()
        config_macro.name = macro_name

        # if len(m.link) > 0:
        #     for link in m.link:
        #         params_dict = identify_param_type(
        #             link, m.parameters, macro_params[0])

        #         # TODO: solve this while dealing with xacros with params
        #         # for name, value in params_dict:
        #         #     param = ConfiguredParameter()
        #         #     param.parameter

        # if len(m.joint) > 0:
        #     for joint in m.joint:
        #         params_dict = identify_param_type(
        #             joint, m.parameters, macro_params[0])

        config_macros.append(config_macro)

    return config_macros

def find_reference_eobj(eobj, ref, value):
    if not eobj:
        return None
    for ref_attr in eobj.eClass.eReferences:
        if ref_attr.eType == ref.eType:
            if ref_attr.containment:
                for attr in list(eobj.eAllContents()):
                    if attr.eClass.name in str(ref.eType):
                        if attr.name == value:
                            return attr

    # Reference object is not found, so go one step higher
    eobj = eobj.eContainer()
    return find_reference_eobj(eobj, ref, value)


# recursively traverses the xacro instance and
# creates corresponding kinematics instances
def parse_elem(node, parent, symbols, params, macros):
    node = node.firstChild
    elem = None
    while node:
        next = node.nextSibling
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            tagName = node.tagName.replace('xacro:', '')
            if tagName not in ['property', 'transmission']:
                if tagName == 'insert_block':
                    name, = kinematics_model_generator.check_attrs(
                        node, ['name'], [])

                    # Assuming '*' is origin block. NEED a better solution!
                    if ("*" + name) in params and hasattr(parent, 'origin'):
                        pose = kinematics_model_generator.kinematics.urdf.urdf.Pose.__call__()
                        pose.ref = quoted(name)
                        setattr(parent, 'origin', pose)
                elif tagName in ['if', 'unless']:
                    condition = Condition()
                    condition.param = dict(node.attributes.items())['value']
                    elem = Block()
                    if tagName == 'if':
                        condition.if_ = elem
                    elif tagName == 'unless':
                        condition.unless = elem
                    parent.condition.append(condition)
                else:
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

                    if not elem_attr:
                        macro_calls = []
                        if handle_macro_call(node, macros, macro_calls, symbols):
                            config_macros = init_macro_calls(macros, macro_calls)
                            node = next
                            continue
                        else:
                            print('unrecognized tagName ' + tagName + ' in parent ' + str(parent))
                            node = next
                            continue
                            # raise Exception('unrecognized tagName ' +
                            #             tagName + ' in parent ' + str(parent))

                    elem = elem_attr.eType.__call__()

                    for name, value in node.attributes.items():
                        conv_val = None
                        conv_val = conv_str_to_type(elem, name, value, symbols)

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

        parse_elem(node, elem, symbols, params, macros)
        node = next


# this function is becoming something else
# originally it was intended to generate the model text
# need to come back to this again
def parse_macros(name, macros, macro_calls, symbols):
    robot = XacroRobot()
    robot.name = quoted(name)

    dot_trees = {}

    for name in macros:
        print(name)
        m = macros[name]

        macro = Macro()
        macro.name = quoted(name)
        m_params = {}

        # print(m.history)

        if not m.body:
            continue

        # grab properties
        # this will be done normally in the original xacro parser only
        # during instantiation of macros
        # but getting the properties at this stage would be useful in
        # visualizing the models for example
        grab_properties(m.body, symbols)

        parse_elem(m.body, macro, symbols, m.params, macros)
        robot.macros.append(macro)

        # parse params
        unused_params = m.params
        for m_param in m.params:
            for link in macro.link:
                if not m_param:
                    break
                param = identify_param_type(link, m_param)
                if param:
                    macro.parameters.append(param)
                    # print(param)
                    m.params.remove(m_param)
                    m_param = None

            for joint in macro.joint:
                if not m_param:
                    break
                param = identify_param_type(joint, m_param)
                if param:
                    macro.parameters.append(param)
                    m_param = None

        # instantiate default params for those which were not identified
        for m_param in m.params:
            param = Parameter(
                name=m_param, type=ParameterType.getEEnumLiteral('String'))
            macro.parameters.append(param)
            m.params.remove(m_param)

        root = create_tree(macro)
        if root:
            print_tree(root)
            graph = tree_to_dict(root)
            dot_trees[name] = graph

            # print(findall(root, lambda node: node.is_rigid))

            # This should be made into a separate function
            # to determine the category
            leaves = list(root.leaves)
            # print(leaves)
            leaves = [leaf for leaf in leaves if leaf.is_rigid]
            # print(leaves)

    for macro in macro_calls:
        macro_name = list(macro.keys())[0]
        macro_params = list(macro.values())

        found = False
        for m in robot.macros:
            if m.name == macro_name:
                found = True
                break

        if not found:
            continue

        configMacro = ConfiguredMacro()
        configMacro.name = macro_name

        if len(m.link) > 0:
            for link in m.link:
                params_dict = identify_param_type(
                    link, m.parameters, macro_params[0])

                # TODO: solve this while dealing with xacros with params
                # for name, value in params_dict:
                #     param = ConfiguredParameter()
                #     param.parameter

        if len(m.joint) > 0:
            for joint in m.joint:
                params_dict = identify_param_type(
                    joint, m.parameters, macro_params[0])

        robot.configuredMacros.append(configMacro)

    return robot, dot_trees


def process_file(input_file_name, **kwargs):
    """main processing pipeline"""
    # initialize file stack for error-reporting
    kinematics_model_generator.restore_filestack([input_file_name])
    # parse the document into a xml.dom tree
    doc = kinematics_model_generator.parse(None, input_file_name)
    # perform macro replacement
    robot_name, macros, macro_calls, symbols = process_doc(doc, **kwargs)

    # adding global macro to the call list since it need not be explicity called
    # not sure about the parameters yet -- can there be global params?
    # maybe there are in symbol?
    macro_calls.append({'global': {}})

    name = input_file_name.split(
        '/')[-1].replace('.xacro', '').replace('.urdf', '')

    print(kwargs['output'])

    # parse URDF elements -- joints, links, etc
    robot, dot_trees = parse_macros(robot_name, macros, macro_calls, symbols)

     # TODO: how to handle this?
    robot.gitRepo = GitRepo(raw_file_url=kwargs['raw_file_url'],
                            repo=kwargs['repo'],
                            package=kwargs['package'], version=kwargs['version'])


    # write model to file
    model_dict = eobj_to_dict(robot)
    filepath = kwargs['output']
    with open(filepath, 'w') as yaml_file:
        yaml_file.write(
            yaml.dump(model_dict, default_flow_style=False, sort_keys=False))

    # insert component in Flask DB
    # TODO: improvements needed
    # is it the right place?
    insert_component(robot.name, 'Manipulator', robot.gitRepo.raw_file_url, robot.gitRepo.repo,
                     robot.gitRepo.package, robot.gitRepo.version, dot_trees=dot_trees, model_dict=model_dict)

    return doc, robot, macros


def process_doc(doc, mappings=None, **kwargs):
    global verbosity
    verbosity = kwargs.get('verbosity', kinematics_model_generator.verbosity)

    # set substitution args
    kinematics_model_generator.substitution_args_context['arg'] = {} if mappings is None \
        else mappings

    # if not yet defined: initialize filestack
    if not kinematics_model_generator.filestack:
        kinematics_model_generator.init_stacks(None)

    macros = kinematics_model_generator.Table()

    # add global 'macro' for kinematic elements
    # which are defined in the main body
    g_macro = macros.get('global', kinematics_model_generator.Macro())
    macros['global'] = g_macro

    symbols = kinematics_model_generator.Table(
        kinematics_model_generator.global_symbols)

    macro_calls = []

    node = doc.documentElement
    while node.tagName != 'robot':
        node = node.nextSibling

    robot_name = ''
    attrs = dict(node.attributes.items())
    if 'name' in attrs:
        robot_name = attrs['name']

    # apply xacro:targetNamespace as global xmlns (if defined)
    targetNS = doc.documentElement.getAttribute('xacro:targetNamespace')
    if targetNS:
        doc.documentElement.removeAttribute('xacro:targetNamespace')
        doc.documentElement.setAttribute('xmlns', targetNS)

    eval_all(doc.documentElement, macros, macro_calls, symbols)

    # reset substitution args
    kinematics_model_generator.substitution_args_context['arg'] = {}

    return robot_name, macros, macro_calls, symbols


def parse_file(input_file_name):
    opts, input_file_name = kinematics_model_generator.process_args([
        input_file_name])
    try:
        # open and process file
        doc, robot, macros = process_file(input_file_name, **vars(opts))
        return robot, macros
        # print()

    # error handling
    except xml.parsers.expat.ExpatError as e:
        kinematics_model_generator.error(
            "XML parsing error: %s" % e, alt_text=None)
        if kinematics_model_generator.verbosity > 0:
            kinematics_model_generator.print_location()
            print(file=sys.stderr)  # add empty separator line before error
            print("Check that:", file=sys.stderr)
            print(" - Your XML is well-formed", file=sys.stderr)
            print(" - You have the xacro xmlns declaration:",
                  "xmlns:xacro=\"http://www.ros.org/wiki/xacro\"",
                  file=sys.stderr)
        sys.exit(2)  # indicate failure,
        # but don't print stack trace on XML errors

    except Exception as e:
        msg = e
        if not msg:
            msg = repr(e)
        kinematics_model_generator.error(msg)
        if kinematics_model_generator.verbosity > 0:
            kinematics_model_generator.print_location()
        if kinematics_model_generator.verbosity > 1:
            print(file=sys.stderr)  # add empty separator line before error
            raise  # create stack trace
        else:
            sys.exit(2)  # gracefully exit with error condition


if __name__ == "__main__":
    opts, input_file_name = kinematics_model_generator.process_args(
        sys.argv[1:])
    try:
        # open and process file
        doc = process_file(input_file_name, **vars(opts))
        # print()

    # error handling
    except xml.parsers.expat.ExpatError as e:
        kinematics_model_generator.error(
            "XML parsing error: %s" % e, alt_text=None)
        if kinematics_model_generator.verbosity > 0:
            kinematics_model_generator.print_location()
            print(file=sys.stderr)  # add empty separator line before error
            print("Check that:", file=sys.stderr)
            print(" - Your XML is well-formed", file=sys.stderr)
            print(" - You have the xacro xmlns declaration:",
                  "xmlns:xacro=\"http://www.ros.org/wiki/xacro\"",
                  file=sys.stderr)
        sys.exit(2)  # indicate failure,
        # but don't print stack trace on XML errors

    except Exception as e:
        msg = e
        if not msg:
            msg = repr(e)
        kinematics_model_generator.error(msg)
        if kinematics_model_generator.verbosity > 0:
            kinematics_model_generator.print_location()
        if kinematics_model_generator.verbosity > 1:
            print(file=sys.stderr)  # add empty separator line before error
