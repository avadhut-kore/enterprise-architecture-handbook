# Data Architecture: FHIR R4 Clinical Data Repository

## 1. Longitudinal Patient Record Resource Graph
The clinical repository models healthcare data according to HL7 FHIR R4 US Core profiles:
- `Patient` (Master Demographics)
- `Encounter` (Inpatient admission, Outpatient visit)
- `Condition` (Clinical diagnoses, problem list, ICD-10 codes)
- `Observation` (Vital signs, laboratory test values, LOINC codes)
- `MedicationRequest` (Prescriptions, RxNorm codes)
- `Consent` (Patient privacy authorizations and research opt-in)

## Operational Guidelines & Reliability Architecture
- **Idempotency & Safe Retries**: All transactions and mutations carry unique correlation IDs preventing duplicate execution.
- **Circuit Breakers & Timeouts**: Strict timeout policies protect core services from downstream cascading latency.
- **Disaster Recovery**: Automated multi-AZ replication guaranteeing operational continuity.
