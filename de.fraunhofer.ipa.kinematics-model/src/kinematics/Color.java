/**
 */
package kinematics;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Color</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link kinematics.Color#getRgba <em>Rgba</em>}</li>
 * </ul>
 *
 * @see kinematics.KinematicsPackage#getColor()
 * @model
 * @generated
 */
public interface Color extends EObject {
	/**
	 * Returns the value of the '<em><b>Rgba</b></em>' attribute.
	 * The default value is <code>"0 0 0 0"</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Rgba</em>' attribute.
	 * @see #isSetRgba()
	 * @see #unsetRgba()
	 * @see #setRgba(String)
	 * @see kinematics.KinematicsPackage#getColor_Rgba()
	 * @model default="0 0 0 0" unsettable="true"
	 * @generated
	 */
	String getRgba();

	/**
	 * Sets the value of the '{@link kinematics.Color#getRgba <em>Rgba</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Rgba</em>' attribute.
	 * @see #isSetRgba()
	 * @see #unsetRgba()
	 * @see #getRgba()
	 * @generated
	 */
	void setRgba(String value);

	/**
	 * Unsets the value of the '{@link kinematics.Color#getRgba <em>Rgba</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #isSetRgba()
	 * @see #getRgba()
	 * @see #setRgba(String)
	 * @generated
	 */
	void unsetRgba();

	/**
	 * Returns whether the value of the '{@link kinematics.Color#getRgba <em>Rgba</em>}' attribute is set.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return whether the value of the '<em>Rgba</em>' attribute is set.
	 * @see #unsetRgba()
	 * @see #getRgba()
	 * @see #setRgba(String)
	 * @generated
	 */
	boolean isSetRgba();

} // Color
