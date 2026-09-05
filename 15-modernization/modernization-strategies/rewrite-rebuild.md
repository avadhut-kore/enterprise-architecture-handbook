# The "Rewrite / Rebuild" Strategy: Ground-Up Re-Engineering

## 1. Architectural Definition
**Rewrite** (or **Rebuild**) discards the existing codebase entirely and develops a completely new software application from scratch on a modern technology stack.

---

## 2. The Perils of Second-System Syndrome
A complete rewrite is the highest-risk strategy in enterprise architecture:
- **The Moving Target**: While the team spends 2 years rebuilding the system, the business continues adding features to the legacy system, widening the functional gap.
- **Forgotten Edge Cases**: The legacy system contains thousands of bug fixes and regulatory workarounds implemented over decades that are not documented in any specification.
- **Fatigue & Cancellation**: When the rewrite runs over budget at month 18 without a production release, executive leadership frequently cancels the program, resulting in a total write-off.

---

## 3. Strict Criteria for Permitting a Rewrite
A rewrite is justified **only** under these stringent conditions:
1. The legacy code is in an obsolete language (e.g., Assembler, MUMPS, VB3) where finding developers is impossible.
2. The fundamental business domain has radically changed, rendering the existing data model completely obsolete.
3. The codebase is under 50,000 lines of code and has clear, well-understood boundaries.
4. The rewrite is delivered in thin, deployable slices that reach production incrementally within 90 days.
