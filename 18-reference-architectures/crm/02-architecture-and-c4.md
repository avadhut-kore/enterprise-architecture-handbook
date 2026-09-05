# C4 Architecture Model & Cloud Mapping: Enterprise CRM

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
title System Context: Enterprise CRM Platform
Person(rep, "Sales & Support Rep", "Manages leads, accounts, and tickets")
Person(customer, "End Customer", "Submits inquiries via portal or email")
System(crm, "Enterprise CRM Platform", "Manages Customer 360, Pipeline, and Service Desk")
System_Ext(erp, "ERP System (SAP)", "Authoritative System of Record for General Ledger & Inventory")
System_Ext(marketing, "Marketing Automation", "HubSpot / Marketo lead generator")
System_Ext(telephony, "Telephony CTI", "Amazon Connect / Genesys voice platform")

Rel(rep, crm, "Manages deals & tickets", "HTTPS")
Rel(customer, crm, "Submits support inquiries", "Email / Web Chat")
Rel(crm, erp, "Syncs closed-won deals & invoices", "Kafka / OData")
Rel(marketing, crm, "Pushes qualified inbound leads", "REST Webhooks")
Rel(telephony, crm, "Pushes call logs & screen pops", "WebSockets")
```

---

## 2. C4 Level 2: Container Diagram

```mermaid
C4Container
title Container Diagram: Enterprise CRM Platform
Container(bff, "Web & Mobile BFF", "Node.js / Express", "Aggregates customer data and manages user sessions")
Container(account_svc, "Account & Contact Service", "Java / Spring Boot", "Maintains Customer 360 hierarchy and deduplication")
Container(opp_svc, "Opportunity & Pipeline Service", "Go", "Manages deal stages, forecasting, and quote generation")
Container(ticket_svc, "Service Desk Engine", "Java / Spring Boot", "Omnichannel routing, SLA timers, and escalation queues")
Container(db_primary, "CRM Master Database", "PostgreSQL Aurora Multi-AZ", "Stores relational entities, pipelines, and audit logs")
Container(timeline_db, "Activity Timeline Store", "Cassandra / DynamoDB", "High-throughput append-only customer interaction history")
Container(event_bus, "Enterprise Event Backbone", "Apache Kafka", "Streams mutations to ERP, data lake, and notification services")

Rel(bff, account_svc, "Fetches customer profiles", "gRPC")
Rel(bff, opp_svc, "Updates opportunity stages", "gRPC")
Rel(account_svc, db_primary, "Reads/Writes accounts", "SQL")
Rel(opp_svc, event_bus, "Publishes opportunity.closed_won", "TCP")
Rel(ticket_svc, timeline_db, "Appends customer call logs", "CQL")
```

---

## 3. Technology-Neutral to Cloud Provider Mapping

| Component | Technology-Neutral | AWS Implementation | Azure Implementation | GCP Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **API Gateway** | Kong / Envoy | Amazon API Gateway | Azure API Management | Apigee / Cloud Endpoints |
| **Microservices Compute**| Kubernetes (Containerized)| Amazon EKS | Azure Kubernetes Service (AKS)| Google Kubernetes Engine (GKE) |
| **Relational OLTP** | PostgreSQL | Amazon Aurora PostgreSQL | Azure Database for PostgreSQL | Cloud SQL for PostgreSQL |
| **Activity Store** | Wide-column NoSQL | Amazon DynamoDB | Azure Cosmos DB | Google Cloud Bigtable |
| **Event Streaming** | Apache Kafka | Amazon MSK | Azure Event Hubs | Google Cloud Pub/Sub |
| **Search Engine** | Elasticsearch / OpenSearch | Amazon OpenSearch Service | Azure AI Search | Google Cloud OpenSearch |
