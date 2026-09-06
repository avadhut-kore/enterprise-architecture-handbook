# Role Readiness Gate: Senior Software Engineer

> **"Readiness for Senior Engineer is proven by autonomous execution, production operability, defensive engineering, and peer mentorship."**

---

## 1. Readiness Threshold Matrix

| Pillar | Required Standard | Verification Method |
| :--- | :--- | :--- |
| **1. Knowledge** | Level 2 (Independent) across Core Foundations; Level 3 in primary language runtime and database engine. | Review against [Competency Matrix](../skill-matrix/architect-competency-matrix.md). |
| **2. Experience** | 6+ months in production on-call rotation; diagnosed and mitigated 2+ live incidents under pressure. | On-call incident logs and post-mortem review. |
| **3. Decisions** | Evaluated 2+ component trade-offs (e.g., sync vs async, cache-aside vs write-through). | Documented design notes and PR review discussions. |
| **4. Evidence** | 2 approved Low-Level Design (LLD) memos; 1 blameless incident post-mortem; 1 performance tuning benchmark. | Git repository review of author contributions. |

---

## 2. Core Readiness Checklist

### Technical & Systemic Competence
- [ ] Autonomously designs database schemas with appropriate indexing, foreign keys, and migration scripts.
- [ ] Proficiently diagnoses memory leaks, thread contention, and slow SQL execution plans in production.
- [ ] Understands and applies distributed system primitives: idempotency, retries with jitter, and circuit breaking.
- [ ] Writes comprehensive unit, integration, and contract tests maintaining high test suite reliability.

### Operational Ownership
- [ ] Regularly takes on-call rotations and can navigate production logs, metrics, and traces without hand-holding.
- [ ] Has authored or tuned Grafana/OpenTelemetry dashboards and alert rules that caught a real production issue.
- [ ] Authors blameless, thorough incident post-mortems focusing on systemic causes rather than individual human error.

### Peer Mentorship & Collaboration
- [ ] Conducts thoughtful, constructive code reviews that teach architectural and clean code principles.
- [ ] Mentors junior engineers and interns to successfully deliver complex features on schedule.
- [ ] Clearly communicates technical constraints and dependencies to product owners.

---

## 3. Mandatory Evidence Portfolio Items
1. **Low-Level Design (LLD)**: Created using [`16-architecture-deliverables/LLD-TEMPLATE.md`](../../16-architecture-deliverables/LLD-TEMPLATE.md) for a non-trivial service feature.
2. **Production Incident Post-Mortem**: Documented root cause analysis, timeline, and permanent architectural remediation.
3. **Performance Optimization Benchmark**: Proof of a measurable performance gain (e.g., cutting p99 latency by >30% or reducing memory utilization by 25%).

---

## 4. Remediation Plan if Not Ready
* **If lacking operational experience**: Request secondary shadowing on the next 3 on-call rotations; audit and improve runbook documentation for the top 5 failing alerts.
* **If lacking design depth**: Shadow a Tech Lead in authoring an LLD; run a spike comparing two database indexing strategies and document the benchmark.
