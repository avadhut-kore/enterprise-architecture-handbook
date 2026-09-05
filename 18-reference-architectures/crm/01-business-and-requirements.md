# Business Architecture & Requirements: Enterprise CRM

## 1. Business Context & User Personas
- **Sales Representatives & Account Executives**: Need instantaneous access to customer timelines, opportunity stages, product catalogs, and real-time quote generation.
- **Customer Support Agents**: Require unified omni-channel ticket queues (voice, chat, email) with SLA countdown timers and embedded customer order histories.
- **Marketing Operations**: Need high-throughput ingestion of marketing campaign leads and real-time behavioral segmentation.

---

## 2. Scale Model & Capacity Assumptions

| Scale Parameter | Baseline | 10x Scale Target | 100x Scale Target |
| :--- | :--- | :--- | :--- |
| **Internal Licensed Users** | 2,500 agents | 25,000 agents | 250,000 agents |
| **Customer Master Records** | 5,000,000 contacts | 50,000,000 contacts | 500,000,000 contacts |
| **Active Opportunities** | 200,000 open | 2,000,000 open | 20,000,000 open |
| **Peak API Throughput** | 800 req/sec | 8,000 req/sec | 80,000 req/sec |
| **Daily Ingested Activities** | 10 Million events | 100 Million events | 1 Billion events |
| **Total Relational Storage** | 1 TB | 10 TB | 100 TB |

---

## 3. Measurable NFR Budgets

| NFR Metric | Target Budget | Measurement & Enforcement Point |
| :--- | :--- | :--- |
| **Read Latency (Customer 360)**| $< 120\text{ ms}$ (p95) | API Gateway edge cache / Redis master profile store |
| **Opportunity Save Latency** | $< 300\text{ ms}$ (p99) | Relational database write transaction boundary |
| **Platform Availability** | 99.95% ($< 21.9\text{ min}$/mo) | Multi-AZ active-active container cluster |
| **Event Sync Latency to ERP** | $< 2.0\text{ seconds}$ | Kafka outbox consumer lag to SAP/Oracle connectors |
| **Data Retention (Audit Trail)**| 7 years immutable | S3 / Blob cold WORM storage for SOX/GDPR compliance |
