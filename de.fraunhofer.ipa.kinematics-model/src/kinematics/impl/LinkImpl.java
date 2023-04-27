/**
 */
package kinematics.impl;

import kinematics.Collision;
import kinematics.Inertial;
import kinematics.KinematicsPackage;
import kinematics.Link;
import kinematics.Visual;

import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;

import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Link</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link kinematics.impl.LinkImpl#getInertial <em>Inertial</em>}</li>
 *   <li>{@link kinematics.impl.LinkImpl#getVisual <em>Visual</em>}</li>
 *   <li>{@link kinematics.impl.LinkImpl#getCollision <em>Collision</em>}</li>
 *   <li>{@link kinematics.impl.LinkImpl#getName <em>Name</em>}</li>
 *   <li>{@link kinematics.impl.LinkImpl#getType <em>Type</em>}</li>
 * </ul>
 *
 * @generated
 */
public class LinkImpl extends MinimalEObjectImpl.Container implements Link {
	/**
	 * The cached value of the '{@link #getInertial() <em>Inertial</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getInertial()
	 * @generated
	 * @ordered
	 */
	protected Inertial inertial;

	/**
	 * The cached value of the '{@link #getVisual() <em>Visual</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getVisual()
	 * @generated
	 * @ordered
	 */
	protected Visual visual;

	/**
	 * The cached value of the '{@link #getCollision() <em>Collision</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getCollision()
	 * @generated
	 * @ordered
	 */
	protected Collision collision;

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
	 * The default value of the '{@link #getType() <em>Type</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getType()
	 * @generated
	 * @ordered
	 */
	protected static final String TYPE_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getType() <em>Type</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getType()
	 * @generated
	 * @ordered
	 */
	protected String type = TYPE_EDEFAULT;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected LinkImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return KinematicsPackage.Literals.LINK;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Inertial getInertial() {
		return inertial;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public NotificationChain basicSetInertial(Inertial newInertial, NotificationChain msgs) {
		Inertial oldInertial = inertial;
		inertial = newInertial;
		if (eNotificationRequired()) {
			ENotificationImpl notification = new ENotificationImpl(this, Notification.SET, KinematicsPackage.LINK__INERTIAL, oldInertial, newInertial);
			if (msgs == null) msgs = notification; else msgs.add(notification);
		}
		return msgs;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setInertial(Inertial newInertial) {
		if (newInertial != inertial) {
			NotificationChain msgs = null;
			if (inertial != null)
				msgs = ((InternalEObject)inertial).eInverseRemove(this, EOPPOSITE_FEATURE_BASE - KinematicsPackage.LINK__INERTIAL, null, msgs);
			if (newInertial != null)
				msgs = ((InternalEObject)newInertial).eInverseAdd(this, EOPPOSITE_FEATURE_BASE - KinematicsPackage.LINK__INERTIAL, null, msgs);
			msgs = basicSetInertial(newInertial, msgs);
			if (msgs != null) msgs.dispatch();
		}
		else if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, KinematicsPackage.LINK__INERTIAL, newInertial, newInertial));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Visual getVisual() {
		return visual;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public NotificationChain basicSetVisual(Visual newVisual, NotificationChain msgs) {
		Visual oldVisual = visual;
		visual = newVisual;
		if (eNotificationRequired()) {
			ENotificationImpl notification = new ENotificationImpl(this, Notification.SET, KinematicsPackage.LINK__VISUAL, oldVisual, newVisual);
			if (msgs == null) msgs = notification; else msgs.add(notification);
		}
		return msgs;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setVisual(Visual newVisual) {
		if (newVisual != visual) {
			NotificationChain msgs = null;
			if (visual != null)
				msgs = ((InternalEObject)visual).eInverseRemove(this, EOPPOSITE_FEATURE_BASE - KinematicsPackage.LINK__VISUAL, null, msgs);
			if (newVisual != null)
				msgs = ((InternalEObject)newVisual).eInverseAdd(this, EOPPOSITE_FEATURE_BASE - KinematicsPackage.LINK__VISUAL, null, msgs);
			msgs = basicSetVisual(newVisual, msgs);
			if (msgs != null) msgs.dispatch();
		}
		else if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, KinematicsPackage.LINK__VISUAL, newVisual, newVisual));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Collision getCollision() {
		return collision;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public NotificationChain basicSetCollision(Collision newCollision, NotificationChain msgs) {
		Collision oldCollision = collision;
		collision = newCollision;
		if (eNotificationRequired()) {
			ENotificationImpl notification = new ENotificationImpl(this, Notification.SET, KinematicsPackage.LINK__COLLISION, oldCollision, newCollision);
			if (msgs == null) msgs = notification; else msgs.add(notification);
		}
		return msgs;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setCollision(Collision newCollision) {
		if (newCollision != collision) {
			NotificationChain msgs = null;
			if (collision != null)
				msgs = ((InternalEObject)collision).eInverseRemove(this, EOPPOSITE_FEATURE_BASE - KinematicsPackage.LINK__COLLISION, null, msgs);
			if (newCollision != null)
				msgs = ((InternalEObject)newCollision).eInverseAdd(this, EOPPOSITE_FEATURE_BASE - KinematicsPackage.LINK__COLLISION, null, msgs);
			msgs = basicSetCollision(newCollision, msgs);
			if (msgs != null) msgs.dispatch();
		}
		else if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, KinematicsPackage.LINK__COLLISION, newCollision, newCollision));
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
			eNotify(new ENotificationImpl(this, Notification.SET, KinematicsPackage.LINK__NAME, oldName, name));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public String getType() {
		return type;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setType(String newType) {
		String oldType = type;
		type = newType;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, KinematicsPackage.LINK__TYPE, oldType, type));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case KinematicsPackage.LINK__INERTIAL:
				return basicSetInertial(null, msgs);
			case KinematicsPackage.LINK__VISUAL:
				return basicSetVisual(null, msgs);
			case KinematicsPackage.LINK__COLLISION:
				return basicSetCollision(null, msgs);
		}
		return super.eInverseRemove(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case KinematicsPackage.LINK__INERTIAL:
				return getInertial();
			case KinematicsPackage.LINK__VISUAL:
				return getVisual();
			case KinematicsPackage.LINK__COLLISION:
				return getCollision();
			case KinematicsPackage.LINK__NAME:
				return getName();
			case KinematicsPackage.LINK__TYPE:
				return getType();
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
			case KinematicsPackage.LINK__INERTIAL:
				setInertial((Inertial)newValue);
				return;
			case KinematicsPackage.LINK__VISUAL:
				setVisual((Visual)newValue);
				return;
			case KinematicsPackage.LINK__COLLISION:
				setCollision((Collision)newValue);
				return;
			case KinematicsPackage.LINK__NAME:
				setName((String)newValue);
				return;
			case KinematicsPackage.LINK__TYPE:
				setType((String)newValue);
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
			case KinematicsPackage.LINK__INERTIAL:
				setInertial((Inertial)null);
				return;
			case KinematicsPackage.LINK__VISUAL:
				setVisual((Visual)null);
				return;
			case KinematicsPackage.LINK__COLLISION:
				setCollision((Collision)null);
				return;
			case KinematicsPackage.LINK__NAME:
				setName(NAME_EDEFAULT);
				return;
			case KinematicsPackage.LINK__TYPE:
				setType(TYPE_EDEFAULT);
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
			case KinematicsPackage.LINK__INERTIAL:
				return inertial != null;
			case KinematicsPackage.LINK__VISUAL:
				return visual != null;
			case KinematicsPackage.LINK__COLLISION:
				return collision != null;
			case KinematicsPackage.LINK__NAME:
				return NAME_EDEFAULT == null ? name != null : !NAME_EDEFAULT.equals(name);
			case KinematicsPackage.LINK__TYPE:
				return TYPE_EDEFAULT == null ? type != null : !TYPE_EDEFAULT.equals(type);
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
		result.append(" (name: ");
		result.append(name);
		result.append(", type: ");
		result.append(type);
		result.append(')');
		return result.toString();
	}

} //LinkImpl
