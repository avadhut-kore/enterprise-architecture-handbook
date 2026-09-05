# Enterprise Architecture Acronyms Glossary

## Overview

This reference document catalogs the standard acronyms utilized in software architecture, enterprise architecture, distributed systems, cloud computing, security, and Site Reliability Engineering (SRE).

---

## Master Acronyms Reference Table

| Acronym | Full Form | Architectural Domain | Description / Definition |
|:---|:---|:---|:---|
| **2PC** | Two-Phase Commit | Distributed Systems | Distributed transaction protocol coordinating commit across multiple nodes. |
| **ACL** | Anti-Corruption Layer | Domain-Driven Design | Translation layer shielding domain models from external schema pollution. |
| **ADR** | Architecture Decision Record | Governance | Document capturing context, options, and trade-offs of an architectural choice. |
| **AMQP** | Advanced Message Queuing Protocol | Messaging | Open standard wire-level protocol for asynchronous message-oriented middleware. |
| **APM** | Application Portfolio Management | Enterprise Architecture | Discipline of evaluating and rationalizing enterprise software applications. |
| **ARB** | Architecture Review Board | Governance | Enterprise governing body reviewing and ratifying technical architectures. |
| **ASR** | Architecturally Significant Requirement | System Design | Requirement with deep structural impact on system topology. |
| **ATAM** | Architecture Tradeoff Analysis Method | Architecture Evaluation | SEI methodology for assessing architectures against quality scenarios. |
| **BaaS** | Backend as a Service | Cloud Computing | Cloud model where third parties manage server logic and backend services. |
| **BASE** | Basically Available, Soft state, Eventual consistency | Data Architecture | Distributed systems consistency model contrasting with relational ACID. |
| **C4** | Context, Containers, Components, Code | Visualization | Hierarchical architectural diagramming framework created by Simon Brown. |
| **CAP** | Consistency, Availability, Partition Tolerance | Distributed Systems | Theorem stating distributed stores can guarantee at most 2 of 3 properties. |
| **CDC** | Change Data Capture | Integration Architecture | Capturing and streaming database-level insert/update/delete change events. |
| **CDN** | Content Delivery Network | Networking | Distributed edge proxy network caching static and dynamic web content. |
| **CQS** | Command-Query Separation | Software Design | Principle stating methods should either perform an action or return data, not both. |
| **CQRS** | Command Query Responsibility Segregation | Architecture Patterns | Segregating read and write data models and pipelines into distinct subsystems. |
| **CVE** | Common Vulnerabilities and Exposures | Security | Publicly disclosed computer security flaws and vulnerability database. |
| **CVSS** | Common Vulnerability Scoring System | Security | Open framework for scoring the technical severity of software vulnerabilities. |
| **DDD** | Domain-Driven Design | Software Design | Design methodology centering software development on business domain models. |
| **DLQ** | Dead Letter Queue | Messaging | Secondary queue capturing unprocessable or poisoned messages. |
| **DORA** | DevOps Research and Assessment | Engineering Metrics | Benchmark metrics (Lead Time, Deployment Frequency, MTTR, Change Failure). |
| **EA** | Enterprise Architecture | Governance | Strategic practice aligning enterprise business strategy with IT execution. |
| **EAB** | Enterprise Architecture Board | Governance | Executive architectural steering committee for portfolio strategy. |
| **EDA** | Event-Driven Architecture | Architecture Patterns | Architectural paradigm centered on producing, detecting, and consuming events. |
| **EIP** | Enterprise Integration Patterns | Integration | Design patterns for asynchronous enterprise messaging systems (Hohpe/Woolf). |
| **FaaS** | Function as a Service | Serverless | Cloud execution model executing stateless, event-driven code snippets. |
| **FinOps** | Financial Operations | Cloud Architecture | Cultural practice of managing and optimizing variable cloud hosting costs. |
| **FMEA** | Failure Mode and Effects Analysis | Reliability | Systematic technique for auditing potential component failures and blast radiuses. |
| **HPA** | Horizontal Pod Autoscaler | Infrastructure | Kubernetes controller dynamically scaling pod replicas based on metrics. |
| **IaC** | Infrastructure as Code | DevSecOps | Managing and provisioning infrastructure via code (Terraform, Pulumi). |
| **IdP** | Identity Provider | Security | System that creates, maintains, and manages identity information (Okta, Auth0). |
| **IOPS** | Input/Output Operations Per Second | Storage | Standard benchmark measuring storage performance and disk throughput. |
| **mTLS** | Mutual Transport Layer Security | Security | Two-way cryptographic authentication where both client and server prove identity. |
| **MTBF** | Mean Time Between Failures | Reliability | Average elapsed time between inherent system failures during normal operation. |
| **MTTD** | Mean Time to Detect | Observability | Average time elapsed from incident onset until automated alerting fires. |
| **MTTR** | Mean Time to Recover / Repair | Reliability | Average time required to restore a failed system or service back to production. |
| **NFR** | Non-Functional Requirement | System Design | Quality attribute constraint (Latency, Scalability, Availability, Security). |
| **OCI** | Open Container Initiative | Platform Engineering | Linux Foundation project standardizing container formats and runtimes (Docker). |
| **OIDC** | OpenID Connect | Security | Identity layer built on top of OAuth 2.0 authorization framework. |
| **OLAP** | Online Analytical Processing | Data Architecture | High-throughput analytical queries and aggregations across large datasets. |
| **OLTP** | Online Transaction Processing | Data Architecture | Fast, transactional, query-specific databases supporting day-to-day operations. |
| **OTel** | OpenTelemetry | Observability | CNCF vendor-neutral standard for traces, metrics, and logs collection. |
| **PACELC**| Partition, Availability, Consistency, Else Latency, Consistency | Distributed Systems | Theorem extending CAP to define trade-offs during normal non-partitioned operation. |
| **PITR** | Point-in-Time Recovery | Disaster Recovery | Restoring database state to any specific second using WAL transaction logs. |
| **PRR** | Production Readiness Review | SRE / Operations | Operational verification checkpoint conducted prior to commercial launch. |
| **QPS** | Queries Per Second | System Design | Metric measuring read throughput capacity on database and cache tiers. |
| **RPO** | Recovery Point Objective | Disaster Recovery | Maximum acceptable data loss duration during a disaster event. |
| **RPS** | Requests Per Second | System Design | Metric measuring incoming traffic volume to API gateways and web servers. |
| **RTO** | Recovery Time Objective | Disaster Recovery | Maximum acceptable duration of downtime before service restoration. |
| **SA** | Solution Architecture | Architecture | Designing end-to-end technical solutions to specific business problems. |
| **SAD** | Solution Architecture Document | Deliverables | Comprehensive design specification documenting a system architecture. |
| **SLA** | Service Level Agreement | Governance | Contractual uptime/performance commitment with external customers. |
| **SLI** | Service Level Indicator | Observability | Quantifiable metric measuring service performance (e.g., error rate). |
| **SLO** | Service Level Objective | SRE | Internal engineering target for service reliability and availability. |
| **SoC** | Separation of Concerns | Software Design | Design principle separating a computer program into distinct feature sections. |
| **SPOF** | Single Point of Failure | Reliability | System component whose failure crashes the entire platform. |
| **SRE** | Site Reliability Engineering | Operations | Discipline applying software engineering principles to infrastructure and ops. |
| **STRIDE**| Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation | Security | Threat modeling framework developed by Microsoft for vulnerability identification. |
| **TCO** | Total Cost of Ownership | FinOps | Complete multi-year financial expenditure across capital, hosting, and operations. |
| **TIME** | Tolerate, Invest, Migrate, Eliminate | Portfolio Governance| Gartner's 4-quadrant application portfolio rationalization methodology. |
| **TPS** | Transactions Per Second | System Design | Metric measuring write and state mutation throughput in transaction engines. |
| **USL** | Universal Scalability Law | System Design | Mathematical model (Neil Gunther) incorporating contention and coherency penalties. |
| **WAL** | Write-Ahead Logging | Databases | Persistence technique where changes are logged to disk before applying to tables. |
| **WORM** | Write Once, Read Many | Storage / DR | Storage data protection preventing modification or deletion of archived records. |
| **XA** | eXtended Architecture | Distributed Systems | Standard specification for distributed transaction coordination (2PC). |
