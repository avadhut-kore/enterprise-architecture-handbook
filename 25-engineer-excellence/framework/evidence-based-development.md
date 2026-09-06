# Evidence-Based Engineering Development

> **"In God we trust; all others must bring telemetry, code diffs, and accepted ADRs."**

---

## 1. The Anti-Credentialist Manifesto

In modern software engineering, traditional credentialing mechanisms have collapsed under the weight of commercial inflation:
- Multiple-choice cloud certifications can be passed via memorization brain dumps without ever deploying a VPC.
- University computer science degrees frequently fail to teach Git discipline, CI/CD, production telemetry, or legacy refactoring.
- Years of experience ("tenure") frequently correlate with organizational comfort rather than technical mastery.
- Self-evaluations are inherently prone to the Dunning-Kruger effect.

**Evidence-Based Development (EBD)** replaces credentialism and subjective self-ratings with a verifiable evidentiary standard:

```mermaid
flowchart LR
    Claim["1. Technical Claim<br/>('Expert in Distributed State')"] --> Practice["2. Deliberate Practice<br/>(Benchmarked raft spike in Go)"]
    Practice --> Outcome["3. Measurable Outcome<br/>(Zero lost transactions during network partition)"]
    Outcome --> Evidence["4. Verifiable Evidence<br/>(ADR-019 + Grafana dashboard + PR #412)"]
    Evidence --> Validation["5. Objective Validation<br/>(Peer audit & promotion readiness)"]
```

If an engineer claims proficiency in an engineering discipline, they must provide verifiable, reproducible artifacts showing the real-world outcome of that proficiency.

---

## 2. The 12 Canonical Evidence Categories

To build an incontrovertible engineering portfolio, artifacts are categorized across 12 distinct evidence types:

```mermaid
mindmap
  root((Engineering Evidence))
    Code Diff
      Refactoring Legacy Monolith
      Zero-Allocation Hot Path
    Architecture
      Accepted ADRs
      RFC Specifications
    Production Telemetry
      Grafana SLO Dashboards
      CloudWatch Alerts
    Incident Forensics
      Blameless Post-Mortems
      Root Cause Analyses
    Performance
      Flamegraphs & Benchmarks
      P99 Latency Reductions
    Security
      STRIDE Threat Models
      Automated SAST/DAST Gates
    Automation
      Zero-Downtime CI/CD
      Self-Healing Infrastructure
    Delivery
      On-Time Epic Delivery
      Zero-Regress Feature Flags
    Documentation
      Runbooks & Playbooks
      Developer Golden Paths
    Mentorship
      Junior Promotions Guided
      Internal Tech Talks
    Leadership
      Cross-Team Consensus
      Technical Standard RFCs
    Business Value
      Infrastructure Cost Savings
      Conversion Rate Increases
```

| Category | High-Value Evidence Artifact | Weak / Unacceptable Evidence |
| :--- | :--- | :--- |
| **1. Code Diff** | Pull request demonstrating clean architectural boundaries, comprehensive unit/integration tests, and zero deadlocks. | "I wrote 15,000 lines of code last month." |
| **2. Architecture** | Accepted ADR documenting evaluated alternatives, trade-offs, consequences, and fitness functions. | Whiteboard photo with no context, trade-offs, or follow-through. |
| **3. Production** | Telemetry dashboard demonstrating compliance with a strict SLO (e.g., 99.99% availability over 90 days). | "The service feels stable." |
| **4. Incident** | Published blameless post-mortem identifying systemic contributing factors and implementing permanent architectural guardrails. | "I stayed up all night to restart the server when it crashed." |
| **5. Performance** | Benchmark reports (e.g., `k6`, `wrk`, flamegraphs) proving a $>50\%$ drop in P99 latency or CPU utilization. | "I refactored the loop to make it faster." |
| **6. Security** | Threat model document (STRIDE) identifying an attack vector, accompanied by automated integration tests and mitigation code. | "I completed the mandatory annual security compliance quiz." |
| **7. Automation** | Fully automated CI/CD pipeline achieving $<10\text{m}$ commit-to-production lead time with automated canary rollback. | "I manually deployed the code using an SSH bash script." |
| **8. Delivery** | Delivering a critical multi-month initiative on schedule through incremental feature flagging and zero regressions. | "I worked 60 hours a week to finish the sprint." |
| **9. Documentation** | Comprehensive incident runbook or onboarding golden path that reduced team ramp-up time from 4 weeks to 3 days. | Outdated Confluence page with broken links and stale instructions. |
| **10. Mentorship** | Guided a junior engineer through their first major system design, leading to their successful independent delivery and promotion. | "I am always available on Slack to answer questions." |
| **11. Leadership** | Driving consensus across 3 divergent engineering teams to standardize an internal API protocol via an RFC process. | "I voiced my opinion loudly in the architecture meeting." |
| **12. Business Value** | Direct, quantified business outcome (e.g., eliminated \$140,000/year in cloud egress fees through VPC endpoint re-architecture). | "Management seemed very pleased with the project." |

