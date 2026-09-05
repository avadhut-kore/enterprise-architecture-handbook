# Security Monitoring & Detection Architecture (`security-monitoring/`)

## Executive Summary

Security monitoring transforms raw logs and telemetry from cloud providers, identity systems, networks, and applications into high-fidelity security alerts and automated detections.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`security-monitoring-architecture.md`](security-monitoring-architecture.md) | Detection Architecture | Event collection, normalizer, correlation engine, SIEM |
| [`siem-and-soc-integration.md`](siem-and-soc-integration.md) | SIEM Topologies | Streaming architecture to Splunk / Microsoft Sentinel |
| [`behavioral-anomaly-detection-and-ueba.md`](behavioral-anomaly-detection-and-ueba.md) | UEBA | User and Entity Behavior Analytics for insider threats |
| [`tamper-proof-audit-logging.md`](tamper-proof-audit-logging.md) | WORM Compliance | Immutable S3 Object Lock, non-repudiation, log integrity |
