# Enterprise Multi-Factor Authentication (MFA) & Passwordless Flow

FIDO2 / WebAuthn passwordless authentication architecture combined with adaptive risk analysis and continuous biometric challenges.

## Mermaid Architecture Diagram

```mermaid
sequenceDiagram
    autonumber
    actor User as Enterprise Employee
    participant Client as Browser / Mobile App
    participant FIDO as Hardware Security Key (YubiKey / TouchID)
    participant AuthEngine as Adaptive Auth Engine
    participant RiskScore as Real-time Threat Intelligence

    User->>Client: Enter Corporate Username / UPN
    Client->>AuthEngine: POST /auth/initiate (user identifier)
    AuthEngine->>RiskScore: Evaluate IP, Geolocation, Device Trust
    RiskScore-->>AuthEngine: Risk Level: LOW (Trusted Corporate Device)
    
    AuthEngine->>AuthEngine: Generate Cryptographic Challenge (Nonce)
    AuthEngine-->>Client: Return Challenge + Allowed Credentials (WebAuthn)
    
    Client->>FIDO: navigator.credentials.get(challenge)
    FIDO->>User: Request Biometric Gesture / Physical Touch
    User-->>FIDO: Provide Fingerprint / Touch
    FIDO-->>Client: Signed ClientDataJSON & AuthenticatorData (Private Key Signature)
    
    Client->>AuthEngine: POST /auth/verify (Assertion Signature)
    Note over AuthEngine: Verify Signature using Stored Public Key
    AuthEngine-->>Client: Issue Secure Session Cookie / OIDC Auth Code
    Client-->>User: Granted Direct Access to Workspace
```

## PlantUML Specification

```plantuml
@startuml
autonumber
actor User
participant "Browser" as browser
participant "FIDO2 Key / TPM" as fido
participant "Auth Engine" as server
participant "Risk Engine" as risk

User -> browser : Enter Username
browser -> server : Initiate Login
server -> risk : Check IP, Device Posture, Behavioral Telemetry
server -> browser : WebAuthn Challenge (nonce)
browser -> fido : Prompt Biometric Touch
User -> fido : User Presence / Biometric verified
fido -> browser : Return Signed Assertion
browser -> server : Complete Authentication
server -> browser : Issue Session
@enduml
```

## Architectural Design Considerations

* **Phishing Resistance**: Prioritize FIDO2 / WebAuthn passkeys over SMS, voice, or push notifications (which are vulnerable to MFA fatigue and adversary-in-the-middle).
* **Step-Up Authentication**: Trigger higher-level verification dynamically when attempting high-privilege operations (e.g., wire transfers, firewall rule modifications).
* **Fallback Hardening**: Ensure account recovery processes require rigorous out-of-band verification to prevent social engineering helpdesk attacks.

## Related Documentation & Patterns

* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
* [Identity Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/identity-flow.md)
* [Privileged Access](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/privileged-access.md)
