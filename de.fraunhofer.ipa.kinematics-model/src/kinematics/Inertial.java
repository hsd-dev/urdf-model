/**
 */
package kinematics;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Inertial</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link kinematics.Inertial#getOrigin <em>Origin</em>}</li>
 *   <li>{@link kinematics.Inertial#getMass <em>Mass</em>}</li>
 *   <li>{@link kinematics.Inertial#getInertia <em>Inertia</em>}</li>
 * </ul>
 *
 * @see kinematics.KinematicsPackage#getInertial()
 * @model
 * @generated
 */
public interface Inertial extends EObject {
	/**
	 * Returns the value of the '<em><b>Origin</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Origin</em>' containment reference.
	 * @see #setOrigin(Pose)
	 * @see kinematics.KinematicsPackage#getInertial_Origin()
	 * @model containment="true"
	 * @generated
	 */
	Pose getOrigin();

	/**
	 * Sets the value of the '{@link kinematics.Inertial#getOrigin <em>Origin</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Origin</em>' containment reference.
	 * @see #getOrigin()
	 * @generated
	 */
	void setOrigin(Pose value);

	/**
	 * Returns the value of the '<em><b>Mass</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Mass</em>' containment reference.
	 * @see #setMass(Mass)
	 * @see kinematics.KinematicsPackage#getInertial_Mass()
	 * @model containment="true"
	 * @generated
	 */
	Mass getMass();

	/**
	 * Sets the value of the '{@link kinematics.Inertial#getMass <em>Mass</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Mass</em>' containment reference.
	 * @see #getMass()
	 * @generated
	 */
	void setMass(Mass value);

	/**
	 * Returns the value of the '<em><b>Inertia</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Inertia</em>' containment reference.
	 * @see #setInertia(Inertia)
	 * @see kinematics.KinematicsPackage#getInertial_Inertia()
	 * @model containment="true"
	 * @generated
	 */
	Inertia getInertia();

	/**
	 * Sets the value of the '{@link kinematics.Inertial#getInertia <em>Inertia</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Inertia</em>' containment reference.
	 * @see #getInertia()
	 * @generated
	 */
	void setInertia(Inertia value);

} // Inertial
