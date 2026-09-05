# Mermaid Pie Charts & Portfolio Allocation

Pie charts communicate high-level architecture portfolio splits, cloud infrastructure cost distributions, and technical debt allocation.

## Cloud Infrastructure Monthly Spend Breakdown

```mermaid
pie title Monthly Cloud Spend by Workload Category (USD)
    "Production Microservices (EKS)" : 42
    "Databases (Aurora & DynamoDB)" : 28
    "Network Transit & NAT Gateways" : 12
    "Observability & Logs (Datadog/OTel)" : 11
    "Non-Production Staging/Dev" : 7
```

## Architectural Guidelines
* Keep categories $\le 6$ slices to maintain visual scannability.
* Highlight dominant cost drivers or technical debt areas directly in Architecture Decision Records (ADRs).
