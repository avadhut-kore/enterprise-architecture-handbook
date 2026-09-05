# ADR-0004: Standardizing on Tail Sampling for Distributed Tracing

* **Status**: Accepted
* **Date**: 2026-04-18
* **Deciders**: Lead Telemetry Architect, SRE Architect, Cloud FinOps Manager
* **Technical Story**: [ARCH-OBS-004] Trace Sampling Architecture

---

## Context and Problem Statement
Application microservices generate 3.2 billion trace spans per day. Storing 100% of spans would cost $180,000/month. Naive 5% head sampling at the API gateway drops 95% of customer-impacting 500 errors and latency spikes, leaving engineers blind during incident root-cause analysis.

## Decision Drivers
* 100% capture of error traces and extreme latency outliers.
* Sustainable trace storage costs ($< \$25,000/\text{month}$).
* Complete absence of blind spots for VIP enterprise accounts.

## Considered Options
1. **Option 1**: 100% Full Fidelity Tracing (No Sampling).
2. **Option 2**: Fixed 5% Probabilistic Head Sampling.
3. **Option 3**: **OpenTelemetry Tail Sampling Collector Pipeline**.

## Decision Outcome
**Chosen Option**: **Option 3: OpenTelemetry Tail Sampling Collector Pipeline**.

### Positive Consequences
* **Zero Lost Error Context**: 100% of traces containing HTTP 5xx, gRPC error codes, or unhandled exceptions are retained.
* **Latency Outlier Protection**: 100% of traces exceeding P95 thresholds are preserved.
* **Cost Reduction**: Nominal, low-latency successful traces are sampled down to 1%, slashing monthly trace storage costs by 86%.

### Negative Consequences
* Tail sampling requires buffering completed trace spans in memory for 10-30 seconds, requiring dedicated collector worker nodes with adequate RAM.

---

## Links
* Reference Guide: [`../cost-and-capacity/sampling-strategies.md`](../cost-and-capacity/sampling-strategies.md)
