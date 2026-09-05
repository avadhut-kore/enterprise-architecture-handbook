# Security Logging, SIEM Integration & Threat Detection

## Executive Summary

Security observability requires centralized aggregation, real-time threat detection, and immutable archiving of all control plane management events and network flow logs.

---

## 1. Centralized Security Telemetry Pipeline

```mermaid
graph TD
    Workload1[AWS Account: Payments Prod] --> FlowLogs[VPC Flow Logs]
    Workload1 --> CloudTrail[Management Events: CloudTrail]
    Workload2[Azure Sub: Wealth Prod] --> Activity[Azure Activity Logs]

    FlowLogs ==> CentralArchive[(Central Log Archive: Immutable WORM S3)]
    CloudTrail ==> CentralArchive
    Activity ==> CentralArchive

    CentralArchive --> SIEM[Enterprise SIEM: Microsoft Sentinel / Splunk / Datadog]
    SIEM --> SOC[24/7 Security Operations Center]
```

---

## 2. Architectural Guardrails

- **Immutable Log Storage (WORM)**: Security audit logs must be routed to a dedicated, isolated Log Archive account protected by **Object Lock in Compliance Mode** with MFA Delete enabled. Even root administrators cannot alter or delete security logs.
- **AI-Driven Threat Detection**: Enable cloud-native anomaly detection engines (AWS GuardDuty, Microsoft Defender for Cloud) that analyze DNS queries, flow logs, and IAM calls for signs of credential compromise, cryptocurrency mining, or port scanning.
