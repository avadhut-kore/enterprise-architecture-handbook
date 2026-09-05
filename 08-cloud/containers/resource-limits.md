# Container Resource Limits: cgroups v2, CPU Throttling & OOM

## Executive Summary

Without explicit resource limits, a single misbehaved container (memory leak, infinite loop) will starve all adjacent containers sharing the host, causing host-wide crashes.

---

## 1. CPU Quotas vs Memory Limits

```mermaid
graph TD
    subgraph CPU Enforcement: Compressible Resource
        AppCPU[Application Spikes CPU] --> CFS[CFS Completely Fair Scheduler Quota]
        CFS --> Throttle[Process Throttled / Clock Cycles Paused: APP SLOWS DOWN, DOES NOT CRASH]
    end

    subgraph Memory Enforcement: Non-Compressible Resource
        AppMem[Application Leaks Memory] --> Limit{Exceeds cgroups Memory Limit?}
        Limit -->|Yes| OOM[Linux Kernel OOM Killer Invoked]
        OOM --> Terminate[Sends SIGKILL: CONTAINER TERMINATED WITH EXIT 137!]
    end
```

---

## 2. cgroups v1 vs cgroups v2

Modern Linux enterprise distributions standardise on **cgroups v2**:
- **Single Unified Hierarchy**: Eliminates conflicting resource controllers present in cgroups v1.
- **Enhanced OOM Control**: Allows orchestrators to kill the entire container cgroup atomically rather than killing a random sub-process.
- **Memory Pressure Stalling Information (PSI)**: Provides kernel metrics indicating memory starvation before the OOM killer triggers.
