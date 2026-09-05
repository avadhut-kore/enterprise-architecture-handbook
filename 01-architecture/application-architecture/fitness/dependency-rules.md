# Automated Dependency Direction Tests

## 1. ArchUnit / NetArchTest Invariants
```csharp
// Example NetArchTest in C#
Types.InAssembly(domainAssembly)
    .ShouldNot()
    .HaveDependencyOn("Infrastructure")
    .Assert();
```
If an engineer tries to import a database repository into the domain, CI fails immediately.
