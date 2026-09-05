# DevOps Architecture Starter Template

Standardized template for authoring end-to-end continuous integration, delivery pipelines, and production release topologies.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph CodeTier ["Source & CI"]
        GitRepo["Git Repository"]
        CIPipeline["CI Runner (Test & Build)"]
        Registry["Image Registry (Harbor)"]
        GitRepo --> CIPipeline
        CIPipeline --> Registry
    end

    subgraph GitOpsTier ["GitOps Delivery"]
        GitOpsRepo["GitOps Config Repository"]
        CDOperator["GitOps Operator (ArgoCD)"]
        GitOpsRepo --> CDOperator
        Registry --> CDOperator
    end

    subgraph ProductionTier ["Target Production Cluster"]
        K8sCluster["Production EKS Cluster"]
        Observability["OTel Telemetry & Monitoring"]
        CDOperator --> K8sCluster
        K8sCluster --> Observability
    end
```

## PlantUML Specification

```plantuml
@startuml
package "CI Engine" {
  [Git Repo] --> [Build & Test]
  [Build & Test] --> [Image Registry]
}
package "CD GitOps" {
  [Image Registry] --> [ArgoCD Controller]
  [Config Git] --> [ArgoCD Controller]
}
package "Production" {
  [ArgoCD Controller] --> [Production K8s]
  [Production K8s] --> [Observability]
}
@enduml
```

## Architectural Design Considerations

* **Standard Starting Pipeline**: Copy and adapt this template when documenting CI/CD infrastructure for new microservice projects.
* **Explicit Gateways**: Clearly document automated quality and security gates preceding production promotions.
* **Feedback Loop**: Telemetry flows from production back into developer dashboards.

## Related Documentation & Patterns

* [GitOps Pipeline](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/gitops-pipeline.md)
* [CI/CD Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/ci-cd-flow.md)
* [DevOps Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/checklists.md)
