# Enterprise Integration Testing Architecture Library

## 1. Overview
Integration testing across distributed enterprise systems requires verifying API contracts, message schemas, asynchronous event delivery, network failure resilience, and high-volume performance.

## 2. Directory Structure
- [contract-testing.md](contract-testing.md): Consumer-driven contract testing with Pact.
- [integration-testing.md](integration-testing.md): Component-level integration testing with Testcontainers.
- [end-to-end-testing.md](end-to-end-testing.md): Managing end-to-end test environments without flaky mocks.
- [message-testing.md](message-testing.md): Asynchronous message verification and event assertion.
- [schema-testing.md](schema-testing.md): Schema validation, backward compatibility, and Confluent Schema Registry.
- [performance-testing.md](performance-testing.md): High-throughput load testing and soak testing (k6, Gatling).
- [failure-testing.md](failure-testing.md): Chaos engineering and failure injection (Chaos Mesh, Toxiproxy).
- [replay-testing.md](replay-testing.md): Validating pipeline correctness by replaying production logs.
- [reconciliation-testing.md](reconciliation-testing.md): Testing break detection and automated financial matching.
- [security-testing.md](security-testing.md): DAST, API penetration testing, and OAuth fuzzing.
- [certification-testing.md](certification-testing.md): Partner certification, sandbox portals, and conformance suites.
- [checklist.md](checklist.md): Enterprise Integration Testing Review Checklist.
