# Architecture Tools (`21-architecture-tools/`)

## Executive Summary

The `21-architecture-tools/` directory provides operationalized instruments, assessment checklists, quantitative sizing calculators, maturity scorecards, and Architecture Review Board (ARB) playbooks used by Principal, Lead, and Enterprise Architects across Fortune 500 and global enterprise engagements.

---

## 1. Architecture Review Checklists (`checklists/`)

Comprehensive, actionable verification checklists to evaluate systems at major gate reviews (Concept, Solution Design, Security Review, Production Readiness, Migration Cutover).

### Security Architecture Checklists (`checklists/security/`)
* [`security-architecture-review.md`](checklists/security/security-architecture-review.md) - High-level architectural security gate review.
* [`threat-model-review.md`](checklists/security/threat-model-review.md) - STRIDE threat model verification gate.
* [`application-security-review.md`](checklists/security/application-security-review.md) - OWASP Top 10 and code-level security checklist.
* [`api-security-review.md`](checklists/security/api-security-review.md) - API gateway, rate limiting, and token verification checklist.
* [`identity-review.md`](checklists/security/identity-review.md) - IAM, least privilege, SCIM, and Workload Identity checklist.
* [`cloud-security-review.md`](checklists/security/cloud-security-review.md) - Multi-account landing zone, VPC, and CSPM checklist.
* [`data-security-review.md`](checklists/security/data-security-review.md) - Envelope encryption, KMS, and tokenization checklist.
* [`devsecops-review.md`](checklists/security/devsecops-review.md) - CI/CD automated gates, SAST, SCA, and image signing checklist.
* [`kubernetes-security-review.md`](checklists/security/kubernetes-security-review.md) - Pod Security Standards (`restricted`) and eBPF checklist.
* [`compliance-architecture-review.md`](checklists/security/compliance-architecture-review.md) - GDPR, PCI-DSS, and SOC 2 readiness checklist.

### Operational & SRE Checklists (`checklists/operations/`)
* [`production-readiness-review.md`](checklists/operations/production-readiness-review.md) - Complete PRR gate before customer traffic launch.
* [`operational-readiness-review.md`](checklists/operations/operational-readiness-review.md) - Service ownership, on-call, and runbook readiness.
* [`sre-readiness-review.md`](checklists/operations/sre-readiness-review.md) - Golden signals, SLI/SLO definitions, and error budget policies.
* [`incident-readiness-review.md`](checklists/operations/incident-readiness-review.md) - Severity matrix, Incident Commander, and communication templates.
* [`dr-readiness-review.md`](checklists/operations/dr-readiness-review.md) - RTO/RPO alignment, cross-region failover, and game day verification.
* [`backup-recovery-review.md`](checklists/operations/backup-recovery-review.md) - Immutable WORM backups and automated restore drill verification.

### Cloud & Infrastructure Checklists (`checklists/cloud/`)
* [`cloud-architecture-review.md`](checklists/cloud/cloud-architecture-review.md) - Formal ARB governance gate evaluating multi-AZ resilience and static stability.
* [`cloud-landing-zone-checklist.md`](checklists/cloud/cloud-landing-zone-checklist.md) - Multi-account hierarchy, root guardrails, and transit networking.
* [`cloud-migration-readiness-checklist.md`](checklists/cloud/cloud-migration-readiness-checklist.md) - Discovery, CDC lag, and reverse-replication rollback.
* [`cloud-disaster-recovery-checklist.md`](checklists/cloud/cloud-disaster-recovery-checklist.md) - Asynchronous replication, secondary IaC automation, and game days.
* [`cloud-security-guardrails-checklist.md`](checklists/cloud/cloud-security-guardrails-checklist.md) - Preventative SCPs, Kubernetes PSS, and CSPM.

### Application Architecture Checklists (`checklists/application/`)
* Checklists covering [.NET](checklists/application/dotnet-architecture-checklist.md), [Java](checklists/application/java-architecture-checklist.md), [Node.js](checklists/application/nodejs-architecture-checklist.md), [Python](checklists/application/python-architecture-checklist.md), [React](checklists/application/react-architecture-checklist.md), [Angular](checklists/application/angular-architecture-checklist.md), [Mobile](checklists/application/mobile-architecture-checklist.md), [Application Security](checklists/application/application-security-checklist.md), and [Testing](checklists/application/application-testing-checklist.md).

---

## 2. Quantitative Sizing & Economic Calculators (`calculators/`)
* Deterministic mathematical sizing tools for Compute Capacity, Kubernetes Nodes, Network Egress, Storage Lifecycles, Compound SLAs, DR Economics, and FinOps Unit Costs.

---

## 3. Scorecards & Evaluation Rubrics (`scorecards/`)
* [`production-readiness-scorecard.md`](scorecards/production-readiness-scorecard.md) - 15-Dimension quantitative scorecard (0–5 rating) evaluating architecture, security, reliability, observability, deployment, and operational ownership.

---

## 4. Architecture Review & Interview Playbooks (`architecture-review/`)
* [`security-operations-interview-playbook.md`](architecture-review/security-operations-interview-playbook.md) - Solutions for 14 high-stakes security & SRE system design scenarios.
* [`cloud-architecture-interview-playbook.md`](architecture-review/cloud-architecture-interview-playbook.md) - Solutions for 14 enterprise cloud design scenarios.
* [`data-and-integration-architecture-review.md`](architecture-review/data-and-integration-architecture-review.md) - ARB governance playbook for data pipelines and financial platforms.

### AI & Modern Architecture Checklists & Tools
* [`checklists/ai-architecture-review.md`](checklists/ai-architecture-review.md) - ARB review checklist for AI, LLM, RAG, and agent workloads.
* [`checklists/ai-production-readiness.md`](checklists/ai-production-readiness.md) - Pre-flight production readiness gate for AI systems.
* [`calculators/ai-cost-calculator.md`](calculators/ai-cost-calculator.md) - Quantitative formulas for token budgets, vector DB RAM, and GPU sizing.
* [`architecture-review/ai-modern-architecture-interview-playbook.md`](architecture-review/ai-modern-architecture-interview-playbook.md) - Interview and review playbook for high-stakes enterprise AI scenarios.

### Enterprise Architecture Tools & Checklists (Phase 9)
* [`ea-maturity-calculator.md`](ea-maturity-calculator.md) - 7-dimension quantitative Enterprise Architecture maturity calculator.
* [`application-tco-calculator.md`](application-tco-calculator.md) - 5-year Total Cost of Ownership (TCO) financial modeling tool.
* [`modernization-priority-calculator.md`](modernization-priority-calculator.md) - Multi-criteria scoring calculator for application modernization.
* [`capability-mapping-worksheet.md`](capability-mapping-worksheet.md) - Standard worksheet for decomposing and cataloging business capabilities.
* [`vendor-evaluation-matrix.md`](vendor-evaluation-matrix.md) - 5-dimension weighted RFP evaluation matrix for enterprise software procurement.
* [`../09-enterprise-architecture/checklists/enterprise-architecture-master-checklist.md`](../09-enterprise-architecture/checklists/enterprise-architecture-master-checklist.md) - Master 9-domain verification checklist.
