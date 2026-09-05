# Authentication Systems Architecture (`authentication/`)

## Executive Summary

Authentication verifies the asserted identity of an entity. This directory covers enterprise authentication mechanisms, multi-factor authentication (MFA), FIDO2 passwordless standards, risk-based adaptive authentication, and session token lifecycles.

---

## Key Guides in this Directory

| Guide | Core Topic | Architectural Impact |
| :--- | :--- | :--- |
| [`authentication-mechanisms.md`](authentication-mechanisms.md) | Auth Factors | Passwordless, FIDO2 / WebAuthn, TOTP, Push Notifications |
| [`adaptive-and-risk-based-authentication.md`](adaptive-and-risk-based-authentication.md) | Risk Scoring | Dynamic step-up authentication based on risk heuristics |
| [`session-management-and-token-lifecycle.md`](session-management-and-token-lifecycle.md) | Token Lifecycles | Short-lived access tokens, refresh token rotation, revocation |
| [`credential-rotation-and-revocation.md`](credential-rotation-and-revocation.md) | Credential Ops | Zero-downtime key rotation, automated certificate renewal |
