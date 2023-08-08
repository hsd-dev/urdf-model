
from .component import getEClassifier, eClassifiers
from .component import name, nsURI, nsPrefix, eClass
from .component import Component, Group

from kinematics_model_generator.kinematics.urdf import Link, Joint

from . import component

__all__ = ['Component', 'Group']

eSubpackages = []
eSuperPackage = None
component.eSubpackages = eSubpackages
component.eSuperPackage = eSuperPackage

Component.joint.eType = Joint
Component.link.eType = Link
Component.group.eType = Group

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
