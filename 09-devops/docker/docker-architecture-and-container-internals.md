# Docker Architecture and Container Internals

Containers do not exist as physical hardware virtualization constructs. A container is a standard Linux process governed by kernel isolation primitives.

## 1. The Kernel Primitives Powering Containers

```
┌─────────────────────────────────────────────────────────────┐
│                    LINUX HOST KERNEL                        │
├──────────────────────────────┬──────────────────────────────┤
│ NAMESPACES (What you can see)│ CGROUPS (How much you use)   │
│ - pid: Process tree isolation│ - cpu.max: CPU core quotas   │
│ - net: Network interface/IP  │ - memory.max: RAM limits/OOM │
│ - mnt: Filesystem mount points│ - io.weight: Disk I/O limits│
│ - ipc: Shared memory IPC     │ - pids.max: Fork bomb defense│
├──────────────────────────────┴──────────────────────────────┤
│ OVERLAYFS (Storage Driver)                                  │
│ - LowerDir (Read-only immutable base image layers)          │
│ - UpperDir (Read-write ephemeral container layer)           │
│ - MergedDir (Unified virtual view presented to application) │
└─────────────────────────────────────────────────────────────┘
```

## 2. Container Runtime Stack
- **Docker CLI / Engine**: High-level developer UX wrapper.
- **containerd**: Industry-standard core container runtime daemon managing image transfer and storage.
- **runc**: Low-level OCI reference implementation that interacts directly with the Linux kernel to instantiate namespaces and cgroups.

## Related Resources
- [Production Dockerfile Optimization](./production-dockerfile-optimization.md)
- [Container Decisions](./container-architecture-decisions.md)
