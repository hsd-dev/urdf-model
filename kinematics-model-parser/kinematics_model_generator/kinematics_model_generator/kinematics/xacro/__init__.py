
from .xacro import getEClassifier, eClassifiers
from .xacro import name, nsURI, nsPrefix, eClass
from .xacro import Macro, ConfiguredMacro, ConfiguredParameter, Parameter, ParameterType, XacroRobot, GitRepo, Condition, Block

from kinematics_model_generator.kinematics.urdf import Link, Joint

from . import xacro

__all__ = ['Macro', 'ConfiguredMacro', 'ConfiguredParameter', 'Parameter',
           'ParameterType', 'XacroRobot', 'GitRepo', 'Condition', 'Block']

eSubpackages = []
eSuperPackage = None
xacro.eSubpackages = eSubpackages
xacro.eSuperPackage = eSuperPackage

Macro.parameters.eType = Parameter
Macro.configuredMacros.eType = ConfiguredMacro
Macro.link.eType = Link
Macro.joint.eType = Joint
Macro.condition.eType = Condition
ConfiguredMacro.macro.eType = Macro
ConfiguredMacro.parameters.eType = ConfiguredParameter
ConfiguredParameter.parameter.eType = Parameter
XacroRobot.macros.eType = Macro
XacroRobot.configuredMacros.eType = ConfiguredMacro
XacroRobot.gitRepo.eType = GitRepo
Condition.if_.eType = Block
Condition.unless.eType = Block
Block.joint.eType = Joint
Block.link.eType = Link

otherClassifiers = [ParameterType]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
