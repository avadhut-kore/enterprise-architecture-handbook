# Virtual Private Networks (VPN) & Dedicated Cloud Interconnects

> **Domain**: `00-foundations/networking`  
> **Status**: Approved  
> **Target Audience**: Solution Architects, Network Architects, Hybrid Cloud Architects

---

## 1. Simple Explanation

A **Virtual Private Network (VPN)** creates an encrypted, private tunnel across the public internet, allowing enterprise servers in an on-premises data center to communicate securely with cloud virtual networks as if they were residing on the same local physical network.

---

## 2. IPsec Site-to-Site VPN vs. Dedicated Cloud Interconnect

In hybrid cloud architectures connecting enterprise corporate offices or data centers to AWS/Azure/GCP:

```text
┌─────────────────────────────────────────────────────────────┐
│                 IPSEC VPN VS. DEDICATED INTERCONNECT        │
├───────────────────┬─────────────────────────────────────────┤
│ SITE-TO-SITE VPN  │ DEDICATED INTERCONNECT                  │
├───────────────────┼─────────────────────────────────────────┤
│ (IPsec / IKEv2)   │ AWS Direct Connect / Azure ExpressRoute │
│ Runs over public  │ Dedicated physical fiber cross-connect  │
│ internet.         │ directly to cloud telco cages.          │
│ Inexpensive, fast │ Expensive ($$$), multi-week telco       │
│ to provision.     │ provisioning lead time.                 │
│ Bandwidth: 1.25 Gbps│ Bandwidth: 10 Gbps – 100 Gbps line-rate.│
│ Unpredictable jitter│ Deterministic sub-millisecond latency;│
│ and packet loss.  │ zero internet exposure; high SLA.       │
└───────────────────┴─────────────────────────────────────────┘
```

```mermaid
flowchart LR
    subgraph OnPrem ["Enterprise On-Premises Data Center"]
        Mainframe["Legacy SAP / Mainframe"] --> Router["Customer Gateway (CGW)"]
    end

    subgraph HybridOptions ["Hybrid Network Options"]
        Router -->|Option A: IPsec Encrypted Tunnel (Public Internet)| VGW["AWS Virtual Private Gateway (VGW)"]
        Router -->|Option B: Dedicated 10 Gbps Fiber Cross-Connect| DX["AWS Direct Connect (Private VIF)"]
    end

    subgraph Cloud ["Enterprise Cloud VPC (10.100.0.0/16)"]
        VGW --> CloudApp["Cloud Core Services"]
        DX --> CloudApp
    end
```

---

## 3. High Availability in Hybrid VPN Architectures

A single IPsec tunnel is a single point of failure (vulnerable to ISP fiber cuts or router maintenance).

### Enterprise Standard: Dual-Tunnel Active-Passive with BGP
* Provision **two distinct IPsec tunnels** terminating on geographically redundant cloud endpoints.
* Run **BGP (Border Gateway Protocol)** dynamic routing over both tunnels:
  * Primary tunnel advertises lower BGP route metrics (`AS-Path` or `MED`).
  * If the primary tunnel drops, BGP automatically reconverges and shifts traffic to the standby tunnel within **3 to 10 seconds** with zero human intervention.

---

## 4. Modern Evolution: Zero Trust Network Access (ZTNA) vs. Client VPN

Traditional Client VPNs (OpenVPN, Cisco AnyConnect) grant users full Layer-3 access to the entire corporate subnet once authenticated ("Castle-and-Moat" model). If a developer's laptop is infected with malware, the malware scans and infects the entire internal corporate network.

### The Modern Replacement: ZTNA / Identity-Aware Proxies
* Solutions like **Tailscale (WireGuard)**, **Cloudflare Access**, or **Google BeyondCorp**:
  * No Layer-3 network joining.
  * Access is granted strictly on a **per-application, per-request basis** authenticated via enterprise OIDC/Okta with device health validation.
