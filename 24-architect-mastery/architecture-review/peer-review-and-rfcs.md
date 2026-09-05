# Peer Review and RFC Workflows

Asynchronous Request for Comments (RFC) workflows democratize architecture, allowing any engineer to propose designs while inviting feedback from domain experts.

## 1. The RFC Lifecycle

```
Draft in Git Branch -> Open Pull Request -> Tag Reviewers & Stakeholders -> Async Discussion -> Merge as Accepted ADR
```

## 2. Review Etiquette for Architects

- **Praise Good Design**: Call out elegant simplifications and thorough trade-off analysis explicitly.
- **Frame Feedback as Questions**: Instead of *"This cache will cause split-brain,"* ask *"What happens if the primary cache node partitions while writes are in flight?"*
- **Distinguish Nitpicks from Blockers**: Prefix review comments:
  - `[BLOCKER]`: Material architectural or security violation that must be resolved.
  - `[SUGGESTION]`: Non-blocking recommendation for optimization.
  - `[NIT]`: Minor styling or nomenclature cleanup.

## Related Modules
- [Architecture Review Board Operating Model](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/architecture-review/architecture-review-board-operating-model.md)
- [Decision Making Framework](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/decision-making/README.md)
