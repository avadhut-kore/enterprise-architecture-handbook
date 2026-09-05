# FinOps Cloud Cost Governance & Optimization Lifecycle

FinOps Foundation architectural lifecycle: Inform (Visibility & Allocation), Optimize (Rate & Usage Reduction), and Operate (Continuous Continuous Alignment).

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph InformPhase ["1. INFORM (Visibility, Tagging & Unit Economics)"]
        Tags["Mandatory Cloud Tagging Policy<br/>(cost-center, owner, env, service)"]
        BillingExport["Consolidated Cloud Billing Ingestion<br/>(AWS CUR, Azure Cost Export)"]
        Dashboards["Team Showback & Chargeback Dashboards<br/>(Unit Cost: $ / Transaction)"]
        Tags --> BillingExport
        BillingExport --> Dashboards
    end

    subgraph OptimizePhase ["2. OPTIMIZE (Rate & Usage Optimization)"]
        RightSizing["Workload Right-Sizing Engine<br/>(Karpenter, Kubecost)"]
        Commitments["Rate Optimization Strategy<br/>(Savings Plans, Reserved Instances, Spot)"]
        WasteElimination["Automated Waste Scrubber<br/>(Unattached EBS, Idle Load Balancers)"]
        Dashboards --> RightSizing
        RightSizing --> Commitments
        Commitments --> WasteElimination
    end

    subgraph OperatePhase ["3. OPERATE (Continuous Governance & Cultural Alignment)"]
        Budgets["Real-Time Anomaly Detection & Budgets"]
        PRChecks["Infracost CI/CD Cost Estimation Checks"]
        ARBGate["ARB Architecture Cost Threshold Sign-off"]
        WasteElimination --> Budgets
        Budgets --> PRChecks
        PRChecks --> ARBGate
    end

    ARBGate -.->|"Continuous Feedback Loop"| InformPhase
```

## PlantUML Specification

```plantuml
@startuml
package "FinOps Lifecycle" {
  node "1. Inform (Visibility)" as p1 {
    [Resource Tagging] --> [Cost Allocation Dashboards]
  }
  node "2. Optimize (Reduction)" as p2 {
    [Compute Right-Sizing] --> [Savings Plans & Spot]
  }
  node "3. Operate (Governance)" as p3 {
    [Infracost CI Checks] --> [Anomaly Alerting]
  }
}
p1 -> p2 : Insights
p2 -> p3 : Implementation
p3 -> p1 : Continuous Optimization
@enduml
```

## Architectural Design Considerations

* **Unit Economics**: Shift focus from raw aggregate cloud spend to unit metrics (e.g., cost per checkout, cost per API call) to measure financial efficiency during business growth.
* **Shift-Left Cost Estimation**: Run Infracost directly inside pull request CI workflows to show engineers the financial impact of Terraform changes before merging.
* **Commitment Coverage**: Maintain 70-80% coverage on baseline steady-state compute with 1-year or 3-year Compute Savings Plans, leaving spikes to on-demand or Spot.

## Related Documentation & Patterns

* [AWS Well-Architected](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/aws-well-architected.md)
* [Cloud Architecture Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/checklists.md)
* [Architecture: Trade-off Matrix](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/tradeoff-matrix.md)
