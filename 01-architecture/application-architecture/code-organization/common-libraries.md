# Common Libraries: The "Core" Library Antipattern

## 1. The Enterprise Trap: MyCompany.Common.dll
Every enterprise creates a `Common` or `Core` repository. Over 5 years:
- It accumulates 500 unrelated utilities, ORM base classes, and logging helpers.
- Every service in the company depends on it.
- Upgrading a single dependency in `Common` breaks 40 downstream teams.

## 2. Architectural Remedy: Micro-Libraries
Decompose `Common` into single-purpose, decoupled packages:
- `MyCompany.Logging.Serilog`
- `MyCompany.Security.Tokens`
- `MyCompany.Http.Resilience`
Teams pull only what they strictly need.
