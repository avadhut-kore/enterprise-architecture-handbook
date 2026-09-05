# Identity & Access Management (IAM) Reference Architecture

Comprehensive enterprise IAM ecosystem uniting workforce identity, customer IAM (CIAM), privileged access, and automated governance.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph UsersLayer ["Identity Personas"]
        Internal["Workforce Employees & Contractors"]
        External["Customers & External Partners"]
        Machines["Non-Human Identities (Workloads / CI/CD)"]
    end

    subgraph AccessMgmt ["Access & Authentication Tier"]
        SSO["Enterprise SSO Gateway"]
        CIAM["Customer IAM Portal"]
        SPIFFE["Workload Identity Broker (SPIFFE/SPIRE)"]
    end

    subgraph GovernanceTier ["IGA & Privileged Management"]
        IGA["Identity Governance & Administration (SailPoint)"]
        PAM["Privileged Access Management (CyberArk)"]
        Directory["Authoritative Directory (Active Directory / Entra)"]
    end

    subgraph ResourceTier ["Protected Cloud & On-Premises Estates"]
        CloudAWS["AWS Multi-Account Organization"]
        CloudAzure["Azure Tenancy & Subscriptions"]
        LegacyApps["On-Premises ERP & Mainframes"]
    end

    Internal --> SSO
    Internal --> PAM
    External --> CIAM
    Machines --> SPIFFE

    SSO --> Directory
    IGA --> Directory
    PAM --> Directory
    CIAM --> Directory

    SSO -->|"SAML / OIDC"| CloudAWS
    SSO -->|"SAML / OIDC"| CloudAzure
    PAM -->|"JIT Vaulting & Session Record"| LegacyApps
    SPIFFE -->|"Workload mTLS"| CloudAWS

    classDef user fill:#e0f7fa,stroke:#00838f,stroke-width:2px;
    classDef core fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef res fill:#f1f8e9,stroke:#558b2f,stroke-width:2px;
    class Internal,External,Machines user;
    class SSO,CIAM,SPIFFE,IGA,PAM,Directory core;
    class CloudAWS,CloudAzure,LegacyApps res;
```

## PlantUML Specification

```plantuml
@startuml
package "Personas" {
  actor "Employee" as emp
  actor "Customer" as cust
  component "Service Workload" as machine
}
package "IAM Core Services" {
  component "Enterprise SSO" as sso
  component "Customer IAM" as ciam
  component "Workload Identity" as spire
  component "Identity Governance (IGA)" as iga
  component "Privileged Access (PAM)" as pam
}
package "Enterprise Target Systems" {
  component "Cloud Platforms (AWS/Azure)" as cloud
  component "Internal Applications" as apps
}

emp --> sso
emp --> pam
cust --> ciam
machine --> spire
sso --> iga
iga --> cloud
sso --> cloud
pam --> apps
@enduml
```

## Architectural Design Considerations

* **Machine Identity Growth**: Non-human identities (service accounts, API keys, certs) outnumber humans 45:1; treat machine identity governance with equal priority.
* **Access Certification**: Schedule automated quarterly access recertification campaigns via IGA tools for regulatory frameworks (SOX, SOC 2, HIPAA).
* **Separation of Duties (SoD)**: Enforce strict architectural segregation preventing single users from both developing and approving production releases.

## Related Documentation & Patterns

* [Identity Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/identity-flow.md)
* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
* [Privileged Access](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/privileged-access.md)
