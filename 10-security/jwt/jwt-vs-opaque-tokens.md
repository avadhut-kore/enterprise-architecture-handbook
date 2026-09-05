# JWT vs Opaque Tokens: Architectural Trade-Off Matrix

## Executive Summary

| Architectural Dimension | Stateless JSON Web Tokens (JWT) | Stateful Opaque Tokens (Reference Tokens) |
| :--- | :--- | :--- |
| **Architecture Model** | Self-contained cryptographic proof | Random 256-bit UUID pointing to central session store |
| **Validation Overhead** | **Local In-Memory**: Sub-millisecond CPU check | **Remote Network Call**: 5–20 ms call to Redis/Database |
| **Revocation Capability** | **Difficult**: Token remains valid until `exp` timestamp | **Instantaneous**: Delete session record from Redis |
| **Bandwidth / Payload Size**| Large (500 bytes – 2 KB per HTTP header) | Compact (32–64 bytes per HTTP header) |
| **Availability Coupling** | Decoupled from central session databases | Tightly coupled to central session store availability |
| **Enterprise Recommendation**| Internal high-throughput microservices | Public-facing browser sessions & administrative consoles |
