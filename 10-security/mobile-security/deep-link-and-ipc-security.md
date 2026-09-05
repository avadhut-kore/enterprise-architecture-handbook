# Deep-Link & IPC Security

## Executive Summary

Custom URL schemes (`myapp://payment/confirm`) can be registered by malicious third-party apps installed on the same device to hijack transactions.

---

## Architectural Standard
- Deprecate custom URI schemes.
- Mandate **iOS Universal Links** and **Android App Links**, which verify domain ownership via cryptographically signed association files hosted on the server (`/.well-known/assetlinks.json` and `/.well-known/apple-app-site-association`).
