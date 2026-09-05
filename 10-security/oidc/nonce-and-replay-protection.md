# OIDC Nonce & Token Replay Protection

## Executive Summary

The `nonce` parameter associates a client session with an ID Token, mitigating token replay attacks where an attacker intercepts an ID token and attempts to inject it into another browser session.

---

## 1. Nonce Verification Mechanism

1. **Client Generation**: The client generates a cryptographically random string ($N$), hashes it, and stores it in an unguessable session cookie.
2. **Authorization Request**: The client includes `nonce=N` in the `/authorize` request.
3. **ID Token Claim**: The OpenID Provider includes `nonce: N` verbatim inside the signed ID Token payload.
4. **Client Verification**: Upon receiving the ID Token, the client verifies that the `nonce` claim inside the signed token exactly matches the stored session cookie. If it does not match, the token is rejected immediately.
