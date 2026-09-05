# C4 Architecture Model & Cloud Mapping: Fintech Platform

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
title System Context: Fintech & Real-Time Payments Engine
Person(customer, "Banking Customer", "Transfers funds and uses debit card")
System(fintech, "Fintech Platform Core", "Ledger, card processing, instant rails, and fraud scoring")
System_Ext(card_net, "Card Networks", "Visa / Mastercard / Discover via ISO 8583")
System_Ext(fednow, "Federal Reserve FedNow", "Instant Settlement via ISO 20022 pacs.008")
System_Ext(hsm, "Hardware Security Module", "AWS CloudHSM / Thales Luna for PIN translation")

Rel(customer, fintech, "Initiates transfer / pays", "HTTPS / Mobile")
Rel(card_net, fintech, "Sends card auth request", "Direct Connect ISO 8583")
Rel(fintech, hsm, "Validates card PIN & CVV", "PKCS#11")
Rel(fintech, fednow, "Submits real-time credit transfer", "mTLS ISO 20022")
```

---

## 2. Technology-Neutral to Cloud Provider Mapping

| Component | Technology-Neutral | AWS Implementation | Azure Implementation | GCP Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **Ledger Database** | CockroachDB / Spanner | Amazon Aurora Multi-Master | Azure Cosmos DB (Strong)| Google Cloud Spanner |
| **Key & PIN Management**| Hardware Security Module| AWS CloudHSM | Azure Dedicated HSM | Google Cloud HSM |
| **Event Streaming** | Apache Kafka | Amazon MSK | Azure Event Hubs | Google Cloud Pub/Sub |
| **In-Memory Auth Cache**| Redis Enterprise | Amazon ElastiCache | Azure Cache for Redis | Cloud Memorystore |
