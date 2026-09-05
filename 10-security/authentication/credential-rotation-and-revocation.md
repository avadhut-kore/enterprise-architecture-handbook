# Credential Rotation & Emergency Revocation

## Executive Summary

Long-lived credentials (API keys, TLS certificates, database passwords, signing keys) must undergo automated, scheduled rotation without causing service downtime. When a compromise is suspected, the architecture must support instant emergency revocation.

---

## 1. The Dual-Key (Overlap) Rotation Pattern

To rotate a credential without downtime:
1. **Phase 1 (Dual Validation)**: Deploy the new signing key ($K_2$) alongside the old key ($K_1$). The authorization server continues signing with $K_1$, but resource servers accept signatures from *either* $K_1$ or $K_2$.
2. **Phase 2 (Active Cutover)**: The authorization server begins signing new tokens with $K_2$. Existing in-flight tokens signed with $K_1$ continue to validate until their 15-minute TTL expires.
3. **Phase 3 (Deprecation)**: Once all tokens signed with $K_1$ have expired, $K_1$ is permanently deleted from the Key Management Service (KMS).
