# Payment Security: PCI-DSS, Encryption, and HSMs

## 1. Defense-in-Depth Security Framework
Enterprise payment architectures enforce multi-layered protection:
- **Transport Security**: Mandatory TLS 1.3 with Perfect Forward Secrecy across all integration interfaces.
- **Payload Tokenization**: Zero unencrypted Primary Account Numbers (PANs) stored in application databases or logs.
- **Hardware Cryptography**: Hardware Security Modules (HSMs) manage cryptographic keys used for PIN verification and token generation.
- **PCI-DSS Compliance**: Full architectural alignment with PCI-DSS v4.0 requirements detailed in [payments/pci-dss/](pci-dss/).
