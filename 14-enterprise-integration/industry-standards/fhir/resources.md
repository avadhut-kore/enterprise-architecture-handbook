# FHIR Resource Taxonomy and Capabilities

## 1. Core Resource Classification
FHIR models healthcare data as modular components termed **Resources**:
- **Foundation**: `Bundle`, `Composition`, `OperationOutcome`.
- **Base / Administrative**: `Patient`, `Practitioner`, `Organization`, `Location`.
- **Clinical**: `Condition` (Diagnoses), `Observation` (Vitals/Labs), `Procedure`, `AllergyIntolerance`.
- **Medications**: `MedicationRequest`, `MedicationAdministration`, `MedicationDispense`.
- **Financial**: `Coverage`, `Claim`, `ExplanationOfBenefit`.
