# Enterprise Network Security & Micro-Segmentation Architecture

Multi-tier network defense incorporating Next-Gen Firewalls (NGFW), IDS/IPS, egress traffic proxies, and VPC micro-segmentation.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph InternetZone ["Untrusted Public Internet"]
        Users["Global Web Users"]
    end

    subgraph EdgeSecurityZone ["DMZ & Edge Inspection"]
        EdgeFW["Palo Alto / Fortinet NGFW Cluster"]
        IDS["Intrusion Detection / Prevention (Snort / Suricata)"]
        WAF["Web Application Firewall"]
        
        Users --> EdgeFW
        EdgeFW --> IDS
        IDS --> WAF
    end

    subgraph InternalAppZone ["Internal Trust Zone 2 (Applications)"]
        InternalLB["Internal Network Load Balancer"]
        AppSubnet["Application Tier (Private Subnets)"]
        MicroSeg["Kubernetes NetworkPolicy / Calico CNI"]
        
        WAF --> InternalLB
        InternalLB --> AppSubnet
        AppSubnet --- MicroSeg
    end

    subgraph RestrictedDataZone ["Restricted Trust Zone 3 (PCI / Core Data)"]
        CoreDB["Production Database Cluster"]
        HSM["Hardware Security Module"]
        InternalDBFW["Database Firewall / Access Proxy"]

        AppSubnet -->|"Inspected DB Queries"| InternalDBFW
        InternalDBFW --> CoreDB
        InternalDBFW --> HSM
    end

    subgraph EgressZone ["Controlled Egress Perimeter"]
        EgressProxy["Egress Inspection Proxy (Squid / Zscaler)"]
        NAT["Secure NAT Gateway"]
        AppSubnet --> EgressProxy
        EgressProxy --> NAT
        NAT -->|"Approved Outbound APIs"| Users
    end

    classDef untrusted fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef dmz fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef secure fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class Users untrusted;
    class EdgeFW,IDS,WAF,EgressProxy,NAT dmz;
    class InternalLB,AppSubnet,MicroSeg,CoreDB,HSM,InternalDBFW secure;
```

## PlantUML Specification

```plantuml
@startuml
package "Public Internet" {
  actor Users
}
package "Perimeter Inspection" {
  component "Next-Gen Firewall (NGFW)" as ngfw
  component "WAF & IDS/IPS" as waf
}
package "Private App Subnet" {
  component "App Cluster" as app
}
package "Secure Data Subnet" {
  database "Encrypted Database" as db
}

Users --> ngfw
ngfw --> waf
waf --> app : Forward inspected traffic
app --> db : Strict port restriction (5432 only)
@enduml
```

## Architectural Design Considerations

* **Default-Deny East-West Rules**: All container-to-container and VPC-to-VPC communication is blocked by default and requires explicit security group/NetworkPolicy white-listing.
* **Egress Traffic Inspection**: Block direct outbound internet access from private subnets; route all external calls through an egress filtering proxy to prevent data exfiltration.
* **Flow Log Analysis**: Stream VPC flow logs to SIEM for automated anomaly detection and lateral movement identification.

## Related Documentation & Patterns

* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
* [WAF & DDoS](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/waf.md)
* [Trust Boundaries](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/trust-boundaries.md)
