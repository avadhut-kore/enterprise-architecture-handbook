# Token Validation: Local (JWKS) vs Remote Introspection (RFC 7662)

## Executive Summary

Resource servers must validate incoming bearer tokens. There are two primary architectural strategies: **Local Stateless Validation** and **Remote Stateful Introspection**.

---

## 1. Comparative Architecture

```mermaid
flowchart TD
    subgraph Local ["1. Local Stateless Validation (High Scale)"]
        RS1["Resource Server"] -->|Caches Public Keys| JWKS["JWKS Endpoint"]
        RS1 -->|Validates Signature & Expiration in Memory (< 1ms)| RS1
    end
    subgraph Remote ["2. Remote Introspection (High Security)"]
        RS2["Resource Server"] -->|HTTP POST per Request (15-40ms)| AS["Authorization Server /introspect"]
        AS -->|Returns active: true/false + metadata| RS2
    end
```

---

## 2. Architectural Trade-off Matrix

| Dimension | Local Stateless Validation (JWKS) | Remote Token Introspection (RFC 7662) |
| :--- | :--- | :--- |
| **Throughput / Latency** | **Sub-millisecond** (In-memory asymmetric verification) | **High Latency** (10–50 ms network round-trip per request) |
| **Availability Dependency**| Decoupled (Survives temporary Auth Server outages) | Coupled (If Auth Server goes down, all APIs fail) |
| **Revocation Speed** | Delayed (Must wait for 15-minute token TTL to expire) | **Instantaneous** (Revocation reflected on next request) |
| **Recommended Use Case** | 95% of enterprise internal microservices | High-value banking transactions, administrative portals |
