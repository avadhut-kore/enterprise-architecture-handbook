# Enterprise Directory Services & Identity Providers (IdPs)

## Executive Summary

Enterprise Identity Providers (IdPs) serve as the authoritative Single Source of Truth (SSOT) for organizational identities, authentication policies, and cross-domain trust relationships.

---

## Enterprise IdP Comparison

| Capability | Microsoft Entra ID (Azure AD) | Okta Universal Directory | HashiCorp Vault / Keycloak |
| :--- | :--- | :--- | :--- |
| **Primary Strength** | Native integration with Windows, Office 365, and Azure | Best-in-class multi-SaaS SSO, advanced adaptive MFA | On-premises, sovereign, fully open-source/self-managed |
| **Federation Protocols** | SAML 2.0, WS-Fed, OIDC, OAuth 2.0 | SAML 2.0, OIDC, WS-Fed, SCIM 2.0 | OIDC, SAML 2.0, Kerberos, LDAP |
| **Workload Identity** | Azure Managed Identities, Workload Federation | Okta Workload Identity | SPIFFE/SPIRE, Kubernetes Service Accounts |
| **Enterprise Standard** | Ideal for global enterprises with EA agreements | Ideal for SaaS-heavy, cloud-native tech platforms | Ideal for air-gapped, defense, or on-prem banking |
