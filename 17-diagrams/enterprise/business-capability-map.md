# Enterprise Business Capability Map (L1 / L2 Hierarchy)

Hierarchical Business Capability Map decomposing enterprise capabilities into Strategic, Core Operational, and Supporting tiers independently of organizational hierarchy.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph StratTier ["1. Strategic & Governance Capabilities"]
        C1["Enterprise Strategy & Planning"]
        C2["Risk, Audit & Regulatory Compliance"]
        C3["Brand, Marketing & Product Design"]
    end

    subgraph CoreTier ["2. Core Customer-Facing Capabilities"]
        subgraph CustomerAcquisition ["Customer Acquisition"]
        CA1["Lead Management"]
        CA2["Digital Onboarding & KYC"]
        CA3["Credit Scoring & Underwriting"]
        end

        subgraph AccountServicing ["Account Servicing & Operations"]
        AS1["Deposit & Checking Accounts"]
        AS2["Payment Processing & Wire Transfers"]
        AS3["Card Issuance & Interchange"]
        end

        subgraph LendingManagement ["Lending & Mortgages"]
        LM1["Mortgage Origination"]
        LM2["Loan Servicing & Collections"]
        end
    end

    subgraph SupportTier ["3. Supporting & Enabling Capabilities"]
        S1["Human Capital Management (HCM)"]
        S2["Financial Accounting & General Ledger"]
        S3["Enterprise IT, Cloud & Cybersecurity"]
        S4["Procurement & Vendor Management"]
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Strategic Capabilities" {
  [Corporate Strategy]
  [Risk & Governance]
}
package "Core Capabilities" {
  folder "Customer Acquisition" {
    [Digital Onboarding & KYC]
    [Credit Assessment]
  }
  folder "Account Servicing" {
    [Payment Processing]
    [Card Management]
  }
}
package "Supporting Capabilities" {
  [Financial Ledger]
  [HR & Talent]
  [IT & Cyber Infrastructure]
}
@enduml
```

## Architectural Design Considerations

* **What vs How**: A capability map describes *what* the business does to generate value, not *how* or *which software application* performs it.
* **Stability Over Time**: Business capabilities change rarely (e.g., banks always need 'Underwriting'), even when underlying technology stacks are rewritten.
* **Investment Heatmapping**: Overlay capability boxes with color codes (Green = High Maturity, Red = Severe Technical Debt) to guide executive IT investment.

## Related Documentation & Patterns

* [Application Portfolio](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/application-portfolio.md)
* [Enterprise Integration Landscape](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/integration-landscape.md)
* [Technology Radar](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/technology-radar.md)
