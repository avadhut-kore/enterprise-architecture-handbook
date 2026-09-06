# Conflict Management: Resolving Architectural Disputes & Deadlocks

> How to de-escalate technical disagreements, resolve database and framework religious wars, establish decision criteria, and maintain team cohesion.

---

## 1. Why Technical Conflicts Occur

Technical disagreements among senior engineers and architects rarely stem from malice. They usually arise from:
1. **Unstated Assumptions**: Engineer A assumes 500 RPS; Engineer B is silently designing for 500,000 RPS.
2. **Asymmetric Risk Tolerances**: One engineer prioritizes immediate delivery velocity; the other prioritizes zero-downtime operational safety.
3. **Resume-Driven Development vs. Conservatism**: One engineer wants to learn Rust or Kubernetes; the other wants to stick with Java 8.

```mermaid
flowchart TD
    Conflict[Technical Disagreement Between Senior Engineers] --> Step1[1. Separate Ego from Architecture]
    Step1 --> Step2[2. Surface Hidden Assumptions & Scale Numbers]
    Step2 --> Step3[3. Define Explicit Objective Evaluation Criteria]
    Step3 --> Step4[4. Time-Boxed Spike / Proof of Concept]
    Step4 --> Step5[5. Disagree and Commit (Decide & Record ADR)]
```

---

## 2. De-escalating Framework Wars: The 4-Step Resolution Method

### Step 1: Establish Shared Objectives First
Before debating tools (e.g., PostgreSQL vs. MongoDB, REST vs. GraphQL), force alignment on **business outcomes and constraints**:
* *"Before we compare databases, let's agree on what we need: What is our write throughput? What are our query patterns? What are our data retention rules? If we agree on the problem specification, the tool choice will become obvious."*

### Step 2: Build an Objective Weighted Scoring Matrix
Remove personal opinion by creating an evaluation rubric agreed upon *before* testing:

| Criteria | Weight | Option A (PostgreSQL) | Option B (MongoDB) |
| :--- | :---: | :---: | :---: |
| ACID Transaction Support | 30% | 5 / 5 | 2 / 5 |
| Team Operational Familiarity | 25% | 5 / 5 | 2 / 5 |
| Dynamic Schema Flexibility | 20% | 3 / 5 | 5 / 5 |
| Cloud Run Cost | 15% | 4 / 5 | 3 / 5 |
| Query Latency | 10% | 4 / 5 | 4 / 5 |
| **Weighted Total** | **100%** | **4.35 / 5** | **2.95 / 5** |

### Step 3: Run a Time-Boxed Spike (Proof of Concept)
* When opinions clash on performance, declare a **3-day spike**:
  * *"Let's build a prototype in both tools, run a 10,000 RPS benchmark using k6 on our actual production payload, and let the telemetry data make the decision for us."*

### Step 4: "Disagree and Commit"
* If a decision remains split 50/50 after data collection, the Chief or Principal Architect must make the call:
  * *"We have heard both perspectives thoroughly. We are moving forward with Option A because it aligns with our enterprise database support contract. I need everyone to commit 100% to making this implementation successful."*
* Document the decision and the dissenting arguments respectfully in an ADR.

---

## 3. Cross-References

* **Stakeholder Management**: [`stakeholder-management.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/leadership/stakeholder-management.md)
* **Influencing Without Authority**: [`influencing-without-authority.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/leadership/influencing-without-authority.md)
* **Leadership Scenarios**: [`scenarios/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/leadership/scenarios/README.md)
