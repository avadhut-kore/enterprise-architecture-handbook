# Zero Trust Architecture (`zero-trust/`)

## Executive Summary

Zero Trust (NIST SP 800-207) is an architectural model premised on the principle: **"Never trust, always verify."** It treats all network traffic—whether originating from the public internet or an internal corporate subnet—as untrusted.

---

## Key Guides in this Directory

| Guide | Scope | Core Principle |
| :--- | :--- | :--- |
| [`zero-trust-architecture-principles.md`](zero-trust-architecture-principles.md) | Core Foundations | NIST SP 800-207 tenets, Policy Decision Point (PDP) |
| [`identity-as-perimeter.md`](identity-as-perimeter.md) | Identity Perimeter | Moving from IP firewalls to cryptographic identity |
| [`device-posture-and-context.md`](device-posture-and-context.md) | Contextual Access | EDR health checks, disk encryption, compliance validation |
| [`microsegmentation-and-service-mesh.md`](microsegmentation-and-service-mesh.md) | East-West Defense | mTLS service mesh, Cilium eBPF network policies |
| [`zero-trust-implementation-roadmap.md`](zero-trust-implementation-roadmap.md) | Migration Journey | 4-Stage enterprise migration from legacy perimeter |
