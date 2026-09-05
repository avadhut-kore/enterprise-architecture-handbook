# Platform as a Product: Customer-Centric Engineering

The single greatest reason internal developer platforms fail is treating the platform as an infrastructure mandate rather than a product consumed by internal customers.

## 1. The Platform Anti-Pattern: The Centralized Ticket Queue

```
DEVELOPER SQUAD ──► File Jira Ticket ──► PLATFORM TEAM (Overwhelmed Ticket Queue)
                                                  │
                                                  ▼ (2-3 Weeks Waiting Time)
                                          Provision Database / SQS / IAM Role
Result: Platform team becomes the organizational bottleneck; shadow IT flourishes.
```

## 2. The Platform as a Product Paradigm

```
DEVELOPER SQUAD ──► Self-Service Portal (Backstage) ──► Instant Automated Provisioning
                                                                  ▲
                                                                  │
                                                        PLATFORM PRODUCT TEAM
                                                        - Interviews developers
                                                        - Measures DevEx metrics
                                                        - Builds self-service APIs
```

## 3. Core Product Management Rituals
1. **Developer User Research**: Interview senior and junior developers to uncover friction points (e.g., "Local environment setup takes 3 days").
2. **Net Promoter Score (Dev-NPS)**: Survey internal developers quarterly on platform satisfaction.
3. **Opt-In Adoption over Mandates**: A golden path should be so easy and fast that teams adopt it voluntarily. If teams must be forced by decree, the platform has failed.

## Related Resources
- [Internal Developer Platform Architecture](./internal-developer-platform-architecture.md)
- [Golden Paths](./golden-paths-and-service-templates.md)
