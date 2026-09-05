# ISO 20022 Financial Messaging Architecture Library

## 1. Overview
ISO 20022 is the universal financial industry messaging standard underpinning the global migration of RTGS networks (Fedwire, CHIPS, TARGET2, CHAPS, Lynx) and real-time instant payment schemes (FedNow, RTP, SEPA Instant).

## 2. Directory Structure
- [overview.md](overview.md): Architectural principles, dictionary model, and global migration timelines.
- [message-model.md](message-model.md): ISO 20022 Business Conceptual, Logical, and Physical message schemas.
- [business-components.md](business-components.md): Business Application Header (BAH - `head.001`) and common types.
- [messages.md](messages.md): Message catalog across pacs, pain, camt, and remt domains.
- [pacs.md](pacs.md): Payment Clearing and Settlement messages (`pacs.008`, `pacs.009`, `pacs.002`, `pacs.004`).
- [pain.md](pain.md): Payment Initiation messages (`pain.001`, `pain.002`, `pain.008`).
- [camt.md](camt.md): Cash Management and Statement messages (`camt.053`, `camt.054`, `camt.052`).
- [remt.md](remt.md): Remittance Advice messages (`remt.001`).
- [message-mapping.md](message-mapping.md): Mapping legacy SWIFT MT and NACHA to ISO 20022 XML.
- [validation.md](validation.md): High-performance XSD and Schematron validation pipelines.
- [transformation.md](transformation.md): XSLT 3.0, Apache Camel, and JSON-LD transformations.
- [versioning.md](versioning.md): Managing yearly ISO 20022 maintenance releases (SR 2023 / SR 2024).
- [compatibility.md](compatibility.md): Backward compatibility and multi-version co-existence.
- [implementation-guidance.md](implementation-guidance.md): Implementation guidance for integration architects.
- [security.md](security.md): XML digital signatures (Enveloped XML-DSig) and PKI.
- [observability.md](observability.md): Tracing End-to-End IDs (`EndToEndId`, `UETR`) across systems.
- [testing.md](testing.md): Automated mock clearing houses and ISO 20022 test suites.
- [examples/pacs008-credit-transfer.md](examples/pacs008-credit-transfer.md): Full annotated production XML.
