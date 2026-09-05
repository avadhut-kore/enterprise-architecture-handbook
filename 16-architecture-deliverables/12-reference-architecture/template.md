# Reference Architecture: [DOMAIN / PATTERN NAME]

---
**Metadata**:
```yaml
refarch_id: "REFARCH-[DOMAIN]-001"
title: "Enterprise Reference Architecture — [Domain Name]"
version: "1.0.0"
status: "Active" # Proposed | Active | Superseded | Retired
owner: "[Chief / Enterprise Architect Name <email>]"
governing_body: "Enterprise Architecture Review Board"
created_date: "YYYY-MM-DD"
review_cadence: "Annual"
```
---

## 1. Problem Domain & Applicability
* What organizational problem space does this reference architecture address (e.g., B2B SaaS, Event-Driven Microservices, Data Mesh)?
* When MUST projects adopt this reference architecture?
* When are projects EXEMPT from this architecture?

## 2. Core Architecture Principles
* Principle 1: Asynchronous decoupling by default for cross-domain communication.
* Principle 2: Zero shared databases across microservice boundaries.
* Principle 3: Immutable infrastructure via GitOps and declarative Infrastructure as Code.

## 3. Conceptual Reference Model
Reference layered conceptual diagram from [[17-diagrams/01-c4-model/README.md](../../17-diagrams/c4/README.md)].

```text
+-------------------------------------------------------------------+
|                        Client Access Layer                        |
|  Web Apps (React)  |  Mobile Apps (Flutter)  |  Partner B2B APIs  |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
|                     API Gateway & Security DMZ                    |
|   TLS 1.3  |  OAuth2 / OIDC  |  Rate Limiting  |  WAF Protection  |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
|                    Domain Microservices Tier                      |
|   Hexagonal Architecture  |  gRPC / REST  |  OpenTelemetry Trace  |
+-------------------------------------------------------------------+
             |                                     |
             v                                     v
+-----------------------------+   +---------------------------------+
|      Persistence Tier       |   |       Enterprise Event Mesh     |
| PostgreSQL / CockroachDB    |   | Kafka / Schema Registry / DLQ   |
+-----------------------------+   +---------------------------------+
```

## 4. Standard Technology Radar (Approved Options)
| Layer | Approved Standards | Tolerated (Legacy Only) | Prohibited |
|---|---|---|---|
| **Compute** | AWS EKS (Kubernetes $\ge 1.28$), AWS Lambda | EC2 Virtual Machines | Bare metal without approval |
| **Language** | Java 21+, Go 1.22+, TypeScript (Node 20+) | Python (for web APIs) | PHP, Ruby |
| **Databases** | PostgreSQL 16+, CockroachDB, DynamoDB | MySQL, Oracle 19c | MongoDB without schema validation |
| **Messaging** | Apache Kafka, AWS SQS | RabbitMQ | JMS ActiveMQ |

## 5. Allowed Variation Points
* **Variation Point 1**: Teams may choose between Java (Spring Boot) and Go depending on latency and throughput requirements.
* **Variation Point 2**: Workloads requiring global multi-region active-active persistence must use CockroachDB; single-region workloads may use Aurora PostgreSQL.

## 6. Adoption Guidance & Getting Started
* Link to project scaffolding starter repositories, Helm charts, and CI/CD pipeline templates.
