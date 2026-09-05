# Container Health Checks: Liveness, Readiness & Startup Probes

## Executive Summary

Health checks allow orchestrators to determine whether a container is healthy, ready to receive client traffic, or needs to be terminated and restarted.

---

## 1. The Three Health Probe Primitives

```mermaid
graph TD
    Start[Container Starts] --> Startup{Startup Probe Passing?}
    Startup -->|No: Still Initializing| Wait1[Wait: Shield Liveness from Premature Termination]
    Startup -->|Yes| ActiveLoop[Active Runtime Loop]

    ActiveLoop --> Liveness{Liveness Probe Passing?}
    Liveness -->|No: Deadlock Detected| Restart[Kill Container & Restart Pod]

    ActiveLoop --> Readiness{Readiness Probe Passing?}
    Readiness -->|Yes| RouteTraffic[Route Traffic via Load Balancer]
    Readiness -->|No: DB Connection Pool Full| RemoveTraffic[Remove from Load Balancer Endpoints: SHED LOAD]
```

---

## 2. Health Check Design Guardrails

1. **Do Not Check Downstream Dependencies in Liveness Probes**:
   - If Service A's `/healthz` liveness probe executes a query against a shared PostgreSQL database, a database outage causes all instances of Service A to fail their liveness probes simultaneously. Kubernetes will kill and restart every container in a cascading reboot loop, exacerbating the outage.
   - **Liveness probes must check ONLY local process health** (e.g., internal event loop is responding, not deadlocked).
2. **Use Readiness Probes for Dependency Health**:
   - If downstream dependencies are unavailable, fail the **Readiness Probe**. This removes the container from load balancer endpoints, shedding client traffic while allowing the container to remain running and reconnect when the database recovers.
