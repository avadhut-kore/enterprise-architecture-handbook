# Chaos Engineering: Validating Telemetry & Resiliency Under Fire

## 1. Executive Summary
The primary purpose of Chaos Engineering is **not** to see if your system crashes; it is to verify that **when the system degrades, your observability platform reveals the failure immediately and accurately**.

If an automated chaos experiment cuts network connectivity between the API gateway and the payment service, but no P1 alert fires, the test has uncovered an **observability defect**, not merely an infrastructure flaw.

---

## 2. The Chaos-to-Telemetry Verification Loop

```mermaid
sequenceDiagram
    autonumber
    participant ChaosEngine as Chaos Mesh / Litmus
    participant AppCluster as Kubernetes Microservices
    participant Telemetry as OpenTelemetry Pipeline
    participant AlertManager as AlertManager / PagerDuty
    participant SRE as On-Call Engineer

    ChaosEngine->>AppCluster: Inject 300ms Network Latency on /payments
    Note over AppCluster: Payment calls degrade; retries spike!
    AppCluster->>Telemetry: Emit high latency spans + HTTP 504 errors
    Note over Telemetry: Verifying metric recording rules execute...
    Telemetry->>AlertManager: Multi-Burn-Rate threshold breached!
    AlertManager->>SRE: Dispatch P1 Page: "Payment Latency SLO Fast Burn"
    Note over SRE: Verifying alert fired within < 2 minutes!<br/>Runbook link leads directly to payment circuit breaker!
    ChaosEngine->>AppCluster: Terminate fault injection (Self-Healing)
```

---

## 3. Production Declarative Chaos Experiment Spec (Chaos Mesh CRD)

```yaml
# /deploy/chaos/payment-network-latency.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: payment-gateway-latency-injection
  namespace: commerce
spec:
  action: delay
  mode: all
  selector:
    namespaces:
      - commerce
    labelSelectors:
      app: "payment-service"
  delay:
    latency: "350ms"
    jitter: "50ms"
    correlation: "25"
  direction: to
  target:
    selector:
      namespaces:
        - commerce
      labelSelectors:
        app: "external-payment-mock"
  duration: "10m"
  scheduler:
    cron: "0 14 * * 2" # Run every Tuesday at 14:00 UTC during active business hours
```

### The 4 Observability Hypotheses for This Experiment
1. **Metric Shift**: Prometheus metric `http_request_duration_seconds{service="payment-service"}` must reflect a P99 jump from $45\text{ms}$ to $\ge 350\text{ms}$ within 30 seconds of injection.
2. **Trace Capture**: Distributed traces must clearly highlight the client-side HTTP span to `external-payment-mock` as the critical path bottleneck.
3. **Alert Triggering**: The `PaymentServiceSlowBurnRate` alert must transition from `Pending` to `Firing` within 3 minutes.
4. **Dashboard Accuracy**: The Tier-1 Commerce RED dashboard must turn Yellow/Red automatically without manual browser refresh.
