# Insurance Core Systems Integration Architecture

## 1. Overview
Insurance enterprise integration spans the policyholder lifecycle across Policy Administration Systems (PAS - Guidewire PolicyCenter, Duck Creek), Claims Management (Guidewire ClaimCenter), Billing Engines (Guidewire BillingCenter), actuarial rating engines, telematics streams, and reinsurer interfaces.

## 2. Insurance Data Standards: ACORD
The **Association for Cooperative Operations Research and Development (ACORD)** defines standard XML and RESTful data models for:
- Property & Casualty (P&C) policy underwriting.
- First Notice of Loss (FNOL) claims processing.
- Reinsurance treaty reporting.

## 3. Claims Processing Architecture Flow
```
[FNOL Mobile Claim Submission] ──> [API Gateway]
                                          │
                                          ▼
                             [Claims Orchestrator]
                                          │
        ┌─────────────────────────────────┼─────────────────────────────────┐
        ▼                                 ▼                                 ▼
[Guidewire ClaimCenter]         [Fraud Detection Engine]          [Vehicle Telematics Data]
(Creates Claim & Reserve)       (Anomaly & Staged Accident)       (Crash Severity G-Force)
```
