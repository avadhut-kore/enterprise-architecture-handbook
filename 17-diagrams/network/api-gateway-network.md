# API Gateway Network Architecture & Ingress Placement

Enterprise network topology detailing the network placement of API Gateways across public and private subnet boundaries, edge TLS offloading, and backend service routing.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph InternetClients ["External Traffic"]
        User["Mobile / Web Clients"]
        Partner["B2B Partner Systems"]
    end

    subgraph EdgeTier ["Cloud Edge Layer"]
        WAF["Cloud Edge WAF / CDN"]
        User --> WAF
        Partner --> WAF
    end

    subgraph IngressVPC ["DMZ / Ingress VPC (10.0.0.0/16)"]
        subgraph PublicSubnets ["Public Subnets (AZ 1a, 1b)"]
            NLB["Network Load Balancer (Static EIPs)"]
            WAF --> NLB
        end

        subgraph GatewaySubnets ["Private Gateway Subnets (AZ 1a, 1b)"]
            KongCluster["Kong / Envoy API Gateway Cluster<br/>- TLS 1.3 Termination<br/>- OAuth2 JWT Verification<br/>- Rate Limiting (Token Bucket)"]
            NLB --> KongCluster
        end
    end

    subgraph CoreAppVPC ["Internal Application VPC (10.1.0.0/16)"]
        PrivateLB["Internal Load Balancer"]
        AppMesh["Microservices Pods (Private EKS)"]
        KongCluster -->|"VPC Peering / PrivateLink (mTLS)"| PrivateLB
        PrivateLB --> AppMesh
    end

    classDef edge fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef gw fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef app fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class User,Partner,WAF edge;
    class NLB,KongCluster gw;
    class PrivateLB,AppMesh app;
```

## PlantUML Specification

```plantuml
@startuml
actor Client
participant "Edge WAF" as waf
node "Public Subnet" {
  component "NLB (Static EIP)" as nlb
}
node "Private Gateway Subnet" {
  component "API Gateway (Envoy/Kong)" as gw
}
node "Private App Subnet" {
  component "Application Microservices" as app
}

Client -> waf : HTTPS Call
waf -> nlb : Forward
nlb -> gw : Layer 4 Forward
gw -> gw : Offload TLS & Validate JWT
gw -> app : Forward via PrivateLink (mTLS)
@enduml
```

## Architectural Design Considerations
* **Dual-Tier Load Balancing**: Use an external NLB for high-throughput Layer 4 TCP termination with static IP addresses, routing traffic directly to private API Gateway instances.
* **Separation of Gateway & App VPCs**: Isolating the API Gateway inside an Ingress/DMZ VPC prevents compromised gateway pods from having direct, uninspected Layer 2 access to internal databases.
* **PrivateLink Connectivity**: Connect Gateway VPCs to Application VPCs using AWS PrivateLink or Azure Private Link to avoid complex inter-VPC routing tables and CIDR overlap.

## Related Documentation & Patterns
* [Zero Trust Network](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/zero-trust-network.md)
* [Ingress & Egress](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/ingress-egress.md)
* [Security: API Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/api-security.md)
