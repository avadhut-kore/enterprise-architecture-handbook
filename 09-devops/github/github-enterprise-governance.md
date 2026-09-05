# GitHub Enterprise Governance

Managing 100+ repositories and thousands of engineers requires centralized governance that enforces security without creating bureaucratic friction.

## 1. Enterprise Hierarchy & Identity Integration

```
┌─────────────────────────────────────────────────────────────┐
│                    ENTERPRISE ACCOUNT                       │
│    Enforces Global Policies, Billing, and Security Defaults │
├──────────────────────────────┬──────────────────────────────┤
│      CORE PLATFORM ORG       │      CONSUMER PRODUCT ORG    │
│  - IAM synced via Okta / Entra│  - IAM synced via Okta / Entra│
│  - SAML SSO + SCIM provisioning│ - SAML SSO + SCIM provisioning│
│  - Internal visibility default│  - Internal visibility default│
├──────────────────────────────┴──────────────────────────────┤
│                    AUDIT LOG STREAMING                      │
│      Real-time SIEM forwarding to Splunk / Datadog / S3     │
└─────────────────────────────────────────────────────────────┘
```

## 2. Mandatory Enterprise Defaults
1. **Default Repository Visibility**: `Internal` (Accessible across the enterprise for inner-sourcing; never `Public`).
2. **Repository Creation**: Restricted to automated scaffolding portals (Backstage) or designated admins.
3. **Audit Log Streaming**: Real-time export of all repository permission changes, token creations, and SSH key additions to enterprise SIEM.

## Related Resources
- [GitHub Actions Architecture](./github-actions-architecture.md)
- [Source Control Governance](../source-control-governance/README.md)
