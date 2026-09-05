# ADR-0002: OpenTelemetry Collector Topology: Node DaemonSet vs Sidecar

* **Status**: Accepted
* **Date**: 2026-03-22
* **Deciders**: Kubernetes Platform Lead, SRE Architect, Infrastructure FinOps Lead
* **Technical Story**: [ARCH-OBS-002] Collector Deployment Topology

---

## Context and Problem Statement
In our Kubernetes clusters (15,000 application pods across 350 worker nodes), we must deploy the OpenTelemetry Collector to aggregate, batch, and scrub telemetry. We need to decide whether to inject the collector as a **Sidecar container** inside every application pod or deploy it as a **Node DaemonSet** (one agent per Kubernetes worker node).

## Decision Drivers
* Cluster memory and CPU overhead efficiency.
* blast-radius isolation.
* Operational upgrade simplicity.

## Considered Options
1. **Option 1**: Sidecar Collector per Application Pod.
2. **Option 2**: Node DaemonSet Collector (One per Node).
3. **Option 3**: Centralized Remote Collector Gateway Only.

## Decision Outcome
**Chosen Option**: **Option 2: Node DaemonSet Collector**.

### Positive Consequences
* **85% Memory Reduction**: 350 DaemonSet instances consume $\approx 70\text{GB}$ cluster RAM total, compared to 15,000 sidecars consuming $> 1.5\text{TB}$ of RAM.
* **Decoupled Upgrades**: Collector configuration updates do not require restarting application containers.
* **Simplified K8s Metadata**: Node agent queries local kubelet directly via Unix domain socket.

### Negative Consequences
* Multi-tenant noisy neighbor risks if one application pod floods the local node collector.
* Remediated by configuring in-memory rate limiters and memory ballast processors on each DaemonSet.

---

## Pros and Cons of the Options

### Option 1: Sidecar Collector
* Pros: Complete resource isolation per pod.
* Cons: Massive cluster memory bloat; pod restart required on collector config change.

### Option 2: Node DaemonSet
* Pros: Highly efficient memory utilization; shared connection pooling; zero app restart.
* Cons: Shared resource requires memory ballast and rate-limiting safeguards.

---

## Links
* Architecture Reference: [`../reference-architectures/01-cloud-native-k8s.md`](../reference-architectures/01-cloud-native-k8s.md)
