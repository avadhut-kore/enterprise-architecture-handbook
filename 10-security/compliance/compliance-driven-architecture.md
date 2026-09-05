# Compliance-Driven Software Architecture

## Executive Summary

Compliance is not an administrative checkbox; it is a foundational architectural driver that dictates network topology, encryption standards, data storage boundaries, and access control models.

---

## Architectural Influence Across Major Regulations

| Regulation | Architectural Mandate | Technical Architecture Solution |
| :--- | :--- | :--- |
| **PCI-DSS 4.0** | Isolate and protect Cardholder Data (PANs) | Tokenization proxy to eliminate CDE scope from web and application tiers |
| **GDPR / CCPA** | Right to be Forgotten & Data Minimization | Automated TTL lifecycles and customer-specific cryptographic shredding |
| **HIPAA** | Safeguard electronic Protected Health Information | Mandatory TLS 1.3, AES-256 encryption at rest, immutable audit trails |
| **Data Residency**| Data must remain within national physical borders | Multi-region cloud architecture pinning storage to sovereign regions |
