# The USE Method: Architecture for Infrastructure & Resources

## 1. Executive Summary
Formulated by Brendan Gregg, the **USE Method** is an infrastructure-oriented observability pattern designed for evaluating the health of physical, virtual, and software resources.

For every resource in a system (CPU, memory, disk I/O, network interface, database connection pool, worker thread pool), measure:
- **Utilization**: The percentage of time that the resource was busy servicing work.
- **Saturation**: The degree to which the resource has extra work queued that it cannot service immediately.
- **Errors**: The count of error events on the resource.

---

## 2. The Resource Degradation Pipeline

```
Workload Increases
       │
       ▼
Utilization Reaches 100% (Resource is fully utilized)
       │
       ▼
Saturation Begins! (Extra work waits in queue; latency increases linearly)
       │
       ▼
Queue Buffers Overflow (Errors spike; packets dropped; connections refused)
```

---

## 3. The Enterprise USE Matrix Across Key Resources

| Resource | Utilization Metric | Saturation Metric | Error Metric |
| :--- | :--- | :--- | :--- |
| **CPU** | % User/System time: `1 - rate(node_cpu_seconds_total{mode="idle"}[1m])` | System Load Average relative to core count: `node_load1 / count(node_cpu_seconds_total{mode="idle"})` | Hardware machine check exceptions (MCEs) |
| **Memory** | % RAM in use: `1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)` | Page swap rate or OOM Killer invocations: `rate(node_vmstat_oom_kill[1m])` | Allocation failures (Out of Memory) |
| **Disk I/O** | % Time doing I/O: `rate(node_disk_io_time_seconds_total[1m])` | Average queue length: `rate(node_disk_io_time_weighted_seconds_total[1m])` | Device I/O read/write errors: `node_disk_read_errors_total` |
| **Network Interface** | Throughput vs link bandwidth: `rate(node_network_transmit_bytes_total[1m]) / speed` | Transmit/Receive queue drops: `rate(node_network_transmit_drop_total[1m])` | CRC errors and packet corruptions: `rate(node_network_transmit_errs_total[1m])` |
| **DB Connection Pool** | Active connections in use: `hikaricp_connections_active / hikaricp_connections_max` | Threads waiting for connection: `hikaricp_connections_pending` | Connection acquisition timeouts: `hikaricp_connections_timeout_total` |
| **Kafka Broker** | Disk space used; network bandwidth % | Consumer group lag: `kafka_consumergroup_lag` | Under-replicated partitions: `kafka_server_replicamanager_underreplicatedpartitions` |

---

## 4. Operational Principle: Saturation Precedes Failure
Never wait for Errors to fire an alert. **Saturation is the leading indicator of impending disaster**:
* When a connection pool's *Utilization* hits 100%, requests begin queuing.
* *Saturation* (pending queue) climbs. Request latency degrades exponentially (Queueing Theory / Little's Law).
* Once the queue timeout expires (e.g., 30s), *Errors* explode. Alerting on Saturation allows SREs to mitigate before user-visible errors manifest.
