# ADR-0009: Pre-Ingestion PII & Sensitive Data Redaction in Collector Memory

* **Status**: Accepted
* **Date**: 2026-07-01
* **Deciders**: Chief Information Security Officer (CISO), Data Privacy Officer (DPO), Lead Observability Architect
* **Technical Story**: [ARCH-OBS-009] Zero-Trust Telemetry Privacy

---

## Context and Problem Statement
Corporate compliance frameworks (GDPR, PCI-DSS, HIPAA) strictly penalize the unauthorized storage of Personally Identifiable Information (PII), cardholder data (PAN), and Protected Health Information (PHI) in centralized log and trace stores. Relying on application developers to remember to redact sensitive data in application code consistently fails.

## Decision Drivers
* Guaranteed zero-leakage of sensitive credentials and compliance data.
* Centralized, declarative redaction rules enforced outside application code.
* In-memory redaction before telemetry crosses network or storage boundaries.

## Considered Options
1. **Option 1**: Developer-enforced redaction in application code (Status Quo).
2. **Option 2**: Post-ingestion redaction in central search indexes.
3. **Option 3**: **Pre-Ingestion In-Memory Redaction via OpenTelemetry Collector Processors**.

## Decision Outcome
**Chosen Option**: **Option 3: Pre-Ingestion In-Memory Redaction in OTel Collectors**.

### Positive Consequences
* **Defense-in-Depth**: Even if an application developer mistakenly logs a raw authorization token or SSN, the local Node DaemonSet collector redacts it in memory before network serialization.
* **Zero Storage Contamination**: Prevents toxic data from ever touching centralized disk storage or cloud object buckets.
* **Audit Verification**: Redaction processors are version-controlled, declarative, and easily verified by external compliance auditors.

### Negative Consequences
* Introduces slight regex processing overhead on the collector memory buffer ($\approx 3\%$ CPU).

---

## Links
* Security Reference: [`../reference-architectures/06-financial-payments.md`](../reference-architectures/06-financial-payments.md)
