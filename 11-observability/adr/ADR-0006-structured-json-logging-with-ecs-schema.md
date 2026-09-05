# ADR-0006: Enforcing Structured JSON Logging with Elastic Common Schema (ECS)

* **Status**: Accepted
* **Date**: 2026-05-15
* **Deciders**: Enterprise Data Architect, Security Architect, Core Frameworks Lead
* **Technical Story**: [ARCH-OBS-006] Unified Structured Logging Standard

---

## Context and Problem Statement
Microservice applications emit logs in disparate unstructured text formats (log4j pattern layouts, custom printf statements, raw stack traces). Ingestion collectors consume massive CPU parsing complex regex patterns (grok filters), and correlated queries across services fail due to inconsistent field naming (`userId` vs `user_id` vs `uid`).

## Decision Drivers
* Zero-regex ingestion overhead at logging collectors.
* Canonical, fleet-wide field naming schema.
* Seamless correlation between logs, traces, and Kubernetes host metadata.

## Considered Options
1. **Option 1**: Unstructured text logging with Fluentbit grok parsing.
2. **Option 2**: Custom internal JSON schema.
3. **Option 3**: **Structured JSON Logging conforming to Elastic Common Schema (ECS) and OpenTelemetry Semantic Conventions**.

## Decision Outcome
**Chosen Option**: **Option 3: Structured JSON conforming to ECS / OTel Semantic Conventions**.

### Positive Consequences
* Standardized top-level attributes: `@timestamp`, `log.level`, `service.name`, `trace.id`, `span.id`, `error.message`.
* Collector ingestion CPU reduced by 60% due to native JSON parsing without regex.
* 100% trace-to-log correlation in Grafana and Kibana out of the box.

### Negative Consequences
* Raw JSON logs are harder for developers to read in local terminals without formatting tools like `jq` or stern.

---

## Links
* Standard Specification: [`../logging/structured-logging.md`](../logging/structured-logging.md)
