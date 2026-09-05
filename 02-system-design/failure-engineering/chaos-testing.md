# Chaos Engineering & Fault Injection

## 1. Principles of Chaos Engineering

Chaos Engineering is the discipline of experimenting on a distributed system in production to build confidence in the system’s capability to withstand turbulent conditions.

Rather than waiting for unpredictable real-world outages to expose hidden flaws, chaos engineers intentionally inject realistic failures in a controlled, monitored environment.

---

## 2. The Scientific Chaos Workflow

```
1. Formulate Hypothesis: "If Redis cluster loses 1 master node, P99 API latency increases by < 20ms."
     └─► 2. Define Steady-State Metrics: (Error rate < 0.01%, Latency < 100ms)
           └─► 3. Inject Controlled Fault: (Kill master node container)
                 └─► 4. Observe Divergence: Verify if hypothesis holds true
                       └─► 5. Auto-Abortion: Terminate test if error rate exceeds 0.5%
                             └─► 6. Remediate & Automate Regression Testing
```

---

## 3. Practical Fault Scenarios

- **Network Delay / Packet Drop**: Introduce 200ms latency on internal gRPC calls using `tc` (traffic control) or Chaos Mesh.
- **Resource Stress**: Saturate CPU cores to 95% or allocate memory to trigger GC pauses.
- **Process Termination**: Randomly kill microservice pods or database read replicas.
- **DNS Failure**: Block UDP port 53 to verify local DNS caching behavior.
