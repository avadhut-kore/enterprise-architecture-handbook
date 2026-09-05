# Enterprise Data Classification Framework

## Executive Summary

Data classification categorizes organizational data based on its sensitivity and the financial, reputational, or regulatory impact of unauthorized disclosure.

---

## 1. The Four-Tier Classification Model

| Tier | Classification | Description | Examples | Required Encryption | Access Controls |
|:---|:---|:---|:---|:---|:---|
| **Tier 1** | **Restricted / Highly Confidential** | Catastrophic impact if breached; regulated by law | Credit card PANs, SSNs, health records, banking credentials | AES-256 Envelope + Field-Level Tokenization | JIT Access, Dual Approval, Full Audit Logging |
| **Tier 2** | **Confidential** | Significant competitive or financial harm | Business contracts, source code, customer PII, financial ledgers | AES-256 with KMS CMKs at rest & TLS 1.3 | Authenticated RBAC/ABAC on internal network |
| **Tier 3** | **Internal** | Minor operational disruption | Internal wikis, employee directories, system logs | Standard storage encryption (AES-256) | Corporate SSO authenticated users |
| **Tier 4** | **Public** | Zero harm; approved for public distribution | Marketing copy, public API documentation | Public HTTPS transport | Unrestricted read access |
