# Data Encryption Standards

## 1. Encryption Tiers
* **In Transit**: TLS 1.3 with cipher suites enforcing forward secrecy.
* **At Rest (Volume)**: AWS KMS AES-256 EBS volume encryption.
* **At Rest (Column)**: Application-level envelope encryption using Tink / libsodium for SSNs and credit card PANs.
