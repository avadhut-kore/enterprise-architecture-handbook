# Benchmarking and Performance Profiling for Architects

Never trust vendor marketing claims or synthetic micro-benchmarks. Validate system performance under realistic enterprise constraints.

## 1. The Coordinated Omission Fallacy

Many load testing tools (and naive tests) suffer from Coordinated Omission: when the server slows down, the testing client pauses before issuing the next request, artificially masking high tail latencies.
- **Rule**: Use open-model load testing tools (e.g., k6, Gatling, Locust) that generate requests on a fixed arrival schedule regardless of server response times.

## 2. Profiling Golden Rules
- **Look at the Tails**: p50 latency is irrelevant to user experience; optimize for p95, p99, and p99.9.
- **Flame Graphs**: Use Linux `perf` or async-profiler to visualize CPU bottlenecks directly down to kernel system calls and JVM/V8 frames.

## Related Modules
- [Architecture Prototyping and Spikes](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/experimentation/architecture-prototyping-and-spikes.md)
- [System Design Methodology](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/system-design/master-system-design-methodology.md)
