# Architecture Tools (`21-architecture-tools/`)

## Executive Summary

The `21-architecture-tools/` directory provides operationalized instruments, assessment checklists, quantitative sizing calculators, governance templates, and Architecture Review Board (ARB) playbooks used by Principal, Lead, and Enterprise Architects across Fortune 500 and global enterprise engagements.

---

## 1. Architecture Review Checklists (`checklists/`)

Comprehensive, actionable verification checklists to evaluate systems at major gate reviews (Concept, Solution Design, Security Review, Production Readiness, Migration Cutover).

### Cloud & Infrastructure Checklists (`checklists/cloud/`)
* [`cloud-architecture-review.md`](checklists/cloud/cloud-architecture-review.md) - Formal ARB governance gate evaluating multi-AZ resilience, security boundaries, and static stability.
* [`cloud-landing-zone-checklist.md`](checklists/cloud/cloud-landing-zone-checklist.md) - Multi-account hierarchy, root guardrails, transit networking, and identity federation.
* [`cloud-migration-readiness-checklist.md`](checklists/cloud/cloud-migration-readiness-checklist.md) - Discovery, schema assessment, CDC lag, cutover runbooks, and reverse-replication rollback.
* [`cloud-disaster-recovery-checklist.md`](checklists/cloud/cloud-disaster-recovery-checklist.md) - Cross-region asynchronous replication, secondary IaC automation, Anycast failover, and game day drills.
* [`cloud-security-guardrails-checklist.md`](checklists/cloud/cloud-security-guardrails-checklist.md) - Preventative SCPs, Kubernetes Pod Security Standards, workload identity, and agentless CSPM.

### Application Architecture Checklists (`checklists/application/`)
* Checklists covering [.NET](checklists/application/dotnet-architecture-checklist.md), [Java](checklists/application/java-architecture-checklist.md), [Node.js](checklists/application/nodejs-architecture-checklist.md), [Python](checklists/application/python-architecture-checklist.md), [React](checklists/application/react-architecture-checklist.md), [Angular](checklists/application/angular-architecture-checklist.md), [Mobile](checklists/application/mobile-architecture-checklist.md), [Application Security](checklists/application/application-security-checklist.md), and [Testing](checklists/application/application-testing-checklist.md).

### System Design & Data Integration Checklists
* [System Design Checklists](checklists/system-design/README.md) - Requirements, scale estimation, HLD, LLD, resilience, and reliability checklists.
* Checklists covering [API Architecture](checklists/api-architecture-checklist.md), [Messaging](checklists/messaging-checklist.md), [Kafka](checklists/kafka-checklist.md), [Event-Driven](checklists/event-driven-checklist.md), [Data Migration](checklists/data-migration-checklist.md), [CDC](checklists/cdc-checklist.md), [Financial Settlement](checklists/settlement-architecture-checklist.md), and [Reconciliation](checklists/reconciliation-checklist.md).

---

## 2. Quantitative Sizing & Economic Calculators (`calculators/`)

Deterministic mathematical formulas, resource estimation models, and economic calculators.

### Cloud Sizing & Economics Calculators
* [`cloud-capacity-calculator.md`](calculators/cloud-capacity-calculator.md) - Peak request rate, latency, target CPU utilization, and fleet headroom formulas.
* [`kubernetes-node-sizing-calculator.md`](calculators/kubernetes-node-sizing-calculator.md) - Pod density, allocatable vCPU/memory, system reservation, and surge capacity sizing.
* [`network-bandwidth-egress-calculator.md`](calculators/network-bandwidth-egress-calculator.md) - Peak throughput, payload size, monthly transfer volume, and data egress cost estimation.
* [`storage-growth-and-lifecycle-calculator.md`](calculators/storage-growth-and-lifecycle-calculator.md) - Multi-tier object storage cost optimization and lifecycle migration formulas.
* [`availability-sla-compound-calculator.md`](calculators/availability-sla-compound-calculator.md) - Serial vs parallel compound availability SLA modeling and annual downtime calculations.
* [`rto-rpo-dr-cost-calculator.md`](calculators/rto-rpo-dr-cost-calculator.md) - Financial risk exposure vs disaster recovery topology cost modeling.
* [`finops-unit-cost-calculator.md`](calculators/finops-unit-cost-calculator.md) - Workload unit economics, direct vs indirect cost allocation, and cost per transaction.

### Data & System Design Calculators
* Sizing calculators for [Database Storage](calculators/database-sizing-calculator.md), [Cache Memory](calculators/cache-calculator.md), [Bandwidth](calculators/bandwidth-calculator.md), [Kafka Partitions](calculators/kafka-and-streaming-sizing-calculator.md), [Message Queues](calculators/messaging-and-queue-throughput-calculator.md), [API Throughput](calculators/api-and-integration-throughput-calculator.md), and [Financial Reconciliation Volume](calculators/financial-settlement-and-recon-volume-calculator.md).

---

## 3. Architecture Review & System Design Playbooks (`architecture-review/`)

Interview frameworks, defense playbooks, and structured Q&A for Principal Architect evaluations.

* [`cloud-architecture-interview-playbook.md`](architecture-review/cloud-architecture-interview-playbook.md) - Structured architectural solutions for 14 high-stakes enterprise cloud design scenarios.
* [`data-and-integration-architecture-review.md`](architecture-review/data-and-integration-architecture-review.md) - Formal ARB governance playbook for data pipelines, streaming architectures, and financial transaction platforms.
