# Enterprise Demilitarized Zone (DMZ) Perimeter Architecture

Network perimeter architecture establishing a hardened Demilitarized Zone (DMZ) isolating external untrusted networks from internal corporate assets.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph UntrustedInternet ["Untrusted External World"]
        PublicUsers["Public Internet Users"]
    end

    subgraph PerimeterFirewalls ["Perimeter Security Layer"]
        OuterFW["External Firewall (Palo Alto NGFW Cluster)"]
        PublicUsers --> OuterFW
    end

    subgraph DMZZone ["DMZ / Perimeter Network (Subnet: 10.0.10.0/24)"]
        WAFProxy["Reverse Proxy & WAF (Nginx / Envoy)"]
        PublicDNS["Public Authoritative DNS"]
        VPNServer["Client VPN Endpoint"]
        
        OuterFW --> WAFProxy
        OuterFW --> PublicDNS
        OuterFW --> VPNServer
    end

    subgraph InternalFirewalls ["Internal Perimeter Security"]
        InnerFW["Internal Firewall (Strict Stateful Inspection)"]
        WAFProxy --> InnerFW
        VPNServer --> InnerFW
    end

    subgraph TrustedCorporateZone ["Trusted Internal Corporate Estate"]
        AppServers["Internal Core Applications (10.1.0.0/16)"]
        DataVault[("Restricted Databases (10.2.0.0/16)")]
        InnerFW --> AppServers
        AppServers --> DataVault
    end

    classDef untrusted fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef dmz fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef trusted fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class PublicUsers untrusted;
    class OuterFW,InnerFW,WAFProxy,PublicDNS,VPNServer dmz;
    class AppServers,DataVault trusted;
```

## PlantUML Specification

```plantuml
@startuml
package "External Internet" {
  actor "User" as user
}
package "DMZ Zone" {
  component "Outer Firewall" as fw1
  component "Reverse Proxy / WAF" as proxy
  component "Inner Firewall" as fw2
}
package "Internal Trust Zone" {
  component "App Cluster" as app
  database "Database" as db
}

user -> fw1 : HTTPS
fw1 -> proxy : Forward to DMZ
proxy -> fw2 : Strict inspected call
fw2 -> app : Forward
app -> db : SQL
@enduml
```

## Architectural Design Considerations
* **Dual-Firewall Architecture**: Employ two distinct firewall layers (ideally from different vendors) to prevent a single configuration defect or CVE from breaching the internal network.
* **No Direct Inbound to Internal**: External internet traffic is strictly terminated in the DMZ; zero direct inbound routing to internal application subnets is permitted.
* **Session Break**: All proxy appliances in the DMZ must terminate client TCP connections and initiate brand-new outbound connections toward internal applications.

## Related Documentation & Patterns
* [API Gateway Network](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/api-gateway-network.md)
* [Ingress & Egress](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/ingress-egress.md)
* [Security: Trust Boundaries](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/trust-boundaries.md)
