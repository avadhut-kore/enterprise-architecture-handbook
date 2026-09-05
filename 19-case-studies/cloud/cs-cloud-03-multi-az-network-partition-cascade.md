# Case Study: Multi-AZ Network Partition Cascade & Synchronous Lockup

> **Metadata**: ID: `CS-CLOUD-03` | Domain: Cloud Infrastructure / Resilience | Type: Synthetic Forensic Case Study | Complexity: Advanced

---

## 01. Executive Summary
An omnichannel retail e-commerce platform processing $2.5B in annual gross merchandise value suffered an 8-hour catastrophic checkout outage across North America. Although the architecture was designed to be "highly available" by distributing container pods across three AWS Availability Zones (`us-east-1a`, `us-east-1b`, `us-east-1c`), the application design relied on **synchronous cross-AZ remote procedure calls (RPCs)** for every shopping cart mutation. When a fiber cut in Northern Virginia introduced 12% packet loss and elevated latency on cross-AZ links connecting `us-east-1a`, the synchronous call chains locked up. Rather than gracefully isolating the degraded zone, the platform suffered a **Cascading Multi-AZ Deadlock**, exhausting thread pools in all three zones and taking down the entire storefront.

---

## 02. Business & System Context
- **Organization**: Omnichannel Retail E-Commerce Enterprise ($2.5B Annual GMV).
- **Core Architecture**: Microservices deployed across 3 Availability Zones on Amazon EKS.
- **Scale**: 35,000 checkout requests/minute during peak promotional windows.

---

## 03. Scope & Stakeholders
- **Incident Commander**: Lead Cloud Reliability Architect.
- **Key Teams**: Core Checkout Engineering, Cloud Networking SRE, Storefront Operations.
- **Impacted Systems**: Shopping Cart Service, Payment Gateway, Inventory Reservation Engine.

---

## 04. Requirements & NFRs
- **Zonal Blast Radius Isolation**: A failure or degradation in a single Availability Zone must *never* impact availability in healthy AZs (**Zonal Independence**).
- **Checkout Latency**: P99 $< 200\text{ ms}$.
- **Availability Target**: 99.99% uptime during holiday shopping promotions.

---

## 05. Constraints & Assumptions
- **The "Multi-AZ is Inherently Resilient" Fallacy**: The architecture team assumed that simply deploying Kubernetes pods across 3 AZs automatically conferred high availability, ignoring that cross-AZ synchronous dependencies bind the fate of all zones together.

---

## 06. Architecture Before: The Cross-AZ Synchronous Web
```mermaid
graph TD
    Client[Shopper] --> ALB[Application Load Balancer: Round Robin across AZs]
    
    subgraph AZ 1: us-east-1a (DEGRADED AZ: 12% Packet Loss)
        PodA[Checkout Pod A]
        DB_A[(Aurora Replica A)]
    end
    
    subgraph AZ 2: us-east-1b (Healthy AZ)
        PodB[Cart Pod B]
        DB_B[(Aurora Primary B)]
    end
    
    subgraph AZ 3: us-east-1c (Healthy AZ)
        PodC[Inventory Pod C]
    end
    
    ALB --> PodA
    PodA -->|Synchronous HTTP across AZ Boundary! (Degraded Link)| PodB
    PodB -->|Synchronous HTTP across AZ Boundary! (Degraded Link)| PodC
    
    Note[Single Degraded AZ Link Freezes Threads across ALL THREE AZs!]
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **Cross-AZ Round-Robin Load Balancing** | Maximized compute utilization and even distribution across pods. | Every request crossed AZ boundaries multiple times; a single degraded AZ link degraded 100% of end-user transactions. |
| **Unbounded HTTP Client Timeouts (Default 60s)** | Prevented premature failures during heavy database writes. | Threads blocked for 60 seconds waiting for packet-loss retries; exhausted all Tomcat and Envoy worker threads in healthy AZs. |

---

## 08. Timeline
```mermaid
timeline
    title Multi-AZ Cascade Timeline
    14:00 UTC : Municipal construction severs redundant metro fiber conduit in Northern Virginia
    14:02 UTC : AWS intra-AZ networking between `us-east-1a` and other AZs reports 12% packet loss
    14:04 UTC : Checkout service latency jumps from 85ms to 12,500ms
    14:08 UTC : HTTP worker thread pools saturate in healthy zones (`us-east-1b` and `us-east-1c`)
    14:15 UTC : Kubernetes readiness probes fail across all 3 zones; pods enter crash-loop
    15:30 UTC : SREs attempt manual AZ eviction; ALB configuration change fails due to API timeouts
    22:00 UTC : Fiber repaired by telecom provider; system automatically stabilizes after 8 hours
```

---

## 09. Incident Event
At 14:00 UTC, a physical backhoe severed underground fiber optic bundles in Ashburn, Virginia, degrading internal AWS transit links connecting `us-east-1a` to `us-east-1b` and `us-east-1c`. Because the application architecture was designed as a distributed web where a service in AZ-A made synchronous REST calls to dependencies in AZ-B and AZ-C, the probability of a transaction crossing the degraded link was over **92%** ($1 - (1/3)^3$). Synchronous TCP connections retransmitted packets repeatedly, stretching request durations from 85ms to 12.5 seconds. Thread pools in healthy AZs completely exhausted. Instead of the failure being isolated to the 33% of compute in AZ-A, **100% of checkout traffic collapsed across all three zones**.

---

## 10. Symptoms & Evidence
- **Fact**: CloudWatch metrics showed `us-east-1b` and `us-east-1c` compute instances running at 100% CPU thread-wait state despite having zero local networking degradation.
- **Fact**: End-to-end checkout success rate dropped from 99.98% to **4.2%** globally.
- **Inference**: High availability cannot be achieved by spreading compute across AZs if synchronous dependencies span cross-AZ network boundaries.

---

## 11. Failure Forensics
```
[User initiates checkout -> Assigned to Pod in Healthy us-east-1b]
                               │
                               ▼
