# Enterprise Project Structure

## 1. Standard Root Structure

```text
root/
├── build/                      # Build scripts, Makefiles, Dockerfiles
├── docs/                       # Architectural Decision Records, C4 diagrams
├── src/                        # Production source code
│   ├── Core/                   # Pure business domain entities & interfaces
│   ├── Application/            # Use cases, command/query handlers
│   ├── Infrastructure/         # DB contexts, third-party clients
│   └── WebApi/                 # Ingress controllers, middleware
├── tests/                      # Automated test suites
│   ├── Unit/
│   ├── Integration/
│   └── Architecture/           # ArchUnit / NetArchTest constraints
└── tools/                      # Database migration CLI, local dev seeds
```
