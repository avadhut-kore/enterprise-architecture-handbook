# Kubernetes Architecture and Control Plane Internals

Understanding the distributed architecture of the Kubernetes control plane is essential for sizing, resilience engineering, and troubleshooting.

## 1. Kubernetes Architecture Topology

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTROL PLANE NODES                      │
│                                                             │
│       ┌──────────────────┐         ┌────────────────────┐   │
│       │ kube-apiserver   │◄───────►│      etcd          │   │
│       │ (Stateless HTTP) │         │ (Raft Consensus DB)│   │
│       └────────┬─────────┘         └────────────────────┘   │
│                │                                            │
│    ┌───────────┴───────────┐         ┌──────────────────┐   │
│    │ kube-controller-mgr   │         │  kube-scheduler  │   │
│    └───────────────────────┘         └──────────────────┘   │
└────────────────┬────────────────────────────────────────────┘
                 │ (mTLS via kubelet API)
┌────────────────▼────────────────────────────────────────────┐
│                      WORKER NODES                           │
│                                                             │
│  ┌───────────────────────┐         ┌─────────────────────┐  │
│  │ kubelet (Node Agent)  │         │ kube-proxy / Cilium │  │
│  └───────────┬───────────┘         └─────────────────────┘  │
│              │                                              │
│  ┌───────────▼───────────┐         ┌─────────────────────┐  │
│  │ containerd (Runtime)  │◄───────►│  Pods (Workloads)   │  │
│  └───────────────────────┘         └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## 2. Critical Production Sizing Rules for Control Plane
- **etcd Performance**: etcd is extraordinarily sensitive to disk I/O latency. Control plane nodes must use fast NVMe SSDs with sub-10ms fsync latency; running etcd on slow magnetic disks or throttled EBS volumes will cause Raft leader election storms and cluster lockup.
- **API Server Scaling**: Run at least 3 API server replicas behind an internal load balancer in multi-zone configurations.

## Related Resources
- [Production Cluster Architecture](./production-cluster-architecture.md)
- [Kubernetes Decision Framework](./kubernetes-decision-framework.md)
