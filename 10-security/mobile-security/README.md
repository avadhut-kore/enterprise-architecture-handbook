# Mobile Application Security Architecture (`mobile-security/`)

## Executive Summary

Mobile applications execute on untrusted, consumer-controlled hardware. Mobile architecture must assume the device may be rooted/jailbroken, the network may be hostile, and the binary may be reverse-engineered.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`mobile-security-architecture.md`](mobile-security-architecture.md) | Mobile Foundations | Secure Enclave, Android KeyStore, hardware-backed keys |
| [`certificate-pinning.md`](certificate-pinning.md) | Network Protection | Public Key Pinning, certificate rotation failure mitigation |
| [`deep-link-and-ipc-security.md`](deep-link-and-ipc-security.md) | Inter-App Security | Universal Links, Android App Links, link hijacking |
| [`offline-data-security-and-encryption.md`](offline-data-security-and-encryption.md) | Local Storage | SQLCipher, biometric key derivation, jailbreak detection |
