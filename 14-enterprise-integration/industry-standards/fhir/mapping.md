# Mapping Legacy HL7 v2 and CDA to FHIR

## 1. Canonical Mapping Tables

| HL7 v2 Field | FHIR Resource Target | Transformation Rule |
| :--- | :--- | :--- |
| `PID-3` (Patient Identifier) | `Patient.identifier` | Map assigning authority namespace to `system` |
| `PID-5` (Patient Name) | `Patient.name` | Separate family name and given names |
| `OBX-3` (Observation Identifier) | `Observation.code` | Extract LOINC code and description |
| `OBX-5` (Observation Value) | `Observation.valueQuantity` | Parse numeric value; bind units to UCUM |
