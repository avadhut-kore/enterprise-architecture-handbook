# Merge vs Rebase vs Squash: History Strategy

Choosing how pull requests integrate into the main branch affects history readability, git bisect capability, and audit traceability.

## 1. The Three Integration Archetypes

```
1. MERGE COMMIT (--no-ff):
   Preserves branch topology and all individual commit SHAs.
   Result: Non-linear, complex diamond graphs; true audit trail.

2. REBASE (--rebase):
   Replays commits on top of base branch.
   Result: Completely linear history; rewritten commit SHAs.

3. SQUASH AND MERGE (--squash):
   Condenses 20 WIP commits into 1 atomic commit on main.
   Result: Clean linear history; loses intermediate granular commits.
```

## 2. Enterprise Recommendation
- **Feature Branches $	o$ Main**: **Squash and Merge** is strongly recommended for trunk-based microservices. It eliminates noisy "fix typo" and "WIP" commits, making `git revert` and `git bisect` trivial.
- **Long-Running Epics**: **Merge Commit** with fast-forward disabled (`--no-ff`) to preserve historical context of complex subsystem refactorings.

## Related Resources
- [Branching Strategies](./branching-strategies-evaluation.md)
- [Source Control Governance](../source-control-governance/README.md)
