# Private DNS & Split-Horizon Architecture

## Executive Summary

**Split-Horizon DNS** allows an enterprise to maintain two completely separate views of the same domain name: a public view for external internet users and a private view for internal VPC workloads.

---

## 1. Split-Horizon DNS Resolution

```mermaid
graph TD
    Domain[Domain Name: api.enterprise.com]

    UserPub[External Public User] --> PubDNS[Public Authoritative DNS]
    PubDNS --> PubIP[Returns Public WAF / CDN IP: 198.51.100.50]

    AppPriv[Internal VPC Microservice] --> PrivDNS[Private Hosted Zone / Azure Private DNS]
    PrivDNS --> PrivIP[Returns Internal Private VPC IP: 10.16.10.15]
```

---

## 2. Cross-Account Private Hosted Zone Sharing

In an enterprise multi-account landing zone:
- Manage core internal domains (e.g., `corp.internal`) in a dedicated **Shared Network Account**.
- Associate the Private Hosted Zone with all workload VPCs across hundreds of child accounts via AWS RAM (Resource Access Manager) or Azure Virtual Network Links.
- Workloads resolve internal microservice endpoints across VPCs privately without traversing the public internet.
