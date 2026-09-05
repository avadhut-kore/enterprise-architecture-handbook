# DevOps for Diverse Application Architectures

Different architectural paradigms require tailored delivery and operational pipelines. Applying a microservices pipeline to a legacy monolith guarantees failure.

## 1. Delivery Architecture by Paradigm

| Paradigm | Primary Pipeline Challenge | Recommended Delivery Strategy | Key Guardrail |
| :--- | :--- | :--- | :--- |
| **Monolith** | Long compile times; massive regression test suites. | Distributed build caching; test sharding; Blue/Green deployment. | Strong rollback automation; feature flags for partial enablement. |
| **Modular Monolith** | Cross-module architectural leakage; build dependencies. | Static boundary fitness tests (ArchUnit/Nx); independent module verification. | Enforce zero cyclic dependencies at compile time. |
| **Microservices** | Complex integration testing; cascading failure risk. | Consumer-driven contract testing (Pact); GitOps; Canary progressive delivery. | Independent deployability without coordinated multi-repo PRs. |
| **Serverless** | Cold starts; distributed tracing across ephemeral functions. | Canary traffic shifting (AWS CodeDeploy); lightweight minimal runtimes. | Automated concurrency limits to prevent database connection exhaustion. |
| **Event-Driven / Streaming** | Schema evolution across producers and consumers. | Schema Registry validation in CI (Avro/Protobuf); outbox patterns. | Consumer backward compatibility checks prior to schema registration. |
| **Batch Systems** | Data pipeline failures; reprocessing large volumes. | Containerized Job/CronJob execution; idempotent retry partitions. | Dead Letter Queues (DLQ) and anomaly detection on processed record counts. |

## Related Resources
- [CI/CD Reference Pipelines](../ci-cd/reference-pipelines/README.md)
- [Application Architecture Catalog](../../01-architecture/README.md)
