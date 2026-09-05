# The 8 Enterprise Reference Models

Standardized blueprints providing baseline starting points for enterprise architecture design.

---

## 1. Enterprise Business Capability Reference Model (BCRM)
* **Customer Domain**: Marketing, Acquisition, Customer Care, Identity/KYC, Loyalty.
* **Product Domain**: Catalog Management, Pricing & Packaging, Actuarial/R&D, Lifecycle Management.
* **Operations Domain**: Order Management, Inventory/Supply Chain, Manufacturing/Execution, Quality.
* **Corporate Domain**: Financial Ledgers, Treasury, Human Capital, Legal/Compliance, Enterprise Procurement.

---

## 2. Enterprise Application Reference Model (ARM)
* **Channel Layer**: Mobile, Web, B2B EDI, IoT Edge, Contact Center Portal.
* **Integration Layer**: API Management Gateway, Event Streaming Mesh, B2B Secure Vault.
* **Domain Services Layer**: Customer Service, Product Engine, Billing Engine, Rules Engine.
* **Core Systems of Record**: ERP, Core Banking/Ledger, Policy Admin, Master Data Hub.

---

## 3. Enterprise Data Reference Model (DRM)
* **Master Data (MDM)**: Customer, Product, Supplier, Location, Chart of Accounts.
* **Transactional Data**: Orders, Invoices, Payments, Claims, Ledger Entries.
* **Analytical Data**: Lakehouse Curated Zone, Feature Stores, Executive Data Marts.

---

## 4. Enterprise Integration Reference Model (IRM)
* **Synchronous**: REST OpenAPI 3.0, gRPC, GraphQL.
* **Asynchronous**: Kafka Pub/Sub, RabbitMQ Queuing, Cloud Native Event Bridges.
* **Batch / Bulk**: SFTP Secure Transit, S3 Parquet Replication, ETL/CDC Pipelines.

---

## 5. Enterprise Technology Reference Model (TRM)
* **Languages**: Java 21, .NET 8, Python 3.12, TypeScript 5.
* **Databases**: PostgreSQL 16 (Relational), Redis 7 (In-Memory), DynamoDB / MongoDB (Document), Snowflake (OLAP).
* **Container Runtimes**: Kubernetes (EKS / AKS / GKE), containerd.

---

## 6. Enterprise Security Reference Model (SRM)
* **Identity**: FIDO2 MFA, OIDC / OAuth2, SPIFFE/SPIRE Machine Identity.
* **Data Protection**: AES-256 GCM at Rest, TLS 1.3 in Transit, Cloud KMS Key Hierarchy.
* **Perimeter**: Web Application Firewall (WAF), Zero-Trust Network Access (ZTNA), SIEM/SOC Telemetry.

---

## 7. Enterprise Cloud Reference Model (CRM)
* **Landing Zone**: Multi-account isolation, Hub-and-Spoke Transit Gateway, Shared Services account.
* **Resilience**: Multi-Availability Zone (99.99%), Multi-Region Active-Passive (Tier-1), Active-Active (Tier-0).

---

## 8. Enterprise AI Reference Model (AIRM)
* **Control Plane**: Central Model Gateway, Rate Limiting, Semantic Cache, Prompt Injection WAF.
* **Capability Services**: Enterprise RAG Knowledge Store, Fine-Tuned SLMs, Tool-Calling Agents.
* **Governance**: EU AI Act Risk Classifier, LLM-as-a-Judge Evaluation Gateways, Token Cost Allocation.
