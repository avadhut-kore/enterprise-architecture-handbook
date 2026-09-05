# DNS Fundamentals: Authoritative vs Recursive & Record Types

## Executive Summary

Understanding DNS query mechanics and record type behaviors is essential for architecting resilient routing systems.

---

## 1. The DNS Query Lifecycle

```mermaid
graph LR
    Client[Client App] -->|Query: api.company.com| Rec[Recursive Resolver: 8.8.8.8]
    Rec --> Root[Root Nameserver '.']
    Rec --> TLD[TLD Nameserver '.com']
    Rec --> Auth[Authoritative Nameserver: ns1.awsdns.com]
    Auth -->|Returns IP: 198.51.100.25 (TTL 60s)| Rec
    Rec --> Client
```

---

## 2. Critical DNS Record Types

- **`A` Record**: Maps a domain name directly to an IPv4 address.
- **`AAAA` Record**: Maps a domain name to an IPv6 address.
- **`CNAME` Record**: Maps a domain name to another domain name. Cannot exist at the zone apex (`company.com`).
- **`ALIAS` / Cloud Route Records (AWS Route 53 / Azure DNS)**: Cloud-proprietary virtual records that allow mapping the **zone apex** (`company.com`) directly to cloud resources (ALBs, CloudFront distributions) while responding directly with `A` records to avoid recursive CNAME lookup latency.
