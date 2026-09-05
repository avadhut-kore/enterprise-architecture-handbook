# Architecture Review Board (ARB) Operating Model

An Architecture Review Board (ARB) exists to align systems with enterprise strategy, prevent redundant investments, and maintain technical integrity across portfolios.

## 1. The Modern ARB Charter

- **Mission**: Accelerate delivery by identifying risks early, ensuring cross-system interoperability, and coaching teams toward modern patterns.
- **Scope**:
  - Significant technology investments (> $250k).
  - Cross-domain integration patterns.
  - New technology additions to the enterprise tech radar.
  - Irreversible Type 1 architectural decisions.

## 2. Review Cadence and SLAs

```
Submission of 2-page RFC -> 5 Business Days Async Review -> 30-min ARB Discussion -> ADR Sign-off
```

- **No Surprise Vetoes**: If an ARB member has objections, they must raise them in writing during the async window before the meeting.
- **Actionable Feedback**: ARB feedback must not say *"We don't like this."* It must specify *"Address data residency risk in Section 4 by adding KMS envelope encryption."*

## Related Modules
- [Peer Review and RFCs](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/architecture-review/peer-review-and-rfcs.md)
- [Pragmatic Governance](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/governance/README.md)
