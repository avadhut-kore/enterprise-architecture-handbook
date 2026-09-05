# ADR-0045: Adoption of Multi-Account AWS Control Tower Landing Zone

## Metadata
```yaml
id: ADR-0045
title: Adoption of Multi-Account AWS Control Tower Landing Zone
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
A single AWS account footprint created an unacceptable security blast radius, noisy neighbor contention, and unmanageable IAM policies.

---

## 2. Decision
We mandate an automated Multi-Account Landing Zone governed by AWS Control Tower and AWS Organizations, dedicating separate accounts per application per environment (Prod, Staging, Dev) and isolating Core Logging and Network Transit.

---

## 3. Positive Consequences
- Strict blast radius containment: a compromise in dev cannot impact production.
- Automated compliance guardrails enforced via Service Control Policies (SCPs).
- 100% granular cost allocation per account.

---

## 4. Negative Consequences & Trade-offs
- Higher administrative overhead in managing cross-account role assumption.
- Requires Transit Gateway for inter-account networking.

---

## 5. Alternatives Considered & Rejected
- **Single Giant AWS Account with VPC Isolation**: Rejected due to IAM privilege escalation risks and service limit throttling.
