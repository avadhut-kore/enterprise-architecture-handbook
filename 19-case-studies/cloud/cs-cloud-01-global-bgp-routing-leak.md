# Case Study: Global BGP Anycast Route Leak & Multi-Region Black Hole

> **Metadata**: ID: `CS-CLOUD-01` | Domain: Cloud Infrastructure / Networking | Type: Synthetic Forensic Case Study | Complexity: Expert

---

## 01. Executive Summary
A planetary-scale public cloud hyperscaler and edge CDN network experienced a 7.5-hour global outage disconnecting 42 cloud regions and knocking over 18,000 enterprise applications offline. An automated software deployment intended to update edge peering router configurations in Singapore inadvertently omitted a BGP route-filter community tag. Tier-1 transit providers propagated the hyperscaler's internal `/24` Anycast IP prefixes to the global internet. The resulting routing leak overwhelmed regional edge routers with transatlantic and transpacific transit traffic, creating an oscillatory feedback loop of BGP session resets, black-holing DNS, and costing an estimated **$42M in direct SLA breach penalty credits**.

---

## 02. Business & System Context
- **Organization**: Global Cloud Hyperscaler & Edge Infrastructure Provider.
- **Core System**: Global Edge Routing Plane terminating Anycast BGP sessions across 220 Point-of-Presence (PoP) datacenters.
- **Scale**: 45 Terabits/sec edge transit capacity; 42 cloud regions; 18,000 enterprise customers.

---

## 03. Scope & Stakeholders
- **Incident Commander**: VP of Global Network Engineering.
- **Key Teams**: Edge Peering Engineering, Core Backbone Operations, SRE Network Control Plane.
- **Impacted Systems**: Global DNS Anycast resolution, API Gateway ingress, Public Cloud Console.

---

## 04. Requirements & NFRs
- **Global Ingress Availability**: 99.999% network uptime ($< 5.26\text{ minutes}$ downtime/year).
- **Blast Radius Containment**: Network configuration pushes must be strictly confined to single regional peering cells.
- **Route Filtering**: 100% of internal cloud prefixes must be stripped before external BGP advertisement.

---

## 05. Constraints & Assumptions
- **The "BGP Automation is Safe" Assumption**: Network automation pipelines pushed updated BGP configuration maps directly to edge border gateway routers without dry-run route dampening or progressive regional canary stages.

---

## 06. Architecture Before: The Un-Canaried Edge Routing Mesh
```mermaid
graph TD
    Automation[Centralized Network Orchestrator: Auto-Push] -->|Global Push: Omitted NO-EXPORT Tag!| EdgeMesh[Global Edge Border Routers: 220 PoPs]
    
    subgraph Global BGP Mesh (Cascading Overload)
        EdgeMesh -->|Advertises Internal /24 Anycast to Tier-1 ISPs| Telia[Tier-1 Telco: Telia / Lumen / NTT]
        Telia -->|Pours 40 Tbps Global Traffic into Singapore PoP!| SingPoP[Singapore Edge PoP: Capacity 2 Tbps]
        SingPoP -->|CPU Overload & TCP Reset| Drop[Black Hole & Global BGP Flapping]
    end
    
    Drop --> Crash[Global DNS & Web Blackout across 42 Regions!]
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **Global Automated Routing Configuration Push** | Minimized configuration drift and accelerated peering turnaround. | Propagated a malformed BGP route map globally within 180 seconds; no cell-level canary verification. |
| **Missing Outbound BGP Prefix Limits** | Relied on upstream ISPs to filter invalid prefix lengths. | Upstream transit carriers accepted the more-specific `/24` prefixes, preferred them over regional aggregates, and diverted global traffic into an undersized PoP. |

---

## 08. Timeline
```mermaid
timeline
    title Global BGP Routing Outage Timeline
    14:02 UTC : Centralized deployment pipeline pushes updated BGP route policies globally
    14:04 UTC : Tier-1 telecom providers accept un-tagged internal `/24` Anycast routes
    14:06 UTC : Global internet traffic shifts aggressively toward the Singapore PoP
    14:15 UTC : Singapore border routers exhaust packet buffer queues; CPU hits 100%
    14:22 UTC : Singapore PoP drops BGP sessions; traffic shifts to Tokyo; Tokyo crashes 6 mins later
    15:30 UTC : Cascading route flapping black-holes global cloud DNS; management console unreachable
    21:30 UTC : Out-of-band console access restores route filters; BGP routes stabilize after 7.5 hours
```

---

## 09. Incident Event
At 14:02 UTC, an automated network deployment pipeline pushed an edge routing policy update. A template syntax bug omitted the `NO-EXPORT` BGP community tag on internal control-plane `/24` Anycast IP blocks. External Tier-1 telecom providers automatically preferred these specific `/24` prefixes over standard `/19` aggregates. Massive volumes of global transit traffic converged on edge routers in Southeast Asia, exceeding physical line-card buffer memory by 1,800%. Routers crashed, dropped BGP peering sessions, and caused traffic to flap violently to the next nearest PoP, initiating a domino-effect collapse across 220 PoPs globally.

---

## 10. Symptoms & Evidence
- **Fact**: Global internet routing tables recorded 12,400 rogue prefix advertisements originating from AS-XXXX within 4 minutes.
- **Fact**: Edge router control-plane CPUs saturated at 100% processing 450,000 BGP route update packets per second.
- **Inference**: Autonomous network configuration pipelines without progressive blast-radius ring deployments will inevitably cause global control-plane collapses.

---

## 11. Failure Forensics
```
[Automated Script pushes config: Missing NO-EXPORT BGP Community]
                              │
                              ▼
