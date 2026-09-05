# Cloud KMS vs Dedicated Cloud HSM

## Executive Summary

| Dimension | Multi-Tenant Cloud KMS (AWS KMS / Azure Key Vault) | Dedicated Cloud HSM (AWS CloudHSM) |
| :--- | :--- | :--- |
| **Hardware Boundary** | Multi-tenant physical HSM partition | Single-tenant dedicated physical HSM appliance |
| **Certification** | FIPS 140-2 / 140-3 Level 2 (or Level 3 in hardware) | FIPS 140-2 Level 3 strictly enforced |
| **Pricing Model** | Pay per API request (cents/month) | Dedicated instance billing (\$1,200+/month/HSM) |
| **API Integration** | Seamless native integration with all cloud services | Requires PKCS#11 / JCE custom drivers |
| **Target Workloads** | 99% of enterprise cloud workloads | Core payment processing, PKI Root CA, custom crypto engines |
