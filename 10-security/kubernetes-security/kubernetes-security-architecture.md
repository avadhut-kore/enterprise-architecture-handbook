# Kubernetes Security Architecture & Control Plane Hardening

## Executive Summary

Hardening the Kubernetes control plane is the foundation of platform security. A compromise of the Kubernetes API server or etcd cluster grants full administrative control over all underlying workloads.

---

## 1. Non-Negotiable Control Plane Invariants
1. **etcd Encryption at Rest**: Encrypt all secrets stored in etcd using KMS envelope encryption (`--encryption-provider-config`). Plaintext etcd storage is strictly prohibited.
2. **Private API Server**: Restrict the Kubernetes API server endpoint to private VPC subnets. Disable public internet access (`0.0.0.0/0`).
3. **Disable Anonymous Authentication**: Configure `--anonymous-auth=false` on `kube-apiserver`.
4. **Node Authorization**: Enable the `NodeRestriction` admission plugin to prevent compromised kubelets from modifying workloads on other nodes.
