# Session Management & Token Lifecycle Architecture

## Executive Summary

Session management bridges authentication and subsequent transactions. Architectures must balance security (limiting token lifetime to reduce blast radius) against user experience and system throughput (avoiding constant re-authentication).

---

## 1. Standard Token Lifecycle & Refresh Rotation

```mermaid
sequenceDiagram
    autonumber
    actor Client as Single Page App / Mobile
    participant Auth as Authorization Server (OIDC)
    participant API as Resource Server (Microservice)

    Client->>Auth: Authenticates with FIDO2 Passkey
    Auth-->>Client: Returns Access Token (15-min TTL) + Refresh Token 1 (24-hr TTL)
    
    Client->>API: GET /orders (Bearer Access Token)
    API-->>Client: 200 OK (Processes order)

    Note over Client,Auth: 15 minutes elapse; Access Token expires
    Client->>Auth: POST /token (grant_type=refresh_token, Refresh Token 1)
    Note over Auth: Refresh Token Rotation: Invalidate Token 1 immediately
    Auth-->>Client: Returns New Access Token + Refresh Token 2
    
    Note over Client,Auth: If Attacker attempts to reuse old Refresh Token 1:
    Client->>Auth: Attacker replays Refresh Token 1
    Auth->>Auth: BREACH DETECTED: Token reuse attempt!
    Auth-->>Client: 400 Bad Request & REVOKES ENTIRE REFRESH FAMILY
```
