/**
 */
package kinematics;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Actuator Transmission</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link kinematics.ActuatorTransmission#getMechanicalReduction <em>Mechanical Reduction</em>}</li>
 *   <li>{@link kinematics.ActuatorTransmission#getName <em>Name</em>}</li>
 * </ul>
 *
 * @see kinematics.KinematicsPackage#getActuatorTransmission()
 * @model
 * @generated
 */
public interface ActuatorTransmission extends EObject {
	/**
	 * Returns the value of the '<em><b>Mechanical Reduction</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Mechanical Reduction</em>' attribute.
	 * @see #isSetMechanicalReduction()
	 * @see #unsetMechanicalReduction()
	 * @see #setMechanicalReduction(double)
	 * @see kinematics.KinematicsPackage#getActuatorTransmission_MechanicalReduction()
	 * @model unsettable="true" required="true"
	 * @generated
	 */
	double getMechanicalReduction();

	/**
	 * Sets the value of the '{@link kinematics.ActuatorTransmission#getMechanicalReduction <em>Mechanical Reduction</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Mechanical Reduction</em>' attribute.
	 * @see #isSetMechanicalReduction()
	 * @see #unsetMechanicalReduction()
	 * @see #getMechanicalReduction()
	 * @generated
	 */
	void setMechanicalReduction(double value);

	/**
	 * Unsets the value of the '{@link kinematics.ActuatorTransmission#getMechanicalReduction <em>Mechanical Reduction</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #isSetMechanicalReduction()
	 * @see #getMechanicalReduction()
	 * @see #setMechanicalReduction(double)
	 * @generated
	 */
	void unsetMechanicalReduction();

	/**
	 * Returns whether the value of the '{@link kinematics.ActuatorTransmission#getMechanicalReduction <em>Mechanical Reduction</em>}' attribute is set.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return whether the value of the '<em>Mechanical Reduction</em>' attribute is set.
	 * @see #unsetMechanicalReduction()
	 * @see #getMechanicalReduction()
	 * @see #setMechanicalReduction(double)
	 * @generated
	 */
	boolean isSetMechanicalReduction();

	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see kinematics.KinematicsPackage#getActuatorTransmission_Name()
	 * @model required="true"
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link kinematics.ActuatorTransmission#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

} // ActuatorTransmission
