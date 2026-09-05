# Why OAuth 2.0 is NOT an Authentication Protocol

## Executive Summary

One of the most dangerous and persistent architectural misunderstandings in software engineering is using OAuth 2.0 alone as an authentication protocol ("Pseudo-Authentication").

**OAuth 2.0 is an authorization framework designed for delegation, not for asserting user identity.**

---

## 1. The Pseudo-Authentication Vulnerability

When a client application receives an OAuth 2.0 `access_token` and assumes the user is authenticated simply because an access token was issued:
1. **No Audience Restriction for the Client**: The access token is intended for the *Resource Server*, not the client application. An attacker can authorize their own malicious application, take the resulting access token, and pass it to a vulnerable client app. The vulnerable client app inspects the token, sees a valid signature, and logs the attacker in as the victim!
2. **No User Profile Guarantees**: OAuth 2.0 specifies zero standard claims for user identity, email, authentication time, or MFA verification.
3. **The Solution**: **OpenID Connect (OIDC)** was created specifically to solve this problem by adding an identity layer (`id_token`) on top of OAuth 2.0.
