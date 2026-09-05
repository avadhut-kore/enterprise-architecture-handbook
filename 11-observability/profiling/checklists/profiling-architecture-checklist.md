# Continuous Profiling & Runtime Analysis Checklist

## 1. Executive Summary
This 25-point checklist provides engineering squads, performance architects, and Architecture Review Boards (ARBs) with an objective verification rubric for continuous profiling deployment, low-overhead safety, and FinOps optimization.

---

## 2. The 25-Point Checklist

### Section 1: Low-Overhead Production Safety
- [ ] **01.** Continuous profiler operates with measured CPU overhead $< 1.0\%$ across all production nodes.
- [ ] **02.** Memory footprint of the node profiling agent is bounded ($< 150\text{MB}$ RAM).
- [ ] **03.** Profiler uses statistical sampling (not synchronous method tracing).
- [ ] **04.** Sampling frequency is configured to an anti-harmonic prime rate (e.g., 19 Hz or 49 Hz).
- [ ] **05.** The profiler agent drops profile batches automatically under local host memory pressure.

### Section 2: Symbolication & Binary Readiness
- [ ] **06.** Compiled binaries (Go, Rust, C++) retain DWARF debug symbols or have symbols uploaded to a symbol server.
- [ ] **07.** JVM workloads are configured with `-XX:+PreserveFramePointer` to prevent safe-point sampling bias.
- [ ] **08.** Node.js / V8 runtimes are launched with `--perf-basic-prof` to expose JIT symbols to eBPF profilers.
- [ ] **09.** Containerized applications map symbol paths cleanly for host-level profiler resolution.

### Section 3: Telemetry Integration & Trace Linking
- [ ] **10.** Continuous profiling profiles are tagged with OpenTelemetry resource attributes (`service.name`, `environment`).
- [ ] **11.** Trace-to-Profile linking is enabled: clicking a trace span in Grafana navigates directly to the span's flame graph.
- [ ] **12.** Profiles are tagged with dynamic release version and Git commit hashes to enable differential analysis.

### Section 4: Analytical Disciplines (CPU, Memory & I/O)
- [ ] **13.** On-CPU profiling is active across all tier-1 microservices.
- [ ] **14.** Off-CPU profiling via eBPF kernel scheduler hooks is available for diagnosing thread contention and I/O blocks.
- [ ] **15.** Memory allocation profiling tracks both `alloc_space` (churn) and `inuse_space` (leaks).
- [ ] **16.** File and block-layer I/O profiling is enabled on database and event streaming brokers.
- [ ] **17.** Differential flame graphs are generated during automated canary releases to detect performance regressions.

### Section 5: FinOps & Cloud Waste Elimination
- [ ] **18.** Performance optimization sprints prioritize wide, flat plateaus at the top of the flame graph.
- [ ] **19.** Top 10 CPU-consuming functions across the enterprise fleet are identified and reviewed monthly.
- [ ] **20.** Cloud compute rightsizing recommendations incorporate CPU utilization profiles.
- [ ] **21.** High-allocation loops churning temporary objects are refactored to reduce GC pause times.
- [ ] **22.** Non-plateau micro-optimizations are avoided in favor of architectural decoupling.
- [ ] **23.** Profile data retention is tiered: 7 days full resolution, 30 days downsampled.
- [ ] **24.** Continuous profiling agents run safely across both Kubernetes worker nodes and bare-metal hosts.
- [ ] **25.** Performance engineers conduct periodic GameDays to validate off-CPU lock contention diagnostic capabilities.
