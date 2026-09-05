# Partner & Multi-Tenant SaaS Identity Federation

## Executive Summary

Multi-tenant B2B SaaS platforms must federate with hundreds of customer identity providers (Okta, Entra ID, Ping) without manual code changes or redeployments.

---

## 1. Dynamic IdP Discovery (Home Realm Discovery)

1. **Email Domain Routing**: User enters `alice@acme-corp.com`. The frontend extracts `acme-corp.com`, queries the SaaS directory, identifies that Acme Corp uses Okta, and automatically redirects Alice to `https://acme.okta.com`.
2. **Dedicated Tenant Vanity URLs**: User navigates directly to `https://acme.saasplatform.com`, which automatically initiates an SP-initiated SAML/OIDC flow with Acme's pre-configured IdP.
