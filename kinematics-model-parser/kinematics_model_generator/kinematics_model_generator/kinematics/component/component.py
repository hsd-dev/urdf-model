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
    joint = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    link = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    group = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, version=None, joint=None, link=None, group=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if version is not None:
            self.version = version

        if joint:
            self.joint.extend(joint)

        if link:
            self.link.extend(link)

        if group:
            self.group.extend(group)


class Group(EObject, metaclass=MetaEClass):

    base_link = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    end_link = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, base_link=None, end_link=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_link is not None:
            self.base_link = base_link

        if end_link is not None:
            self.end_link = end_link
