# Distributed Design Principle: Fail-Fast

## 1. Core Principle Definition

The Fail-Fast principle requires a system to immediately detect, validate, and halt execution upon encountering an invalid input, missing dependency, or corrupted state, rather than attempting to proceed under uncertain conditions.

---

## 2. Fail-Fast vs Fail-Silent

```
Fail-Silent / Permissive (Dangerous):
Client sends JSON with negative balance: -500
Service catches error, sets balance to 0, continues processing
(Silent data corruption, difficult debugging, financial discrepancy)

Fail-Fast (Robust):
Client sends JSON with negative balance: -500
Validator fails immediately: Returns HTTP 422 Unprocessable Entity
(Stops execution within 2ms, zero database write, clear error message)
```

---

## 3. Boundary Implementation

- **Strict Ingress Schema Validation**: Check headers, data types, and bounds before allocating application resources.
- **Startup Pre-flight Health Checks**: If a required database connection, secret key, or encryption certificate is missing at boot, terminate the process immediately (`exit(1)`) so Kubernetes does not route traffic to the dead pod.
