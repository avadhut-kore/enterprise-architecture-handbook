# Case Study: Unauthenticated Kubernetes Kubelet Exploit & Monero Cryptomining

> **Metadata**: ID: `CS-SEC-05` | Domain: Security / Cloud Native | Type: Synthetic Forensic Case Study | Complexity: Advanced

---

## 01. Executive Summary
A digital marketing enterprise managing a self-hosted Kubernetes cluster (250 EC2 instances) experienced an infrastructure takeover by an automated cryptomining botnet. The vulnerability was an architectural networking misconfiguration: the Kubelet API port (**TCP 10250**) on worker nodes was exposed directly to the public internet without an external security group boundary, and the Kubelet configuration had **`authentication.anonymous.enabled = true`**. An automated Shodan scanner detected the open unauthenticated API, executed arbitrary remote commands via the Kubelet `exec` endpoint, and deployed an unauthorized Monero cryptomining DaemonSet across all 250 worker nodes. The cluster ran at 100% CPU for 14 days, generating a **$350,000 surprise cloud compute bill**.

---

## 02. Business & System Context
- **Organization**: Global Digital Marketing & AdTech Enterprise ($80M Revenue).
- **Infrastructure**: Self-Managed Kubernetes Cluster (250 AWS EC2 `c5.9xlarge` compute instances).
- **Workload**: Batch Ad Impression Processing, Machine Learning Attribution, and Web Analytics.

---

## 03. Scope & Stakeholders
- **Incident Commander**: Lead Platform Security Architect.
- **Key Teams**: Cloud Infrastructure SRE, Platform Engineering, FinOps Committee.
- **External Dependencies**: AWS Cloud Security Incident Response Team (SIRT).

---

## 04. Requirements & NFRs
- **Zero Public Attack Surface**: Zero administrative or control-plane ports exposed to the public internet.
- **Mutual TLS Enforcement**: 100% of internal Kubernetes cluster communication authenticated via mTLS.
- **Workload Admission Governance**: Block deployment of any container images not originating from trusted enterprise registries.

---

## 05. Constraints & Assumptions
- **The "VPC is Private" Fallacy**: The infrastructure team used a home-grown Terraform script that attached public IPv4 addresses to worker nodes in public subnets, assuming that "nobody knows our IP addresses" was sufficient security.

---

## 06. Architecture Before: The Exposed Kubelet API
```mermaid
graph TD
    Scanner[Automated Shodan Scanner / Attacker] -->|Port 10250 Open to Public 0.0.0.0/0!| Kubelet[Worker Node Kubelet: Port 10250]
    
    subgraph Unauthenticated Kubelet Worker Node (Vulnerable)
        Kubelet --> Config[Kubelet Config: anonymous.enabled = true!]
        Kubelet --> ExecAPI[POST /run/{pod}/{container}: Remote Code Execution!]
        ExecAPI --> RootCompromise[Host Escape & Root Docker Socket Access]
    end
    
    RootCompromise --> Miner[Deploys Monero XMRig Cryptominer DaemonSet]
    Miner --> SaturatedCluster[250 Worker Nodes Pegged at 100% CPU for 14 Days!]
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **Worker Nodes in Public Subnets with Public IPs** | Allowed easy direct SSH access for developers without setting up a VPN or Bastion Host. | Exposed internal cluster administration ports (Kubelet 10250, NodePort ranges) directly to the global internet. |
| **Default Kubelet Anonymous Authentication** | Avoided configuring client certificates between the API server and Kubelet during manual cluster bootstrap. | Anyone who can reach port 10250 over TCP possesses full administrative remote execution rights inside all running containers on the node. |

---

## 08. Timeline
```mermaid
timeline
    title Cryptomining Takeover Timeline
    Day 1, 02:15 : Automated mass-internet scanner identifies open TCP port 10250 on worker node
    Day 1, 02:18 : Bot scripts verify anonymous execution via `POST /run/kube-system/...`
    Day 1, 02:30 : Bot deploys lightweight bash script installing XMRig Monero miner as DaemonSet
    Day 1, 03:00 : All 250 worker nodes (9,000 CPU cores) begin mining cryptocurrency at 100% CPU
    Day 7        : Ad analytics batch jobs take 8x longer to complete; engineering assumes "data growth"
    Day 14       : AWS Account Representative calls CFO regarding sudden $350k compute spend anomaly
    Day 14       : Forensic investigation confirms cluster compromise; cluster terminated
```

---

## 09. Incident Event
An automated threat-actor botnet scanning public IPv4 ranges for port 10250 discovered the enterprise's Kubernetes worker nodes. Because the nodes had been provisioned with public IP addresses and an AWS Security Group rule allowing `0.0.0.0/0` on all ports, the scanner reached the Kubelet directly. Finding `anonymous-auth` enabled, the bot issued an HTTP POST request to `/run/kube-system/kube-proxy/kube-proxy` executing a base64-encoded shell script. The script mounted the host root filesystem (`/`), escalated to root privileges, and spawned containerized **XMRig Monero cryptominers** across all 250 servers. The cluster consumed 9,000 CPU cores at 100% capacity for two weeks before the monthly cloud billing anomaly was detected.

---

## 10. Symptoms & Evidence
- **Fact**: CloudWatch CPU utilization metrics across all 250 EC2 instances showed a flat horizontal line at **99.8% CPU** for 14 consecutive days.
- **Fact**: Outbound firewall logs showed persistent encrypted Stratum mining protocol connections to mining pools (`xmr-pool.supportxmr.com:3333`).
- **Inference**: High-compute infrastructure without automated billing anomaly alerts or admission control guardrails can be hijacked silently for profit.

---

## 11. Failure Forensics
```
[Automated Shodan Bot scans random IP: Discovers open TCP 10250]
                               │
                               ▼
