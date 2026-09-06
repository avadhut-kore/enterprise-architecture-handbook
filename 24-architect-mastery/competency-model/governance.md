# Competency Deep Dive: Architecture Governance & ARB

> **"Architecture governance is not about slowing down delivery with bureaucratic approval committees; it is about providing clear guardrails, automated fitness functions, and transparent decision forums that empower teams to move fast safely."**

---

## 1. Definition & Core Essence

**Architecture Governance & ARB** is the discipline of aligning decentralized engineering decisions with corporate strategy, security policies, and long-term architectural health. It encompasses:
* Governance bodies: Architecture Review Board (ARB), Technical Design Authority (TDA), and Architecture Working Groups.
* Review methodologies: Architecture Trade-off Analysis Method (ATAM), lightweight peer reviews, and exception waivers.
* Technology portfolio stewardship: Corporate Technology Radar curation (Adopt, Trial, Assess, Hold).
* Automated governance: Architectural fitness functions, CI/CD linters (ArchUnit, [`doc_linter.py`](../../21-architecture-tools/linters/doc_linter.py)), and automated policy enforcement.

---

## 2. Why It Matters for Modern Architects

* **Solution Architects**: Provides the formal mechanism to validate complex designs against organizational standards and gain cross-functional alignment.
* **Technical Architects**: Presides over review sessions, curates technology lifecycles, and replaces bureaucratic sign-offs with automated CI fitness functions.
* **Enterprise Architects**: Establishes corporate-wide governance charters that satisfy regulatory compliance without paralyzing engineering velocity.

---

## 3. 5-Tier Behavioral Capability Progression

| Level | Behavioral Capability Anchor |
| :--- | :--- |
| **L1 (Practitioner)** | Follows team coding standards, linting rules, and security guidelines in everyday pull requests. |
| **L2 (Independent)** | Participates actively in team design reviews; adheres to established architectural patterns and ADRs. |
| **L3 (Advanced)** | Prepares and submits complete architecture review packages to the ARB; remediates review conditions decisively. |
| **L4 (Architect)** | Presides over Architecture Review Boards; curates the corporate Technology Radar; shifts governance from manual gatekeeping to automated CI linters. |
| **L5 (Strategic)** | Establishes enterprise architecture governance policies across business divisions, balancing regulatory compliance against product agility. |

---

## 4. Practical Experiences & Apprenticeship Exercises

1. **Chair an Architecture Review Board Session**: Review a proposed high-impact solution architecture; evaluate security, reliability, cost, and operability; issue clear, constructive conditions for approval.
2. **Implement an Automated Architectural Fitness Function**: Write a CI test that verifies no service directly imports classes from a forbidden layer (e.g., controllers calling database repositories directly).
3. **Curate a Technology Radar Cycle**: Lead a quarterly review evaluating emerging technologies across engineering squads; move candidate tools between Adopt, Trial, Assess, and Hold.

---

## 5. Objective Evidence of Capability (What to Inspect in Git)

- [ ] Approved Architecture Review Package with minutes, risk assessments, and conditions of approval.
- [ ] Published corporate Technology Radar updates with documented ADR justifications.
- [ ] Automated architectural linting rules integrated into CI/CD pipelines.

---

## 6. Common Cognitive Gaps & Blind Spots

* **Bureaucratic Gatekeeping**: Treating the ARB as an adversarial checkpoint that rejects designs over trivial formatting issues, driving engineers toward shadow IT.
* **Toothless Governance**: Operating an ARB that rubber-stamps every proposal without evaluating trade-offs, leading to runaway technical fragmentation.
* **Manual Compliance Policing**: Spending hours manually checking architecture rules that could be verified in 3 seconds by an automated linter.

---

## 7. Authoritative Repository Links

* Architecture Governance Core: [`01-architecture/architecture-governance/`](../../01-architecture/architecture-governance/README.md)
* Architecture Review Methodology: [`24-architect-mastery/architecture-review/`](../architecture-review/README.md)
* Architecture Review Checklist: [`21-architecture-tools/checklists/solution-architecture-checklist.md`](../../21-architecture-tools/README.md)
* Living Technology Radar: [`TECHNOLOGY-RADAR.md`](../../TECHNOLOGY-RADAR.md)

---

## 8. Diagnostic Assessment Questions

1. *How do you transform an Architecture Review Board from a dreaded bureaucratic bottleneck into a valued coaching and enablement forum?*
2. *What is an architectural fitness function, and how does it automate governance in modern CI/CD pipelines?*
3. *Under what conditions should an architect grant an architectural exception or waiver, and how should that waiver be tracked and retired?*
