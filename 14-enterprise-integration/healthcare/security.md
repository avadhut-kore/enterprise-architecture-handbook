# SMART on FHIR Security and OAuth 2.0 Scopes

## 1. SMART App Launch Architecture
SMART on FHIR specifies how third-party applications securely launch inside or outside an EHR session using OAuth 2.0 and OpenID Connect.

```
[Clinician Desktop (EHR)] ──(Launches App with launch_token)──> [SMART App]
                                                                     │
                                  ┌── (Requests Token with launch scope)
                                  ▼
                     [EHR Authorization Server]
                                  │
                                  ▼ (Returns Access Token + patient ID)
[SMART App] ──(GET /Patient/{id})──> [EHR FHIR API Server]
```

## 2. Fine-Grained Clinical Scopes
- `patient/Observation.read`: Grants read-only access to observation records of the current patient.
- `user/Condition.write`: Grants clinician-scoped write permission to problem lists.
