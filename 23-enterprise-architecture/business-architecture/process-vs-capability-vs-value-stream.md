# Process vs Capability vs Value Stream vs Function vs Organization

One of the most frequent enterprise architecture failures is confusing *processes*, *capabilities*, *value streams*, *functions*, and *organizational units*.

---

## 1. The Definitive Distinction Matrix

| Concept | Definition | Answers | Stability Over Time | Example |
| :--- | :--- | :--- | :--- | :--- |
| **Value Stream** | An end-to-end collection of value-adding activities that creates an overall result for a customer or stakeholder. | **Why & When?** (Context & Journey) | High (Journeys persist for decades) | *Order-to-Cash*, *Procure-to-Pay*, *Claim-to-Settlement* |
| **Business Capability** | What an organization does or has the capacity to do to deliver value, independent of how it is executed. | **What?** (Core Capacity) | Very High (Capabilities outlive tech & org changes) | *Payment Processing*, *Customer Identity*, *Inventory Valuation* |
| **Business Process** | A specific sequence of tasks, inputs, decisions, and outputs executed by systems and people to achieve a result. | **How?** (Operational Workflow) | Low to Medium (Processes change frequently with automation) | *Approve Loan Application via 3-tier underwriting rules* |
| **Business Function** | A logical grouping of specialized business activities, knowledge, or expertise. | **Which Discipline?** | High | *Treasury*, *Human Resources*, *Legal Compliance* |
| **Organization Unit** | A structural management boundary or hierarchy of personnel (departments, divisions, teams). | **Who?** (Reporting Line) | Very Low (Reorganized frequently by leadership) | *Digital Banking BU*, *EMEA Risk Division* |

---

## 2. Concrete Example: Insurance Claim Processing

```text
VALUE STREAM:
└── Policyholder Claim Settlement Journey
    ├── Stage 1: First Notice of Loss (FNOL)
    ├── Stage 2: Policy Coverage Verification
    ├── Stage 3: Damage Assessment & Fraud Triage
    ├── Stage 4: Claim Adjudication
    └── Stage 5: Payment Disbursement

SUPPORTING BUSINESS CAPABILITIES:
├── Policy Administration (What)
├── Claim Fraud Detection (What)
├── Digital Payment Disbursement (What)
└── Customer Notification (What)

BUSINESS PROCESSES (How it is executed today):
└── "Auto-Claim Adjudication Workflow v4.2"
    1. Parse incident photo via mobile app OCR
    2. Query policy database for active coverage
    3. Run fraud score model via fraud API
    4. If score < 20 and claim < $1,000, trigger automated ACH payment
    5. Else, assign ticket to Tier-2 manual adjuster

ORGANIZATIONAL UNITS (Who manages it):
├── Customer Care Contact Center
├── Special Investigations Unit (SIU)
└── Claims Adjudication Operations
```

> **Architectural Takeaway**: When designing target software systems, **anchor your domain boundaries and microservices to Business Capabilities, NOT to Organization Units or Processes**. Organizations get re-shuffled every 18 months; business capabilities remain constant for decades.
