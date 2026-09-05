# Enterprise Healthcare Integration Architecture Library

## 1. Overview
Integrating enterprise healthcare systems requires bridging clinical EHR/EMR platforms (Epic, Cerner/Oracle Health), medical imaging archives (PACS/DICOM), laboratory information systems (LIS), pharmacy systems, and health insurance payers while strictly adhering to HIPAA, HITECH, and ONC 21st Century Cures Act interoperability mandates.

## 2. Directory Structure
- [healthcare-integration.md](healthcare-integration.md): Clinical interoperability paradigms and core principles.
- [ehr-integration.md](ehr-integration.md): Electronic Health Record integration architectures (Epic Interconnect, Cerner Ignite).
- [emr-integration.md](emr-integration.md): Clinical EMR departmental integrations and interfaces.
- [patient-identity.md](patient-identity.md): Enterprise Master Patient Index (EMPI) and deterministic/probabilistic matching.
- [clinical-data.md](clinical-data.md): Clinical data modeling, CDA, and structured observation stores.
- [terminology.md](terminology.md): Standard terminologies: SNOMED-CT, LOINC, RxNorm, ICD-10, CPT.
- [interoperability.md](interoperability.md): ONC 21st Century Cures Act, TEFCA, and USCDI standards.
- [event-driven-healthcare.md](event-driven-healthcare.md): Real-time clinical alerts, vitals streaming, and FHIR Subscriptions.
- [batch-healthcare-integration.md](batch-healthcare-integration.md): Bulk FHIR ($export), HIPAA X12 837/835 claim batches.
- [security.md](security.md): SMART on FHIR, OAuth 2.0 scopes, patient consent, and audit.
- [privacy.md](privacy.md): HIPAA de-identification (Safe Harbor vs. Expert Determination).
- [audit.md](audit.md): ATNA (Audit Trail and Node Authentication) and IHE compliance.
- [reconciliation.md](reconciliation.md): Clinical vs. billing reconciliation and claim settlement breaks.
- [reference-architecture.md](reference-architecture.md): Hospital-to-Cloud Interoperability Reference Architecture.
- [examples/ehr-fhir-bridge.md](examples/ehr-fhir-bridge.md): Annotated production EHR-to-FHIR event bridge.
