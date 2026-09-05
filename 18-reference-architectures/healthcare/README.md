# Healthcare & Clinical Interoperability Platform Reference Architecture

## 1. Executive Summary & Architectural Vision
The Healthcare & Clinical Interoperability Platform is a HIPAA-compliant health system foundation designed to integrate hospital Electronic Health Records (EHR/EMR), departmental clinical systems (LIS, PACS), pharmacy systems, and patient portals into a unified **FHIR R4 Clinical Data Repository (CDR)**.

It combines deterministic and probabilistic Enterprise Master Patient Index (EMPI) identity resolution, an HL7 v2 MLLP adapter mesh, clinical terminology cross-mapping, and SMART on FHIR OAuth 2.0 access.

```
[Patient Portal, Provider EHR, SMART on FHIR Apps, External Health Info Exchanges]
                                  │
             ═════════════════════▼═════════════════════  [SMART on FHIR Gateway]
                      Clinical Core Services
     ┌─────────────────┬──────────────────┬──────────────────┐
     ▼                 ▼                  ▼                  ▼
[Patient Identity]    [FHIR R4 CDR]      [Terminology Hub]  [Consent & HIPAA]
(EMPI Matching Engine)(Clinical Entities)(SNOMED / LOINC)   (Audit Vault)
     │                 │                  │                  │
     └─────────────────┼──────────────────┴──────────────────┘
                       ▼
            [Clinical Event Stream (Kafka)]
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
[HL7 v2 MLLP Adapter]       [DICOM Medical Imaging]
(Epic / Cerner Integration) (Orthanc / Cloud Healthcare)
```

## 2. Architectural Package Contents
- [01-business-and-requirements.md](01-business-and-requirements.md): Clinical safety, patient personas, and HIPAA NFR budgets.
- [02-architecture-and-c4.md](02-architecture-and-c4.md): C4 Context, Container, Component models, and cloud mappings.
- [03-application-architecture.md](03-application-architecture.md): EMPI matching engine, FHIR REST controllers, and SMART on FHIR.
- [04-data-architecture.md](04-data-architecture.md): FHIR resource graph, longitudinal patient records, and consent stores.
- [05-integration-architecture.md](05-integration-architecture.md): HL7 v2 ADT/ORU processing, MLLP sockets, and FHIR $export.
- [06-security-and-compliance.md](06-security-and-compliance.md): HIPAA Security/Privacy, BAA requirements, and audit logging.
- [07-infrastructure-and-devops.md](07-infrastructure-and-devops.md): HIPAA-compliant cloud landing zones, Terraform, and K8s.
- [08-observability-and-reliability.md](08-observability-and-reliability.md): Clinical telemetry, HL7 ACK error rates, and DR.
- [09-cost-and-finops.md](09-cost-and-finops.md): Storage growth for clinical imaging, FHIR compute, and monthly TCO.
- [10-sequences-and-flows.md](10-sequences-and-flows.md): Lab result ingestion (ORU_R01 to Observation) and SMART on FHIR SSO.
- [11-adrs-and-evolution.md](11-adrs-and-evolution.md): Canonical ADRs (FHIR R4 Repository, Probabilistic EMPI) and roadmap.
