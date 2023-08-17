
from .component import getEClassifier, eClassifiers
from .component import name, nsURI, nsPrefix, eClass
from .component import Component, Group, GitRepo

from kinematics_model_generator.kinematics.urdf import Link, Joint

from . import component

__all__ = ['Component', 'Group', 'GitRepo']

eSubpackages = []
eSuperPackage = None
component.eSubpackages = eSubpackages
component.eSuperPackage = eSuperPackage

Component.gitRepo.eType = GitRepo
Component.group.eType = Group
Component.component.eType = Component
Component.link.eType = Link
Component.joint.eType = Joint

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
