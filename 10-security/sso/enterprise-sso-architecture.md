# Enterprise SSO Architecture: SP-Initiated vs IdP-Initiated

## Executive Summary

In enterprise SSO, authentication can be initiated either by the Service Provider (SP) or by the Identity Provider (IdP). 

**Architectural Standard: SP-Initiated SSO is mandated; IdP-Initiated SSO is deprecated due to inherent CSRF risks.**

---

## 1. SP-Initiated SSO Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Employee Browser
    participant SP as Enterprise App (Salesforce / Internal Portal)
    participant IdP as Microsoft Entra ID / Okta

    User->>SP: Navigates to app.enterprise.com
    SP->>User: Redirects to IdP with signed Authentication Request
    User->>IdP: Authenticates via FIDO2 Passkey + Device Posture Check
    IdP-->>User: Issues signed SAML Assertion / OIDC ID Token via HTTP POST
    User->>SP: Posts Token to Assertion Consumer Service (ACS) endpoint
    SP->>SP: Validates signature against IdP certificate; logs user in
```
