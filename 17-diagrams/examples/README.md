# Industry Vertical Architecture Reference Examples

This directory provides comprehensive, end-to-end architecture reference designs for 11 critical enterprise industry verticals.

Each reference architecture is a complete, production-ready solution design package incorporating:
1. **Business Drivers & Non-Functional Requirements (NFRs)**
2. **C4 Level 1: System Context Blueprint**
3. **C4 Level 2: Container Architecture & Service Mesh**
4. **Core Business Sequence & Transaction Flow**
5. **Physical Deployment & Multi-AZ/Multi-Region Topology**
6. **Data-Flow & Analytics Pipeline**
7. **Architectural Decisions (ADRs) & Security Controls**

## Vertical Reference Catalog

| Industry Vertical | Primary Domain Focus | Key Architecture Highlights |
|:------------------|:---------------------|:----------------------------|
| [Global E-Commerce Platform](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/ecommerce-platform.md) | High-volume retail & checkout | Multi-region active-active, flash-sale scaling, event-driven fulfillment |
| [Core Banking & Real-Time Payments](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/core-banking.md) | Financial accounting & ISO 20022 | Double-entry ledger, HSM key signing, Zero Trust, sub-second settlement |
| [Insurance Claims Processing](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/insurance-claims.md) | FNOL & automated claim settlement | AI/OCR intake, fraud detection scoring, human-in-the-loop workflows |
| [Healthcare EHR & Telemedicine](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/healthcare-ehr.md) | Clinical records & video consults | HIPAA/HITECH compliance, HL7/FHIR APIs, de-identification pipeline |
| [Telecom CDR & Real-Time Billing](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/telecom-billing.md) | High-throughput telecom mediation | 500k events/sec Flink stream processing, rating engine, partitioned storage |
| [Retail Omnichannel & Edge POS](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/retail-omnichannel.md) | Store operations & unified commerce | Offline-first edge POS, eventual sync, unified inventory availability |
| [Smart Manufacturing & Industrial IoT](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/manufacturing-iot.md) | Factory telemetry & predictive maintenance | Edge MQTT broker, time-series lakehouse, digital twin, automated anomaly alerts |
| [Supply Chain & Fleet Logistics](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/logistics-supply-chain.md) | Real-time tracking & route dispatch | Geofencing, IoT event streaming, dynamic warehouse routing |
| [Government Digital Services Portal](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/government-portal.md) | Citizen identity & public services | National digital ID, accessibility, zero-trust inter-agency data exchange |
| [Multi-Tenant Enterprise B2B SaaS](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/saas-multitenant.md) | Cloud B2B SaaS application | Tenant isolation tiers (silo vs pool), dynamic DB routing, usage metering |
| [Enterprise Generative AI Platform](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/ai-agent-platform.md) | Multi-agent workflows & RAG | Autonomous ReAct loops, vector store ACLs, sandboxed tool execution |
| [Vertical Example Template](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/template.md) | Architecture blueprint starter | Standard template for authoring new vertical reference designs |
| [Industry Architecture Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/examples/checklists.md) | Domain-specific ARB review | 30-point evaluation standard across regulatory and domain requirements |
