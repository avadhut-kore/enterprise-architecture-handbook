# Decommissioning and Sunsetting Systems

A system is not finished when the replacement goes live; it is finished when the old system is completely deleted, its data archived, and its infrastructure bills cease.

## 1. The 6-Stage Sunsetting Lifecycle

```
[Announce Sunset & Deprecation Timeline]
                    │
                    ▼
[Disable New Feature Development (Read-Only Mode)]
                    │
                    ▼
[The Scream Test (Intentional Planned Brownouts)]
                    │
                    ▼
[Final Cryptographic Archive & Compliance Export]
                    │
                    ▼
[Infrastructure Teardown (Terraform Destroy)]
                    │
                    ▼
[Cost Recapture Verification & Post-Mortem]
```

## 2. The "Scream Test" Protocol
Before permanently deleting an unowned legacy service:
1. Temporarily reroute its traffic to a mock 503 response for 2 hours during low-risk hours.
2. If nobody notices or escalates, increase brownout window to 24 hours.
3. If still zero escalations, initiate final data backup and destroy the infrastructure.

## Related Modules
- [Modernization Mastery](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/modernization/legacy-modernization-mastery.md)
- [Application Portfolio Management](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/portfolio-thinking/application-portfolio-management.md)
