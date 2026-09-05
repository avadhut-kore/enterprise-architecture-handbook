# Refresh Token Rotation & Breach Detection

## Executive Summary

Refresh tokens are long-lived credentials. If a refresh token is stolen by an attacker (e.g., extracted from mobile storage or intercepted via network tapping), the attacker could silently generate valid access tokens indefinitely. 

**Refresh Token Rotation (RTR)** mitigates this threat by ensuring that **every refresh token can only be used once**.

---

## 1. Breach Detection & Family Revocation Mechanism

```mermaid
sequenceDiagram
    autonumber
    participant Legitimate as Legitimate User App
    participant Attacker as Attacker (Stole Token RT1)
    participant AS as Authorization Server

    Note over Legitimate,AS: Normal Rotation
    Legitimate->>AS: POST /token (uses RT1)
    AS->>AS: Invalidates RT1; Generates RT2
    AS-->>Legitimate: Returns AT2 + RT2
    
    Note over Attacker,AS: Attack Attempt: Replay of Stolen RT1
    Attacker->>AS: POST /token (attempts to use RT1)
    AS->>AS: ALERT: Previously consumed refresh token (RT1) replayed!
    Note over AS: Automatic Breach Response: Revoke all tokens in family (RT1, RT2)!
    AS-->>Attacker: 400 Bad Request (invalid_grant)
    
    Note over Legitimate,AS: Legitimate app attempts next refresh
    Legitimate->>AS: POST /token (uses RT2)
    AS-->>Legitimate: 400 Bad Request (Token family revoked due to compromise)
    Note over Legitimate: Forces user to perform fresh interactive MFA login
```
