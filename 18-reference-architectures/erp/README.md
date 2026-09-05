# Enterprise Resource Planning (ERP) Platform Reference Architecture

## 1. Executive Summary & Architectural Vision
The Cloud-Native ERP Platform is an enterprise system of record governing financial accounting (General Ledger, AP/AR), procurement (Procure-to-Pay), sales order fulfillment (Order-to-Cash), and material master data across global subsidiaries. 

It implements the modern **Clean Core** architecture: keeping the core financial journal standardized while deploying business extensions on cloud-native sidecars integrated via real-time event streams and standard REST/OData APIs.

```
[Enterprise Applications: CRM, E-Commerce, Payroll, Procurement Portals]
                                  │
             ═════════════════════▼═════════════════════  [Integration Gateway]
                        ERP Core Services
     ┌─────────────────┬──────────────────┬──────────────────┐
     ▼                 ▼                  ▼                  ▼
[General Ledger]      [Procure-to-Pay]   [Order-to-Cash]    [Master Data Hub]
(Universal Journal)   (3-Way Matching)   (Billing Engine)   (Customer & Vendor)
     │                 │                  │                  │
     └─────────────────┼──────────────────┴──────────────────┘
                       ▼
            [Enterprise Event Backbone (Kafka)]
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
[Banking Payment Rails]     [Corporate Data Lakehouse]
(ISO 20022 camt/pain)       (SOX Financial Audit Vault)
```

## 2. Architectural Package Contents
- [01-business-and-requirements.md](01-business-and-requirements.md): Value streams, multi-currency ledger scale, and SOX NFRs.
- [02-architecture-and-c4.md](02-architecture-and-c4.md): C4 Context, Container, Component models, and cloud mappings.
- [03-application-architecture.md](03-application-architecture.md): Service boundaries, general ledger posting, and three-way match.
- [04-data-architecture.md](04-data-architecture.md): Universal Journal schema (`ACDOCA`), master data, and immutability.
- [05-integration-architecture.md](05-integration-architecture.md): Banking payment integration, EDI 850/810, and Clean Core sidecars.
- [06-security-and-compliance.md](06-security-and-compliance.md): Segregation of Duties (SoD), SOX 404, and audit trails.
- [07-infrastructure-and-devops.md](07-infrastructure-and-devops.md): High-availability database clusters, Terraform IaC, and CI/CD.
- [08-observability-and-reliability.md](08-observability-and-reliability.md): Month-end closing timers, journal reconciliation, and DR.
- [09-cost-and-finops.md](09-cost-and-finops.md): Database memory sizing, ERP compute licensing, and TCO model.
- [10-sequences-and-flows.md](10-sequences-and-flows.md): Procure-to-pay workflow, three-way invoice matching, and ledger posting.
- [11-adrs-and-evolution.md](11-adrs-and-evolution.md): Canonical ADRs (Clean Core Sidecars, In-Memory Columnar Ledger) and roadmap.
