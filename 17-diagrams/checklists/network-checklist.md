# Network Diagram Architecture Checklist

- [ ] Are all VPC CIDR blocks explicitly labeled and non-overlapping with on-premises ranges?
- [ ] Are public, private, and restricted database subnets strictly segregated?
- [ ] Are internet egress paths routed through redundant NAT Gateways or inspection proxies?
- [ ] Are private endpoints (AWS PrivateLink / Azure Private Link) used for managed PaaS connectivity?
- [ ] Are Next-Gen Firewall (NGFW) or WAF inspection points clearly identified?
