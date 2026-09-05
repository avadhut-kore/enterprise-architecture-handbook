# Architecture Decision-Making Framework

An architect is paid for judgment, not diagrams. Making high-quality decisions requires a repeatable, rigorous, and defensible framework rather than ad-hoc gut feeling.

## 1. The Decision Lifecycle

```
[Trigger / Problem Statement]
             │
             ▼
[Framing & Constraint Identification]
             │
             ▼
[Option Generation (Min 3 Options)]
             │
             ▼
[Multi-Criteria Evaluation Matrix]
             │
             ▼
[Red Team / Pre-Mortem Review]
             │
             ▼
[Decision Formulation & ADR Publication]
             │
             ▼
[Monitoring & Re-Evaluation Trigger]
```

## 2. Decision Framing: The 6-Step Methodology

### Step 1: Define the Root Problem
Never solve a symptom. Frame the architectural dilemma around business capability, operational risk, or non-functional thresholds (e.g., "Support 10x traffic growth within $10k/mo cloud spend" rather than "Migrate to Kubernetes").

### Step 2: Establish Inviolable Constraints
Identify the boundaries that disqualify solutions immediately:
- **Regulatory**: Data residency, GDPR/HIPAA compliance.
- **Financial**: Maximum CapEx/OpEx thresholds.
- **Skillset**: Existing engineering competencies and ramp-up curves.
- **Timeline**: Hard delivery deadlines dictated by external contracts or market conditions.

### Step 3: Option Generation
Always formulate at least three genuine options:
1. **Option A: Conservative / Evolutionary** (Extend current architecture, minimal blast radius).
2. **Option B: Modern / Strategic** (Target-state architecture, cloud-native or modern paradigm).
3. **Option C: Radical / Clean-Slate** (PaaS/SaaS off-the-shelf, re-platform, or serverless re-write).
*(A binary choice between "do nothing" and "complete rewrite" is a false dichotomy).*

### Step 4: Multi-Criteria Scoring Matrix

| Evaluation Dimension | Weight (1-5) | Option A Score (1-5) | Option B Score (1-5) | Option C Score (1-5) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Operational Simplicity** | 5 | 4 (20) | 3 (15) | 2 (10) | Team maintenance burden |
| **Time to Market** | 4 | 5 (20) | 3 (12) | 2 (8) | Months to first production traffic |
| **Cost Efficiency (TCO)** | 4 | 3 (12) | 4 (16) | 4 (16) | Infrastructure + licensing + staff |
| **Architectural Optionality** | 3 | 2 (6) | 4 (12) | 5 (15) | Ease of pivoting in 24 months |
| **Failure Blast Radius** | 5 | 3 (15) | 4 (20) | 4 (20) | Blast radius containment |
| **Weighted Total** | — | **73** | **75** | **69** | High-fidelity scoring comparison |

### Step 5: Document in ADR Format
Every material decision must produce an ADR detailing:
- Context and Driving Forces
- Evaluated Options
- Decision and Rationale
- Consequences (Positive, Negative, and Neutral)
- Review Triggers

### Step 6: Post-Decision Feedback Loop
Set a calendar date (e.g., 6 months post-deployment) to inspect real-world metrics against projected assumptions.

## Related Resources
- [Irreversible vs Reversible Decisions](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/decision-making/irreversible-vs-reversible-decisions.md)
- [Architecture Deliverables](../../16-architecture-deliverables/README.md)
