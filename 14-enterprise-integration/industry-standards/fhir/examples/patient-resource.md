# Implementation Example: Production FHIR Patient Resource

## 1. Validated US Core Patient Resource (JSON)
```json
{
  "resourceType": "Patient",
  "id": "pat-10029",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
    ]
  },
  "identifier": [
    {
      "use": "usual",
      "type": {
        "coding": [{
          "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
          "code": "MR"
        }]
      },
      "system": "http://hospital.enterprise.org/mrn",
      "value": "MRN-881920"
    }
  ],
  "active": true,
  "name": [
    {
      "use": "official",
      "family": "Doe",
      "given": ["Jane", "Elizabeth"]
    }
  ],
  "gender": "female",
  "birthDate": "1984-06-15"
}
```
