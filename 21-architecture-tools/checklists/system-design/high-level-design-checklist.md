# System Design Checklist: High-Level Architecture

## 1. Topology & Separation of Concerns
- [ ] C4 System Context and Container diagrams documented?
- [ ] Clear separation between Client, Edge Gateway, Compute, and Storage tiers?
- [ ] Stateless compute tier decoupled from persistent state stores?
- [ ] External third-party integrations isolated via Anti-Corruption Layers?

## 2. Data Flow & Communication
- [ ] End-to-end read and write sequence diagrams documented with step numbers?
- [ ] Asynchronous event streaming utilized for non-blocking downstream tasks?
- [ ] Single Points of Failure (SPOF) identified and mitigated across all tiers?
