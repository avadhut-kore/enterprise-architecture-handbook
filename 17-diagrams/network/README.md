# Enterprise Network Diagrams & Topologies

Network diagrams define **traffic flow, subnet boundaries, IP allocation schemas, routing tables, and security perimeters** across on-premises, cloud, and hybrid infrastructures.

## Core Network Topologies Covered
1. **Cloud Virtual Networks**: VPC/VNet architectures, public vs private subnets, NAT gateways, and route tables.
2. **Enterprise Hub-and-Spoke**: Centralized transit routing (AWS Transit Gateway / Azure Virtual WAN) with shared ingress/egress firewalls.
3. **Hybrid & Inter-Cloud Connectivity**: DirectConnect, ExpressRoute, IPSec VPN, and SD-WAN fabrics.
4. **Zero-Trust Network Access (ZTNA)**: Microsegmentation, software-defined perimeters, and service mesh mTLS overlay networks.
5. **Kubernetes CNI Networking**: Pod CIDR allocations, NodePort routing, ClusterIP service discovery, and NetworkPolicies.
6. **Perimeter Defense & Ingress/Egress**: Cloud edge WAFs, Next-Gen Firewalls (NGFW), DMZ routing, and Private Endpoints (PrivateLink).

---

## Directory Contents
- [`basic-enterprise-network.md`](./basic-enterprise-network.md) — Standard dual-zone perimeter network.
- [`three-tier-network.md`](./three-tier-network.md) — Web, App, and DB subnet isolation.
- [`vpc-vnet.md`](./vpc-vnet.md) — Multi-AZ VPC/VNet CIDR allocation and routing tables.
- [`public-private-subnet.md`](./public-private-subnet.md) — NAT gateway routing and bastion isolation.
- [`hub-spoke.md`](./hub-spoke.md) — Enterprise Hub-and-Spoke architecture.
- [`transit-network.md`](./transit-network.md) — Multi-account Transit Gateway mesh.
- [`hybrid-connectivity.md`](./hybrid-connectivity.md) — Dedicated leased lines, BGP routing, and VPN fallback.
- [`zero-trust-network.md`](./zero-trust-network.md) — Identity-aware proxy and microsegmentation.
- [`kubernetes-network.md`](./kubernetes-network.md) — Pod-to-Pod and Ingress network overlays.
- [`ingress-egress.md`](./ingress-egress.md) — Inspection VPCs and centralized outbound proxy.
- [`api-gateway-network.md`](./api-gateway-network.md) — North-South API gateway network topology.
- [`dmz.md`](./dmz.md) — Demilitarized zone with dual-tier stateful firewalls.
- [`multi-region-network.md`](./multi-region-network.md) — Inter-region VPC peering and global backbone transit.
- [`firewall.md`](./firewall.md) — Stateful packet inspection and Layer 7 deep packet inspection.
- [`private-endpoints.md`](./private-endpoints.md) — AWS PrivateLink / Azure Private Endpoints.
- [`dns.md`](./dns.md) — Split-horizon DNS and private hosted zones.
- [`load-balancing.md`](./load-balancing.md) — Layer 4 (TCP/UDP) vs Layer 7 (HTTP/HTTPS) routing.
- [`template.md`](./template.md) — Copy-pasteable network topology starter templates.
- [`checklists.md`](./checklists.md) — Network architecture review checklist.
