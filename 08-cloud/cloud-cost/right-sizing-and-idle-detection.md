# Right-Sizing Architecture & Idle Resource Detection

## Executive Summary

Enterprise cloud environments are filled with "zombie infrastructure"—unattached disks, idle load balancers, and severely over-provisioned virtual machines.

---

## 1. Automated Garbage Collection Pipeline

```mermaid
graph LR
    Schedule[Nightly AWS Lambda / Azure Function Audit] --> Scan[Scans Cloud APIs]
    Scan --> Check1{Unattached EBS Volume > 7 Days?}
    Scan --> Check2{EBS Snapshot Age > 90 Days?}
    Scan --> Check3{Average CPU < 3% over 14 Days?}

    Check1 -->|True| SnapshotDelete[Take Final Snapshot & Delete Volume]
    Check2 -->|True| PurgeSnap[Purge Expired Snapshot]
    Check3 -->|True| Downgrade[Downsize Instance Type Automatically]
```

---

## 2. Right-Sizing Sizing Guardrails
- **Target Utilization**: Size production compute instances to operate at **60–70% average CPU and memory utilization**. An instance running at 10% CPU is 4x over-provisioned.
- **Modernize Instance Generations**: Upgrading from generation 5 (e.g., `m5`) to generation 7 (e.g., `m7g`) provides a 20% performance increase at a 15% lower nominal hourly rate.
