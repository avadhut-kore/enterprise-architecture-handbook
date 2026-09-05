# GitHub Enterprise Architecture & Governance

This module establishes architecture standards for enterprise GitHub organizations, GitHub Actions runners, branch protection, and security posture.

## Contents

- [GitHub Enterprise Governance](./github-enterprise-governance.md) — Organization structure, SAML SSO, team synchronization, and audit log streaming.
- [GitHub Actions Architecture](./github-actions-architecture.md) — Self-hosted runners, Actions Runner Controller (ARC) on Kubernetes, ephemeral runners, and OIDC auth.
- [Branch Protection and Environments](./branch-protection-and-environments.md) — Rulesets, required status checks, environment approvals, and secret scoping.

## Core Rule
Never use long-lived cloud credentials (AWS Access Keys, Azure Service Principal secrets) in GitHub Secrets. Enforce OIDC federated workload identity for all cloud interactions.
