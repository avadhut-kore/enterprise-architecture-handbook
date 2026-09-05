# Exception Handling Best Practices

## 1. Core Rules
1. Never catch generic `Exception` and silently swallow it (`catch (Exception e) {}`).
2. Only catch exceptions you can genuinely handle or translate.
3. Preserve the original exception using inner-exception wrapping to prevent losing stack traces.
