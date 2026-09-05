# Multi-Tier Load Balancing Architecture (Global DNS, L4, L7)

Comprehensive load balancing topology detailing traffic distribution across Global DNS (Anycast), Layer 4 Transport Load Balancers, and Layer 7 Application Proxies.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph GlobalDNSLayer ["1. Global Traffic Management"]
        User["Global Web / Mobile Client"]
        Anycast["Global Anycast BGP & Geo-DNS (Route 53 / Cloudflare)"]
        User --> Anycast
    end

    subgraph Layer4Transport ["2. Layer 4 Transport Load Balancer (NLB)"]
        NLB["AWS Network Load Balancer (NLB)<br/>- Ultra-low latency<br/>- Millions of concurrent TCP connections<br/>- Static Elastic IP Addresses"]
        Anycast -->|"Direct Route"| NLB
    end

    subgraph Layer7Application ["3. Layer 7 Application Load Balancer (ALB / Envoy)"]
        ALB["Application Load Balancer (ALB)<br/>- TLS 1.3 Offloading<br/>- Path-based routing (/api vs /static)<br/>- HTTP/2 & gRPC multiplexing"]
        NLB -->|"TCP Forwarding"| ALB
    end

    subgraph MicroservicePods ["4. Target Microservice Fleets"]
        Pod1["order-service Pod 1 (AZ 1a)"]
        Pod2["order-service Pod 2 (AZ 1b)"]
        Pod3["order-service Pod 3 (AZ 1c)"]
        ALB --> Pod1
        ALB --> Pod2
        ALB --> Pod3
    end

    classDef gtm fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef l4 fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef l7 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef app fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class User,Anycast gtm;
    class NLB l4;
    class ALB l7;
    class Pod1,Pod2,Pod3 app;
```

## PlantUML Specification

```plantuml
@startuml
actor Client
participant "Route 53 (Geo DNS)" as dns
component "Layer 4 NLB (TCP)" as nlb
component "Layer 7 ALB (HTTP/2)" as alb
component "App Service Pods" as pods

Client -> dns : Resolve hostname
dns -> Client : Return optimal Regional IP
Client -> nlb : High-speed TCP stream
nlb -> alb : Balance across availability zones
alb -> pods : Route by path (/api/v1/orders)
@enduml
```

## Architectural Design Considerations
* **Layer 4 vs Layer 7 Trade-off**: L4 (NLB) offers extreme throughput and static IPs without inspecting payload; L7 (ALB) enables intelligent path routing, cookie stickiness, and header inspection.
* **Cross-Zone Load Balancing**: Enable cross-zone balancing on load balancers to distribute traffic uniformly across backend pods regardless of target availability zone sizing.
* **Deregistration Delay**: Configure connection draining (deregistration delay: 30-60s) to allow inflight HTTP transactions to complete cleanly before terminating pods.

## Related Documentation & Patterns
* [API Gateway Network](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/api-gateway-network.md)
* [Three-Tier Network](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/three-tier-network.md)
* [Multi-Region Network](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/multi-region-network.md)
