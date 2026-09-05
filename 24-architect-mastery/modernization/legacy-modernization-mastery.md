# Legacy Modernization Mastery

The greatest mistake in enterprise modernization is attempting a multi-year "Big Bang" rewrite. Big Bang rewrites fail over 70% of the time due to moving business targets, feature parity traps, and unmitigated risk.

## 1. The Modernization Decision Matrix (7Rs)

```
                            [Evaluate Legacy Asset]
                                      │
              ┌───────────────────────┴───────────────────────┐
      Low Business Value                              High Business Value
              │                                               │
      ┌───────┴───────┐                               ┌───────┴───────┐
Low Quality      High Quality                   Low Quality      High Quality
      │               │                               │               │
  [RETIRE]        [RETAIN]                       [REFACTOR/       [REHOST/
(Decommission)  (Leave Alone)                    RE-ARCHITECT]    RE-PLATFORM]
```

## 2. Core Modernization Strategies
1. **Vertical Slice Extraction**: Modernize one complete business capability end-to-end (e.g., Customer Address Management) rather than rewriting technical layers horizontally.
2. **Anti-Corruption Layer (ACL)**: Isolate the clean new domain model from the tangled legacy database schemas using translator adapters.
3. **Telemetry Parity**: Run old and new systems concurrently in shadow mode; compare responses at the API gateway before routing user traffic.

## Related Modules
- [Strangler Fig and Data Migration](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/modernization/strangler-fig-and-data-migration.md)
- [Legacy Modernization Guide](../../15-modernization/README.md)
