# Source Control Governance & Repository Standards

Source control is the foundation of the enterprise software delivery lifecycle. This domain establishes enterprise standards for repository lifecycles, branch hygiene, automated branch protection, secret leak prevention, and code ownership.

## Core Governance Pillars

1. **Repository Lifecycle Management**: Enforcing structured naming taxonomies, standard folder layouts, mandatory templates (CODEOWNERS, CONTRIBUTING.md, README.md), and automated decommission/archival processes.
2. **Access Control & Least Privilege**: Role-based access control (RBAC), team-based repository assignments, and emergency break-glass elevation protocols.
3. **Branch Protection & Quality Gates**: Mandatory multi-approver pull request policies, required green CI status checks, linear history enforcement, and cryptographically signed commits.
4. **Secret Zero Prevention**: Client-side pre-commit hooks and server-side push protection to prevent hardcoded credentials, tokens, or private keys from entering commit history.

## Contents

- [Enterprise Repository Standards](./enterprise-repository-standards.md) - Complete taxonomy, mandatory file specifications, CODEOWNERS rules, branch protection policies, secret detection tooling, and repository archival checklists.
- [Cross-Reference: Git Architecture & Branching](../git/README.md) - Git internals, branching strategies, rebase vs merge analysis, and monorepo governance.