[Tier-1 Telcos receive and propagate specific /24 internal prefixes]
                              │
                              ▼
[Global internet routes all cloud traffic to single PoP (Singapore)]
                              │
                              ▼
[Inbound traffic (40 Tbps) overwhelms PoP hardware capacity (2 Tbps)]
                              │
                              ▼
[Hardware Buffer Queue Exhaustion -> BGP TCP Peering Sessions Terminated]
                              │
                              ▼
[Routes withdraw -> Traffic slams Tokyo PoP -> Tokyo Crashes -> CASCADING FLAP]
                              │
                              ▼
[Complete Global Outage across 42 Cloud Regions for 7.5 Hours]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why were 42 cloud regions unreachable?** -> Anycast edge routers were dropping packets and flapping BGP routes continuously.
2. **Why were edge routers flapping?** -> Routers were overwhelmed by traffic exceeding line-card hardware memory limits.
3. **Why did so much traffic hit those routers?** -> Global Tier-1 transit providers routed internet traffic toward internal Anycast IPs.
4. **Why did Tier-1 providers route traffic there?** -> Edge routers advertised internal `/24` prefixes without `NO-EXPORT` community filters.
5. **Why were bad route policies advertised?** -> A central deployment script pushed an un-canaried configuration template globally without automated route simulation or canary blast-radius boundaries.

---

## 13. Contributing Factors
- **Shared Out-of-Band Network Dependency**: The out-of-band management network utilized the same edge DNS resolution system that collapsed, preventing engineers from accessing routers remotely for 3 hours.
- **Lack of Route Flap Damping**: Upstream peering providers had disabled BGP Route Flap Damping (RFC 2439), allowing rapid route oscillation to amplify.

---

## 14. Architecture After: Cell-Based Canary Routing & Route Damping
```mermaid
graph TD
    subgraph Controlled Deployment Plane
        CD[GitOps Network Pipeline] --> Batfish[Batfish Network Simulation Engine: Validates No-Export!]
        Batfish --> CanaryPoP[Ring 0: Single Test PoP (1% Traffic)]
        CanaryPoP -->|24-Hour Soak Test Passing| Wave1[Ring 1: Regional PoP Tier]
    end
    
    subgraph Autonomous Safeguards
        Wave1 --> HardFilter[Hardware RPKI & Maximum Prefix Limit Governors]
        HardFilter --> ExternalBGP[Tier-1 Telco Peering]
        OOB[Dedicated Satellite Out-of-Band Console Access] -.-> HardFilter
    end
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: SREs utilized physical serial-over-LAN terminal servers to manually tear down BGP peering sessions on edge routers; restored baseline configurations PoP by PoP.
- **Permanent Architectural Fix**:
  - **Automated Network Simulation in CI**: Deployed **Batfish** into the network GitOps pipeline. Every configuration change is parsed and verified mathematically against formal network invariants (e.g., "internal prefixes must never be advertised to external peers").
  - **Progressive Ring Deployments (Cell-Based Routing)**: BGP routing changes are now rolled out across **4 progressive rings** (Ring 0: Isolated Test PoP, Ring 1: 5% non-critical PoPs, Ring 2: Regional Hubs, Ring 3: Global). Each ring enforces a mandatory **6-hour soak period**.
  - **Independent Out-of-Band Console Access**: Built a dedicated, completely air-gapped satellite-linked terminal network with immutable local IP routing.

---

## 16. Business & Technical Impact
- **Financial**: $42M in direct SLA breach credits; $14M in emergency consulting and remediation fees.
- **Market Perception**: Major enterprise customers demanded contractual multi-cloud redundancy clauses upon renewal.
- **Engineering Overhaul**: Transformed network operations from manual template scripts to a fully codified, unit-tested Software-Defined Network (SDN) control plane.

---

## 17. What Went Well
- Physical datacenter infrastructure (power, cooling, compute, storage) remained 100% operational throughout the routing storm.
- Customer data was never breached or corrupted; the incident was purely a network connectivity loss.

---

## 18. Lessons Learned
- **Architecture**: In global Anycast networking, there is no such thing as a "local" BGP change unless enforced by rigid architectural cell boundaries.
- **Out-of-Band Networks**: Never allow management console networks to depend on the production systems they are designed to repair.

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Mandate Batfish pre-deployment routing policy simulation in network CI | NetDevOps | Zero unverified BGP pushes |
| **60 Days** | Implement 4-ring progressive canary rollouts for all network configurations | SRE Lead | 100% ring governance |
| **90 Days** | Verify physical air-gapped out-of-band console access across all PoPs | Infra Arch | 100% independent console |
