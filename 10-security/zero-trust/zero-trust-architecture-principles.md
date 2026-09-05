# Zero Trust Architecture Principles (NIST SP 800-207)

## Executive Summary

The NIST SP 800-207 standard establishes the canonical logical architecture for Zero Trust. Access decisions are evaluated dynamically by a **Policy Decision Point (PDP)** and enforced by a **Policy Enforcement Point (PEP)**.

---

## 1. NIST SP 800-207 Logical Architecture

```mermaid
flowchart TD
    Subject["Subject (User / Workload)"] --> PEP["Policy Enforcement Point (PEP)<br/>[API Gateway / Service Mesh]"]
    PEP --> Resource["Target Enterprise Resource"]

    subgraph ControlPlane ["Zero Trust Control Plane"]
        PDP["Policy Decision Point (PDP)<br/>[Policy Engine / OPA]"]
        PA["Policy Administrator"]
    end

    PEP <-->|Requests Evaluation| PDP
    PDP <-->|Configures Access Rules| PA

    subgraph ContextSignals ["Dynamic Context Feeds"]
        C1["Continuous Threat Intel"]
        C2["Data Access Policies"]
        C3["PKI / Certificate Authority"]
        C4["SIEM Audit Telemetry"]
    end
    ContextSignals --> PDP
```
