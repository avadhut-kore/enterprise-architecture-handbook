# Sequence Diagram Architectural Review Checklist

- [ ] Is autonumbering enabled (`autonumber`) across all sequence steps?
- [ ] Are error handling, network timeouts, and circuit breaker states modeled using `critical`, `alt`, or `opt` blocks?
- [ ] Are asynchronous events differentiated from synchronous blocking RPC calls?
- [ ] Are external third-party API dependencies clearly demarcated?
- [ ] Are idempotency key transmissions documented for money-movement or state-mutating requests?
