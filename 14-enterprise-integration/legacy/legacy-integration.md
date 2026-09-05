# Principles of Legacy Systems Integration

## 1. The Realities of Legacy Infrastructure
1. **MIPS Are Expensive**: Every direct API call into an IBM mainframe consumes Million Instructions Per Second (MIPS), driving exponential software licensing bills.
2. **Batch Windows Rule**: Legacy systems frequently lock databases during overnight batch windows; real-time interfaces must buffer mutations during downtime.
3. **Domain Models Are Entangled**: Business logic is often scattered across 40-year-old COBOL programs with no existing documentation.
