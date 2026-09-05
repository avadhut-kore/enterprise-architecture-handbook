# Canary Progressive Delivery Architecture (Argo Rollouts / Flagger)

Automated progressive delivery architecture shifting a small fraction of live production traffic to a new version, monitoring metrics, and auto-promoting or aborting.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph TrafficManager ["Edge Traffic Shifter (Envoy / Istio / ALB)"]
        Users["Live User Traffic"]
        Shifter["Weighted Traffic Splitter<br/>- 90% Route to Stable<br/>- 10% Route to Canary"]
        Users --> Shifter
    end

    subgraph StableFleet ["Stable Replica Set (Version 1.4)"]
        StableApp["Stable Application Pods (v1.4)<br/>- 9 Pods (Serving 90% of requests)"]
    end

    subgraph CanaryFleet ["Canary Replica Set (Version 1.5)"]
        CanaryApp["Canary Application Pods (v1.5)<br/>- 1 Pod (Serving 10% of requests)"]
    end

    subgraph AutomatedAnalysis ["Automated Metric Analysis Engine (Argo Rollouts)"]
        Prometheus["Prometheus / Datadog Metrics<br/>(Query: HTTP 5xx error rate & p99 latency)"]
        RolloutController["Rollout Controller<br/>- Condition: 5xx rate < 0.1%<br/>- Condition: Latency p99 < 150ms"]
        Prometheus --> RolloutController
    end

    Shifter -->|"90% Traffic"| StableApp
    Shifter -->|"10% Traffic"| CanaryApp
    CanaryApp -.->|"Telemetry"| Prometheus
    RolloutController -->|"Auto-Promote to 25% -> 50% -> 100%"| Shifter
    RolloutController -.->|"Auto-Abort & Rollback on Error Spike"| Shifter
```

## PlantUML Specification

```plantuml
@startuml
actor Users
component "Istio / Envoy Ingress" as ingress
component "Stable Service (v1.4)" as stable
component "Canary Service (v1.5)" as canary
component "Prometheus Metrics" as prom
component "Flagger Controller" as flagger

Users -> ingress : Live Traffic
ingress -> stable : 90% Traffic
ingress -> canary : 10% Traffic
canary -> prom : Emit error rates
prom -> flagger : Query HTTP 5xx & latency
flagger -> ingress : Metric healthy -> Shift to 25%, 50%, 100%
@enduml
```

## Architectural Design Considerations

* **Automated Rollback Criteria**: Define strict statistical thresholds (e.g., error rate > 0.5% over 5 consecutive minutes) that automatically abort the canary without human intervention.
* **Synthetic vs Real Traffic**: Real canary evaluation requires authentic user traffic; synthetic testing cannot capture all production edge cases.
* **Targeted Canaries**: Use HTTP request headers (e.g., `X-Internal-Beta: true`) to route canary traffic to internal employees before exposing it to public users.

## Related Documentation & Patterns

* [Blue-Green Deployment](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/blue-green.md)
* [GitOps Pipeline](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/gitops-pipeline.md)
* [Observability Pipeline](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/observability-pipeline.md)
