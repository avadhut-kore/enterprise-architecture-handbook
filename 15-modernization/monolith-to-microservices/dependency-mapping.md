# Monolith Dependency Mapping & Hotspot Analysis

## 1. Static vs. Dynamic Dependency Analysis
- **Static Analysis (AST Parsing)**: Analyze import statements, package dependencies, and class references using tools like SonarQube, ArchUnit, or JDeodorant to calculate the Afferent (Ca) and Efferent (Ce) coupling.
- **Dynamic Analysis (Runtime Profiling)**: Trace actual call stacks and database query execution in production using OpenTelemetry and APM tools (Datadog, Dynatrace).

---

## 2. Identifying the Ideal First Extraction Candidate
Score candidate domains on a 2x2 matrix:

```
       ┌─────────────────────────────────────────────────────────────┐
       │                                                             │
  High │  [ SECOND EXTRACTION: Core ]      [ AVOID: Entangled Core ] │
B      │  High business value,             High business value,      │
U      │  low coupling.                    high coupling.            │
S      │  High ROI once proven.            Too risky for pilot.      │
I      ├─────────────────────────────────────────────────────────────┤
N      │  [ FIRST EXTRACTION: Ideal Pilot ][ AVOID: Low Value Sink ] │
E      │  Moderate business value,         Low business value,       │
S      │  minimal dependencies.            high complexity.          │
S      │  Safe training ground for team.   Negative ROI.             │
  Low  └─────────────────────────────────────────────────────────────┘
                     Low                                High
                            COUPLING & DEPENDENCIES
```

**Rule of Thumb**: Never pick your most critical, complex domain (e.g., Core Ledger) as your first extraction candidate. Pick a self-contained, low-dependency capability (e.g., Notifications or Shipping Label Generation) to establish your CI/CD pipelines, observability, and team muscle.
