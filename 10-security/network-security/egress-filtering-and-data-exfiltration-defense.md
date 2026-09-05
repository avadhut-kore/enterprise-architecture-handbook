# Egress Filtering & Data Exfiltration Defense

## Executive Summary

Most security breaches involve data exfiltration over outbound internet connections (e.g., an attacker uploads a database dump to an external S3 bucket or connects to an external Command & Control server).

---

## Architectural Mandates
1. **Zero Open Outbound Internet**: Private subnets must not have unconstrained outbound access (`0.0.0.0/0`) through a simple NAT gateway.
2. **Next-Generation Egress Firewall**: Route all outbound traffic through an egress proxy (AWS Network Firewall / Palo Alto) that enforces **TLS SNI domain whitelisting** (e.g., only permitting outbound traffic to `api.github.com` and `pypi.org`).
