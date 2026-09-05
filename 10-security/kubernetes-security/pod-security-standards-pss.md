# Kubernetes Pod Security Standards (PSS)

## Executive Summary

Pod Security Standards define three security baselines enforced natively by the Kubernetes Pod Security Admission (PSA) controller: **Privileged**, **Baseline**, and **Restricted**.

---

## 1. Comparison Matrix

| Standard | Privilege Level | Restrictions Enforced | Target Environment |
| :--- | :--- | :--- | :--- |
| **Privileged** | Unrestricted | None (Can access host kernel, devices, root) | Network CNI plugins, storage CSI drivers only |
| **Baseline** | Default Minimization | Prevents known privilege escalations; default Linux caps | Development sandboxes, legacy applications |
| **Restricted** | **Hardened (Mandated)** | Must run as non-root; drop ALL capabilities; read-only root FS | **All Enterprise Production Workloads** |

```yaml
# Enforce Restricted PSS at the namespace level
apiVersion: v1
kind: Namespace
metadata:
  name: production-payments
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
```
