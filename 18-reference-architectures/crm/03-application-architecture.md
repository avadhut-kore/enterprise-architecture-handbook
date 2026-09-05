# Application Architecture: Enterprise CRM

## 1. Domain Services & State Machines
1. **Lead-to-Opportunity Domain Engine**:
   - Manages the progressive sales state machine: `NEW -> QUALIFIED -> DISCOVERY -> PROPOSAL -> NEGOTIATION -> CLOSED_WON / CLOSED_LOST`.
   - Built-in validation rules: Moving to `PROPOSAL` mandates attached quote line items and credit verification.
2. **Customer 360 Master Graph**:
   - Models complex parent-child corporate account hierarchies (`Global Enterprise -> Subsidiary -> Regional Branch -> Buyer Contact`).
   - Dynamic deduplication worker: Runs Levenshtein distance matching on email domains and phone numbers to prevent duplicate account creation.
3. **Omni-Channel Service Desk**:
   - Skills-based ticket routing engine distributing customer inquiries to support reps based on language, product tier, and active agent queue capacity.
