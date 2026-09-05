# Identity Lifecycle Management & SCIM 2.0

## Executive Summary

Identity Lifecycle Management (Joiners, Movers, Leavers) governs how digital identities are born, modified, and terminated. The greatest enterprise security vulnerability in identity is **orphaned accounts**—identities belonging to terminated employees or decommissioned services that retain active access.

---

## 1. Automated SCIM 2.0 Provisioning Architecture

```mermaid
sequenceDiagram
    autonumber
    participant HR as Workday / HR System
    participant IdP as Microsoft Entra ID / Okta
    participant App1 as Enterprise SaaS (Salesforce)
    participant App2 as Internal Microservices Platform

    HR->>IdP: Employee Terminated (Leaver Event)
    IdP->>IdP: Revokes all active refresh tokens & SSO sessions
    IdP->>App1: SCIM HTTP DELETE /Users/{id}
    App1-->>IdP: 204 No Content (Deactivated)
    IdP->>App2: SCIM HTTP PATCH /Users/{id} (active: false)
    App2-->>IdP: 200 OK (Account Disabled)
```
