# Enterprise Security Architecture Diagram Template

Production-ready, copy-pasteable boilerplate template for authoring enterprise security architectures, trust boundaries, and credential flows.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph UntrustedZone ["Zone 0: Public / Untrusted Zone"]
        Client["External Client / Public User"]
    end

    subgraph PerimeterZone ["Zone 1: Perimeter DMZ"]
        WAF["Web Application Firewall (WAF)"]
        IngressProxy["Ingress Gateway (TLS Termination)"]
        Client -->|"HTTPS / TLS 1.3"| WAF
        WAF --> IngressProxy
    end

    subgraph SecureCoreZone ["Zone 2: Secure Application Zone"]
        AuthPDP["Policy Decision Point (PDP / IdP)"]
        AppService["Application Microservice (PEP)"]
        IngressProxy -->|"Inspect JWT & Claims"| AuthPDP
        IngressProxy -->|"Forward (mTLS)"| AppService
    end

    subgraph DataVaultZone ["Zone 3: Restricted Data Vault"]
        Database[(Encrypted DB Cluster)]
        KMS["Enterprise Key Management (KMS)"]
        AppService -->|"Encrypted Queries"| Database
        Database -.->|"Envelope Key Decryption"| KMS
    end

    classDef untrusted fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef dmz fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef core fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef vault fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;
    class Client untrusted;
    class WAF,IngressProxy dmz;
    class AuthPDP,AppService core;
    class Database,KMS vault;
```

## PlantUML Specification

```plantuml
@startuml
package "Zone 0: Untrusted" {
  [Client]
}
package "Zone 1: DMZ" {
  [WAF & Ingress]
}
package "Zone 2: Internal Services" {
  [Microservices]
}
package "Zone 3: Data Vault" {
  database "Encrypted Database"
}
[Client] --> [WAF & Ingress] : TLS 1.3
[WAF & Ingress] --> [Microservices] : mTLS + Token Check
[Microservices] --> [Encrypted Database] : Restricted Port Access
@enduml
```

## Architectural Design Considerations

* **Copy and Adapt**: Use this template as the starting baseline for creating new architecture security diagrams across projects.
* **Consistent Color Palette**: Red (#ffebee) for untrusted zones, Orange (#fff3e0) for DMZ, Green (#e8f5e9) for application zones, and Purple (#f3e5f5) for restricted vaults.
* **Clarity of Boundaries**: Explicitly outline perimeter transitions using dashed subgraphs and numbered sequence flows.

## Related Documentation & Patterns

* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
* [Trust Boundaries](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/trust-boundaries.md)
* [Security Checklists](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/checklists.md)
