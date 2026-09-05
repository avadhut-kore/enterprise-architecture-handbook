# Secure by Default Architecture

## Executive Summary

**Secure by Default** mandates that all software components, infrastructure modules, and cloud services ship and deploy in their most restrictive, secure state out of the box. Security controls must not require manual opt-in by engineers.

---

## 1. Core Architectural Defaults

| Dimension | Insecure Default (Prohibited) | Secure by Default (Mandated) |
| :--- | :--- | :--- |
| **Network Ports** | All ports open; engineer closes unwanted ports | Zero ports open; explicit ingress firewall rules required per port |
| **Database Encryption**| Plaintext storage; encryption enabled via optional flag | Transparent Data Encryption (TDE) and EBS encryption enforced globally by policy |
| **Cloud Storage** | Public read allowed; engineer enables private ACL | Cloud Account-level "Block Public Access" enabled by default via SCP |
| **HTTP Transport** | HTTP allowed; HTTPS optional | HSTS header enforced; port 80 requests permanently dropped or 301 redirected |
| **Session Lifetime** | Infinite or 30-day session cookies | Short-lived 15-minute access tokens; explicit refresh required |
| **Error Handling** | Detailed stack traces returned to client | Generic error code returned to client; full stack trace logged to secure telemetry |
| **CORS Policy** | `Access-Control-Allow-Origin: *` | CORS disabled by default; explicit whitelist of exact domain origins required |
| **Container User** | Container runs as `root` (UID 0) | Container runs as unprivileged user (`USER 10001`); root execution blocked |
