# Enterprise Secrets Management for Integration Systems

## 1. The Zero Hardcoded Secrets Mandate
Integration components (iPaaS, ESB, connectors, microservices) must never store credentials, database passwords, private keys, or API secrets in source code, configuration files, environment variables, or container images.

## 2. Dynamic Secret Architecture (HashiCorp Vault / AWS Secrets Manager)

```
[Integration Worker Pod] 
       │ (1) Authenticates via Kubernetes ServiceAccount Token
       ▼
[Vault Server / Cloud Secrets Engine]
       │ (2) Dynamically provisions ephemeral DB credentials (TTL = 1 hour)
       ▼
[Integration Worker Pod] ──(3) Connects to Oracle/PostgreSQL DB using short-lived credentials
```

## 3. Key Operational Rules
- **Automated Rotation**: Any long-lived API key must be rotated automatically without downtime via blue-green secret rotation.
- **Audit Logging**: Every secret read operation must generate a tamper-evident audit record logged to an external SIEM.
- **Fail-Secure Caching**: Cache secrets in memory with a short TTL (e.g., 5 minutes) to withstand brief secrets vault outages, but purge memory immediately on process shutdown.
