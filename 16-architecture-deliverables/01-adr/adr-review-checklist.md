# ADR Review Checklist

Use this 15-point checklist before submitting an ADR to the Architecture Review Board (ARB) or merging into main.

---

## 1. Context & Motivation
- [ ] **Problem Clarity**: The business and technical problem is described objectively without pre-determining the outcome.
- [ ] **Constraints Stated**: Real-world constraints (budget, timeline, team skills, existing systems) are explicitly listed.
- [ ] **Scope Defined**: The decision boundary is atomic and addresses exactly one core question.

## 2. Alternatives & Evaluation
- [ ] **Viable Alternatives Considered**: At least two credible alternatives were thoroughly investigated (including "Do Nothing").
- [ ] **Fair Comparison**: Pros and cons of all options are balanced and supported by data, benchmarks, or prototypes.
- [ ] **Cost Analysis**: Infrastructure and operational costs are evaluated for each option at anticipated scale.

## 3. Decision Rationale & Trade-offs
- [ ] **Direct Rationale**: Explains specifically *why* the winning option was chosen over the highest-ranking alternative.
- [ ] **Explicit Trade-offs**: Clearly lists what benefits were sacrificed and what technical debt or complexity is accepted.
- [ ] **Clear Rejection Reasons**: States explicit reasons why alternatives were rejected.

## 4. Operational & Security Consequences
- [ ] **Security Review**: Authentication, authorization, encryption, and compliance impacts are documented.
- [ ] **Observability & Telemetry**: Specifies required metrics, logs, and alert triggers.
- [ ] **Failure Modes**: Outlines how the chosen solution behaves during network partitions, outages, or overload.
- [ ] **Rollback / Exit Strategy**: Defines how the organization can migrate away if the choice proves unviable.

## 5. Metadata & Traceability
- [ ] **Accurate Status**: Status is correctly assigned (`Proposed`, `Accepted`, etc.).
- [ ] **Traceability Links**: References related requirements, designs ([03-hld/](../03-hld/README.md)), and diagram specs.
