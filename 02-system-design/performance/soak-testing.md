# Soak (Endurance) Testing

## 1. Detecting Insidious Long-Tail Degradation
Many catastrophic production outages are caused by defects that only surface after days or weeks of continuous runtime operation. **Soak testing** runs a sustained, steady-state workload ($70\%\text{--}80\%$ load) continuously for **24 to 72 hours**.

```mermaid
flowchart LR
    Hour1[Hour 1: Heap 1.2GB - Healthy] --> Hour24[Hour 24: Heap 3.8GB - Slow Leak]
    Hour24 --> Hour72[Hour 72: Heap 7.9GB -> Out Of Memory Crash!]
    
    style Hour72 fill:#f66,stroke:#333
```

---

## 2. Critical Defects Uncovered by Soak Testing
* **Slow Memory Leaks**: Objects held in static collections, unbounded thread-local maps, or uncollected event listeners.
* **Database Connection Leaks**: Backend exceptions that bypass `connection.close()` or `try-with-resources` blocks, gradually consuming connection pools.
* **File Descriptor & Socket Leaks**: Unclosed HTTP response bodies leaving TCP sockets in `CLOSE_WAIT` state until the Linux `ulimit -n` limit is breached.
* **Disk Saturation**: Rapidly growing unrotated container logs or unvacuumed database dead tuples.
