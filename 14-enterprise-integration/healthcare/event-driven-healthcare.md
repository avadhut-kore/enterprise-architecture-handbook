# Event-Driven Architecture in Clinical Integrations

## 1. Asynchronous Clinical Event Flows
Critical clinical events must trigger immediate real-time notifications:
- **Vital Sign Deterioration**: Sepsis early warning score (MEWS) spike triggers immediate ICU team paging.
- **Critical Lab Value Alert**: Blood potassium $> 6.5	ext{ mEq/L}$ published to `clinical.alerts.critical` topic.

## 2. FHIR Subscriptions Framework (R5 / R4 Backport)
```http
POST /fhir/r4/Subscription HTTP/1.1
Host: ehr.hospital.internal
Content-Type: application/json

{
  "resourceType": "Subscription",
  "status": "requested",
  "reason": "Notify clinical decision support engine on new lab results",
  "criteria": "Observation?code=http://loinc.org|883-9",
  "channel": {
    "type": "rest-hook",
    "endpoint": "https://cds-engine.hospital.internal/webhook/labs",
    "header": ["Authorization: Bearer sec_tok_99182"]
  }
}
```
