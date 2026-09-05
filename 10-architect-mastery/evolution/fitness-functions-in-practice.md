# Fitness Functions in Practice

An architectural fitness function provides an objective, automated mechanism to evaluate whether a system meets its architectural requirements over time.

## 1. Taxonomy of Fitness Functions

| Type | Frequency | Execution Location | Example Metric / Tool |
| :--- | :--- | :--- | :--- |
| **Atomic** | Every Build | CI Pipeline | ArchUnit: No cyclic dependencies; controller cannot call database directly. |
| **Holistic** | Nightly / Weekly | Integration Env | End-to-end chaos test: Kill primary DB node and measure recovery time (<15s). |
| **Triggered** | On Deployment | Canary Gate | Production canary error rate and p99 latency check via Prometheus. |
| **Continual** | Continuous | Production | FinOps budget alert: Hourly cloud spend spike detection. |

## 2. Concrete Implementation Examples

### Java / ArchUnit Structural Fitness Function
```java
@AnalyzeClasses(packages = "com.enterprise.banking")
public class ArchitectureFitnessTest {

    @ArchTest
    public static final ArchRule controllers_must_not_access_repositories =
        noClasses().that().resideInAPackage("..controllers..")
        .should().accessClassesThat().resideInAPackage("..repositories..");

    @ArchTest
    public static final ArchRule domain_must_not_depend_on_frameworks =
        classes().that().resideInAPackage("..domain..")
        .should().onlyDependOnClassesThat().resideInAnyPackage("java..", "com.enterprise.banking.domain..");
}
```

### TypeScript / Dependency-Cruiser Fitness Function
```json
{
  "forbidden": [
    {
      "name": "no-circular-dependencies",
      "severity": "error",
      "from": { "path": "^src" },
      "to": { "circular": true }
    },
    {
      "name": "services-cannot-touch-ui",
      "severity": "error",
      "from": { "path": "^src/services" },
      "to": { "path": "^src/components" }
    }
  ]
}
```

## Related Modules
- [Evolutionary Architecture Mastery](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/evolution/evolutionary-architecture-mastery.md)
- [Quality Assurance & Testing](../../16-architecture-deliverables/README.md)
