# Authorization Code Flow with PKCE (RFC 7636)

## Executive Summary

Proof Key for Code Exchange (PKCE, pronounced "pixy") was originally designed for mobile native apps to prevent Authorization Code interception attacks. Today, OAuth 2.1 mandates PKCE for **ALL client applications**, including server-side confidential web apps and Single Page Applications (SPAs).

---

## 1. Protocol Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    actor User as User Browser / App
    participant Client as Client Application
    participant AS as Authorization Server
    participant RS as Resource Server (API)

    Note over Client: 1. Generate code_verifier (cryptographic random)<br/>2. Compute code_challenge = BASE64URL(SHA256(code_verifier))
    Client->>User: Redirects to Authorization Endpoint with code_challenge & method=S256
    User->>AS: GET /authorize?response_type=code&client_id=...&code_challenge=...
    AS->>User: Prompts for Authentication & Consent
    User->>AS: Submits credentials (Passkey/MFA)
    AS-->>User: Redirects with Authorization Code
    User-->>Client: Delivers Authorization Code

    Note over Client: 3. Redeem Code with original code_verifier
    Client->>AS: POST /token (code, code_verifier, client_id)
    Note over AS: Computes SHA256(code_verifier) and compares to stored code_challenge.<br/>Matches! Proof of origin verified.
    AS-->>Client: Returns Access Token + Refresh Token
    Client->>RS: GET /api/orders (Authorization: Bearer <token>)
    RS-->>Client: 200 OK (Protected Data)
```

---

## 2. Cryptographic Construction
- **Code Verifier**: A cryptographically random string using the unreserved characters `[A-Z]`, `[a-z]`, `[0-9]`, `-`, `.`, `_`, `~`, with a minimum length of 43 characters and a maximum length of 128 characters.
- **Code Challenge**:
  $$\text{code\_challenge} = \text{BASE64URL-ENCODE}(\text{SHA-256}(\text{code\_verifier}))$$
  The `code_challenge_method` must strictly be set to `S256`. The legacy `plain` method is strictly prohibited by enterprise security standards.
