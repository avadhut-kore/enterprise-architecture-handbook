# Cloud Architecture & Well-Architected Review Checklist

Evaluate cloud-hosted infrastructure against the industry-standard Well-Architected pillars (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability).

---

## 1. Operational Excellence
* [ ] **Infrastructure as Code (IaC)**: Are 100% of cloud resources defined declaratively via Terraform, OpenTofu, or Pulumi? No manual ClickOps.
* [ ] **GitOps Deployment**: Are Kubernetes and application configurations reconciled automatically from Git repositories via ArgoCD or Flux?
* [ ] **Automated Rollback**: Can failed deployments automatically roll back within 60 seconds without manual operator intervention?
* [ ] **Configuration Drift Detection**: Are automated drift detection jobs scheduled to identify discrepancies between IaC code and live cloud state?

---

## 2. Security
* [ ] **Landing Zone Architecture**: Is cloud infrastructure partitioned into separate accounts/subscriptions (Management, Identity, Security, Shared Services, Workload Prod, Workload Non-Prod)?
* [ ] **Private Endpoints / PrivateLink**: Are cloud-managed services (databases, storage buckets, queues) accessed over private VPC endpoints rather than public internet IPs?
* [ ] **Strict Network Security Groups**: Are ingress rules restricted to specific CIDR blocks or security group IDs? (`0.0.0.0/0` ingress on SSH/RDP/DB strictly blocked).
* [ ] **CloudTrail / Activity Logging**: Are cloud control-plane management logs enabled in all regions and forwarded to an immutable S3 bucket?

---

## 3. Reliability & Resiliency
* [ ] **Multi-Availability Zone (Multi-AZ)**: Are all compute nodes, load balancers, and databases distributed across at least 3 distinct Availability Zones?
* [ ] **Autoscaling Tested**: Has horizontal autoscaling (Karpenter, HPA) been tested to ensure compute capacity expands within 2 minutes of traffic surges?
* [ ] **Chaos Engineering**: Have instance termination, network blackhole, and zone evacuation scenarios been simulated in staging?

---

## 4. Performance Efficiency
* [ ] **Modern Compute Architectures**: Are modern ARM-based instances (AWS Graviton, Azure Ampere) utilized for compute-intensive workloads to maximize price-performance?
* [ ] **Edge Caching & CDN**: Are static assets and cacheable API responses offloaded to global Edge/CDN points of presence (Cloudflare, AWS CloudFront)?
* [ ] **Network Latency Optimization**: Are compute pods and managed database instances co-located within the same cloud availability zone to minimize cross-AZ latency?

---

## 5. Cost Optimization (FinOps)
* [ ] **Resource Tagging**: Are 100% of resources tagged with `CostCenter`, `Environment`, `Owner`, and `Service`?
* [ ] **Rightsizing Conducted**: Have compute instances and container requests/limits been rightsized based on actual 95th percentile CPU/memory utilization?
* [ ] **Reserved Instances / Savings Plans**: Are baseline steady-state workloads covered by 1-year or 3-year Savings Plans / Reserved Instances?
* [ ] **Spot Instances for Non-Critical Workers**: Are asynchronous batch processing and worker queue consumers leveraging spot instances with graceful termination handling?
* [ ] **Egress Cost Mitigation**: Are high-volume data transfers between services kept within the same region and VPC peering to avoid inter-region bandwidth charges?