---

## 3. Evidence Quality Rubric: Weak vs. Strong

When assessing an engineering portfolio, evaluate each artifact against the **Evidence Quality Rubric**:

```mermaid
flowchart TD
    subgraph Weak["Level 1: Weak Evidence (Unverified & Subjective)"]
        W1["Self-declared assertions ('I know Kubernetes')"]
        W2["Vanity metrics (Commits count, lines of code)"]
        W3["Passive participation ('Attended weekly planning')"]
    end

    subgraph Moderate["Level 2: Moderate Evidence (Activity-Based)"]
        M1["Completed a multi-module online course"]
        M2["Closed 45 Jira tickets in a sprint"]
        M3["Wrote code that was reviewed and merged"]
    end

    subgraph Strong["Level 3: Strong Evidence (Outcome-Backed & Verifiable)"]
        S1["Merged PR with automated tests, bench results, and zero regressions"]
        S2["Accepted ADR with multi-stakeholder sign-off and documented trade-offs"]
        S3["Grafana dashboard proving P99 latency dropped from 450ms to 42ms"]
        S4["Incident post-mortem with automated regression test preventing recurrence"]
    end

    Weak --> Moderate
    Moderate --> Strong
```

### The 4 Criteria of High-Grade Evidence:
1. **Verifiability**: Can an independent staff engineer or architect click a link, inspect the Git commit history, and examine the telemetry data directly?
2. **Attribution**: Is the individual's specific contribution clearly isolated from the broader team's work?
3. **Counterfactual Rigor**: What would have happened if this work was not done? Did it tangibly prevent failure or create new business leverage?
4. **Longevity**: Did the system survive the test of production reality over 3 to 6 months without degrading into chronic operational burden?

---

## 4. Constructing the Engineering Portfolio

Engineers should maintain a live, machine-readable repository or document tracking their evidence ledger:

```yaml
# engineering-evidence-entry.yaml
entry_id: EVD-2026-004
date: 2026-08-14
author: "Engineering Lead / Senior IC"
dimension: "System Design & Production Engineering"
target_maturity: "L3 -> L4"

claim: "Engineered high-throughput, idempotent payment webhook ingestion engine."

context:
  problem: "Third-party payment gateways flooded ingestion endpoint with duplicate webhooks during retries, causing database row-locking and duplicate credit allocations."
  scale: "18,000 requests/sec peak, $45M daily transactional volume."

practice_and_execution:
  spike: "Benchmarked Redis distributed locks vs. PostgreSQL transactional advisory locks using k6 in sandbox environment."
  implementation: "Implemented transactional outbox with Redis Bloom filter deduplication layer and PostgreSQL unique idempotency keys."

artifacts:
  adr: "https://github.com/company/architecture-decisions/blob/main/adr/0042-idempotent-webhooks.md"
  pull_request: "https://github.com/company/billing-service/pull/1289"
  dashboard: "https://grafana.internal.net/d/billing-idempotency-v2"
  post_mortem: "https://company.atlassian.net/wiki/spaces/ENG/pages/90124/post-mortem-inc-402"

outcomes:
  duplicate_allocations: "Reduced from 0.04% (approx. $18,000/day) to 0.0000%."
  p99_latency: "Dropped from 840ms to 38ms under 2x peak synthetic load."
  operational_toil: "Zero on-call alerts triggered for webhook ingestion in the subsequent 90 days."

validation:
  reviewed_by: "Principal Solution Architect"
  status: "Verified & Accepted"
```

See [evidence-types.md](../evidence/evidence-types.md) and [engineering-portfolio.md](../evidence/engineering-portfolio.md) for full formatting standards and portfolio management guides.
