/**
 */
package kinematics;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Link</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link kinematics.Link#getInertial <em>Inertial</em>}</li>
 *   <li>{@link kinematics.Link#getVisual <em>Visual</em>}</li>
 *   <li>{@link kinematics.Link#getCollision <em>Collision</em>}</li>
 *   <li>{@link kinematics.Link#getName <em>Name</em>}</li>
 *   <li>{@link kinematics.Link#getType <em>Type</em>}</li>
 * </ul>
 *
 * @see kinematics.KinematicsPackage#getLink()
 * @model
 * @generated
 */
public interface Link extends EObject {
	/**
	 * Returns the value of the '<em><b>Inertial</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Inertial</em>' containment reference.
	 * @see #setInertial(Inertial)
	 * @see kinematics.KinematicsPackage#getLink_Inertial()
	 * @model containment="true"
	 * @generated
	 */
	Inertial getInertial();

	/**
	 * Sets the value of the '{@link kinematics.Link#getInertial <em>Inertial</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Inertial</em>' containment reference.
	 * @see #getInertial()
	 * @generated
	 */
	void setInertial(Inertial value);

	/**
	 * Returns the value of the '<em><b>Visual</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Visual</em>' containment reference.
	 * @see #setVisual(Visual)
	 * @see kinematics.KinematicsPackage#getLink_Visual()
	 * @model containment="true"
	 * @generated
	 */
	Visual getVisual();

	/**
	 * Sets the value of the '{@link kinematics.Link#getVisual <em>Visual</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Visual</em>' containment reference.
	 * @see #getVisual()
	 * @generated
	 */
	void setVisual(Visual value);

	/**
	 * Returns the value of the '<em><b>Collision</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Collision</em>' containment reference.
	 * @see #setCollision(Collision)
	 * @see kinematics.KinematicsPackage#getLink_Collision()
	 * @model containment="true"
	 * @generated
	 */
	Collision getCollision();

	/**
	 * Sets the value of the '{@link kinematics.Link#getCollision <em>Collision</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Collision</em>' containment reference.
	 * @see #getCollision()
	 * @generated
	 */
	void setCollision(Collision value);

	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see kinematics.KinematicsPackage#getLink_Name()
	 * @model required="true"
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link kinematics.Link#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

	/**
	 * Returns the value of the '<em><b>Type</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Type</em>' attribute.
	 * @see #setType(String)
	 * @see kinematics.KinematicsPackage#getLink_Type()
	 * @model
	 * @generated
	 */
	String getType();

	/**
	 * Sets the value of the '{@link kinematics.Link#getType <em>Type</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Type</em>' attribute.
	 * @see #getType()
	 * @generated
	 */
	void setType(String value);

} // Link
