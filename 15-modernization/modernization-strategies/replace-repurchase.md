# The "Replace / Repurchase" Strategy: Build vs. Buy & SaaS

## 1. Architectural Definition
**Replace** (or **Repurchase**) decommissions bespoke, custom-built enterprise software in favor of an off-the-shelf Commercial Off-The-Shelf (COTS) platform or Cloud Software-as-a-Service (SaaS) solution (e.g., replacing a 20-year-old custom CRM with Salesforce, or replacing custom HR software with Workday).

---

## 2. The Build vs. Buy Decision Matrix

```
       ┌─────────────────────────────────────────────────────────────┐
       │                                                             │
  High │  [ CUSTOM BUILD / REARCHITECT ]   [ BUY BEST-OF-BREED SaaS] │
C      │  Core competitive differentiator. Specialized capabilities. │
O      │  Unique intellectual property.    (e.g., AI Fraud, Billing) │
M      │  Custom software required.                                  │
P      ├─────────────────────────────────────────────────────────────┤
E      │  [ ELIMINATE / RETIRE ]           [ BUY STANDARD SaaS/COTS] │
T      │  Zero differentiation,            Commodity process.        │
I      │  low business utility.            Industry standard better. │
T      │                                   (e.g., HR, Payroll, CRM)  │
  Low  └─────────────────────────────────────────────────────────────┘
                     High                                Low
                         BUSINESS DIFFERENTIATION
```

---

## 3. Migration Pitfalls in SaaS Replacement
- **The Customization Trap**: Attempting to customize the SaaS platform to mimic 100% of the old bespoke legacy software's quirks. This breaks the vendor's upgrade path and recreates technical debt.
- **Data Migration Impedance**: Mapping 20 years of unstructured, denormalized legacy relational tables into rigid SaaS data models.
- **Vendor Lock-In**: Ensure the SaaS contract guarantees export of raw transactional data in standardized formats at reasonable egress costs.
