# 7 Architecture Apprentice Projects: Building an Unassailable Evidence Portfolio

> **"Theoretical knowledge is easily forgotten. True architectural judgment is forged by leading concrete, end-to-end architecture initiatives that face production constraints, cost limits, and failure modes."**

---

## 1. Project 1: High-Throughput Microservice with Multi-Tier Caching & Tracing
* **Business Problem**: A core catalog service experiences database CPU spikes and p99 latency degradation (>1.2s) during peak traffic events.
* **Architecture Challenge**: Design a horizontally scalable service handling 10,000 QPS with p99 latency < 50ms, cache-aside Redis invalidation, and full OpenTelemetry distributed tracing.
* **Key Decisions**: In-memory vs remote cache, connection pool sizing, cache thundering herd prevention (mutex/probabilistic early expiration).
* **Target Deliverables**: Low-Level Design (LLD), load-test benchmark report, Grafana dashboard definition.
* **Reference Grounding**: [`02-system-design/`](../../02-system-design/README.md) & [`06-data/caching/`](../../06-data/caching/README.md).

---

## 2. Project 2: Resilient Event-Driven Order Pipeline with Distributed Sagas
* **Business Problem**: Direct synchronous HTTP calls between Order, Inventory, Payment, and Shipping services cause cascading failures and inconsistent order states when payment fails.
* **Architecture Challenge**: Architect an asynchronous event-driven workflow using the Transactional Outbox pattern, Kafka event streams, and an Orchestrated Saga with compensating transactions.
* **Key Decisions**: Choreography vs Orchestration, idempotency keys, Dead-Letter Queue (DLQ) retry backoff, outbox table polling vs Debezium CDC.
* **Target Deliverables**: High-Level Design (HLD) with sequence diagrams, 2 formal ADRs, chaos failure test report.
* **Reference Grounding**: [`07-integration/`](../../07-integration/README.md) & [`13-architecture-patterns/`](../../13-architecture-patterns/README.md).

---

## 3. Project 3: End-to-End Multi-Tenant SaaS E-Commerce Platform
* **Business Problem**: The company is launching a B2B SaaS platform serving 500 enterprise customers, requiring strict data isolation, zero-downtime deployments, and 99.99% availability.
* **Architecture Challenge**: Design the complete solution architecture spanning frontend portal, API gateway, multi-tenant database isolation, Stripe payment processing, and multi-region failover.
* **Key Decisions**: Database-per-tenant vs shared schema with row-level security (RLS), multi-region active-active vs active-passive failover, STRIDE threat model.
* **Target Deliverables**: Full Solution Architecture Document (SAD), NFR Matrix, STRIDE Threat Model, Disaster Recovery Runbook.
* **Reference Grounding**: [`16-architecture-deliverables/SOLUTION-ARCHITECTURE-TEMPLATE.md`](../../16-architecture-deliverables/SOLUTION-ARCHITECTURE-TEMPLATE.md) & [`18-reference-architectures/`](../../18-reference-architectures/README.md).

---

## 4. Project 4: Enterprise Integration Backbone (ERP, CRM & Banking)
* **Business Problem**: Orders placed in Salesforce CRM fail to synchronize reliably into SAP S/4HANA ERP, causing invoice discrepancies and manual reconciliation overhead.
* **Architecture Challenge**: Architect an enterprise integration fabric bridging Salesforce CDC/CometD events, enterprise iPaaS transformations, and SAP OData APIs with guaranteed delivery and bidirectional reconciliation.
* **Key Decisions**: Real-time streaming vs batch sync, canonical data model (CDM) vs point-to-point mapping, error queue triage workflows.
* **Target Deliverables**: Enterprise Integration Architecture Document, Canonical Data Schema, Reconciliation Runbook.
* **Reference Grounding**: [`14-enterprise-integration/`](../../14-enterprise-integration/README.md) & [`07-integration/enterprise-integration/`](../../07-integration/enterprise-integration/README.md).

---

## 5. Project 5: Legacy Monolith Modernization via the Strangler Fig Pattern
* **Business Problem**: A 15-year-old monolithic billing system cannot scale, deploys only once a quarter, and has high bug regression rates.
* **Architecture Challenge**: Formulate an 18-month phased migration using the Strangler Fig pattern, decomposing customer accounts and payment processing into microservices without stopping business operations.
* **Key Decisions**: Reverse proxy routing, dual-write synchronization, database decoupling without downtime, automated data reconciliation.
* **Target Deliverables**: Modernization Strategy Roadmap, Risk Mitigation Plan, Cutover and Fallback Playbook.
* **Reference Grounding**: [`15-modernization/`](../../15-modernization/README.md).

---

## 6. Project 6: Enterprise GenAI Serving & Hybrid Search Platform
* **Business Problem**: Multiple product squads are independently building uncoordinated OpenAI API integrations, leaking sensitive customer data and racking up uncontrolled API token bills.
* **Architecture Challenge**: Architect a centralized, enterprise-grade AI platform featuring self-hosted open-weights LLMs (vLLM with PagedAttention), hybrid search (BM25 + HNSW vector DB), semantic prompt caching, and strict data loss prevention (DLP) guardrails.
* **Key Decisions**: Self-hosted GPU cluster vs commercial SaaS APIs (TCO comparison), vector chunking strategy, prompt injection defense.
* **Target Deliverables**: Enterprise GenAI Serving Architecture, Threat Model, FinOps Token Cost Model.
* **Reference Grounding**: [`12-ai/model-serving/`](../../12-ai/model-serving/README.md) & [`06-data/search/`](../../06-data/search/README.md).

---

## 7. Project 7: Enterprise Application Portfolio Rationalization (APM)
* **Business Problem**: A global enterprise operating 120 applications across 4 business units spends $45M annually on overlapping software licenses and redundant infrastructure.
* **Architecture Challenge**: Conduct an enterprise application portfolio audit using the TIME framework (Tolerate, Invest, Migrate, Eliminate); calculate 5-year Total Cost of Ownership (TCO); formulate a retirement roadmap saving $5M+ annually.
* **Key Decisions**: Vendor consolidation, business capability mapping, investment prioritization, stakeholder alignment across conflicting business unit heads.
* **Target Deliverables**: Enterprise Business Capability Map, Application TIME Scorecard, Executive Capital Allocation Proposal.
* **Reference Grounding**: [`23-enterprise-architecture/`](../../23-enterprise-architecture/README.md) & [`21-architecture-tools/application-tco-calculator.md`](../../21-architecture-tools/application-tco-calculator.md).
