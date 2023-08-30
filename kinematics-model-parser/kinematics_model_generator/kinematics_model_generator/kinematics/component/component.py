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


class Component(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    version = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    category = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    gitRepo = EReference(ordered=True, unique=True, containment=True, derived=False)
    group = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    component = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    link = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    joint = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, version=None, category=None, gitRepo=None, group=None, component=None, link=None, joint=None):
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

        if group:
            self.group.extend(group)

        if component:
            self.component.extend(component)

        if link:
            self.link.extend(link)

        if joint:
            self.joint.extend(joint)


class Group(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    base_link = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    end_link = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    ros2_control = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None, base_link=None, end_link=None, ros2_control=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if base_link is not None:
            self.base_link = base_link

        if end_link is not None:
            self.end_link = end_link

        if ros2_control is not None:
            self.ros2_control = ros2_control


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
