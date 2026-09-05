# Network Segmentation and Zero-Trust Isolation

## 1. Segmentation Verification Mandate
Under PCI-DSS Requirement 11.4.5, enterprise entities must perform penetration testing and segmentation verification at least once every 6 months and after any network modification.

## 2. Technical Segmentation Controls
- **Stateful Network Firewalls**: Strict IP/Port whitelist rules blocking all non-essential traffic.
- **Software-Defined Perimeter / Microsegmentation**: Kubernetes NetworkPolicies isolating payment pods at the kernel layer (Calico / Cilium eBPF).
- **Zero Shared Infrastructure**: CDE workloads must not share virtualization clusters, Active Directory domains, or management tools with general corporate subnets.
