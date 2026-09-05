# C4 Architecture Model & Cloud Mapping: Global EdTech Platform

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
title System Context: Global EdTech Platform
Person(student, "Student", "Accesses courses, watches lectures, takes exams")
Person(teacher, "Teacher / Instructor", "Creates curriculum, grades assignments, conducts live sessions")
System(edtech, "Global EdTech Platform", "LMS, video streaming, assessment, and analytics")
System_Ext(sis, "School Information System", "PowerSchool / Ellucian Banner via LTI")
System_Ext(cdn, "Global Video CDN", "Cloudflare / Fastly HLS Video Distribution")
System_Ext(proctor, "AI Proctoring Service", "Automated eye-tracking and audio anomaly detection")

Rel(student, edtech, "Interacts with courses", "HTTPS / WSS")
Rel(student, cdn, "Streams video chunks", "HLS / DASH")
Rel(teacher, edtech, "Manages curriculum", "HTTPS")
Rel(edtech, sis, "Syncs rosters and final grades", "LTI 1.3 / REST")
Rel(edtech, proctor, "Streams exam telemetry", "WebSockets")
```

---

## 2. Technology-Neutral to Cloud Provider Mapping

| Component | Technology-Neutral | AWS Implementation | Azure Implementation | GCP Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **Video Transcoding** | FFmpeg on Spot Workers | AWS Elemental MediaConvert | Azure Media Services | GCP Transcoder API |
| **Video Distribution**| HLS / DASH over CDN | Amazon CloudFront | Azure Front Door / CDN | Google Cloud CDN |
| **LMS Relational DB** | PostgreSQL | Amazon Aurora PostgreSQL | Azure Database for PostgreSQL | Cloud SQL for PostgreSQL |
| **Telemetry Store** | Wide-column / Time-series| Amazon Timestream / DynamoDB| Azure Cosmos DB | Google Cloud Bigtable |
| **Live Classroom** | WebRTC SFU (LiveKit) | EKS with UDP Load Balancers | AKS with UDP Load Balancers | GKE with UDP Load Balancers |
