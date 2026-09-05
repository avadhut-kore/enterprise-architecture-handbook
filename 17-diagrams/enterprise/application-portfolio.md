# Application Portfolio Rationalization Matrix (Gartner TIME Model)

Strategic application portfolio assessment mapping enterprise applications across Business Value and Technical Fitness into Tolerate, Invest, Migrate, and Eliminate quadrants.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph TIMEMatrix ["Gartner TIME Application Quadrants"]
        subgraph InvestQuad ["INVEST (High Value / High Tech Fit)"]
            App1["Cloud-Native Digital Banking Platform<br/>(Modern Go/React, High Growth)"]
            App2["Real-Time Fraud Detection Engine<br/>(Flink, Kafka, High ROI)"]
        end

        subgraph TolerateQuad ["TOLERATE (High Value / Low Tech Fit)"]
            App3["Core Mainframe Deposit Ledger<br/>(COBOL/DB2 - Critical Business Value, High Cost)"]
            App4["Legacy Policy Administration System<br/>(Monolithic Java 8)"]
        end

        subgraph MigrateQuad ["MIGRATE (Low Value / High Tech Fit)"]
            App5["Modern Internal Wiki / Portal<br/>(Move to Standard SaaS)"]
            App6["Custom HR Expense Tracker<br/>(Replace with Workday SaaS)"]
        end

        subgraph EliminateQuad ["ELIMINATE (Low Value / Low Tech Fit)"]
            App7["Redundant Lotus Notes Database<br/>(Decommission immediately)"]
            App8["Legacy Access Database Reporting Tool<br/>(Sunsetting scheduled Q3)"]
        end
    end

    classDef inv fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef tol fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef mig fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef elm fill:#ffebee,stroke:#c62828,stroke-width:2px;
    class InvestQuad,App1,App2 inv;
    class TolerateQuad,App3,App4 tol;
    class MigrateQuad,App5,App6 mig;
    class EliminateQuad,App7,App8 elm;
```

## PlantUML Specification

```plantuml
@startuml
rectangle "High Technical Fitness / High Business Value" as invest #e8f5e9 {
  [INVEST: Cloud Digital Platform]
}
rectangle "Low Technical Fitness / High Business Value" as tolerate #fff8e1 {
  [TOLERATE: Core Mainframe DB2]
}
rectangle "High Technical Fitness / Low Business Value" as migrate #e1f5fe {
  [MIGRATE: Custom Tool -> Replace with SaaS]
}
rectangle "Low Technical Fitness / Low Business Value" as eliminate #ffebee {
  [ELIMINATE: Redundant Legacy Databases]
}
@enduml
```

## Architectural Design Considerations

* **Objective Decision Framework**: Eliminates emotional bias in software replacement decisions by plotting measurable business metrics against technical code quality.
* **Actionable Roadmap**:
  - **Tolerate**: Maintain system stability; minimize new feature investment; prepare modernization wrappers.
  - **Invest**: Allocate budget, top engineering talent, and expand capability.
  - **Migrate**: Standardize on off-the-shelf commercial SaaS.
  - **Eliminate**: Decommission application, archive data, and reclaim licensing costs.

## Related Documentation & Patterns

* [Business Capability Map](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/business-capability-map.md)
* [Enterprise Integration Landscape](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/integration-landscape.md)
* [Technology Radar](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/technology-radar.md)
