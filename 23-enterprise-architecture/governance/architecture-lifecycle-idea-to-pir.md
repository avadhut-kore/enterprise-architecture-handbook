# Architecture Lifecycle: Idea to Post-Implementation Review

The formal governance stages an enterprise initiative traverses from initial conception to production retirement.

---

## 1. The 8 Stages of the Architecture Lifecycle

```mermaid
flowchart TD
    S1["1. Idea & Strategic Assessment<br/>(EA validates capability fit & strategic alignment)"] --> S2["2. Business Case & Budget Sizing<br/>(Capex/Opex estimation, high-level feasibility)"]
    S2 --> S3["3. Solution Architecture Design<br/>(SA authors Solution Architecture Document - SAD)"]
    S3 --> S4["4. ARB Review & Approval Gate<br/>(Peer review, standards check, exception grant)"]
    S4 --> S5["5. Implementation & Paved Road Delivery<br/>(Continuous CI/CD fitness function validation)"]
    S5 --> S6["6. Pre-Production Architecture Audit<br/>(Disaster recovery, security pentest, SLA signoff)"]
    S6 --> S7["7. Production Go-Live<br/>(Operational observability, APM inventory active)"]
    S7 --> S8["8. Post-Implementation Review (PIR)<br/>(Evaluate actual vs projected ROI & tech debt, 90 days post-launch)"]
```
