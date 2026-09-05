# Server-Side Request Forgery (SSRF) Defense Architecture

## Executive Summary

SSRF occurs when a backend server fetches a remote resource (e.g., importing an avatar image, rendering a PDF from URL, or sending a webhook) using an attacker-controlled URL, allowing the attacker to access internal private networks or cloud metadata.

---

## 1. Multi-Layered SSRF Defense Architecture

```mermaid
flowchart TD
    User["Attacker Submits URL:<br/>'http://169.254.169.254/latest/meta-data/'"] --> App["Application Server"]
    App --> Proxy["Dedicated Egress Proxy (Squid / Envoy)"]
    
    subgraph EgressRules ["Forward Proxy Inspection Rules"]
        R1["1. Parse Destination IP via Secure DNS Resolver"]
        R2["2. DENY Private RFC 1918 Ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)"]
        R3["3. DENY Cloud Metadata IP (169.254.169.254 / fe80::/10)"]
        R4["4. DENY Loopback (127.0.0.1 / ::1)"]
        R5["5. Enforce Scheme Whitelist (Strictly http:// and https://)"]
    end
    Proxy --> EgressRules

    EgressRules -->|Blocked| Drop["Connection Dropped (HTTP 403 Forbidden)"]
    EgressRules -->|Passed Whitelist| PublicInternet["Public Web Server"]
```

### Additional Infrastructure Hardening:
- **Mandate AWS IMDSv2**: Enforce `HttpTokens=required` and `HttpPutResponseHopLimit=1` on all EC2 instances, preventing containers from reaching the metadata service.
