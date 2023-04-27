/**
 */
package kinematics;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Material</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link kinematics.Material#getColor <em>Color</em>}</li>
 *   <li>{@link kinematics.Material#getTexture <em>Texture</em>}</li>
 *   <li>{@link kinematics.Material#getName <em>Name</em>}</li>
 * </ul>
 *
 * @see kinematics.KinematicsPackage#getMaterial()
 * @model
 * @generated
 */
public interface Material extends EObject {
	/**
	 * Returns the value of the '<em><b>Color</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Color</em>' containment reference.
	 * @see #setColor(Color)
	 * @see kinematics.KinematicsPackage#getMaterial_Color()
	 * @model containment="true"
	 * @generated
	 */
	Color getColor();

	/**
	 * Sets the value of the '{@link kinematics.Material#getColor <em>Color</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Color</em>' containment reference.
	 * @see #getColor()
	 * @generated
	 */
	void setColor(Color value);

	/**
	 * Returns the value of the '<em><b>Texture</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Texture</em>' containment reference.
	 * @see #setTexture(Texture)
	 * @see kinematics.KinematicsPackage#getMaterial_Texture()
	 * @model containment="true"
	 * @generated
	 */
	Texture getTexture();

	/**
	 * Sets the value of the '{@link kinematics.Material#getTexture <em>Texture</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Texture</em>' containment reference.
	 * @see #getTexture()
	 * @generated
	 */
	void setTexture(Texture value);

	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see kinematics.KinematicsPackage#getMaterial_Name()
	 * @model
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link kinematics.Material#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

} // Material
