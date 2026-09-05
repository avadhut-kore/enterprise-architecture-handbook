# Java 21 / Spring Boot 3 Enterprise Reference Pipeline

Architectural blueprint for Java microservices utilizing modern JVM runtimes.

## 1. Pipeline Architecture Flow

```
[Commit] ──► [Maven/Gradle Daemon Build] ──► [ArchUnit Fitness Tests] ──► [Testcontainers Integration]
                                                                                  │
[GitOps Deploy] ◄── [Cosign Sign Image] ◄── [Jib Build Distroless] ◄──────────────┘
```

## 2. Hardening & Best Practices
- **Daemon Caching**: Cache `~/.gradle/caches` or `~/.m2/repository` with cryptographic key checksums.
- **Testcontainers**: Run real PostgreSQL and Kafka instances in CI runners via Docker-in-Docker or Podman.
- **Daemonless OCI Packaging**: Build container images without a Docker daemon using Google Jib or Cloud Native Buildpacks targeting `gcr.io/distroless/java21-debian12:nonroot`.

## Related Resources
- [Java Backend Architecture](../../../03-backend/java/README.md)
- [Fitness Functions](../../../10-architect-mastery/evolution/fitness-functions-in-practice.md)
