# Enterprise Authentication Mechanisms (Passwordless, FIDO2, MFA)

## Executive Summary

Traditional passwords are the single greatest attack vector in enterprise computing, responsible for over 80% of data breaches via phishing, credential stuffing, and brute-force attacks. Modern enterprise architecture mandates the transition to **phishing-resistant passwordless authentication**.

---

## 1. Authentication Factor Comparison

| Mechanism | Resistance to Phishing | User Experience | Operational Overhead | Architectural Recommendation |
| :--- | :---: | :---: | :---: | :--- |
| **Passwords** | Zero (Vulnerable) | Terrible | High (Reset tickets) | **Phased Deprecation**: Ban for interactive enterprise logins. |
| **SMS OTP** | Low (SIM swap, phishing) | Moderate | Moderate (SMS telecom costs) | **Prohibited**: Non-compliant with modern NIST 800-63B standards. |
| **TOTP Authenticator Apps** | Moderate (Phishable via reverse proxy) | Moderate | Low | **Transitional**: Acceptable secondary factor during transition. |
| **Push Notifications with Number Matching** | High (Resistant to MFA fatigue) | High | Low | **Approved**: Minimum standard for mobile workforce MFA. |
| **FIDO2 / WebAuthn (Passkeys / YubiKey)** | **Immune to Phishing** | Exceptional (Biometric) | Low | **Gold Standard**: Mandated for all enterprise administrative & core systems. |
