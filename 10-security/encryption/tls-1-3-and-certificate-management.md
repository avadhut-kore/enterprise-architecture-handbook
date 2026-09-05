# TLS 1.3 Architecture & Forward Secrecy

## Executive Summary

TLS 1.3 (RFC 8446) redesigns the transport handshake:
1. **1-RTT Handshake**: Cuts connection establishment latency by 50% compared to TLS 1.2.
2. **Mandatory Perfect Forward Secrecy (PFS)**: Completely eliminates static RSA key exchange. Even if an attacker compromises the server's private certificate in the future, they cannot retroactively decrypt recorded network traffic.
3. **Approved Cipher Suites**: Restricts ciphers strictly to authenticated AEAD algorithms (`TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`).
