# Implementation Example: EHR to FHIR Integration Bridge

## 1. Architecture Context
This service consumes raw HL7 v2 `ORU^R01` (Unsolicited Observation Result) socket messages emitted by hospital laboratory analyzers, parses them into FHIR `Observation` JSON resources, and publishes them to a Kafka event topic.

## 2. Python Processing Engine
```python
import json
import hl7

def transform_hl7_oru_to_fhir_observation(raw_hl7_message: str) -> dict:
    parsed = hl7.parse(raw_hl7_message)
    
    # Extract MSH and OBR/OBX segments
    patient_id = str(parsed.segment('PID')[3][0])
    loinc_code = str(parsed.segment('OBX')[3][0])
    test_name = str(parsed.segment('OBX')[3][1])
    value = float(str(parsed.segment('OBX')[5][0]))
    units = str(parsed.segment('OBX')[6][0])
    effective_time = str(parsed.segment('OBR')[7][0])

    fhir_observation = {
        "resourceType": "Observation",
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "laboratory"
            }]
        }],
        "code": {
            "coding": [{
                "system": "http://loinc.org",
                "code": loinc_code,
                "display": test_name
            }]
        },
        "subject": {
            "reference": f"Patient/{patient_id}"
        },
        "valueQuantity": {
            "value": value,
            "unit": units,
            "system": "http://unitsofmeasure.org"
        }
    }
    return fhir_observation
```
