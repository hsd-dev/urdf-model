"""Definition of meta model 'xacro'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'xacro'
nsURI = 'http://www.ipa.fraunhofer.de/xacro'
nsPrefix = 'xacro'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
ParameterType = EEnum('ParameterType', literals=['Link', 'String', 'Pose'])


class Macro(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    parameters = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    configuredMacros = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    link = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    joint = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    condition = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, parameters=None, configuredMacros=None, link=None, joint=None, condition=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if parameters:
            self.parameters.extend(parameters)

        if configuredMacros:
            self.configuredMacros.extend(configuredMacros)

        if link:
            self.link.extend(link)

        if joint:
            self.joint.extend(joint)

        if condition:
            self.condition.extend(condition)


class ConfiguredMacro(EObject, metaclass=MetaEClass):

    macro = EReference(ordered=True, unique=True, containment=False, derived=False)
    parameters = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, macro=None, parameters=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if macro is not None:
            self.macro = macro

        if parameters:
            self.parameters.extend(parameters)


class ConfiguredParameter(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    parameter = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, parameter=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value

        if parameter is not None:
            self.parameter = parameter


class Parameter(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=ParameterType, unique=True, derived=False, changeable=True)
    default = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None, type=None, default=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if type is not None:
            self.type = type

        if default is not None:
            self.default = default

        if value is not None:
            self.value = value


class XacroRobot(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    macros = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    configuredMacros = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    gitRepo = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, name=None, macros=None, configuredMacros=None, gitRepo=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if macros:
            self.macros.extend(macros)

        if configuredMacros:
            self.configuredMacros.extend(configuredMacros)

        if gitRepo is not None:
            self.gitRepo = gitRepo


class GitRepo(EObject, metaclass=MetaEClass):

    raw_file_url = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    package = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    version = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    repo = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, raw_file_url=None, package=None, version=None, repo=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if raw_file_url is not None:
            self.raw_file_url = raw_file_url

        if package is not None:
            self.package = package

        if version is not None:
            self.version = version

        if repo is not None:
            self.repo = repo


class Condition(EObject, metaclass=MetaEClass):

    param = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    if_ = EReference(ordered=True, unique=True, containment=True, derived=False)
    unless = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, param=None, if_=None, unless=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if param is not None:
            self.param = param

        if if_ is not None:
            self.if_ = if_

        if unless is not None:
            self.unless = unless


class Block(EObject, metaclass=MetaEClass):

    joint = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    link = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, joint=None, link=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if joint:
            self.joint.extend(joint)

        if link:
            self.link.extend(link)
