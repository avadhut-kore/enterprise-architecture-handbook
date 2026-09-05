# Adaptive & Risk-Based Authentication

## Executive Summary

Adaptive authentication dynamically adjusts the friction and verification requirements of an authentication challenge based on real-time contextual risk signals.

---

## 1. Risk Evaluation Architecture

```mermaid
flowchart TD
    User["User Login Attempt"] --> Engine["Risk Assessment Engine"]
    
    subgraph Signals ["Real-Time Contextual Signals"]
        S1["IP Geolocation & Impossible Travel"]
        S2["Device Posture & EDR Telemetry"]
        S3["Behavioral Biometrics & Time of Day"]
        S4["Threat Intelligence (Tor / Proxy IPs)"]
    end
    Signals --> Engine

    Engine --> Decision{"Calculated Risk Score"}
    Decision -->|Low Risk (< 20)| A1["Seamless Access Granted (Passkey)"]
    Decision -->|Medium Risk (20 - 70)| A2["Step-Up Challenge Required (Hardware Token MFA)"]
    Decision -->|High Risk (> 70)| A3["Block Access & Alert SOC (Automated Account Lock)"]
```
