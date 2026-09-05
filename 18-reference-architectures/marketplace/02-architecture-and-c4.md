# C4 Architecture Model & Cloud Mapping: Marketplace Platform

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
title System Context: Multi-Sided Marketplace Platform
Person(buyer, "Buyer", "Browses, purchases, and writes reviews")
Person(seller, "Merchant Seller", "Publishes listings and receives payouts")
System(mkt, "Marketplace Core Platform", "Listings, search, escrow payments, and payouts")
System_Ext(pay_platform, "Payout Rail (Stripe Connect)", "Manages seller connected accounts and payouts")
System_Ext(kyc_provider, "Seller KYC (Persona / Jumio)", "Verifies government IDs and business tax numbers")

Rel(buyer, mkt, "Orders products", "HTTPS")
Rel(seller, mkt, "Manages inventory & views payouts", "HTTPS")
Rel(mkt, pay_platform, "Authorizes charge & triggers split transfers", "mTLS REST")
Rel(mkt, kyc_provider, "Validates seller merchant identity", "REST")
```

---

## 2. Technology-Neutral to Cloud Provider Mapping

| Component | Technology-Neutral | AWS Implementation | Azure Implementation | GCP Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **Catalog Search** | OpenSearch / Elasticsearch | Amazon OpenSearch Service | Azure AI Search | Google Cloud OpenSearch |
| **Transactional DB** | PostgreSQL Aurora Multi-AZ | Amazon Aurora PostgreSQL | Azure Database for PostgreSQL | Cloud SQL for PostgreSQL |
| **Payout Orchestrator**| Stripe Connect / Adyen | Stripe API Integration | Stripe / Adyen API | Stripe / Adyen API |
| **Event Streaming** | Apache Kafka | Amazon MSK | Azure Event Hubs | Google Cloud Pub/Sub |
