# Decision Framework: Data Mesh vs Centralized Data Platform

---

## 1. Context & Architectural Dilemma
> "Determining when an organization is mature enough to transition from a central data team to Data Mesh."

In enterprise architectures, making this decision incorrectly leads to either catastrophic operational paralysis or unbounded technological sprawl.

---

## 2. Evaluation Criteria & Weighting

| Evaluation Dimension | Weight | Considerations |
| :--- | :---: | :--- |
| **Strategic Alignment & Agility** | 0.30 | How this decision impacts time-to-market and long-term corporate vision. |
| **Total Cost of Ownership (5-Yr TCO)** | 0.25 | Capital expenditure, licensing, operational headcount, and cloud spend. |
| **Operational Resilience & Risk** | 0.25 | Availability, compliance liability, security perimeter, and disaster recovery. |
| **Organizational Complexity** | 0.20 | Cognitive load on engineering teams, skill availability, and governance overhead. |

---

## 3. Options & Trade-Off Analysis
* Option A: Central Data Platform (Appropriate for <500 employees). Option B: Data Mesh (Mandatory for complex enterprises with >10 distinct business domains).

---

## 4. Failure Modes & Warning Signs
* **Premature Decision**: Committing to an irreversible one-way door decision before business domain boundaries are understood.
* **Ignoring Hidden Costs**: Factoring software license cost while ignoring the 10x engineering integration and cloud egress costs.
* **Political Compromise**: Choosing a hybrid solution that incorporates the worst attributes of both options to appease internal factions.

---

## 5. Enterprise Case Example & Verdict
In a Tier-1 global enterprise environment, the recommended architectural heuristic is:
* Default to the option that maximizes **reversibility**, minimizes **cognitive load on delivery squads**, and enforces **strict compliance and data security boundaries by default**.
