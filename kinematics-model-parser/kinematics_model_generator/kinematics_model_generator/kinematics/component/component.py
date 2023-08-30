"""Definition of meta model 'component'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'component'
nsURI = 'http://www.ipa.fraunhofer.de/component'
nsPrefix = 'component'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class Attachment(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    origin = EReference(ordered=True, unique=True, containment=True, derived=False)
    parent = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, name=None, origin=None, parent=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if origin is not None:
            self.origin = origin

        if parent is not None:
            self.parent = parent


class Component(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    version = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    category = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    gitRepo = EReference(ordered=True, unique=True, containment=True, derived=False)
    baseAttachment = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    flangeAttachment = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    group = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    component = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    connection = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    link = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    joint = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, version=None, category=None, gitRepo=None, baseAttachment=None, flangeAttachment=None, group=None, component=None, connection=None, link=None, joint=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if version is not None:
            self.version = version

        if category is not None:
            self.category = category

        if gitRepo is not None:
            self.gitRepo = gitRepo

        if baseAttachment:
            self.baseAttachment.extend(baseAttachment)

        if flangeAttachment:
            self.flangeAttachment.extend(flangeAttachment)

        if group:
            self.group.extend(group)

        if component:
            self.component.extend(component)

        if connection:
            self.connection.extend(connection)

        if link:
            self.link.extend(link)

        if joint:
            self.joint.extend(joint)


class ConfiguredComponent(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    prefix = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    type = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, name=None, type=None, prefix=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if prefix is not None:
            self.prefix = prefix

        if type is not None:
            self.type = type


class Connection(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    baseAttachment = EReference(ordered=True, unique=True, containment=False, derived=False)
    flangeAttachment = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, name=None, baseAttachment=None, flangeAttachment=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if baseAttachment is not None:
            self.baseAttachment = baseAttachment

        if flangeAttachment is not None:
            self.flangeAttachment = flangeAttachment


class Group(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    ros2_control = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    baseLink = EReference(ordered=True, unique=True, containment=False, derived=False)
    endLink = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, name=None, ros2_control=None, baseLink=None, endLink=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if ros2_control is not None:
            self.ros2_control = ros2_control

        if baseLink is not None:
            self.baseLink = baseLink

        if endLink is not None:
            self.endLink = endLink


class GitRepo(EObject, metaclass=MetaEClass):

    distro = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    repo = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    package = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    version = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    branch = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, distro=None, repo=None, package=None, version=None, branch=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if distro is not None:
            self.distro = distro

        if repo is not None:
            self.repo = repo

        if package is not None:
            self.package = package

        if version is not None:
            self.version = version

        if branch is not None:
            self.branch = branch


class BaseAttachment(Attachment):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class FlangeAttachment(Attachment):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
