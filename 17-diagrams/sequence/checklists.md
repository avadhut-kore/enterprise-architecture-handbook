# Sequence Diagram Review Checklist

- [ ] Does the diagram clearly identify all participating lifelines and actors?
- [ ] Is every message labeled with explicit intent and payload format?
- [ ] Are synchronous arrows (solid `->>`) distinguished from asynchronous signals (dashed `-->>` or `-.->`)?
- [ ] Are failure paths and negative responses (e.g., 401, 404, 500) explicitly documented alongside the happy path?
- [ ] In Saga transactions, are compensating rollback calls explicitly represented?
- [ ] Are timeout budgets and retry loop termination conditions unambiguous?
