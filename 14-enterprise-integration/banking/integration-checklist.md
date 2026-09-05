# Core Banking Integration Architecture Checklist

- [ ] Is an Anti-Corruption Layer (ACL) deployed between legacy CPYBOOK formats and modern REST/JSON microservices?
- [ ] Are high-frequency read queries diverted to a low-latency read replica cache to save mainframe MIPS?
- [ ] Is every financial transaction posted via double-entry balancing ($Debits == Credits$)?
- [ ] Are real-time payment operations protected by end-to-end `Idempotency-Key` tracking?
- [ ] Is automated three-way reconciliation configured against central bank clearing statements?
- [ ] Are PIN blocks and card keys isolated within FIPS 140-2 Level 3 Hardware Security Modules?
