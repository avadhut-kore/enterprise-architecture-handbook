# System Design Checklist: Requirements Clarification

## 1. Functional Scope Clarification
- [ ] What are the top 3 core user workflows that generate 80% of business value?
- [ ] What capabilities are explicitly **out of scope** for this design phase?
- [ ] What are the client form factors (Mobile, Web, IoT, Headless API)?
- [ ] Are operations real-time synchronous, asynchronous batch, or event-driven?

## 2. Non-Functional Requirements (Quantified Targets)
- [ ] Target Availability SLA defined (e.g., 99.9% vs 99.99%)?
- [ ] Target Latency defined (P50 < 50ms, P95 < 150ms, P99 < 300ms)?
- [ ] Consistency requirements classified (Strict Linearizable vs Eventual)?
- [ ] Data durability and retention requirements defined (e.g., 7 years for compliance)?
