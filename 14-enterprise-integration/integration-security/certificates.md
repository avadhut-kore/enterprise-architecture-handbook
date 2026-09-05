# Public Key Infrastructure (PKI) for Enterprise Integration

## 1. Enterprise PKI Hierarchy

```
                 [Root Offline CA] (Air-gapped, HSM backed)
                         │
        ─────────────────┴─────────────────
        │                                 │
 [Intermediate CA: Internal Workloads]  [Intermediate CA: External Partners]
        │                                 │
 [API Gateway / Service Mesh Certs]     [B2B Partner Webhook Certs]
```

## 2. Certificate Architecture Rules
1. **Never Trust Public Commercial CAs for Internal Routing**: Internal microservices must only trust the private enterprise root CA.
2. **Short Certificate Lifespans**: Internal service mesh certificates must have a maximum lifetime of 24 to 72 hours, rotated automatically via SPIFFE/SPIRE or cert-manager.
3. **Automated Monitoring**: Prometheus and Datadog monitors must alert 30 days, 14 days, and 7 days prior to any intermediate or partner certificate expiration.