[Pod in 1b makes synchronous call to Inventory Svc in Degraded 1a]
                               │
                               ▼
[12% Packet Loss causes TCP Retransmission Storm (RTT climbs to 2.8s)]
                               │
                               ▼
[Pod in 1b holds Tomcat thread open for 60 seconds waiting for response]
                               │
                               ▼
[Thousands of incoming shoppers exhaust thread pool in Healthy us-east-1b]
                               │
                               ▼
[Healthy AZ-1b crashes -> Healthy AZ-1c crashes -> TOTAL MULTI-AZ COLLAPSE]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why did the checkout service fail across all AZs?** -> All worker thread pools were exhausted waiting for remote network responses.
2. **Why were threads waiting so long?** -> Inter-service network calls crossed an Availability Zone boundary suffering 12% packet loss.
3. **Why did services call across AZ boundaries?** -> Pods randomly distributed inter-service calls across all AZs using round-robin load balancing.
4. **Why was traffic not confined to the local AZ?** -> The architecture lacked **Zonal Routing (Cellular Zonal Independence)**.
5. **Why was the degraded AZ not evicted automatically?** -> SRE teams lacked automated **AZ-Level Health Probing and Evacuation Guardrails**.

---

## 13. Contributing Factors
- **Coarse Health Checks**: Health checks probed local pod status (`/healthz`) rather than cross-AZ link latency, reporting pods as "healthy" while they were functionally paralyzed.
- **Missing Circuit Breakers**: Inter-service calls lacked aggressive circuit breaking; requests continued hammering the degraded zone.

---

## 14. Architecture After: Zonal Independence & Automated AZ Evacuation
```mermaid
graph TD
    Client[Shopper] --> Route53[Route 53 ARC: Zonal Shift Controller]
    
    subgraph Fully Autonomous Zone 1 (Cell 1)
        ALB_A[ALB Zone A] --> Web_A[Web Pod A]
        Web_A -->|LOCAL AZ CALL ONLY!| Cart_A[Cart Pod A]
        Cart_A -->|LOCAL AZ CALL ONLY!| DB_A[(Aurora Replica A)]
    end
    
    subgraph Fully Autonomous Zone 2 (Cell 2)
        ALB_B[ALB Zone B] --> Web_B[Web Pod B]
        Web_B -->|LOCAL AZ CALL ONLY!| Cart_B[Cart Pod B]
        Cart_B -->|LOCAL AZ CALL ONLY!| DB_B[(Aurora Primary B)]
    end
    
    Route53 -.->|AUTOMATED ZONAL SHIFT: Evacuates Zone A in < 60s!| ALB_B
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: SREs manually updated Route 53 DNS routing policies to stop sending traffic to `us-east-1a` IP addresses.
- **Permanent Architectural Fix**:
  - **Zonal Independence (Cellular Alignment)**: Redesigned the microservices architecture into **Strict Zonal Cells**. A request arriving in AZ-B *only* calls services and databases residing physically within AZ-B. Cross-AZ network hops are eliminated from the synchronous transactional path.
  - **Automated Zonal Shift (AWS Route 53 ARC)**: Deployed **Amazon Route 53 Application Recovery Controller (ARC)**. If synthetic canary latency in any AZ exceeds 500ms, the control plane automatically triggers a **Zonal Shift**, evicting the unhealthy AZ from DNS in $< 60\text{ seconds}$.
  - **Tightened Circuit Breakers**: Configured Resilience4j circuit breakers on all inter-service clients: failure threshold set to 50% over 5 seconds; timeout capped at **1,500ms**.

---

## 16. Business & Technical Impact
- **Financial**: $18M in lost sales during peak weekend shopping; $1.2M in customer compensation vouchers issued.
- **Resilience Verification**: Simulated complete fiber isolation of an AZ in staging: Route 53 ARC successfully evacuated 100% of traffic to remaining healthy AZs in **42 seconds with zero customer transaction loss**.

---

## 17. What Went Well
- Aurora PostgreSQL storage nodes in the healthy AZs maintained data durability throughout the incident without split-brain or data corruption.
- Customer support routing remained functional, allowing communication with stranded online shoppers.

---

## 18. Lessons Learned
- **Architecture**: Multi-AZ deployments that make cross-AZ synchronous calls do not have 3-AZ availability; they have $1/3$ the availability of a single AZ because they are vulnerable to failure in *any* of the three zones.
- **Zonal Autonomy**: Keep traffic local to the Availability Zone. A zone must be a self-contained island.

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Configure Envoy / Kubernetes service topology routing to prefer local AZ | Platform SRE | 95% local-AZ routing |
| **60 Days** | Deploy Route 53 Application Recovery Controller (ARC) for automated Zonal Shift | Cloud Arch | $< 60	ext{s}$ AZ evacuation |
| **90 Days** | Conduct Chaos Engineering GameDay severing intra-AZ network connectivity | QA Lead | Zero cross-zone deadlocks |
