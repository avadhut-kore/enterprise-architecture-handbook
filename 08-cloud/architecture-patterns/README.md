# Enterprise Cloud Architecture Patterns

## Executive Summary

This section provides 10 battle-tested, production-grade cloud reference architecture patterns. Each pattern adheres to a comprehensive **13-point architectural specification**: Problem, Context, Architecture, When to Use, When NOT to Use, Benefits, Trade-offs, Failure Modes, Security, Scalability, Cost, Operational Considerations, and Evolution.

---

## The 10 Enterprise Patterns

| Pattern | Architectural Domain | Key Cloud Primitives |
| :--- | :--- | :--- |
| **[Three-Tier Cloud](three-tier-cloud.md)** | Web Applications | Public Ingress, Private App, Isolated DB Subnets, ALB, Aurora |
| **[N-Tier Cloud](n-tier-cloud.md)** | Complex Enterprise Services | API Gateway, Microservices, Caching Tier, Message Broker, DB |
| **[Cloud-Native Microservices](cloud-native-microservices.md)**| Container Orchestration | Kubernetes (EKS/AKS/GKE), Service Mesh, OTel, GitOps |
| **[Modular Monolith on Cloud](modular-monolith-on-cloud.md)**| Pragmatic Modernization | Single Deployment Unit, Internal Bounded Contexts, Container PaaS |
| **[Event-Driven Cloud](event-driven-cloud.md)** | Asynchronous Streaming | Managed Kafka (MSK), EventBridge, SQS, Outbox Pattern, DLQ |
| **[Serverless Cloud Platform](serverless-cloud-pattern.md)**| Ephemeral Event Processing | API Gateway, Lambda/Cloud Run, DynamoDB, Step Functions |
| **[Multi-Region Active-Active](multi-region-active-active.md)**| Planetary Resilience | Global Anycast LB, Multi-Region Spanner/DynamoDB, CRDT |
| **[Multi-Region Active-Passive](multi-region-active-passive.md)**| Disaster Recovery | Warm Standby, Aurora Global DB, Route 53 ARC Failover |
| **[Hub-and-Spoke Networking](hub-and-spoke-networking.md)** | Network Transit | Transit Gateway / Virtual WAN, Inspection VPC, PrivateLink |
| **[Shared Services Landing Zone](shared-services-landing-zone.md)**| Platform Engineering | Centralized CI/CD, Artifacts, Directory Services, Log Vault |
