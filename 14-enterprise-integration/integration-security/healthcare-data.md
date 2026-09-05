# Healthcare Data Protection: HIPAA, HITECH, and Clinical Data

## 1. Protected Health Information (PHI)
Under HIPAA § 164.514, PHI comprises 18 direct identifiers (names, dates, geographic data below state, phone numbers, medical record numbers) linked to physical or mental health conditions, healthcare provision, or payment.

## 2. Security Architecture for Healthcare Integration
- **De-Identification Pipelines**: Strip the 18 Safe Harbor identifiers before routing clinical records to data analytics, AI models, or third-party platforms.
- **BAA Enforcement**: Any cloud integration service or iPaaS handling PHI must have a signed Business Associate Agreement (BAA).
- **mTLS + Access Logging**: Every EHR query via FHIR or HL7 v2 must record the clinician identity, purpose of use (`emergency`, `treatment`, `billing`), and timestamp.
