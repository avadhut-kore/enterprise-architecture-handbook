# Kubernetes Architecture & Production Engineering

This module provides enterprise-level architecture guidance for Kubernetes control planes, workload abstractions, production cluster sizing, multi-cluster topology, and the core decision: *"Should we use Kubernetes?"*

## Contents

- [Kubernetes Architecture and Control Plane](./kubernetes-architecture-and-control-plane.md) — API Server, etcd, Scheduler, Controller Manager, kubelet, and networking (CNI/Kube-Proxy).
- [Workload Abstractions Architecture](./workload-abstractions-architecture.md) — Pods, Deployments, StatefulSets, DaemonSets, Jobs, Services, Ingress, and Gateway API.
- [Kubernetes Decision Framework](./kubernetes-decision-framework.md) — Deep architectural evaluation: When Kubernetes is necessary, and when it is an expensive mistake.
- [Production Cluster Architecture](./production-cluster-architecture.md) — Multi-zone sizing, upgrades, Karpenter autoscaling, PDBs, quotas, and network policies.
- [Multi-Cluster Architecture](./multi-cluster-architecture.md) — Single cluster vs multi-cluster, blast-radius reduction, and fleet management.

## Core Rule
Kubernetes is a platform for building platforms. Do NOT give developers raw access to Kubernetes YAML; provide self-service golden paths.
