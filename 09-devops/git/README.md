# Git Architecture & Repository Strategy

This module provides enterprise-level guidance on Git internals, repository structures, branching workflows, and commit management.

## Contents

- [Git Architecture and Internals](./git-architecture-and-internals.md) — Directed Acyclic Graphs (DAG), object database (blobs, trees, commits), packfiles, and plumbing commands.
- [Branching Strategies Evaluation](./branching-strategies-evaluation.md) — Deep comparative analysis of Trunk-Based Development vs GitFlow vs GitHub Flow vs Release Trains.
- [Merge vs Rebase vs Squash](./merge-vs-rebase-vs-squash.md) — Architectural trade-offs in commit history cleanliness, bisectability, and linear history.
- [Monorepo vs Polyrepo Architecture](./monorepo-vs-polyrepo-architecture.md) — Multi-criteria evaluation matrix, change detection, scale tooling, and enterprise governance.

## Architectural Principles
1. **Short-Lived Branches**: Branches that live longer than 24-48 hours dramatically increase merge conflict friction and decouple development from CI.
2. **Deterministic History**: Commit history is an audit trail; enforce conventional commits and signed commits (GPG/SSH).
