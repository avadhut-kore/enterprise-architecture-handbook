# Application Architecture: Healthcare Platform

## 1. Enterprise Master Patient Index (EMPI) Matching Engine
Resolves identities across disparate hospital systems using two-stage matching:
1. **Deterministic Match**: Exact match on SSN + Date of Birth, or Government ID.
2. **Probabilistic Match (Fellegi-Sunter Algorithm)**: Weights match scores on First Name (Soundex/Jaro-Winkler), Last Name, Gender, Address Zip Code, and Phone Number.
- Score $\ge 0.85$: Automated merge.
- Score $0.65 - 0.84$: Routed to manual HIM (Health Information Management) duplicate review queue.
- Score $< 0.65$: Create new distinct patient identifier.
