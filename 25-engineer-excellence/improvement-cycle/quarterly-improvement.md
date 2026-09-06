# The Quarterly Engineering Improvement Cadence

> **"A quarter is the fundamental planning horizon of the tech industry. It is long enough to architect, build, and ship a non-trivial subsystem, and short enough to evaluate its real-world production outcome."**

---

## 1. Overview of the Quarterly Cadence

The **Quarterly Improvement Cadence** aligns personal capability expansion with the organization's business OKRs and roadmap milestones. Every quarter represents one complete execution of the **90-Day Improvement Cycle**, transitioning an engineer from gap diagnosis to production evidence.

```mermaid
flowchart LR
    EndQ["End of Quarter N:<br/>Retrospective & Evidence Audit"] --> Recal["Recalibrate 10-Dimension Baseline"]
    Recal --> Select["Select Next Quarter Focus<br/>(1 Primary + 1 Secondary)"]
    Select --> StartQ["Quarter N+1:<br/>Execute 90-Day Plan"]
```

---

## 2. Setting Quarterly Engineering Capability OKRs

Never set vague, unmeasurable learning goals (e.g., *"Learn more about distributed systems"*). Structure quarterly development goals using the **Objective & Key Results (OKR)** framework:

```mermaid
graph TD
    Obj["Objective: Advance System Design capability from L2 (Independent) to L3 (Advanced)"]
    KR1["KR 1: Author accepted RFC & ADR for new idempotent webhook ingestion pipeline by Day 30."]
    KR2["KR 2: Build and benchmark a Redis Bloom-filter deduplication spike proving 10K RPS by Day 50."]
    KR3["KR 3: Ship pipeline to production behind feature flag with < 50ms P99 latency by Day 75."]
    KR4["KR 4: Verify zero duplicate allocations over 30 days and publish post-launch case study by Day 90."]

    Obj --> KR1
    Obj --> KR2
    Obj --> KR3
    Obj --> KR4
```

### Guidelines for High-Rigor Engineering OKRs:
1. **At Least One Key Result Must Be an Artifact**: An accepted ADR, an RFC, or a published runbook.
2. **At Least One Key Result Must Be a Production Metric**: P99 latency reduction, error budget compliance, zero regressions.
3. **No Credentialist Key Results**: Do not use "complete course X" or "read book Y" as Key Results; use the *application* of that knowledge as the metric.

---

## 3. The Quarterly Retrospective & Transition Ritual

At the conclusion of each quarter (typically during the final two weeks):
1. **Score the Outgoing 90-Day Plan**:
   - Evaluate completion of Key Results.
   - Did the primary dimension advance to the target maturity level on the [Maturity Rubric](../capability-matrix/maturity-levels.md)?
2. **Update the Portfolio Dossier**:
   - Compile the quarter's CPOE entries into a dedicated project dossier in `dossiers/`.
   - Obtain formal peer/lead sign-off on the evidence ledger.
3. **Run the Gap Analysis**:
   - Re-run the [Capability Gap Analysis](../assessment/capability-gap-analysis.md).
   - Formulate the next [90-Day Improvement Plan](./90-day-improvement-plan.md).
