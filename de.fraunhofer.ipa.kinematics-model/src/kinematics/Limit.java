/**
 */
package kinematics;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Limit</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link kinematics.Limit#getEffort <em>Effort</em>}</li>
 *   <li>{@link kinematics.Limit#getLower <em>Lower</em>}</li>
 *   <li>{@link kinematics.Limit#getUpper <em>Upper</em>}</li>
 *   <li>{@link kinematics.Limit#getVelocity <em>Velocity</em>}</li>
 * </ul>
 *
 * @see kinematics.KinematicsPackage#getLimit()
 * @model
 * @generated
 */
public interface Limit extends EObject {
	/**
	 * Returns the value of the '<em><b>Effort</b></em>' attribute.
	 * The default value is <code>"0"</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Effort</em>' attribute.
	 * @see #isSetEffort()
	 * @see #unsetEffort()
	 * @see #setEffort(double)
	 * @see kinematics.KinematicsPackage#getLimit_Effort()
	 * @model default="0" unsettable="true"
	 * @generated
	 */
	double getEffort();

	/**
	 * Sets the value of the '{@link kinematics.Limit#getEffort <em>Effort</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Effort</em>' attribute.
	 * @see #isSetEffort()
	 * @see #unsetEffort()
	 * @see #getEffort()
	 * @generated
	 */
	void setEffort(double value);

	/**
	 * Unsets the value of the '{@link kinematics.Limit#getEffort <em>Effort</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #isSetEffort()
	 * @see #getEffort()
	 * @see #setEffort(double)
	 * @generated
	 */
	void unsetEffort();

	/**
	 * Returns whether the value of the '{@link kinematics.Limit#getEffort <em>Effort</em>}' attribute is set.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return whether the value of the '<em>Effort</em>' attribute is set.
	 * @see #unsetEffort()
	 * @see #getEffort()
	 * @see #setEffort(double)
	 * @generated
	 */
	boolean isSetEffort();

	/**
	 * Returns the value of the '<em><b>Lower</b></em>' attribute.
	 * The default value is <code>"0"</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Lower</em>' attribute.
	 * @see #isSetLower()
	 * @see #unsetLower()
	 * @see #setLower(double)
	 * @see kinematics.KinematicsPackage#getLimit_Lower()
	 * @model default="0" unsettable="true"
	 * @generated
	 */
	double getLower();

	/**
	 * Sets the value of the '{@link kinematics.Limit#getLower <em>Lower</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Lower</em>' attribute.
	 * @see #isSetLower()
	 * @see #unsetLower()
	 * @see #getLower()
	 * @generated
	 */
	void setLower(double value);

	/**
	 * Unsets the value of the '{@link kinematics.Limit#getLower <em>Lower</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #isSetLower()
	 * @see #getLower()
	 * @see #setLower(double)
	 * @generated
	 */
	void unsetLower();

	/**
	 * Returns whether the value of the '{@link kinematics.Limit#getLower <em>Lower</em>}' attribute is set.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return whether the value of the '<em>Lower</em>' attribute is set.
	 * @see #unsetLower()
	 * @see #getLower()
	 * @see #setLower(double)
	 * @generated
	 */
	boolean isSetLower();

	/**
	 * Returns the value of the '<em><b>Upper</b></em>' attribute.
	 * The default value is <code>"0"</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Upper</em>' attribute.
	 * @see #isSetUpper()
	 * @see #unsetUpper()
	 * @see #setUpper(double)
	 * @see kinematics.KinematicsPackage#getLimit_Upper()
	 * @model default="0" unsettable="true"
	 * @generated
	 */
	double getUpper();

	/**
	 * Sets the value of the '{@link kinematics.Limit#getUpper <em>Upper</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Upper</em>' attribute.
	 * @see #isSetUpper()
	 * @see #unsetUpper()
	 * @see #getUpper()
	 * @generated
	 */
	void setUpper(double value);

	/**
	 * Unsets the value of the '{@link kinematics.Limit#getUpper <em>Upper</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #isSetUpper()
	 * @see #getUpper()
	 * @see #setUpper(double)
	 * @generated
	 */
	void unsetUpper();

	/**
	 * Returns whether the value of the '{@link kinematics.Limit#getUpper <em>Upper</em>}' attribute is set.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return whether the value of the '<em>Upper</em>' attribute is set.
	 * @see #unsetUpper()
	 * @see #getUpper()
	 * @see #setUpper(double)
	 * @generated
	 */
	boolean isSetUpper();

	/**
	 * Returns the value of the '<em><b>Velocity</b></em>' attribute.
	 * The default value is <code>"0"</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Velocity</em>' attribute.
	 * @see #isSetVelocity()
	 * @see #unsetVelocity()
	 * @see #setVelocity(double)
	 * @see kinematics.KinematicsPackage#getLimit_Velocity()
	 * @model default="0" unsettable="true"
	 * @generated
	 */
	double getVelocity();

	/**
	 * Sets the value of the '{@link kinematics.Limit#getVelocity <em>Velocity</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Velocity</em>' attribute.
	 * @see #isSetVelocity()
	 * @see #unsetVelocity()
	 * @see #getVelocity()
	 * @generated
	 */
	void setVelocity(double value);

	/**
	 * Unsets the value of the '{@link kinematics.Limit#getVelocity <em>Velocity</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #isSetVelocity()
	 * @see #getVelocity()
	 * @see #setVelocity(double)
	 * @generated
	 */
	void unsetVelocity();

	/**
	 * Returns whether the value of the '{@link kinematics.Limit#getVelocity <em>Velocity</em>}' attribute is set.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return whether the value of the '<em>Velocity</em>' attribute is set.
	 * @see #unsetVelocity()
	 * @see #getVelocity()
	 * @see #setVelocity(double)
	 * @generated
	 */
	boolean isSetVelocity();

} // Limit
