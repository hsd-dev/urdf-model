/**
 */
package kinematics.impl;

import kinematics.ActuatorTransmission;
import kinematics.KinematicsPackage;

import org.eclipse.emf.common.notify.Notification;

import org.eclipse.emf.ecore.EClass;

import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Actuator Transmission</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link kinematics.impl.ActuatorTransmissionImpl#getMechanicalReduction <em>Mechanical Reduction</em>}</li>
 *   <li>{@link kinematics.impl.ActuatorTransmissionImpl#getName <em>Name</em>}</li>
 * </ul>
 *
 * @generated
 */
public class ActuatorTransmissionImpl extends MinimalEObjectImpl.Container implements ActuatorTransmission {
	/**
	 * The default value of the '{@link #getMechanicalReduction() <em>Mechanical Reduction</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getMechanicalReduction()
	 * @generated
	 * @ordered
	 */
	protected static final double MECHANICAL_REDUCTION_EDEFAULT = 0.0;

	/**
	 * The cached value of the '{@link #getMechanicalReduction() <em>Mechanical Reduction</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getMechanicalReduction()
	 * @generated
	 * @ordered
	 */
	protected double mechanicalReduction = MECHANICAL_REDUCTION_EDEFAULT;

	/**
	 * This is true if the Mechanical Reduction attribute has been set.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	protected boolean mechanicalReductionESet;

	/**
	 * The default value of the '{@link #getName() <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getName()
	 * @generated
	 * @ordered
	 */
	protected static final String NAME_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getName() <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getName()
	 * @generated
	 * @ordered
	 */
	protected String name = NAME_EDEFAULT;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ActuatorTransmissionImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return KinematicsPackage.Literals.ACTUATOR_TRANSMISSION;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public double getMechanicalReduction() {
		return mechanicalReduction;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setMechanicalReduction(double newMechanicalReduction) {
		double oldMechanicalReduction = mechanicalReduction;
		mechanicalReduction = newMechanicalReduction;
		boolean oldMechanicalReductionESet = mechanicalReductionESet;
		mechanicalReductionESet = true;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, KinematicsPackage.ACTUATOR_TRANSMISSION__MECHANICAL_REDUCTION, oldMechanicalReduction, mechanicalReduction, !oldMechanicalReductionESet));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void unsetMechanicalReduction() {
		double oldMechanicalReduction = mechanicalReduction;
		boolean oldMechanicalReductionESet = mechanicalReductionESet;
		mechanicalReduction = MECHANICAL_REDUCTION_EDEFAULT;
		mechanicalReductionESet = false;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.UNSET, KinematicsPackage.ACTUATOR_TRANSMISSION__MECHANICAL_REDUCTION, oldMechanicalReduction, MECHANICAL_REDUCTION_EDEFAULT, oldMechanicalReductionESet));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public boolean isSetMechanicalReduction() {
		return mechanicalReductionESet;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public String getName() {
		return name;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setName(String newName) {
		String oldName = name;
		name = newName;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, KinematicsPackage.ACTUATOR_TRANSMISSION__NAME, oldName, name));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case KinematicsPackage.ACTUATOR_TRANSMISSION__MECHANICAL_REDUCTION:
				return getMechanicalReduction();
			case KinematicsPackage.ACTUATOR_TRANSMISSION__NAME:
				return getName();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
			case KinematicsPackage.ACTUATOR_TRANSMISSION__MECHANICAL_REDUCTION:
				setMechanicalReduction((Double)newValue);
				return;
			case KinematicsPackage.ACTUATOR_TRANSMISSION__NAME:
				setName((String)newValue);
				return;
		}
		super.eSet(featureID, newValue);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eUnset(int featureID) {
		switch (featureID) {
			case KinematicsPackage.ACTUATOR_TRANSMISSION__MECHANICAL_REDUCTION:
				unsetMechanicalReduction();
				return;
			case KinematicsPackage.ACTUATOR_TRANSMISSION__NAME:
				setName(NAME_EDEFAULT);
				return;
		}
		super.eUnset(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
			case KinematicsPackage.ACTUATOR_TRANSMISSION__MECHANICAL_REDUCTION:
				return isSetMechanicalReduction();
			case KinematicsPackage.ACTUATOR_TRANSMISSION__NAME:
				return NAME_EDEFAULT == null ? name != null : !NAME_EDEFAULT.equals(name);
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String toString() {
		if (eIsProxy()) return super.toString();

		StringBuilder result = new StringBuilder(super.toString());
		result.append(" (mechanicalReduction: ");
		if (mechanicalReductionESet) result.append(mechanicalReduction); else result.append("<unset>");
		result.append(", name: ");
		result.append(name);
		result.append(')');
		return result.toString();
	}

} //ActuatorTransmissionImpl
