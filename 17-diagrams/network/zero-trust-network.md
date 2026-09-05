# Zero-Trust Network Microsegmentation Architecture

Replaces perimeter security with identity-aware proxies, strict mutual TLS (mTLS), and cryptographic identity enforcement.

```mermaid
flowchart LR
    subgraph Untrusted["External & Employee Networks"]
        User["Remote Employee / Partner"]
        Device["Corporate Laptop (mTLS + CrowdStrike)"]
    end

    subgraph ZTNA_Edge["Zero-Trust Policy Enforcement Point (PEP)"]
        IAP["Identity-Aware Proxy (Zscaler / Cloudflare Access)"]
        PolicyEngine["Policy Decision Point (PDP)
[Device Posture + Okta MFA + GeoIP]"]
    end

    subgraph InternalMesh["Internal Service Mesh (Envoy / Istio)"]
        subgraph PodA["Service A (Fronting Pod)"]
            SidecarA["Envoy Sidecar Proxy (SPIFFE mTLS)"]
            AppA["App Process"]
        end

        subgraph PodB["Service B (Internal Core)"]
            SidecarB["Envoy Sidecar Proxy (SPIFFE mTLS)"]
            AppB["App Process"]
        end
    end

    User --> Device --> IAP
    IAP --> PolicyEngine
    PolicyEngine -->|Authorize Session| IAP
    IAP -->|Encrypted Tunnel (WireGuard/TLS)| SidecarA
    SidecarA --> AppA
    AppA --> SidecarA
    SidecarA == Strict mTLS with Peer Auth ==> SidecarB
    SidecarB --> AppB
```
