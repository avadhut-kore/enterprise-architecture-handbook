# Global EdTech & Learning Management Platform Reference Architecture

## 1. Executive Summary & Architectural Vision
The Global EdTech & Learning Management Platform is a scalable educational system supporting 10+ million students with high-definition adaptive video streaming, interactive real-time assessments, automated proctoring telemetry, gradebook calculations, and strict student data privacy (FERPA / COPPA).

```
[Student App (Web/Mobile), Teacher Portal, Parent Dashboard, Admin]
                                  │
             ═════════════════════▼═════════════════════  [Global CDN Edge]
                       API Gateway & BFF
     ┌─────────────────┬──────────────────┬──────────────────┐
     ▼                 ▼                  ▼                  ▼
[Course & Content]    [Video Streaming]  [Assessment Engine] [Student Analytics]
(Curriculum CMS)      (HLS/DASH with DRM)(Real-Time Scoring) (Progress Tracking)
     │                 │                  │                  │
     └─────────────────┼──────────────────┴──────────────────┘
                       ▼
            [Event Backbone (Apache Kafka)]
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
[Proctoring Telemetry]      [AI Personalized Tutor]
(WebRTC Stream Ingestion)   (RAG Educational Assistant)
```

## 2. Architectural Package Contents
- [01-business-and-requirements.md](01-business-and-requirements.md): Student personas, scale assumptions, and FERPA privacy NFRs.
- [02-architecture-and-c4.md](02-architecture-and-c4.md): C4 Context, Container, Component models, and cloud mappings.
- [03-application-architecture.md](03-application-architecture.md): Service boundaries, assessment engines, and video streaming.
- [04-data-architecture.md](04-data-architecture.md): Curriculum graphs, time-series telemetry, and gradebook schemas.
- [05-integration-architecture.md](05-integration-architecture.md): LTI (Learning Tools Interoperability), Zoom/WebRTC, and SIS sync.
- [06-security-and-compliance.md](06-security-and-compliance.md): FERPA, COPPA, student PII protection, and DRM content security.
- [07-infrastructure-and-devops.md](07-infrastructure-and-devops.md): Video transcoding pipelines, CDN caching, and Kubernetes.
- [08-observability-and-reliability.md](08-observability-and-reliability.md): Video buffering ratio, assessment submission SLOs, and DR.
- [09-cost-and-finops.md](09-cost-and-finops.md): Video bandwidth economics, transcoding compute, and monthly TCO.
- [10-sequences-and-flows.md](10-sequences-and-flows.md): Timed assessment submission, video stream auth, and proctoring.
- [11-adrs-and-evolution.md](11-adrs-and-evolution.md): Canonical ADRs (HLS Video Streaming, Cassandra Telemetry) and roadmap.
