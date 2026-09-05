# C4 Model Review Checklist

Use this checklist to audit C4 diagrams for architectural rigor and clarity before submitting to stakeholders or the Architecture Review Board (ARB).

---

## Level 1: System Context Review
- [ ] Is the primary software system under design immediately recognizable in the center?
- [ ] Are all human user roles modeled as Persons with distinct responsibilities?
- [ ] Are all external dependencies (SaaS, legacy backends, payment rails) shown outside the system boundary?
- [ ] Are internal implementation details (databases, microservices, languages) strictly excluded?
- [ ] Does every relationship arrow indicate a clear business purpose (e.g., "Submits loan application")?

## Level 2: Container Review
- [ ] Is every container a genuinely separate deployable unit (SPA, mobile app, API, DB, worker)?
- [ ] Is the technology stack explicitly noted on every container (e.g., `[Spring Boot 3.2]`, `[PostgreSQL 16]`)?
- [ ] Are datastores explicitly tied to their owning services (avoiding shared-database coupling)?
- [ ] Are transport protocols and serialization formats documented on communication lines?
- [ ] Are asynchronous event brokers and queues clearly differentiated from synchronous REST/gRPC calls?

## Level 3: Component Review
- [ ] Does the diagram focus on a single container rather than spanning across multiple services?
- [ ] Are component boundaries organized by architectural layer or DDD bounded context?
- [ ] Are outbound infrastructure adapters separated from core domain business services?
- [ ] Is the diagram simple enough that a new developer can understand service structure in 5 minutes?

## Deployment Review
- [ ] Are physical hosting nodes (Cloud VPCs, Availability Zones, Kubernetes clusters) clearly demarcated?
- [ ] Are container-to-node allocations unambiguous?
- [ ] Are network security subnets (public ingress vs isolated private data subnets) explicit?
