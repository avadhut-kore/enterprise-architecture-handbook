# The Engineering Evidence Framework

> **"In science and engineering, assertions without empirical verification are hypotheses at best and fabrications at worst. Capability is an empirical claim that demands verifiable proof."**

---

## 1. Foundational Evidentiary Principles

The **Engineering Evidence Framework (EEF)** eliminates subjectivity, charisma bias, and tenure inflation from engineering career development. It applies the standards of scientific peer review and forensic auditing to software engineering capability.

```mermaid
flowchart TD
    subgraph Rules["The 5 Rules of Valid Engineering Evidence"]
        R1["1. Verifiability<br/>(Must be clickable, inspectable, and auditable)"]
        R2["2. Attribution<br/>(Candidate's specific contribution must be isolated)"]
        R3["3. Counterfactual Rigor<br/>(What would have happened if this work was not done?)"]
        R4["4. Production Longevity<br/>(Did the system survive 90+ days in production?)"]
        R5["5. Recency<br/>(Artifacts must be produced within the last 18 months)"]
    end
```

### Rule 1: Verifiability
An artifact must be publicly or internally auditable by an independent Staff Engineer or Architect. Verbal claims ("*I optimized the database*") are disqualified. The engineer must provide a clickable Git commit diff, an accepted markdown ADR, or a persisted telemetry dashboard link.

### Rule 2: Attribution
Modern software is built by teams. The candidate must clearly isolate their individual contribution from the collective output of the team. If a PR contains 10 authors, the candidate's specific commits, design choices, and architectural leadership must be explicitly documented.

### Rule 3: Counterfactual Rigor
High-grade evidence proves not just that work was performed, but that it achieved a quantifiable, beneficial outcome that would not have occurred otherwise. Did it prevent an outage? Did it save \$100,000? Did it reduce latency by 60%?

### Rule 4: Production Longevity
A feature merged into production that causes chronic alert fatigue, breaks two weeks later, or requires an emergency rewrite is **negative evidence**. True capability is demonstrated by systems that run stably, reliably, and quietly in production for months.

### Rule 5: Recency
Software engineering moves rapidly. Mastery of an obsolete framework from 2018 does not substantiate L3 capability in modern cloud-native systems. Evidence must have been generated within the preceding 18 months unless actively maintained.

---

## 2. The Evidentiary Lifecycle

Evidence is not gathered in a desperate scramble the night before a promotion review. It is captured continuously as part of the engineer's daily and weekly operating loop:

```mermaid
sequenceDiagram
    autonumber
    actor Engineer
    participant System as Production System
    participant Repo as Git / Doc Repo
    participant Portfolio as Engineering Portfolio
    participant Lead as Tech Lead / Architect

    Engineer->>Repo: 1. Authors RFC & ADR for Subsystem
    Engineer->>System: 2. Ships PR behind feature flag with telemetry
    System-->>Engineer: 3. Production metrics confirm latency drop & zero errors
    Engineer->>Portfolio: 4. Logs Entry (Context, PR link, Grafana metrics)
    Portfolio->>Lead: 5. Submits entry for quarterly peer validation
    Lead-->>Portfolio: 6. Validates & signs off on evidence authenticity
```

---

## 3. The Claim $\to$ Practice $\to$ Outcome $\to$ Evidence (CPOE) Model

Every entry in an engineer’s portfolio must follow the four-part CPOE structure:

```mermaid
graph TD
    C["1. Claim<br/>What capability are you claiming?"] --> P["2. Practice & Implementation<br/>What technical work did you perform?"]
    P --> O["3. Measurable Outcome<br/>What quantifiable business or operational value was created?"]
    O --> E["4. Verifiable Evidence<br/>Where is the audit trail?"]
```

### Example 1: System Design & Concurrency
- **Claim**: Advanced capability in distributed consistency and high-throughput event processing (L3).
- **Practice**: Designed and implemented an idempotent transactional outbox consumer in Go using PostgreSQL advisory locks and Redis Bloom filters.
- **Outcome**: Processed 14 million daily transactions with zero duplicate payments and zero row-lock timeouts, reducing P99 processing latency from 450ms to 28ms.
- **Evidence**:
  - RFC: `https://github.com/company/rfcs/blob/main/rfc-042-idempotent-outbox.md`
  - Pull Request: `https://github.com/company/billing-core/pull/1120`
  - Dashboard: `https://grafana.internal.net/d/billing-outbox-v2`
  - Benchmark: `https://github.com/company/billing-core/blob/main/bench/k6-loadtest.js`

### Example 2: Production Engineering & Observability
- **Claim**: Advanced production troubleshooting, incident response, and SLO management (L3).
- **Practice**: Served as Incident Commander during a major database connection pool exhaustion outage; diagnosed the root cause (unbounded thread spawning in legacy ORM); implemented connection pooling, circuit breakers, and SLO-based alerting.
- **Outcome**: Restored service in 14 minutes; eliminated all subsequent connection pool failures over the next 180 days; reduced off-hours PagerDuty alerts by 85%.
- **Evidence**:
  - Post-Mortem: `https://company.atlassian.net/wiki/spaces/ENG/pages/89012/inc-402-postmortem`
  - PR: `https://github.com/company/user-service/pull/982` (HikariCP connection pool refactor)
  - Dashboard: `https://grafana.internal.net/d/user-service-slo`
