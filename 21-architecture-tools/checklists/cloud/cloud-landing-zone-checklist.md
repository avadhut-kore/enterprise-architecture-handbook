# Cloud Landing Zone Review Checklist

- [ ] Multi-Account hierarchy structured by business unit and environment (Core, Security, Log Archive, Workloads).
- [ ] Central Log Archive account deployed with S3 Object Lock in Compliance Mode (WORM) and MFA Delete.
- [ ] AWS Control Tower / Azure Management Groups enforcing automated preventative guardrails (SCPs / Azure Policy).
- [ ] Non-overlapping enterprise RFC 1918 CIDR IP space allocated across on-premises and cloud transit hubs.
- [ ] Centralized transit networking (Transit Gateway / Virtual WAN) deployed with dedicated inspection VPC.
- [ ] Identity Center federated with corporate Entra ID / Okta with SCIM automated user deprovisioning.
