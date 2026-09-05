# Change Management Architecture (`change-management/`)

## Executive Summary

Modern enterprise change management eliminates bureaucratic change boards (CAB) by automating change risk assessments, peer reviews, and deployment execution through Infrastructure as Code (IaC) and GitOps.

---

## Key Guides in this Directory

| Guide | Scope | Core Model |
| :--- | :--- | :--- |
| [`modern-change-management.md`](modern-change-management.md) | Categorization | Standard (Automated) vs Normal (Peer-Reviewed) vs Emergency |
| [`automated-change-governance-gitops.md`](automated-change-governance-gitops.md) | GitOps Control | Pull request approvals, immutable commit hashes, ArgoCD |
