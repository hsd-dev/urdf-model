
from .urdf import getEClassifier, eClassifiers
from .urdf import name, nsURI, nsPrefix, eClass
from .urdf import ActuatorTransmission, Axis, Box, Calibration, Child, Collision, Color, Cylinder, Dynamics, GapJointTransmission, Geometry, Inertia, Inertial, Joint, JointType, Limit, Link, Mass, Material, MaterialGlobal, Mesh, Mimic, Name, Parent, PassiveJointTransmission, Pose, Robot, SafetyController, Sphere, Texture, Transmission, UseSimulatedGripperJointType, Verbose, Visual


from . import urdf

__all__ = ['ActuatorTransmission', 'Axis', 'Box', 'Calibration', 'Child', 'Collision', 'Color', 'Cylinder', 'Dynamics', 'GapJointTransmission', 'Geometry', 'Inertia', 'Inertial', 'Joint', 'JointType', 'Limit', 'Link', 'Mass',
           'Material', 'MaterialGlobal', 'Mesh', 'Mimic', 'Name', 'Parent', 'PassiveJointTransmission', 'Pose', 'Robot', 'SafetyController', 'Sphere', 'Texture', 'Transmission', 'UseSimulatedGripperJointType', 'Verbose', 'Visual']

eSubpackages = []
eSuperPackage = None
urdf.eSubpackages = eSubpackages
urdf.eSuperPackage = eSuperPackage

Collision.origin.eType = Pose
Collision.geometry.eType = Geometry
Collision.verbose.eType = Verbose
Geometry.box.eType = Box
Geometry.cylinder.eType = Cylinder
Geometry.sphere.eType = Sphere
Geometry.mesh.eType = Mesh
Inertial.origin.eType = Pose
Inertial.mass.eType = Mass
Inertial.inertia.eType = Inertia
Joint.origin.eType = Pose
Joint.parent.eType = Parent
Joint.child.eType = Child
Joint.axis.eType = Axis
Joint.calibration.eType = Calibration
Joint.dynamics.eType = Dynamics
Joint.limit.eType = Limit
Joint.safetyController.eType = SafetyController
Joint.mimic.eType = Mimic
Link.inertial.eType = Inertial
Link.visual.eType = Visual
Link.collision.eType = Collision
Material.color.eType = Color
Material.texture.eType = Texture
MaterialGlobal.color.eType = Color
MaterialGlobal.texture.eType = Texture
Robot.joint.eType = Joint
Robot.link.eType = Link
Robot.material.eType = MaterialGlobal
Robot.transmission.eType = Transmission
Transmission.leftActuator.eType = ActuatorTransmission
Transmission.rightActuator.eType = ActuatorTransmission
Transmission.flexJoint.eType = ActuatorTransmission
Transmission.rollJoint.eType = ActuatorTransmission
Transmission.gapJoint.eType = GapJointTransmission
Transmission.passiveJoint.eType = PassiveJointTransmission
Transmission.useSimulatedGripperJoint.eType = UseSimulatedGripperJointType
Transmission.actuator.eType = Name
Transmission.joint.eType = Name
Visual.origin.eType = Pose
Visual.geometry.eType = Geometry
Visual.material.eType = Material

otherClassifiers = [JointType]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
