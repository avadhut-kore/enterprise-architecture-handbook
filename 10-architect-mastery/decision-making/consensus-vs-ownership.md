# Consensus vs Ownership in Architecture

A common enterprise failure pattern is "Design by Committee," where decisions are diluted until no one objects, but no one is satisfied. High-performing architecture teams balance ownership, consultation, and informed consent.

## 1. Decision Governance Models

| Model | Velocity | Alignment | Quality | Best Applied When |
| :--- | :--- | :--- | :--- | :--- |
| **Consensus** (Everyone must agree) | Very Slow | High | Mediocre (Watered down) | Rarely suitable for technical architecture; causes deadlock. |
| **Consent** (No valid, reasoned objections) | Fast | Moderate | High | Cross-team architectural standards, platform tool adoption. |
| **Benevolent Dictatorship / Single Owner** | Immediate | Low/Variable | High (If expert) | Incident response, critical emergency fixes, initial Greenfield kernel. |
| **Consultative Ownership (RFC Model)** | Moderate | High | Very High | Standard architectural decisions, ADRs, platform changes. |

## 2. The RFC (Request for Comments) Architecture Process

1. **Driver**: A single architect or principal engineer owns the problem and draft.
2. **Approver**: The designated chief architect or engineering director who has sign-off authority.
3. **Contributors**: Subject matter experts, security, operations, and product partners.
4. **Informed**: The broader engineering organization.

### Rules of Engagement
- **Time-Boxed Review**: RFCs open for review have a strict expiration window (e.g., 10 business days).
- **Disagree and Commit**: Dissenting opinions are explicitly documented in the ADR consequences section. Once the decision is signed, all teams execute aligned with the outcome.

## Related Modules
- [Leadership for Architects](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/leadership/README.md)
- [Architecture Governance](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/governance/README.md)
