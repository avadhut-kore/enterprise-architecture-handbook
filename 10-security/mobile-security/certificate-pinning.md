# Mobile Certificate Pinning Architecture

## Executive Summary

Certificate pinning associates a mobile client exclusively with a specific server certificate or public key, preventing Man-in-the-Middle (MitM) attacks even if an attacker installs a malicious root CA on the mobile device.

---

## Operational Risk of Pinning (The Bricking Hazard)
- If an enterprise pins a leaf certificate that expires unexpectedly or must be revoked during a breach, **all mobile apps will fail to connect globally** until an emergency app store update is approved (which can take 48–72 hours).
- **Architectural Solution: Public Key Pinning with Backup Pins**: Pin the **Subject Public Key Info (SPKI)** of the intermediate CA and include a minimum of **two backup pins** for future key rotations.
