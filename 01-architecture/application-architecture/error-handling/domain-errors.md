# Domain Errors vs Exceptions

## 1. The Result Pattern
Exceptions in many runtimes (.NET, Java) incur severe performance penalties (stack trace capture). Furthermore, domain errors (e.g., `CardExpired`) are **not exceptional**; they are standard business outcomes.

```csharp
// Prefer Result<T, E> over throwing exceptions for business errors
public record Result<TValue, TError>
{
    public bool IsSuccess { get; init; }
    public TValue Value { get; init; }
    public TError Error { get; init; }
}
```
