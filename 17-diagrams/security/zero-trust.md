# Zero Trust Architecture (NIST SP 800-207)

Comprehensive Zero Trust Architecture establishing continuous dynamic verification, policy engine evaluation, and identity-aware micro-segmentation across untrusted networks.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph SubjectZone ["Subject Context"]
        User["Corporate User / Remote Worker"]
        Device["Managed Workstation (EDR Healthy)"]
        User --> Device
    end

    subgraph ControlPlane ["Zero Trust Control Plane"]
        PEP["Policy Enforcement Point (PEP)<br/>[Identity Aware Proxy / Envoy]"]
        PDP["Policy Decision Point (PDP)"]
        PE["Policy Engine<br/>[Risk Assessment / Rules]"]
        PA["Policy Administrator<br/>[Session Token Issuer]"]
        
        PDP --> PE
        PDP --> PA
    end

    subgraph SignalsPlane ["Continuous Context Signals"]
        IDP["Enterprise IdP<br/>[Azure AD / Okta]"]
        EDR["Device Posture / EDR<br/>[CrowdStrike / Defender]"]
        SIEM["Threat Intel / SIEM"]
        HR["HR / Directory Store"]
        
        IDP --> PDP
        EDR --> PDP
        SIEM --> PDP
        HR --> PDP
    end

    subgraph DataPlane ["Target Enterprise Resource (Data Plane)"]
        AppSvc["Internal Core Banking Service"]
        DB[(Restricted Ledger DB)]
        AppSvc --> DB
    end

    Device -->|"1. Access Request (TLS 1.3)"| PEP
    PEP -->|"2. Query Authorization Decision"| PDP
    PA -.->|"3. Issue Short-Lived Credential / mTLS Cert"| PEP
    PEP -->|"4. Allow Inspected & Segregated Traffic"| AppSvc

    classDef control fill:#fbf0ea,stroke:#c44601,stroke-width:2px;
    classDef signal fill:#e8f4f8,stroke:#007791,stroke-width:2px;
    classDef data fill:#edf7ed,stroke:#2e7d32,stroke-width:2px;
    class PEP,PDP,PE,PA control;
    class IDP,EDR,SIEM,HR signal;
    class AppSvc,DB data;
```

## PlantUML Specification

```plantuml
@startuml
skinparam handwritten false
skinparam monochrome false
skinparam packageStyle rectangle

actor "Corporate User" as user
component "Managed Device" as dev
component "Policy Enforcement Point (PEP)" as pep
component "Policy Decision Point (PDP)" as pdp
database "IdP & Posture Engine" as signals
component "Target Resource" as target

user -> dev : Authenticates
dev -> pep : 1. Access Request (mTLS)
pep -> pdp : 2. Evaluate Context (User, Device, Posture)
pdp <-> signals : Query Real-time Context
pdp -> pep : 3. Allow Access (Time-bound ticket)
pep -> target : 4. Forward Authorized Traffic
@enduml
```

## Architectural Design Considerations

* **Never Trust, Always Verify**: Network locality provides zero implicit trust; every transaction is authenticated, authorized, and encrypted end-to-end.
* **Continuous Adaptive Evaluation**: Sessions are reassessed in real time if device compliance fails (e.g., EDR disabled or impossible travel detected).
* **Least Privilege Access**: Permissions are granted per session and per resource rather than broad subnet-level permissions.

## Related Documentation & Patterns

* [Identity Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/identity-flow.md)
* [Trust Boundaries](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/trust-boundaries.md)
* [Network Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/network-security.md)
