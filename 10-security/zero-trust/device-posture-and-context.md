# Device Posture & Contextual Access

## Executive Summary

Valid user credentials are insufficient for access. If an employee logs in with valid credentials from an unmanaged, malware-infected personal laptop, the enterprise remains vulnerable to session hijacking and keystroke logging.

---

## 1. Device Posture Verification Signals
Before granting access to internal resources, the Policy Decision Point verifies:
- **Endpoint Detection & Response (EDR)**: CrowdStrike / Defender agent is active and reporting zero high-severity malware alerts.
- **Disk Encryption**: FileVault / BitLocker is fully enabled.
- **OS Patch Level**: Operating system version is within the approved 30-day patch window.
- **Hardware Enclave**: Device possession proven via TPM / Secure Enclave hardware certificate.
