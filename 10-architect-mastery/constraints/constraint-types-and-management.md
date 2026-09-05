# Constraint Types and Management

Managing architectural constraints requires systematic identification, categorization, and validation.

## 1. Detailed Constraint Breakdown

### A. Technical & Physical Constraints
- **Network Bandwidth & Latency**: 1 Gbps WAN link limits replication throughput; cross-continental roundtrips impose irreducible 150ms+ latencies.
- **Data Volume**: Petabyte-scale operational databases cannot be restored via standard backups in under 24 hours.

### B. Commercial & Financial Constraints
- **CapEx vs OpEx**: Fixed enterprise annual capital allocations versus variable cloud consumption spend.
- **Contractual Lock-In**: Existing 5-year multi-million-dollar agreements with enterprise database vendors.

### C. Regulatory & Sovereign Constraints
- **Data Sovereignty**: EU citizen personally identifiable information (PII) must not traverse outside European boundaries.
- **Financial Auditability**: Cryptographic immutability and WORM (Write Once, Read Many) storage rules for ledger data.

## 2. The Constraint Validation Checklist

Before accepting a constraint into an ADR, ask:
1. *Who established this constraint and when?*
2. *Is it backed by physical law, statute, or organizational habit?*
3. *What would it cost in money or political capital to dissolve this constraint?*
4. *If this constraint were removed tomorrow, what would our architecture look like?*
