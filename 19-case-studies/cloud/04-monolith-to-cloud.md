# Case Study 04: Monolith Decomposition to Cloud Microservices via Strangler Fig

## 1. Business Problem
A legacy e-commerce monolith suffered from 4-week deployment cycles, frequent regression outages, and inability to scale the checkout engine independently of the browsing catalog.

---

## 2. Current Architecture
Single Java WAR deployment running on Apache Tomcat with a massive single-instance Oracle 11g database containing 800 tables.

---

## 3. Constraints
Cannot afford a 2-year feature freeze to execute a complete rewrite. Business requires continuous delivery of new customer capabilities.

---

## 4. Non-Functional Requirements (NFRs)
- **Deployment Velocity**: Daily independent releases for core domains.
- **Resilience**: A failure in product reviews must not crash checkout.
- **Latency**: Checkout API response < 150ms.

---

## 5. Architectural Options Evaluated
1. **Option A: Big Bang Rewrite**: High probability of catastrophic failure.
2. **Option B: Strangler Fig Modernization**: Incremental service extraction behind an API routing proxy.

---

## 6. Architecture Decision & Rationale
Selected **Option B**. Gradually strangled the monolith over 18 months, extracting bounded contexts into independent microservices on managed Kubernetes.

---

## 7. Target Architecture Blueprint

```mermaid
graph TD
    Client[Web & Mobile Clients] --> Ingress[CloudFront / WAF Routing Proxy]
    Ingress -->|/api/v1/orders (New)| OrderSvc[Order Microservice: EKS]
    Ingress -->|/api/v1/catalog (New)| CatalogSvc[Catalog Microservice: EKS]
    Ingress -->|/* (Legacy Fallback)| Monolith[(Legacy Monolith on EC2)]

    OrderSvc --> OrderDB[(Aurora PostgreSQL)]
    Monolith <--> OracleLegacy[(Legacy Oracle DB)]
    OrderSvc -.->|Kafka Event| Monolith
```

---

## 8. Migration Strategy & Wave Plan
Decomposed in 5 iterative phases: 1. Routing facade, 2. Customer Reviews (low risk), 3. Product Catalog, 4. Order Ingestion, 5. Payment Clearing.

---

## 9. Security & Compliance Architecture
mTLS service mesh communication between microservices. OAuth2 JWT validation at the ingress gateway.

---

## 10. Day-2 Operations & Observability
Distributed tracing via OpenTelemetry and Jaeger to track requests traversing both modern microservices and legacy monolith code.

---

## 11. Financial Cost Modeling & ROI
Initial cost increased by 15% due to running dual environments during migration; reduced by 35% once legacy monolith servers were decommissioned.

---

## 12. Architectural Risks & Mitigations
- **Risk: Distributed transaction data divergence**. Mitigation: Implemented the Transactional Outbox pattern and asynchronous reconciliation jobs.

---

## 13. Technical Trade-Offs
- Accepted distributed systems latency overhead in exchange for independent team deployment autonomy.

---

## 14. Failure Scenarios & Self-Healing
- **Legacy Monolith Outage**: Modernized microservices continued taking customer orders asynchronously, storing them in Kafka until the legacy database recovered.

---

## 15. Lessons Learned & Retrospective
The Strangler Fig pattern is the only reliable methodology for decomposing enterprise monoliths without business disruption.
