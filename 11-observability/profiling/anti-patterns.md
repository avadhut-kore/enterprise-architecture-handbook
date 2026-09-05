# Continuous Profiling Anti-Patterns Catalog

## 1. Executive Summary
This document catalogs 12 widespread enterprise anti-patterns in application profiling, runtime analysis, and performance optimization.

---

## 2. The 12 Profiling Anti-Patterns

### 1. Profiling Only in Staging / Development
* **Problem**: Profiling code exclusively on local developer laptops or artificial test environments.
* **Why It Happens**: Fear of production profiling overhead.
* **Impact**: Dev environments lack production traffic volume, diverse data distributions, and real cache contention; production bottlenecks remain hidden until outages.
* **Remediation**: Deploy modern low-overhead ($< 1\%$) eBPF continuous profiling across 100% of production workloads.

### 2. Stripping DWARF Debug Symbols from Production Binaries
* **Problem**: Compiling Go/Rust/C++ binaries with `-s -w` (stripping symbol tables) without preserving external debuginfo.
* **Why It Happens**: Trying to reduce container image size by a few megabytes.
* **Impact**: Flame graphs display hex memory addresses (`0x7fff812a`) instead of function names (`processOrder()`), rendering profiles useless.
* **Remediation**: Preserve symbol tables or upload DWARF symbols to a centralized symbol server (debuginfod / Parca Symbol Server).

### 3. Ignoring Off-CPU Time
* **Problem**: Investigating latency solely with CPU profilers.
* **Why It Happens**: Unawareness of Off-CPU eBPF profiling tools.
* **Impact**: Engineers spend weeks optimizing a function taking 20ms on CPU while ignoring a 2,000ms mutex lock delay.
* **Remediation**: Pair On-CPU profiling with eBPF Off-CPU scheduling analysis.

### 4. Running Heavy Tracing Profilers in Production
* **Problem**: Attaching full method-tracing profilers (which record every single method entry and exit) in live production.
* **Why It Happens**: Using development IDE profiling tools in production.
* **Impact**: Application latency degrades by $500\%$; CPU spikes to 100%; system collapses.
* **Remediation**: Enforce statistical **sampling profilers** (19 Hz) only.

### 5. Optimizing Non-Plateau Functions
* **Problem**: Refactoring a function that represents only 1% of horizontal flame graph width.
* **Why It Happens**: Developer optimizes code they are familiar with rather than what the data indicates.
* **Impact**: Wasted engineering sprints with negligible real-world performance gain.
* **Remediation**: Focus performance sprints strictly on wide, flat plateaus at the top of the flame graph.

### 6. Sampling at Harmonic Frequencies (50 Hz / 100 Hz)
* **Problem**: Configuring profiling timers to sample at exact multiples of 10 or 50.
* **Why It Happens**: Intuitive preference for round numbers.
* **Impact**: Harmonics cause the profiler to repeatedly sample the same periodic background task, distorting data.
* **Remediation**: Sample at prime frequencies: **19 Hz**, **49 Hz**, or **99 Hz**.

### 7. Confusing Allocation Rate with Memory Leak
* **Problem**: Alerting on high memory allocation rate as an indicator of an OOM leak.
* **Why It Happens**: Misunderstanding memory metrics.
* **Impact**: False alarms during batch jobs that allocate and immediately free millions of objects safely.
* **Remediation**: Distinguish between `alloc_space` (churn) and `inuse_space` (leak).

### 8. Manual Heap Dumps During Outages
* **Problem**: Running `jcmd GC.heap_dump` on a production pod during a SEV-1 incident.
* **Why It Happens**: Desperation to diagnose a memory leak.
* **Impact**: The JVM freezes completely for 60 seconds while writing a 32GB dump file to disk, triggering health-check timeouts and container restarts.
* **Remediation**: Use continuous sampling allocation profilers that maintain continuous low-overhead snapshots.

### 9. Blind Micro-Optimization of Inlined Functions
* **Problem**: Spending days rewriting arithmetic loops that modern JIT/LLVM compilers inline automatically.
* **Why It Happens**: Lack of understanding of compiler optimization passes.
* **Impact**: Obfuscates code readability with zero runtime speedup.
* **Remediation**: Verify assembly and inlining graphs before rewriting readable domain logic.

### 10. Forgetting to Enable JVM Async-Profiler Safe-Point Fixes
* **Problem**: Using standard JVM profiling that relies on GC safe points (`-XX:+PreserveFramePointer` omitted).
* **Why It Happens**: Incomplete JVM configuration.
* **Impact**: Safe-point bias skews flame graphs, making loops without safe points appear invisible.
* **Remediation**: Always pass `-XX:+PreserveFramePointer` and use Async-Profiler for unbiased sampling.

### 11. Unbounded Flame Graph Storage Retention
* **Problem**: Storing raw un-aggregated continuous profile data for 180 days.
* **Why It Happens**: Lack of downsampling policies.
* **Impact**: Profiling cluster storage costs explode.
* **Remediation**: Downsample profiles: retain 10-second resolution for 7 days, 1-hour resolution for 30 days.

### 12. Disconnected Profiling Telemetry
* **Problem**: Profiling tools living in an isolated portal with no links to metrics or traces.
* **Why It Happens**: Ad-hoc tool adoption by disparate teams.
* **Impact**: Responders cannot navigate from a specific slow trace span to its corresponding CPU profile.
* **Remediation**: Integrate continuous profiling into Grafana (Tempo -> Pyroscope deep-linking via trace span tags).
