# AI Privacy Architecture & Data Minimization (`ai-privacy/`)

## Executive Summary

Enterprise systems handling customer Personally Identifiable Information (PII), Protected Health Information (PHI), or financial records must ensure that data is not exposed to public foundation models or retained across multi-tenant environments.

---

## Directory Catalog

* **[PII Redaction & Anonymization Architecture](pii-redaction-and-anonymization.md)** — Client-side vs. gateway-side masking, reversible tokenization, and NER scrubbers.
* **[Zero Data Retention & Cloud Provider Contracts](zero-data-retention-and-cloud-contracts.md)** — Architectural requirements for enterprise vendor agreements and audit logging.
* **[Differential Privacy & Training Data Protection](differential-privacy-and-training-data.md)** — Preventing memorization of sensitive training records in fine-tuned model checkpoints.
