
from .component import getEClassifier, eClassifiers
from .component import name, nsURI, nsPrefix, eClass
from .component import Attachment, BaseAttachment, Component, ConfiguredComponent, Connection, FlangeAttachment, Group, GitRepo

from kinematics_model_generator.kinematics.urdf import Link, Joint

from . import component

__all__ = ['Attachment', 'BaseAttachment', 'Component', 'ConfiguredComponent',
           'Connection', 'FlangeAttachment', 'Group', 'GitRepo']

eSubpackages = []
eSuperPackage = None
component.eSubpackages = eSubpackages
component.eSuperPackage = eSuperPackage

Attachment.origin.eType = Pose
Attachment.parent.eType = Link
Component.gitRepo.eType = GitRepo
Component.baseAttachment.eType = BaseAttachment
Component.flangeAttachment.eType = FlangeAttachment
Component.group.eType = Group
Component.component.eType = ConfiguredComponent
Component.connection.eType = Connection
Component.link.eType = Link
Component.joint.eType = Joint
ConfiguredComponent.type.eType = Component
Connection.baseAttachment.eType = BaseAttachment
Connection.flangeAttachment.eType = FlangeAttachment
Group.baseLink.eType = Link
Group.endLink.eType = Link

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
