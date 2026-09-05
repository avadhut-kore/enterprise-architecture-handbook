# Integration Design Specification: [INTEGRATION NAME]

---
**Metadata**:
```yaml
document_id: "INT-[NAME]-001"
title: "Integration Design Specification — [Integration Name]"
version: "1.0.0"
status: "Draft" # Draft | In Review | Approved | Implemented
owner: "[Integration Architect / Lead Engineer Name <email>]"
source_system: "[Source System Name (Owner)]"
target_system: "[Target System Name (Owner)]"
interaction_type: "Asynchronous Event" # Sync REST | gRPC | Async Event | Batch sFTP
created_date: "YYYY-MM-DD"
```
---

## 1. Executive Summary & Business Flow
* What business process requires this integration (e.g., Order-to-Cash, Hire-to-Retire)?
* High-level sequence diagram linking source, middleware, and target systems.

## 2. Systems & Ownership Boundaries
| System | Role | Technology Stack | Hosting Environment | Technical Owner |
|---|---|---|---|---|
| **System A** | Source (Producer) | Node.js / PostgreSQL | AWS us-east-1 | Order Management Team |
| **System B** | Target (Consumer) | SAP S/4HANA | On-Premises Corporate DC | ERP Finance Team |

## 3. Interaction Pattern & Protocol
* Transport: Apache Kafka Topic `erp.finance.order-settled.v1` | HTTPS REST.
* Payload Format: JSON Schema / Protobuf / ISO 20022 XML.

## 4. Message Ordering & Partitioning
* Partitioning key used to guarantee sequential delivery (e.g., `customer_id` or `order_id`).

## 5. Failure Handling & Circuit Breaking
* Maximum retry attempts: 5 attempts with exponential backoff and decorrelated jitter.
* Dead-Letter Queue (DLQ): Topic `erp.finance.order-settled.dlq`.
* Alerting threshold: > 5 messages in DLQ triggers PagerDuty escalation.

## 6. Deduplication & Idempotency
* Idempotency check mechanism: Target system verifies `event_id` against a deduplication table before executing financial postings.

## 7. Security & Transport Encryption
* Network: AWS Direct Connect / IPsec VPN tunnel with mTLS (X.509 client certificates).
* Authentication: OAuth 2.0 Client Credentials Grant.

## 8. Reconciliation & Audit
* Daily automated batch job compares record counts and financial balances between source and target systems.
