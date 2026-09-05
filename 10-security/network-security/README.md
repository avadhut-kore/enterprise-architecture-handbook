# Network Security Architecture (`network-security/`)

## Executive Summary

Network security provides layered traffic isolation, perimeter inspection, volumetric attack absorption, and egress data-loss prevention across enterprise cloud and hybrid topologies.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`network-segmentation-and-microsegmentation.md`](network-segmentation-and-microsegmentation.md) | Network Isolation | Subnet tiering, NACLs, Cilium eBPF microsegmentation |
| [`waf-and-ddos-mitigation.md`](waf-and-ddos-mitigation.md) | Edge Defenses | Layer 3/4 volumetric absorption vs Layer 7 WAF inspection |
| [`egress-filtering-and-data-exfiltration-defense.md`](egress-filtering-and-data-exfiltration-defense.md) | Egress Controls | NAT inspection, domain whitelisting, preventing exfiltration |
