# EHR Integration Architecture: Epic, Cerner, and Hybrid Clouds

## 1. Major EHR Vendor Ecosystems
- **Epic Systems**: Integrates via Epic App Orchard / Vendor Services, Interconnect Web Services (SOAP), Epic FHIR APIs, and Chronicle database extracts.
- **Oracle Health (Cerner)**: Integrates via Cerner Ignite APIs (SMART on FHIR), Millennium Open Developer experience, and HL7 v2 foreign system interfaces (FSI).

## 2. Real-Time vs. Bulk EHR Extract Patterns
```
High-Frequency Read (Point of Care)
[Clinical App] ──(SMART on FHIR: GET /Patient/123/Observation)──> [Epic FHIR Gateway] (SLA < 300ms)

Population Health Analytics (Bulk Export)
[Analytics Lake] ──(FHIR Bulk Data $export)──> [EHR Bulk Server] ──(NDJSON Stream to S3)
```
