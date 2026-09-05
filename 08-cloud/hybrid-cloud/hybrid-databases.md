# Hybrid Database Topologies & CAP Constraints

## Executive Summary

Deploying databases across hybrid boundaries requires strict adherence to the CAP theorem. Network latency across hybrid links (typically 10–50 ms) makes synchronous multi-master transactions mathematically incompatible with acceptable system throughput.

---

## 1. Supported vs Prohibited Topologies

```mermaid
graph TD
    subgraph Pattern A: Read-Replica in Cloud [RECOMMENDED]
        Master[(On-Prem Primary Master)] -->|Asynchronous Replication| CloudReplica[(Cloud Read Replica)]
        App[Cloud API Services] -->|Read Queries| CloudReplica
        App -.->|Write Transactions| Master
    end

    subgraph Pattern B: Synchronous Multi-Master [PROHIBITED ACROSS WAN]
        NodeA[(On-Prem DB Node)] <=- -=>|Synchronous 2PC / Raft consensus: HIGH LATENCY / TIMEOUTS| NodeB[(Cloud DB Node)]
    end
```

---

## 2. Architectural Analysis

| Topology Pattern | Feasibility | Latency Impact | Failure Mode |
| :--- | :--- | :--- | :--- |
| **On-Prem Master + Cloud Async Read Replica** | **High** | Writes: Local (sub-ms); Reads: Local in cloud (sub-ms) | Replication lag ($100\text{ ms} - 2\text{ s}$); cloud reads are eventually consistent. |
| **Cloud Master + On-Prem Read Replica** | **High** | Writes: Cloud (sub-ms); Reads: Local on-prem (sub-ms) | If hybrid link drops, on-prem queries succeed on stale data; writes fail. |
| **Synchronous 2PC across Hybrid WAN** | **PROHIBITED** | Every commit incurs $2\times$ RTT ($20 - 100\text{ ms}$) | Network jitter stalls database connection pools; cascading thread starvation. |
| **Split-Brain Disaster Scenario** | **CRITICAL RISK**| Occurs if hybrid link drops and both sides accept writes | Irreconcilable data corruption; manual database surgery required. |
