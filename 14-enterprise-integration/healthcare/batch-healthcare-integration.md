# Batch Healthcare Integration: Bulk FHIR and HIPAA X12

## 1. HIPAA X12 Electronic Data Interchange (EDI) Formats
Health insurance payer integrations rely heavily on ANSI X12 batch file transactions:
- **X12 837**: Healthcare Claim Submission (Institutional / Professional).
- **X12 835**: Healthcare Claim Payment and Remittance Advice.
- **X12 270 / 271**: Eligibility and Benefit Inquiry / Response.

## 2. Bulk FHIR $export Architecture
To transfer population health data without crashing operational EHRs:
```
[Analytics Platform] ──(POST /Group/123/$export)──> [EHR Bulk Gateway]
                                                           │ (Returns HTTP 202 Accepted)
                                                           ▼
                             [Asynchronous Job Generates NDJSON Files]
                                                           │
[Analytics Platform] ◄──(Pulls NDJSON Files from S3)───────┘
```
