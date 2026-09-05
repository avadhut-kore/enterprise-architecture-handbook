# C4 Architecture Model & Cloud Mapping: Logistics Platform

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
title System Context: Logistics & Freight Orchestration Platform
Person(driver, "Truck Driver", "Executes routes via Mobile App")
Person(dispatcher, "Dispatcher", "Monitors fleet map and assigns loads")
System(logistics, "Logistics Platform", "TMS, VRP optimization, telematics, and EDI")
System_Ext(telematics, "Vehicle Telematics (ELD)", "Streams GPS, speed, fuel, and reefer temperature")
System_Ext(carrier_edi, "Partner Carrier Rails", "Exchanges EDI 204 tenders & EDI 214 status updates")
System_Ext(map_provider, "Map & Routing Provider", "HERE / Google Maps / Mapbox routing tiles")

Rel(driver, logistics, "Syncs route & submits proof of delivery", "HTTPS / Offline Sync")
Rel(telematics, logistics, "Streams sensor coordinates", "MQTT over TLS")
Rel(dispatcher, logistics, "Manages fleet & routes", "HTTPS / WebSockets")
Rel(logistics, carrier_edi, "Exchanges load tender documents", "AS2 / SFTP")
Rel(logistics, map_provider, "Calculates travel times & traffic", "REST")
```

---

## 2. Technology-Neutral to Cloud Provider Mapping

| Component | Technology-Neutral | AWS Implementation | Azure Implementation | GCP Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **IoT Telematics Ingress**| EMQX / VerneMQ (MQTT) | AWS IoT Core | Azure IoT Hub | Google Cloud IoT Core |
| **Spatial Indexing DB** | PostGIS / Uber H3 | Amazon Aurora PostgreSQL | Azure Database for PostgreSQL | Cloud SQL for PostgreSQL |
| **Route Optimization Engine**| OptaPlanner / VRP Worker| Amazon EKS Batch Pods | Azure Batch / AKS | Google Cloud Batch / GKE |
| **Time-Series Telematics**| ClickHouse / TimescaleDB| Amazon Managed Grafana/Timestream| Azure Data Explorer | BigQuery Time Series |
