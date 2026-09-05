# Architecture Discovery Methodology

Architecture discovery is the structured process of transforming ambiguous stakeholder wishes into clear architectural drivers.

---

## 1. The 5-Stage Discovery Workflow

```mermaid
flowchart LR
    S1["1. Stakeholder Mapping<br/>(Identify Sponsors, Users, SREs, Security)"] --> S2["2. Context & Driver Interviews<br/>(Uncover pain points, business goals, regulatory mandates)"]
    S2 --> S3["3. Technical Environment Audit<br/>(Inspect legacy code, database schemas, network links)"]
    S3 --> S4["4. Constraint & Assumption Synthesis<br/>(Formalize constraint and assumption registers)"]
    S4 --> S5["5. Architectural Driver Matrix<br/>(Prioritize top 5 NFRs driving the design)"]
```

---

## 2. The 3 Types of Discovery

1. **Business Discovery**: Revenue models, customer personas, value streams, compliance obligations.
2. **Technical Discovery**: Existing codebases, database dependencies, network topology, cloud landing zones, deployment pipelines.
3. **Organizational Discovery**: Team structures, skill profiles, operational maturity, release frequency, political incentives.
