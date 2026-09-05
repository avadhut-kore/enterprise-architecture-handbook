# Common JWT Architectural Vulnerabilities & Mitigations

## Executive Summary

1. **The `alg: none` Vulnerability**: Attackers modify the JWT header to `"alg": "none"` and strip the signature segment.
   - *Mitigation*: The validation library must enforce a strict allowlist of approved asymmetric algorithms (`["RS256", "ES256"]`); reject tokens with `"alg": "none"` unconditionally.
2. **Algorithm Confusion (HMAC vs RSA)**: An attacker takes an RSA public key (which is publicly available) and uses it as the shared HMAC secret to sign a token with `"alg": "HS256"`.
   - *Mitigation*: The validation library must bind the expected key type to the algorithm; never pass an RSA public key to an HMAC verifier.
3. **Missing Audience (`aud`) Validation**: A token issued for a public marketing service is forwarded by an attacker to the core banking API.
   - *Mitigation*: Every microservice must validate that its own unique identifier is present in the `aud` claim.
