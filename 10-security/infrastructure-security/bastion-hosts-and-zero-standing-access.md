# Bastion Hosts & Zero Standing Access (SSM / Teleport)

## Executive Summary

Traditional SSH bastion jump hosts require open inbound port 22, public IP addresses, and long-lived SSH private keys—creating an attractive target for attackers.

---

## 1. Modern Bastion Replacement Architecture
1. **AWS Systems Manager (SSM) Session Manager**:
   - Zero open inbound ports; zero public IP addresses.
   - Outbound-only TLS agent connects to AWS control plane.
   - Interactive sessions authenticated via Okta SSO and logged to S3/CloudWatch.
2. **Identity-Aware Proxies (Teleport / Cloudflare Access)**:
   - Ephemeral, short-lived SSH certificates issued dynamically after FIDO2 MFA and device posture checks.
