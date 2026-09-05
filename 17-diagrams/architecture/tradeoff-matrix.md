# Architectural Trade-Off Visual Analysis (Spider & Radar Maps)

Multi-dimensional architectural trade-off framework comparing architectural styles across Non-Functional Requirements (NFRs).

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph Styles ["Architectural Candidates"]
        StyleA["Modular Monolith"]
        StyleB["Microservices Architecture"]
        StyleC["Event-Driven Serverless"]
    end

    subgraph TradeoffMetrics ["Evaluated NFR Dimensions"]
        M1["Development Simplicity: High (A) vs Low (B)"]
        M2["Independent Deployability: Low (A) vs High (B/C)"]
        M3["Operational Complexity: Low (A) vs Very High (B)"]
        M4["Elastic Scalability: Moderate (A) vs High (B) vs Infinite (C)"]
        M5["Data Consistency: Strong ACID (A) vs Eventual (B/C)"]
        M6["Infrastructure Cost at Idle: High (A/B) vs Zero (C)"]
    end

    StyleA --- M1
    StyleA --- M3
    StyleA --- M5
    StyleB --- M2
    StyleB --- M4
    StyleC --- M6
```

## PlantUML Specification

```plantuml
@startuml
skinparam monochrome false
rectangle "Modular Monolith" as mono
rectangle "Microservices" as ms
rectangle "Serverless EDA" as sls

mono -down-> [Simplicity: HIGH | Deployability: LOW | Consistency: ACID]
ms -down-> [Simplicity: LOW | Deployability: HIGH | Consistency: EVENTUAL]
sls -down-> [Idle Cost: ZERO | Cold Starts: NON-ZERO | Scalability: AUTO]
@enduml
```

## Architectural Design Considerations

* **No Free Lunch**: Every architectural decision involves trading one set of problems for another (e.g., trading monolithic deployment bottlenecks for distributed system network failures).
* **Context Over Hype**: Choose architectural patterns suited to current organization scale and team cognitive load rather than aspirational hyperscale architectures.
* **Quantifiable Scoring**: Score competing patterns across 1-5 scales against explicit project architectural quality attributes.

## Related Documentation & Patterns

* [ADRs Visualized](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/adrs-visualized.md)
* [High-Level Design](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/high-level-design.md)
* [Diagram Selection Guide](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/diagram-selection-guide.md)
