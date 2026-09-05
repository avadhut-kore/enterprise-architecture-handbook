# Architecture Diagram Review Checklist

Use this 50-point review gate during **Architecture Review Boards (ARB)**, Technical Design Reviews (TDD), Security Audits, and Production Readiness Reviews (PRR).

---

## 1. Clarity & Communication (10 Points)
- [ ] 1. Does the diagram have an unambiguous, descriptive title and declared version?
- [ ] 2. Is the target audience explicitly identified (Executive, Engineering, Security, Ops)?
- [ ] 3. Is the abstraction level declared (System Context, Container, Component, Deployment)?
- [ ] 4. Does the diagram answer one primary architectural question without visual clutter?
- [ ] 5. Is there a clear, readable visual hierarchy with consistent left-to-right or top-to-bottom flow?
- [ ] 6. Are all acronyms and specialized domain terms defined in an accompanying legend?
- [ ] 7. Are node boxes appropriately sized and labeled with business functional names?
- [ ] 8. Are technologies clearly marked on container/deployment elements?
- [ ] 9. Does the diagram minimize crossing connector lines to avoid visual confusion?
- [ ] 10. Can an engineer or architect understand the diagram within 60 seconds without verbal explanation?

---

## 2. Boundaries & Modularity (10 Points)
- [ ] 11. Are system boundaries clearly delineated with visual subgraphs or bounding boxes?
- [ ] 12. Are external third-party SaaS and partner APIs clearly distinguished from internal systems?
- [ ] 13. Is the boundary of the system under design unambiguously separated from existing systems?
- [ ] 14. Are database and storage boundaries shown per service (avoiding shared-database anti-patterns)?
- [ ] 15. Are asynchronous queues and event brokers shown decoupling producers from consumers?
- [ ] 16. Are client types (Web, Mobile iOS/Android, IoT, Partner B2B) explicitly separated?
- [ ] 17. Are API Gateways and Ingress Controllers positioned at the appropriate boundary?
- [ ] 18. Are batch workflows visually separated from real-time synchronous request paths?
- [ ] 19. Are domain bounded contexts respected according to Domain-Driven Design (DDD)?
- [ ] 20. Are internal and external service endpoints clearly distinguished?

---

## 3. Protocols & Relationships (10 Points)
- [ ] 21. Is every relationship arrow labeled with its business action (e.g., `Submit Order`)?
- [ ] 22. Does every arrow indicate the transport protocol (HTTPS, gRPC, WSS, TCP, AMQP)?
- [ ] 23. Does every arrow indicate payload serialization (JSON, Protobuf, Avro, XML)?
- [ ] 24. Are synchronous invocations distinguished visually from asynchronous event broadcasts?
- [ ] 25. Is the direction of dependency clearly distinguished from the direction of data flow?
- [ ] 26. Are polling mechanisms distinguished from webhook callbacks or streaming push?
- [ ] 27. Are database read operations distinguished from write/mutation operations where relevant?
- [ ] 28. Are caching lookups and cache-miss fallback flows explicitly documented?
- [ ] 29. Are dead-letter queue (DLQ) pathways documented for asynchronous workers?
- [ ] 30. Are inter-service timeouts and retry boundaries identifiable?

---

## 4. Security & Compliance (10 Points)
- [ ] 31. Are trust boundaries (Public Internet, DMZ, Private Subnet, Secure Enclave) drawn?
- [ ] 32. Is user authentication and token exchange (OAuth2/OIDC) explicitly mapped?
- [ ] 33. Are service-to-service authorization controls (mTLS, JWT, IAM roles) indicated?
- [ ] 34. Are secrets and key management systems (Vault, KMS, HSM) represented?
- [ ] 35. Are encryption-in-transit (TLS 1.3) and encryption-at-rest boundaries documented?
- [ ] 36. Are edge security protections (WAF, DDoS mitigation, Bot management) visual?
- [ ] 37. Are PII or PCI-DSS regulated data pathways clearly tagged and isolated?
- [ ] 38. Are privileged administrative access and break-glass pathways documented?
- [ ] 39. Is the attack surface identifiable for STRIDE threat modeling analysis?
- [ ] 40. Are audit logging and SIEM telemetry aggregation pipelines shown?

---

## 5. Operations, Resilience & Deployment (10 Points)
- [ ] 41. Are physical deployment environments (Multi-AZ, Multi-Region, On-Prem) marked?
- [ ] 42. Are single points of failure (SPOFs) identifiable and mitigated with redundancy?
- [ ] 43. Are load balancers, health check probes, and traffic splitters represented?
- [ ] 44. Are disaster recovery (DR) replication links and RTO/RPO expectations evident?
- [ ] 45. Are circuit breakers, fallback routes, and bulkhead isolation patterns visible?
- [ ] 46. Are telemetry agents (OpenTelemetry, Prometheus, Fluentbit) represented?
- [ ] 47. Is autoscaling topology (K8s HPA/Cluster Autoscaler, VM Scale Sets) indicated?
- [ ] 48. Does the diagram match the active Infrastructure as Code (Terraform/Bicep)?
- [ ] 49. Are backup storage and immutable retention mechanisms visualized?
- [ ] 50. Is the diagram version-controlled in Git as Mermaid or PlantUML code?
