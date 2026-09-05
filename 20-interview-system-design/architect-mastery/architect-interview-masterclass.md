# Architect Interview Masterclass

System design interviews for Principal and Enterprise Architects differ fundamentally from mid-level software engineer rounds. The interviewer is not evaluating whether you know Redis exists; they are evaluating your **judgment, framing, constraint discovery, trade-off depth, and leadership poise**.

## 1. The 18-Step Live System Design Framework

```
[Phase 1: Problem Framing & Discovery (0-10 min)]
1. Clarify the business objective & success metrics.
2. Discover hard constraints (regulatory, financial, physical).
3. Quantify NFRs & SLOs (p99 latency, availability, RPO/RTO).
4. Estimate scale & capacity back-of-the-envelope (QPS, IOPS, Storage).

[Phase 2: High-Level Architecture (10-20 min)]
5. Define API contracts & domain bounded contexts.
6. Design the high-level topology & data flow.
7. Select primary persistence engines based on access patterns.
8. Establish caching & data tiering topology.

[Phase 3: Deep Dives & Trade-Offs (20-35 min)]
9. Address core consistency & transaction semantics (CAP/PACELC).
10. Sharding, partitioning, and routing strategy (Consistent hashing).
11. Asynchronous processing, sagas, and event ordering.
12. Failure modes, blast radius, and circuit breaking.
13. Security, zero-trust identity, and data sovereignty.

[Phase 4: Operationalization & Synthesis (35-45 min)]
14. Observability, golden signals, and PRR gates.
15. FinOps & unit cost economics modeling.
16. Architectural red-teaming (adversarial attack scenarios).
17. Evolutionary roadmap & phased strangler migration.
18. One-page executive summary synthesis.
```

## 2. Navigating Ambiguity
When an interviewer says: *"Design a global ridesharing platform"*:
- **Do not** immediately start drawing microservice boxes.
- **Do**: Frame the scope. *"Are we focusing on the real-time driver-rider geospatial matching engine, or the end-of-trip payments and ledger reconciliation? Let's prioritize the matching engine first, while designing clean interfaces for payments."*

## 3. Behavioral & Leadership Questions for Architects
- *"Tell me about a time an engineering team refused to follow your architectural recommendation."*
  - Frame using influence without authority: prototype a spike, show data, uncover their unstated fears, align on shared metrics.
- *"Describe your most catastrophic production architectural failure."*
  - Frame with ownership and systemic learning: what broke, how the war room was led, the blameless post-mortem, and the automated fitness function built to prevent recurrence.

## Related Modules
- [Scenario Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/scenario-library/README.md)
- [Master System Design Methodology](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/system-design/master-system-design-methodology.md)
