"""Definition of meta model 'urdf'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'urdf'
nsURI = 'http://www.ipa.fraunhofer.de/urdf'
nsPrefix = 'urdf'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
JointType = EEnum('JointType', literals=[])


class ActuatorTransmission(EObject, metaclass=MetaEClass):

    mechanicalReduction = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, mechanicalReduction=None, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if mechanicalReduction is not None:
            self.mechanicalReduction = mechanicalReduction

        if name is not None:
            self.name = name


class Axis(EObject, metaclass=MetaEClass):

    xyz = EAttribute(eType=EString, unique=True, derived=False,
                     changeable=True, default_value='1 0 0')

    def __init__(self, *, xyz=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if xyz is not None:
            self.xyz = xyz


class Box(EObject, metaclass=MetaEClass):

    size = EAttribute(eType=EString, unique=True, derived=False,
                      changeable=True, default_value='0 0 0')

    def __init__(self, *, size=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if size is not None:
            self.size = size


class Calibration(EObject, metaclass=MetaEClass):

    falling = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    referencePosition = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    rising = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, falling=None, referencePosition=None, rising=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if falling is not None:
            self.falling = falling

        if referencePosition is not None:
            self.referencePosition = referencePosition

        if rising is not None:
            self.rising = rising


class Child(EObject, metaclass=MetaEClass):

    link = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, link=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if link is not None:
            self.link = link


class Collision(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    origin = EReference(ordered=True, unique=True, containment=True, derived=False)
    geometry = EReference(ordered=True, unique=True, containment=True, derived=False)
    verbose = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, origin=None, geometry=None, verbose=None, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if origin is not None:
            self.origin = origin

        if geometry is not None:
            self.geometry = geometry

        if verbose is not None:
            self.verbose = verbose


class Color(EObject, metaclass=MetaEClass):

    rgba = EAttribute(eType=EString, unique=True, derived=False,
                      changeable=True, default_value='0 0 0 0')

    def __init__(self, *, rgba=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if rgba is not None:
            self.rgba = rgba


class Cylinder(EObject, metaclass=MetaEClass):

    length = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    radius = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, length=None, radius=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if length is not None:
            self.length = length

        if radius is not None:
            self.radius = radius


class Dynamics(EObject, metaclass=MetaEClass):

    damping = EAttribute(eType=EDouble, unique=True, derived=False,
                         changeable=True, default_value=0.0)
    friction = EAttribute(eType=EDouble, unique=True, derived=False,
                          changeable=True, default_value=0.0)

    def __init__(self, *, damping=None, friction=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if damping is not None:
            self.damping = damping

        if friction is not None:
            self.friction = friction


class GapJointTransmission(EObject, metaclass=MetaEClass):

    a = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    b = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    gearRatio = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    h = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    l0 = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    mechanicalReduction = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    phi0 = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    r = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    screwReduction = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    t0 = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    theta0 = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, a=None, b=None, gearRatio=None, h=None, l0=None, mechanicalReduction=None, name=None, phi0=None, r=None, screwReduction=None, t0=None, theta0=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if a is not None:
            self.a = a

        if b is not None:
            self.b = b

        if gearRatio is not None:
            self.gearRatio = gearRatio

        if h is not None:
            self.h = h

        if l0 is not None:
            self.l0 = l0

        if mechanicalReduction is not None:
            self.mechanicalReduction = mechanicalReduction

        if name is not None:
            self.name = name

        if phi0 is not None:
            self.phi0 = phi0

        if r is not None:
            self.r = r

        if screwReduction is not None:
            self.screwReduction = screwReduction

        if t0 is not None:
            self.t0 = t0

        if theta0 is not None:
            self.theta0 = theta0


class Geometry(EObject, metaclass=MetaEClass):

    box = EReference(ordered=True, unique=True, containment=True, derived=False)
    cylinder = EReference(ordered=True, unique=True, containment=True, derived=False)
    sphere = EReference(ordered=True, unique=True, containment=True, derived=False)
    mesh = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, box=None, cylinder=None, sphere=None, mesh=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if box is not None:
            self.box = box

        if cylinder is not None:
            self.cylinder = cylinder

        if sphere is not None:
            self.sphere = sphere

        if mesh is not None:
            self.mesh = mesh


class Inertia(EObject, metaclass=MetaEClass):

    ixx = EAttribute(eType=EString, unique=True, derived=False, changeable=True, default_value='0')
    ixy = EAttribute(eType=EString, unique=True, derived=False, changeable=True, default_value='0')
    ixz = EAttribute(eType=EString, unique=True, derived=False, changeable=True, default_value='0')
    iyy = EAttribute(eType=EString, unique=True, derived=False, changeable=True, default_value='0')
    iyz = EAttribute(eType=EString, unique=True, derived=False, changeable=True, default_value='0')
    izz = EAttribute(eType=EString, unique=True, derived=False, changeable=True, default_value='0')

    def __init__(self, *, ixx=None, ixy=None, ixz=None, iyy=None, iyz=None, izz=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if ixx is not None:
            self.ixx = ixx

        if ixy is not None:
            self.ixy = ixy

        if ixz is not None:
            self.ixz = ixz

        if iyy is not None:
            self.iyy = iyy

        if iyz is not None:
            self.iyz = iyz

        if izz is not None:
            self.izz = izz


class Inertial(EObject, metaclass=MetaEClass):

    origin = EReference(ordered=True, unique=True, containment=True, derived=False)
    mass = EReference(ordered=True, unique=True, containment=True, derived=False)
    inertia = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, origin=None, mass=None, inertia=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if origin is not None:
            self.origin = origin

        if mass is not None:
            self.mass = mass

        if inertia is not None:
            self.inertia = inertia


class Joint(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    origin = EReference(ordered=True, unique=True, containment=True, derived=False)
    parent = EReference(ordered=True, unique=True, containment=True, derived=False)
    child = EReference(ordered=True, unique=True, containment=True, derived=False)
    axis = EReference(ordered=True, unique=True, containment=True, derived=False)
    calibration = EReference(ordered=True, unique=True, containment=True, derived=False)
    dynamics = EReference(ordered=True, unique=True, containment=True, derived=False)
    limit = EReference(ordered=True, unique=True, containment=True, derived=False)
    safetyController = EReference(ordered=True, unique=True, containment=True, derived=False)
    mimic = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, origin=None, parent=None, child=None, axis=None, calibration=None, dynamics=None, limit=None, safetyController=None, mimic=None, name=None, type=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if type is not None:
            self.type = type

        if origin is not None:
            self.origin = origin

        if parent is not None:
            self.parent = parent

        if child is not None:
            self.child = child

        if axis is not None:
            self.axis = axis

        if calibration is not None:
            self.calibration = calibration

        if dynamics is not None:
            self.dynamics = dynamics

        if limit is not None:
            self.limit = limit

        if safetyController is not None:
            self.safetyController = safetyController

        if mimic is not None:
            self.mimic = mimic


class Limit(EObject, metaclass=MetaEClass):

    effort = EAttribute(eType=EString, unique=True, derived=False,
                        changeable=True, default_value='0')
    lower = EAttribute(eType=EString, unique=True, derived=False,
                       changeable=True, default_value='0')
    upper = EAttribute(eType=EString, unique=True, derived=False,
                       changeable=True, default_value='0')
    velocity = EAttribute(eType=EString, unique=True, derived=False,
                          changeable=True, default_value='0')

    def __init__(self, *, effort=None, lower=None, upper=None, velocity=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if effort is not None:
            self.effort = effort

        if lower is not None:
            self.lower = lower

        if upper is not None:
            self.upper = upper

        if velocity is not None:
            self.velocity = velocity


class Link(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    inertial = EReference(ordered=True, unique=True, containment=True, derived=False)
    visual = EReference(ordered=True, unique=True, containment=True, derived=False)
    collision = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, inertial=None, visual=None, collision=None, name=None, type=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if type is not None:
            self.type = type

        if inertial is not None:
            self.inertial = inertial

        if visual is not None:
            self.visual = visual

        if collision is not None:
            self.collision = collision


class Mass(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EString, unique=True, derived=False,
                       changeable=True, default_value='0')

    def __init__(self, *, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value


class Material(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    color = EReference(ordered=True, unique=True, containment=True, derived=False)
    texture = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, color=None, texture=None, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if color is not None:
            self.color = color

        if texture is not None:
            self.texture = texture


class MaterialGlobal(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    color = EReference(ordered=True, unique=True, containment=True, derived=False)
    texture = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, color=None, texture=None, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if color is not None:
            self.color = color

        if texture is not None:
            self.texture = texture


class Mesh(EObject, metaclass=MetaEClass):

    filename = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    scale = EAttribute(eType=EString, unique=True, derived=False,
                       changeable=True, default_value='1 1 1')

    def __init__(self, *, filename=None, scale=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if filename is not None:
            self.filename = filename

        if scale is not None:
            self.scale = scale


class Mimic(EObject, metaclass=MetaEClass):

    joint = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    multiplier = EAttribute(eType=EDouble, unique=True, derived=False,
                            changeable=True, default_value=1.0)
    offset = EAttribute(eType=EDouble, unique=True, derived=False,
                        changeable=True, default_value=0.0)

    def __init__(self, *, joint=None, multiplier=None, offset=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if joint is not None:
            self.joint = joint

        if multiplier is not None:
            self.multiplier = multiplier

        if offset is not None:
            self.offset = offset


class Name(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


class Parent(EObject, metaclass=MetaEClass):

    link = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, link=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if link is not None:
            self.link = link


class PassiveJointTransmission(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


class Pose(EObject, metaclass=MetaEClass):

    rpy = EAttribute(eType=EDouble, unique=False, derived=False,
                     changeable=True, upper=-1, default_value=0.0)
    xyz = EAttribute(eType=EDouble, unique=False, derived=False,
                     changeable=True, upper=-1, default_value=0.0)

    def __init__(self, *, rpy=None, xyz=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if rpy:
            self.rpy.extend(rpy)

        if xyz:
            self.xyz.extend(xyz)


class Robot(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    version = EAttribute(eType=EString, unique=True, derived=False,
                         changeable=True, default_value='1.0')
    joint = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    link = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    material = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    transmission = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, joint=None, link=None, material=None, transmission=None, name=None, version=None):
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

        if material:
            self.material.extend(material)

        if transmission:
            self.transmission.extend(transmission)


class SafetyController(EObject, metaclass=MetaEClass):

    kPosition = EAttribute(eType=EDouble, unique=True, derived=False,
                           changeable=True, default_value=0.0)
    kVelocity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    softLowerLimit = EAttribute(eType=EDouble, unique=True, derived=False,
                                changeable=True, default_value=0.0)
    softUpperLimit = EAttribute(eType=EDouble, unique=True, derived=False,
                                changeable=True, default_value=0.0)

    def __init__(self, *, kPosition=None, kVelocity=None, softLowerLimit=None, softUpperLimit=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if kPosition is not None:
            self.kPosition = kPosition

        if kVelocity is not None:
            self.kVelocity = kVelocity

        if softLowerLimit is not None:
            self.softLowerLimit = softLowerLimit

        if softUpperLimit is not None:
            self.softUpperLimit = softUpperLimit


class Sphere(EObject, metaclass=MetaEClass):

    radius = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, radius=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if radius is not None:
            self.radius = radius


class Texture(EObject, metaclass=MetaEClass):

    filename = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, filename=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if filename is not None:
            self.filename = filename


class DerivedLeftactuator(EDerivedCollection):
    pass


class DerivedRightactuator(EDerivedCollection):
    pass


class DerivedFlexjoint(EDerivedCollection):
    pass


class DerivedRolljoint(EDerivedCollection):
    pass


class DerivedGapjoint(EDerivedCollection):
    pass


class DerivedPassivejoint(EDerivedCollection):
    pass


class DerivedUsesimulatedgripperjoint(EDerivedCollection):
    pass


class DerivedActuator(EDerivedCollection):
    pass


class DerivedJoint(EDerivedCollection):
    pass


class Transmission(EObject, metaclass=MetaEClass):

    mechanicalReduction = EAttribute(eType=EDouble, unique=True,
                                     derived=False, changeable=True, upper=-1)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    leftActuator = EReference(ordered=True, unique=True, containment=True,
                              derived=True, upper=-1, transient=True, derived_class=DerivedLeftactuator)
    rightActuator = EReference(ordered=True, unique=True, containment=True,
                               derived=True, upper=-1, transient=True, derived_class=DerivedRightactuator)
    flexJoint = EReference(ordered=True, unique=True, containment=True,
                           derived=True, upper=-1, transient=True, derived_class=DerivedFlexjoint)
    rollJoint = EReference(ordered=True, unique=True, containment=True,
                           derived=True, upper=-1, transient=True, derived_class=DerivedRolljoint)
    gapJoint = EReference(ordered=True, unique=True, containment=True,
                          derived=True, upper=-1, transient=True, derived_class=DerivedGapjoint)
    passiveJoint = EReference(ordered=True, unique=True, containment=True,
                              derived=True, upper=-1, transient=True, derived_class=DerivedPassivejoint)
    useSimulatedGripperJoint = EReference(ordered=True, unique=True, containment=True,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedUsesimulatedgripperjoint)
    actuator = EReference(ordered=True, unique=True, containment=True,
                          derived=True, upper=-1, transient=True, derived_class=DerivedActuator)
    joint = EReference(ordered=True, unique=True, containment=True, derived=True,
                       upper=-1, transient=True, derived_class=DerivedJoint)

    def __init__(self, *, leftActuator=None, rightActuator=None, flexJoint=None, rollJoint=None, gapJoint=None, passiveJoint=None, useSimulatedGripperJoint=None, mechanicalReduction=None, actuator=None, joint=None, name=None, type=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if mechanicalReduction:
            self.mechanicalReduction.extend(mechanicalReduction)

        if name is not None:
            self.name = name

        if type is not None:
            self.type = type

        if leftActuator:
            self.leftActuator.extend(leftActuator)

        if rightActuator:
            self.rightActuator.extend(rightActuator)

        if flexJoint:
            self.flexJoint.extend(flexJoint)

        if rollJoint:
            self.rollJoint.extend(rollJoint)

        if gapJoint:
            self.gapJoint.extend(gapJoint)

        if passiveJoint:
            self.passiveJoint.extend(passiveJoint)

        if useSimulatedGripperJoint:
            self.useSimulatedGripperJoint.extend(useSimulatedGripperJoint)

        if actuator:
            self.actuator.extend(actuator)

        if joint:
            self.joint.extend(joint)


class UseSimulatedGripperJointType(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Verbose(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value


class Visual(EObject, metaclass=MetaEClass):

    origin = EReference(ordered=True, unique=True, containment=True, derived=False)
    geometry = EReference(ordered=True, unique=True, containment=True, derived=False)
    material = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, origin=None, geometry=None, material=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if origin is not None:
            self.origin = origin

        if geometry is not None:
            self.geometry = geometry

        if material is not None:
            self.material = material


class Block(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
