# Checklist 07: Service Level Objective (SLO) Implementation Audit

## 1. Overview
Provides Product Managers, Technical Architects, and SREs with an objective verification rubric for defining, publishing, and governing Service Level Objectives and Error Budgets.

---

## 2. Verification Rubric

| SLO Step | Verification Criteria | Status |
| :--- | :--- | :--- |
| **User Journey Focus** | SLO directly models a Critical User Journey (CUJ), not an internal implementation detail. | [ ] |
| **SLI Formulation** | SLI formulated as the ratio of Good Events over Total Valid Events: $\frac{\text{Good Events}}{\text{Total Events}} \ge \text{Target}$. | [ ] |
| **Target Defensibility**| Target (e.g., 99.9%) is defensible based on customer tolerance, not arbitrary aspiration. | [ ] |
| **Measurement Window** | Defined over a rolling 30-day or rolling 28-day window. | [ ] |
| **Error Budget Policy** | Formal, executive-signed policy defines mandatory actions when budget is depleted. | [ ] |
| **CI/CD Integration** | Deployment pipelines query error budget balance to evaluate canary promotions. | [ ] |
| **Executive Visibility**| Weekly automated error budget consumption report distributed to engineering leadership. | [ ] |
