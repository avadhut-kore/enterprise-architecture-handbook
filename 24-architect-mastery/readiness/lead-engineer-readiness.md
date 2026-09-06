# Role Readiness Gate: Lead Software Engineer (Tech Lead)

> **"Readiness for Lead Engineer is proven by team multiplier leverage, architectural decomposition, delivery predictability, and cross-team consensus building."**

---

## 1. Readiness Threshold Matrix

| Pillar | Required Standard | Verification Method |
| :--- | :--- | :--- |
| **1. Knowledge** | Level 3 (Advanced) across Software Architecture, System Design, and Integration. | Review against [Competency Matrix](../skill-matrix/architect-competency-matrix.md). |
| **2. Experience** | Led 1+ multi-month epic across 3+ engineers from design to production; facilitated 1+ team game-day or DR drill. | Sprint retrospectives, delivery timeline tracking, post-mortems. |
| **3. Decisions** | Authored 3+ formal Architecture Decision Records (ADRs) evaluating non-trivial technical trade-offs. | Inspect Git ADR directory. |
| **4. Evidence** | 2 approved High-Level Designs (HLD); 1 prioritized team technical debt roadmap; 3 documented ADRs. | Git repository artifacts and ARB approval records. |

---

## 2. Core Readiness Checklist

### Multiplier Leverage & Team Direction
- [ ] Breaks down large, ambiguous product epics into cleanly decoupled, technically sequenced engineering tasks.
- [ ] Empowers team members to deliver complex components rather than coding the entire critical path personally.
- [ ] Establishes team-wide coding, testing, and CI/CD quality standards that survive personal absence.

### Architectural Stewardship
- [ ] Authors comprehensive HLDs with clear C4 Container and Component models before implementation begins.
- [ ] Uses `python 21-architecture-tools/generators/adr_generator.py` to document architectural trade-offs.
- [ ] Proactively designs for failure: handles downstream timeouts, circuit breaking, fallback states, and idempotency.

### Cross-Team Alignment & Product Partnership
- [ ] Negotiates clear, backward-compatible API contracts with adjacent engineering squads.
- [ ] Partners effectively with the Product Manager to balance product feature velocity against technical debt reduction.
- [ ] Decisively resolves technical deadlocks within the team while maintaining psychological safety and high morale.

---

## 3. Mandatory Evidence Portfolio Items
1. **High-Level Design (HLD)**: Authoring a multi-service architecture blueprint ([HLD Template](../../16-architecture-deliverables/HLD-TEMPLATE.md)).
2. **Architecture Decision Records (ADRs)**: 3 peer-reviewed ADRs justifying database selection, communication styles, or caching topologies ([ADR Template](../../16-architecture-deliverables/ADR-TEMPLATE.md)).
3. **Team Technical Debt Ledger**: Quantified technical debt backlog with business impact and remediation timelines.

---

## 4. Remediation Plan if Not Ready
* **If lacking delegation/multiplier skills**: Explicitly assign the next high-visibility feature to a mid-level engineer; coach them through the design and delivery without writing the code.
* **If lacking architectural rigor**: Author an HLD for an upcoming epic and schedule a peer review with a Staff or Solution Architect.
