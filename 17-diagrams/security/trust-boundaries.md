# Security Trust Boundaries & Zone Isolation Architecture

Multi-zone security segmentation detailing trust levels, data validation checkpoints, and sanitization gates crossing perimeter boundaries.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph Zone0 ["Zone 0: Public / Untrusted Zone"]
        WebUsers["Public Internet Users & External APIs"]
    end

    subgraph TrustBoundary1 ["Trust Boundary A (Perimeter Gate)"]
        EdgeWAF["Edge WAF & DDoS Scrubbing"]
    end

    subgraph Zone1 ["Zone 1: DMZ / Presentation Tier"]
        ReverseProxy["Ingress Reverse Proxy / Envoy"]
        StaticCDN["Static Assets / Public Web Portal"]
    end

    subgraph TrustBoundary2 ["Trust Boundary B (Authentication Gate)"]
        AuthTokenInspection["OAuth2 JWT & mTLS Enforcer"]
    end

    subgraph Zone2 ["Zone 2: Application / Processing Tier"]
        CoreBusinessServices["Microservices (Payments, Orders, Ledger)"]
    end

    subgraph TrustBoundary3 ["Trust Boundary C (Data Isolation Gate)"]
        DBFirewall["Database Firewall / Privilege Proxy"]
    end

    subgraph Zone3 ["Zone 3: Restricted Data Vault (Crown Jewels)"]
        VaultDB[(Encrypted Core Database)]
        HSM["Hardware Security Module (KMS Keys)"]
    end

    WebUsers -->|"Untrusted Data"| EdgeWAF
    EdgeWAF --> ReverseProxy
    ReverseProxy --> AuthTokenInspection
    AuthTokenInspection --> CoreBusinessServices
    CoreBusinessServices --> DBFirewall
    DBFirewall --> VaultDB
    DBFirewall --> HSM

    classDef z0 fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef z1 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;
    classDef z2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef z3 fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px;
    class WebUsers z0;
    class ReverseProxy,StaticCDN z1;
    class CoreBusinessServices z2;
    class VaultDB,HSM z3;
```

## PlantUML Specification

```plantuml
@startuml
node "Zone 0: Untrusted Internet" {
  [Client]
}
node "Zone 1: DMZ" {
  [Ingress Proxy]
}
node "Zone 2: Core Microservices" {
  [Business Logic]
}
node "Zone 3: Vault / Crown Jewels" {
  database "Encrypted Database"
}

[Client] --> [Ingress Proxy] : Trust Boundary 1 (TLS Termination & WAF)
[Ingress Proxy] --> [Business Logic] : Trust Boundary 2 (JWT & mTLS)
[Business Logic] --> [Encrypted Database] : Trust Boundary 3 (Strict Port & Credential Check)
@enduml
```

## Architectural Design Considerations

* **Explicit Sanitization at Boundaries**: Never trust data originating from an adjacent lower-trust zone without schema validation and input sanitization.
* **No Transitive Trust**: Access to Zone 1 (DMZ) does not grant implicit access to Zone 3 (Data Vault); each boundary must enforce its own authentication and authorization.
* **Blast Radius Containment**: Isolate compromised containers within their respective trust zones using kernel-level sandboxing (gVisor / Firecracker).

## Related Documentation & Patterns

* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
* [Threat Model](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/threat-model.md)
* [Network Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/network-security.md)
