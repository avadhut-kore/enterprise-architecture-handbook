# Clinical Terminology and Ontology Normalization

## 1. Global Clinical Terminologies

| Terminology Standard | Clinical Domain | Example Code / Usage |
| :--- | :--- | :--- |
| **SNOMED-CT** | Clinical diagnoses, findings, procedures | `44054006` (Type 2 diabetes mellitus) |
| **LOINC** | Laboratory observations and clinical measurements | `883-9` (ABO group in blood) |
| **RxNorm** | Normalized clinical drug names and dosages | `310965` (Amoxicillin 500 MG Oral Tablet) |
| **ICD-10-CM** | Morbidity coding and billing diagnostic codes | `E11.9` (Type 2 diabetes without complications) |
| **CPT / HCPCS** | Billing procedure codes and medical services | `99213` (Office outpatient visit, 20-29 min) |

## 2. Real-Time Terminology Translation Service
Integration gateways must translate local hospital laboratory codes into standardized LOINC codes using FHIR ConceptMap resources before sharing data with health information exchanges (HIEs).
