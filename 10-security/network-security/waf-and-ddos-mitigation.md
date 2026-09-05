# WAF & DDoS Mitigation Architecture

## Executive Summary

1. **Layer 3/4 Volumetric DDoS (SYN Flood, UDP Amplification)**: Mitigated by global Anycast edge networks (Cloudflare Magic Transit, AWS Shield Advanced) capable of absorbing tens of terabits per second across distributed edge PoPs.
2. **Layer 7 Application DDoS (HTTP Floods, Slowloris)**: Mitigated by Web Application Firewalls (WAF) enforcing rate limits, JavaScript browser challenges, and IP reputation scoring.