[Kubelet evaluates request: authentication.anonymous.enabled == TRUE]
                               │
                               ▼
[Attacker calls Kubelet API: POST /run/{namespace}/{pod}/{container}]
                               │
                               ▼
[Shell commands execute with root permissions inside container]
                               │
                               ▼
[Mounts host /var/run/docker.sock -> Escapes to Host Operating System]
                               │
                               ▼
[Launches XMRig Monero Cryptominer across 250 Nodes (9,000 Cores)]
                               │
                               ▼
[$350,000 Cloud Compute Cost Incurred Before Detection]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why was the enterprise billed $350,000 in unexpected compute fees?** -> 250 compute instances were utilized to mine cryptocurrency for an attacker.
2. **How did the attacker deploy miners?** -> They executed remote commands via the Kubelet API on port 10250.
3. **Why did the Kubelet accept unauthenticated commands?** -> Anonymous authentication was set to `true` in `/var/lib/kubelet/config.yaml`.
4. **Why was port 10250 accessible over the public internet?** -> Worker nodes were assigned public IP addresses with permissive security groups (`0.0.0.0/0`).
5. **Why were nodes configured so insecurely?** -> The platform team rolled their own unhardened Kubernetes deployment using custom scripts rather than using managed EKS with CIS Benchmark hardening.

---

## 13. Contributing Factors
- **Absence of Admission Controllers**: The cluster lacked OPA Gatekeeper or Kyverno, which would have automatically rejected containers running as root or mounting host sockets.
- **Delayed FinOps Visibility**: Cloud billing alerts were evaluated monthly rather than via real-time daily cost anomaly detectors.

---

## 14. Architecture After: Managed EKS, Private Subnets & Kyverno Admission
```mermaid
graph TD
    Attacker[External Internet] --> IGW[Internet Gateway]
    
    subgraph Isolated Cloud VPC (Zero Public Access)
        IGW --> WAF[Cloudflare / AWS WAF]
        WAF --> ALB[Public Load Balancer]
        
        subgraph Private Worker Subnet (NO PUBLIC IPs!)
            ALB --> Node1[Worker Node 1: EKS Managed]
            Node1 --> Kubelet1[Kubelet Port 10250: Internal Only / mTLS Auth ONLY!]
            Node1 --> Kyverno[Kyverno Admission Controller: Blocks Root & HostMounts]
        end
    end
    
    Kubelet1 -.-> Drop[Public Access Physically Impossible!]
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: Terminated all 250 compromised EC2 instances; rebuilt cluster from clean GitOps repositories.
- **Permanent Architectural Fix**:
  - **Private-Only Compute Subnets**: Worker nodes are now strictly provisioned in **isolated private subnets with RFC 1918 private IPs**. Zero public IPv4 addresses assigned.
  - **Enforce Kubelet Hardening**: Configured Kubelet to enforce **x509 client certificate authentication** and disable anonymous access:
    ```yaml
    authentication:
      anonymous:
        enabled: false
      webhook:
        enabled: true
    authorization:
      mode: Webhook
    ```
  - **Kubernetes Admission Governance (Kyverno)**: Deployed **Kyverno** policies blocking any container from running with `privileged: true`, mounting `/var/run/docker.sock`, or pulling images from non-approved public registries.
  - **Real-Time FinOps Cost Anomaly Detection**: Configured AWS Cost Anomaly Detection with Slack alerts for any daily spend deviation $> 15\%$.

---

## 16. Business & Technical Impact
- **Financial**: $350,000 cloud infrastructure loss (AWS credited $150k following formal forensic proof of compromise).
- **Operational Transformation**: Abandoned bespoke self-managed Kubernetes; migrated entire container estate to managed **Amazon EKS**.
- **Security Certification**: Achieved 100% compliance with the CIS Amazon EKS Benchmark.

---

## 17. What Went Well
- Customer transactional data was isolated in dedicated RDS databases with separate security groups and was never accessed by the cryptominers.
- Rebuilding the entire cluster using Terraform and ArgoCD GitOps took under 3 hours once infrastructure scripts were corrected.

---

## 18. Lessons Learned
- **Architecture**: In cloud infrastructure, convenience is the enemy of security. Placing worker nodes in public subnets with public IPs to avoid setting up a VPN is a fatal architectural compromise.
- **Admission Control**: Kubernetes clusters without admission controllers (Kyverno / OPA) are un-governed environments where any compromised container can seize host root privileges.

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Ensure `anonymous-auth=false` on all Kubelets and isolate port 10250 | Platform SRE | Zero exposed Kubelets |
| **30 Days** | Deploy Kyverno admission policies blocking root execution and host mounts | DevSecOps | 100% pod governance |
| **60 Days** | Enable AWS Cost Anomaly Detection with immediate PagerDuty integration | FinOps Lead | Alert if spend $> 15\%$ |
