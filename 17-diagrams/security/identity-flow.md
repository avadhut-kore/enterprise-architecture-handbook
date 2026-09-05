# Enterprise Identity Lifecycle & Federation Flow

End-to-end identity synchronization, automated SCIM provisioning, and cross-domain enterprise federation across disparate corporate directories.

## Mermaid Architecture Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Employee as New Hire
    participant HRIS as HR System (Workday)
    participant IGA as Identity Governance (SailPoint)
    participant IdP as Enterprise IdP (Entra ID)
    participant TargetApp as SaaS / Cloud App (AWS / Salesforce)

    Employee->>HRIS: Onboarded into Corporate HR
    HRIS->>IGA: Trigger Worker Created Webhook
    Note over IGA: Evaluate Role Matrix & Birthright Policies
    IGA->>IdP: Create User Object via Graph API
    IdP->>TargetApp: SCIM 2.0 Provisioning (User & Groups)
    TargetApp-->>IdP: Account Provisioned (201 Created)
    IdP-->>IGA: Sync Status Confirmation
    IGA-->>HRIS: Employee Identity Active
    
    Employee->>TargetApp: Initial SSO Login Attempt
    TargetApp->>IdP: SAML / OIDC AuthN Request
    IdP->>Employee: Challenge for MFA & Device Health
    Employee-->>IdP: Provide Biometric FIDO2 Assertion
    IdP-->>TargetApp: Signed Assertion / Claims Token
    TargetApp-->>Employee: Session Established (RBAC applied)
```

## PlantUML Specification

```plantuml
@startuml
autonumber
actor "Employee" as emp
participant "Workday (HRIS)" as hr
participant "SailPoint (IGA)" as iga
participant "Okta (Enterprise IdP)" as idp
participant "Cloud App" as app

hr -> iga : Employee Created Event
iga -> iga : Compute Role Mappings & Approvals
iga -> idp : Provision Directory Account
idp -> app : SCIM 2.0 Provision User
emp -> app : Access Application (SSO)
app -> idp : Authenticate User
idp -> emp : Prompt MFA Challenge
emp -> idp : FIDO2 Passkey
idp -> app : SAML Assertion / JWT
app -> emp : Login Granted
@enduml
```

## Architectural Design Considerations

* **Authoritative Source of Truth**: HRIS (e.g., Workday) drives the identity lifecycle; no manual user creation in downstream applications.
* **Just-In-Time (JIT) vs SCIM**: Prefer automated SCIM 2.0 provisioning over JIT to ensure instant deprovisioning when an employee departs.
* **Auditability**: Every role mutation and account lifecycle event must emit structured audit events to SIEM.

## Related Documentation & Patterns

* [IAM Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/iam.md)
* [OAuth 2.0](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/oauth2.md)
* [Privileged Access Management](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/privileged-access.md)
