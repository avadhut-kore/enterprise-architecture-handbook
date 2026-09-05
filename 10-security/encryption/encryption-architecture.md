# Enterprise Encryption Architecture: Rest, Transit & In-Use

## Executive Summary

1. **Encryption in Transit**: Mandatory TLS 1.3 for 100% of network traffic (north-south and east-west).
2. **Encryption at Rest**: AES-256-GCM applied to all block storage, relational databases, object storage, and backups.
3. **Encryption in Use (Confidential Computing)**: Hardware-enforced memory encryption (AMD SEV-SNP, Intel SGX, AWS Nitro Enclaves) isolating sensitive data in memory even from the host hypervisor and cloud administrators.
