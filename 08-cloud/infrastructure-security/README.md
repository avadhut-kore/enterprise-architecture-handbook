# Cloud Infrastructure Security Architecture

## Executive Summary

Cloud security operates under the assumption of an untrusted physical and network environment. Enterprise infrastructure security enforces a **Defense-in-Depth** strategy where controls are implemented across perimeter, network, host, container, data, and identity tiers.

---

## Defense-in-Depth Layered Architecture

```mermaid
graph TD
    Threat[External / Insider Threat] --> L1[1. Perimeter Defense: DDoS Shield, Cloud WAF, Anycast Edge]
    L1 --> L2[2. Network Security: Private Subnets, Transit Inspection, Default-Deny Security Groups]
    L2 --> L3[3. Workload Isolation: Distroless Containers, Non-Root Users, MicroVM Sandboxing]
    L3 --> L4[4. Identity & Authorization: Zero Standing Privileges, PIM, Workload Identity]
    L4 --> L5[5. Data Protection: KMS Envelope Encryption at Rest, mTLS in Transit, WORM Locks]
    L5 --> L6[6. Detection & Response: SIEM Aggregation, GuardDuty / Sentinel Anomaly Detection]
```

---

## Deliverables & Guides

| Document | Focus Area | Architectural Impact |
| :--- | :--- | :--- |
| **[Defense in Depth](defense-in-depth.md)** | Multi-layered controls | Layered security controls from internet edge to physical data |
| **[Network Segmentation](network-segmentation.md)** | Network micro-segmentation | Zero-trust boundaries, DMZ topologies, isolated compliance enclaves |
| **[Workload Identity](workload-identity.md)** | Machine identity federation | Eliminating service account keys via OIDC JWT token exchange |
| **[Vulnerability Management](vulnerability-management.md)** | Continuous security posture | CVE scanning, golden image pipelines, patch automation |
| **[CSPM & Compliance](cspm-and-compliance.md)** | Posture management & drift | Cloud Security Posture Management, automated policy enforcement |
| **[Security Logging & SIEM](security-logging-monitoring.md)** | Telemetry & threat detection | CloudTrail, Sentinel, GuardDuty, immutable WORM log archiving |
| **[Zero Trust Architecture](zero-trust-architecture.md)** | Identity-centric security | BeyondCorp model, contextual access, continuous verification |
