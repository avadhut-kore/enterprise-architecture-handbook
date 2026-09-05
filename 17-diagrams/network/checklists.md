# Network Architecture Review Checklist

- [ ] Are IP CIDR blocks non-overlapping across all interconnected cloud VPCs and on-premises subnets?
- [ ] Are routing tables explicit, with default 0.0.0.0/0 egress directed through controlled firewalls?
- [ ] Are database and data stores isolated in subnets with zero Internet Gateway routes?
- [ ] Is East-West traffic between sensitive applications controlled by microsegmentation or firewalls?
- [ ] Are private endpoints (PrivateLink) leveraged for managed cloud services to prevent public transit?
