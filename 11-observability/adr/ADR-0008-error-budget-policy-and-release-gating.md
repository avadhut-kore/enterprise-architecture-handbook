# ADR-0008: Automated Error Budget Policies in CI/CD Delivery Gates

* **Status**: Accepted
* **Date**: 2026-06-15
* **Deciders**: VP of Engineering, Head of Product, Lead Release Architect
* **Technical Story**: [ARCH-OBS-008] Error Budget CI/CD Gating

---

## Context and Problem Statement
Tension between Product Management (demanding rapid feature velocity) and Engineering Operations (demanding production stability) leads to chaotic release cycles, uncoordinated hotfixes, and frequent production outages. We lack an objective, binding mechanism to enforce reliability governance.

## Decision Drivers
* Objective mathematical arbitration between feature releases and reliability debt.
* Automated CI/CD pipeline enforcement without human managerial disputes.
* Protecting customer experience as the supreme architectural priority.

## Considered Options
1. **Option 1**: Subjective Change Advisory Board (CAB) manual approval gates.
2. **Option 2**: Unrestricted continuous deployment regardless of failure rates.
3. **Option 3**: **Automated Error Budget Policy with CI/CD Promotion Gates**.

## Decision Outcome
**Chosen Option**: **Option 3: Automated Error Budget Policy with CI/CD Gates**.

### Positive Consequences
* **Automated Release Gating**: When a service's 30-day error budget is depleted ($< 0\%$), CI/CD pipelines (ArgoCD / GitLab) automatically block non-security feature promotions.
* **Cultural Alignment**: Product managers actively prioritize technical debt and resiliency when their feature release velocity is throttled by stability metrics.
* **Fast Recovery Incentives**: Squads prioritize fixing bugs and MTTR to restore their error budget balance.

### Negative Consequences
* Requires formal executive buy-in and organizational willingness to hold feature deadlines accountable to reliability data.

---

## Links
* Policy Document: [`../slo-management/error-budget-policy.md`](../slo-management/error-budget-policy.md)
