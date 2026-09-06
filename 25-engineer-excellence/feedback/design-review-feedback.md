# Architectural Design Review & RFC Feedback

> **"A design review is not an audition to prove who is the smartest engineer in the room. It is a collaborative stress-test designed to break the architecture on paper before we spend six months building it in production."**

---

## 1. The Mindset of Architectural Critique

When reviewing an Architecture Decision Record (ADR) or Request for Comments (RFC), reviewers must balance rigorous scrutiny with intellectual humility. Critiquing an architecture requires evaluating **trade-offs against business constraints**, not enforcing personal aesthetic preferences:

```mermaid
flowchart TD
    subgraph BadCritique["Unproductive / Dogmatic Critique"]
        B1["'I don't like MongoDB; we should use Postgres.'"]
        B2["'Why isn't this written in Rust?'"]
        B3["'This feels over-complicated.'"]
    end

    subgraph HighRigorCritique["High-Rigor / Objective Critique"]
        H1["'Given our NFR of < 15ms P99 at 10K RPS, how will this schema handle document locking during concurrent balance updates?'"]
        H2["'What is our disaster recovery RPO if the single primary node suffers hardware failure?'"]
        H3["'What is the projected 3-year cloud storage cost under 50GB/day growth?'"]
    end

    BadCritique -. Transform Into .-> HighRigorCritique
```

---

## 2. The Architectural Pre-Mortem Protocol

The most effective technique for critiquing an architectural proposal is the **Architectural Pre-Mortem**:

```mermaid
sequenceDiagram
    actor Facilitator as Lead Architect / Reviewer
    actor Author as RFC Author
    actor Team as Review Committee

    Facilitator->>Team: 1. 'Assume it is 12 months from now, the system failed catastrophically in production, and we are holding a Sev-1 post-mortem.'
    Team->>Team: 2. Silent generation of failure modes (5 mins)
    Team->>Author: 3. Surface failure modes (Data loss, deadlock, cloud bill explosion)
    Author->>Team: 4. Co-create architectural mitigations on paper
```

### Pre-Mortem Prompt Questions:
1. *Where will this system bottleneck when transaction volume grows by $5\times$?*
2. *What happens to customer requests when the third-party dependency injects a 30-second timeout?*
3. *How will an on-call engineer diagnose this distributed state machine at 3:00 AM using our existing dashboards?*
4. *How difficult will it be to reverse this decision if our business assumptions prove false in 6 months?*

---

## 3. The 4 Categories of Architectural Review Feedback

Reviewers should organize their RFC comments into four distinct categories:

1. **Constraint Incompatibility (Blocking)**:
   - The proposed design directly violates a hard business, regulatory, or infrastructure constraint (e.g., violating GDPR data residency or exceeding maximum latency budgets).
2. **Unaddressed Failure Mode (Blocking)**:
   - The design fails to specify behavior during network partitions, disk saturation, or poison-pill message processing.
3. **Operational Burden / TCO (Non-Blocking Advisory)**:
   - Highlighting that a technology introduces significant operational complexity (e.g., self-hosting a multi-node distributed cluster when a managed service exists).
4. **Simplification Opportunity (Non-Blocking Suggestion)**:
   - Proposing an alternative architecture that achieves 90% of the desired business capability with 30% of the architectural complexity.
