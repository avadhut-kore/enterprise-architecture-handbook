# Enterprise Integration Complexity Assessment Framework

## 1. Objective
Quantifies the architectural complexity and risk of a proposed integration initiative before design approval.

## 2. The 5-Dimensional Complexity Scoring Model

| Dimension | Low Complexity (Score: 1) | Medium Complexity (Score: 3) | High / Critical Complexity (Score: 5) |
| :--- | :--- | :--- | :--- |
| **Data Sensitivity** | Public catalog / Telemetry | Internal operational data | PCI-DSS Cardholder Data, PHI, Core Banking Ledger |
| **Latency SLA** | Batch / Hours | Near real-time (1s - 5s) | Sub-second real-time (< 200ms) with strict timeout budgets |
| **Consistency Model**| Eventual consistency acceptable| Compensating actions allowed | Strict transactional atomicity / Multi-system Saga required |
| **Protocol Legacy** | Modern REST / JSON / GraphQL | SOAP / XML / JMS | Mainframe SNA, EBCDIC Copybooks, 3270 Terminal Screen Scraping |
| **Integration Volume**| < 10,000 requests/day | 10k - 1,000,000 requests/day | > 10,000,000 requests/day (> 1,000 TPS burst) |

### Total Complexity Index Formula
$$	ext{Complexity Score} = \sum_{i=1}^{5} w_i 	imes 	ext{Dimension Score}_i$$
- **Score 5 - 11**: Tier 3 (Standard Lightweight Integration). Fast-track ARB review.
- **Score 12 - 18**: Tier 2 (Standard Enterprise Integration). Requires formal ADR and security review.
- **Score 19 - 25**: Tier 1 (Mission-Critical Integration). Mandates full ARB review, threat model, and chaos testing.
