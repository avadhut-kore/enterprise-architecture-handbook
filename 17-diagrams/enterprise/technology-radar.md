# Enterprise Technology Radar (Adopt, Trial, Assess, Hold)

ThoughtWorks style enterprise technology radar governing technology lifecycle adoption across Languages & Frameworks, Platforms, Tools, and Data Stores.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph RadarRings ["Technology Radar Rings (Lifecycle States)"]
        subgraph AdoptRing ["1. ADOPT (Strong consensus; standard for production)"]
            R1["Go 1.22 / TypeScript / Python 3.12"]
            R2["Kubernetes / AWS EKS / Terraform"]
            R3["PostgreSQL 16 / Apache Kafka"]
        end

        subgraph TrialRing ["2. TRIAL (Pursuing on select projects; ready for production evaluation)"]
            R4["Rust / Next.js App Router"]
            R5["OpenTelemetry SDK / ArgoCD"]
            R6["Apache Iceberg / ClickHouse"]
        end

        subgraph AssessRing ["3. ASSESS (Exploring; R&D proof-of-concept only)"]
            R7["Mojo / Zig"]
            R8["WebAssembly on Cloud (WasmEdge)"]
            R9["Milvus Vector DB / DuckDB"]
        end

        subgraph HoldRing ["4. HOLD (Do not use on new projects; plan deprecation)"]
            R10["Java 8 / AngularJS 1.x / PHP"]
            R11["CloudFormation / Puppet / Chef"]
            R12["Oracle RAC / Apache Cassandra / SOAP APIs"]
        end
    end

    classDef adp fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef tri fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef ass fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef hld fill:#ffebee,stroke:#c62828,stroke-width:2px;
    class AdoptRing,R1,R2,R3 adp;
    class TrialRing,R4,R5,R6 tri;
    class AssessRing,R7,R8,R9 ass;
    class HoldRing,R10,R11,R12 hld;
```

## PlantUML Specification

```plantuml
@startuml
package "Enterprise Tech Radar" {
  node "ADOPT (Production Standard)" as adopt #e8f5e9 {
    [PostgreSQL, Kafka, Go, Kubernetes]
  }
  node "TRIAL (Select Projects)" as trial #e1f5fe {
    [Rust, OpenTelemetry, Apache Iceberg]
  }
  node "ASSESS (Proof of Concept)" as assess #fff8e1 {
    [WebAssembly, Vector DBs]
  }
  node "HOLD (Deprecate / Do Not Use)" as hold #ffebee {
    [Java 8, AngularJS, Oracle RAC]
  }
}
@enduml
```

## Architectural Design Considerations

* **Prevent Technology Proliferation**: Constrains organizational cognitive load by establishing an agreed, vetted baseline of supported technologies.
* **Controlled Innovation**: Provides an established path for engineers to experiment with new technologies (Assess $ightarrow$ Trial $ightarrow$ Adopt).
* **Sunset Governance**: The 'Hold' ring clearly communicates to development teams that older technologies must not be chosen for greenfield initiatives.

## Related Documentation & Patterns

* [Business Capability Map](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/business-capability-map.md)
* [Application Portfolio](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/application-portfolio.md)
* [Architecture: Trade-off Matrix](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/tradeoff-matrix.md)
