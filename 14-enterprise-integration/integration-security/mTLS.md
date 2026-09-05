# Mutual TLS (mTLS) Architecture and Lifecycle

## 1. Core Architecture
Mutual TLS (mTLS) provides bidirectional cryptographic authentication, tamper-proofing, and encryption. In mTLS, both the client and the server present X.509 digital certificates issued by a trusted Certificate Authority (CA), verifying each other's identity before completing the TLS handshake.

```
[Integration Client]                                     [Integration Gateway]
         │                                                         │
         ├────────── (1) Client Hello ────────────────────────────>│
         │<───────── (2) Server Hello + Server Certificate ────────┤
         │<───────── (3) Certificate Request (Mandates Client Cert)┤
         ├────────── (4) Client Certificate + Key Exchange ───────>│
         ├────────── (5) Certificate Verify (Cryptographic Proof) ─>│
         │<───────── (6) Handshake Finished (Encrypted Tunnel) ────┤
         │                                                         │
         │<══════════ Application Traffic Encrypted (TLS 1.3) ═════>│
```

## 2. Certificate Lifecycle Management (CLM)

| Stage | Process | Enterprise Automation Tooling |
| :--- | :--- | :--- |
| **Key Generation** | ECDSA (P-256/P-384) or RSA 4096-bit generated in HSM/KMS | HashiCorp Vault, AWS KMS, Cloudflare Keyless |
| **CSR Signing** | Certificate Signing Request validated against enterprise CMDB | Venafi, cert-manager, Smallstep CA |
| **Distribution** | Ephemeral injection into container pods or sidecar volumes | Kubernetes CSI Secret Store, Vault Agent |
| **Validation** | OCSP Stapling, dynamic CRL polling, SAN matching | Envoy Proxy, NGINX Plus, API Connect |
| **Rotation** | Automated zero-downtime rolling renewal at 60% TTL | cert-manager automated ACME / Vault renewer |
| **Revocation** | Immediate serial revocation published to CRL/OCSP | CRL distribution point, HSM revocation hook |

## 3. High-Security Envoy Configuration
```yaml
static_resources:
  listeners:
  - name: mtls_listener
    address:
      socket_address: { address: 0.0.0.0, port_value: 8443 }
    filter_chains:
    - transport_socket:
        name: envoy.transport_sockets.tls
        typed_config:
          "@type": type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.DownstreamTlsContext
          common_tls_context:
            tls_certificates:
            - certificate_chain: { filename: "/etc/certs/server.crt" }
              private_key: { filename: "/etc/certs/server.key" }
            validation_context:
              trusted_ca: { filename: "/etc/certs/enterprise-ca.crt" }
              require_client_certificate: true
              match_typed_subject_alt_names:
              - san_type: DNS
                matcher:
                  exact: "client.payment-processor.internal"
```

## 4. Key Enterprise Traps
- **Certificates Expiring in Production**: Implement alerting at 30, 14, and 7 days prior to expiry via Prometheus metrics (`x509_cert_expiry`).
- **Intermediate CA Chaining Failures**: Always include the full bundle of intermediate certificates in the server response; clients must only need the root in their trust store.
