# Kubernetes NetworkPolicies & eBPF Microsegmentation

## Executive Summary

By default, Kubernetes networking is completely flat: any pod in any namespace can communicate with any other pod in the cluster. This allows an attacker who compromises a frontend pod to connect directly to internal databases or backend payment services.

---

## 1. Default-Deny-All Baseline Policy
Every enterprise namespace must deploy a default-deny ingress and egress policy:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production-orders
spec:
  podSelector: {} # Selects all pods in namespace
  policyTypes:
  - Ingress
  - Egress
```
Subsequent explicit policies must be authored to allow traffic only between verified microservices on specific ports.
