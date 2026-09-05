# Shared Libraries, Utilities, and Code Governance

## 1. The Shared Library Coupling Trap
When decomposing a monolith, developers often extract common domain models and database entities into a shared corporate library (`enterprise-common.jar` or `Enterprise.Shared.dll`). 

> **Danger**: A change in the shared library requires re-compiling and re-deploying all 30 microservices simultaneously, recreating monolithic coupling at the binary level.

---

## 2. Golden Rules for Code Sharing
1. **Share Technical Utilities, Never Domain Models**: Sharing a JSON serialization utility, logging helper, or JWT validator is encouraged. Sharing `Order` or `Customer` domain models creates tight coupling.
2. **Prefer Duplication Over Premature Coupling**: It is better to duplicate a 15-line DTO across three services than to bind them to a common shared library release lifecycle.
3. **Semantic Versioning & Backward Compatibility**: Any shared platform library must adhere strictly to SemVer (`MAJOR.MINOR.PATCH`). Never break backward compatibility on minor updates.
