# ADR-0007: Continuous Production Profiling via Zero-Overhead eBPF

* **Status**: Accepted
* **Date**: 2026-06-01
* **Deciders**: Principal Performance Architect, SRE Architect, Security Lead
* **Technical Story**: [ARCH-OBS-007] Production Continuous Profiling

---

## Context and Problem Statement
Production performance bottlenecks (garbage collection stalls, lock contention, memory leaks, off-CPU scheduling latency) are invisible in high-level metrics and distributed traces. Traditional bytecode profilers (e.g., Java Flight Recorder, pprof) introduce unacceptable runtime CPU overhead ($5\% - 15\%$) or require invasive application restarts.

## Decision Drivers
* Fleet-wide, continuous profiling in production 24/7/365.
* Absolute runtime overhead $< 1.0\%$ CPU and $< 50\text{MB}$ RAM.
* Zero application code modification or pod restart requirements.

## Considered Options
1. **Option 1**: On-demand profiling via ad-hoc SSH and pprof/JFR.
2. **Option 2**: In-process runtime profiler agents (e.g., Datadog Continuous Profiler).
3. **Option 3**: **Kernel-Level eBPF Continuous Profiling (Grafana Pyroscope / Parca)**.

## Decision Outcome
**Chosen Option**: **Option 3: Kernel-Level eBPF Continuous Profiling**.

### Positive Consequences
* **Zero Code Touch**: eBPF attaches directly to kernel tracepoints and perf events; profiles all processes (compiled C/Go, JVM, Python, Node.js) automatically.
* **Sub-1% Overhead**: Statistical sampling at 19 Hz consumes $< 0.8\%$ CPU overhead.
* **Flame Graph Diagnostics**: Instant historical flame graph diffs reveal exact line-of-code regressions between deployment versions.

### Negative Consequences
* Requires modern Linux kernels ($\ge 5.4$) with `BPF_PROG_TYPE_PERF_EVENT` support and elevated Kubernetes DaemonSet privileges (`CAP_SYS_ADMIN` or `CAP_BPF`).

---

## Links
* Profiling Specification: [`../profiling/continuous-profiling.md`](../profiling/continuous-profiling.md)
