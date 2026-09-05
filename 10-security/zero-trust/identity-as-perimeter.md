# Identity as the Primary Perimeter

## Executive Summary

In a cloud-native, distributed architecture, physical network boundaries (VPNs, corporate IP ranges) are obsolete. An attacker who gains physical or network access to an internal subnet has zero trust or privilege.

---

## Architectural Tenets
1. **Network Blindness**: Microservices must not trust any connection based on the source IP address.
2. **Cryptographic Identity on Every Packet**: Every request must carry an authenticated identity: an mTLS X.509 certificate for transport, and an OIDC JWT for application authorization.
3. **Continuous Re-Authorization**: Authorization is not evaluated once at the perimeter; it is evaluated at every microservice hop along the request path.
