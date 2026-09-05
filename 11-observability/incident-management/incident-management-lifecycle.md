# Incident Management Lifecycle & Workflow

## Executive Summary

```mermaid
flowchart TD
    D["1. Detection (SLO Burn Page)"] --> T["2. Triage & Severity Declaration"]
    T --> IC["3. Appoint Incident Commander (War Room)"]
    IC --> M["4. Mitigation (Rollback / Shed Load / Failover)"]
    M --> V["5. Validation & Recovery"]
    V --> C["6. Stakeholder Communication"]
    C --> PIR["7. Blameless Post-Incident Review (PIR)"]
```
- **Mitigation vs Resolution**: During an active outage, the goal is **rapid mitigation** (stopping customer pain via rollback or traffic diversion), NOT finding the academic root cause. Investigation occurs after customer traffic is safe.
