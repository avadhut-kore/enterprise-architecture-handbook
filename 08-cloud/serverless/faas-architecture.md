# Function-as-a-Service (FaaS) Architecture

## Executive Summary

Function-as-a-Service (FaaS) executes individual application functions in response to discrete events. Platforms utilize lightweight **MicroVMs** (e.g., AWS Firecracker, Google gVisor) to provide hardware-level virtualization isolation with container-level startup speeds.

---

## 1. Firecracker MicroVM Execution Architecture

```mermaid
graph TD
    BareMetal[Physical Metal Host] --> KVM[Linux KVM Hypervisor]
    KVM --> MicroVM1[Firecracker MicroVM 1: 5MB RAM Overhead / Boot in 5ms]
    KVM --> MicroVM2[Firecracker MicroVM 2: 5MB RAM Overhead / Boot in 5ms]

    MicroVM1 --> GuestKernel1[Minimal Linux Guest Kernel]
    GuestKernel1 --> Runtime1[Language Runtime: Node.js / Python / Go]
    Runtime1 --> Handler1[User Function Handler: exports.handler = ...]
```

---

## 2. MicroVM Advantages
- **Security Isolation**: Unlike standard container runtimes that share the host kernel, MicroVMs provide distinct virtualized guest kernels, eliminating container breakout risks in multi-tenant environments.
- **Ultra-Fast Provisioning**: Boots a secure microVM in under $5\text{ milliseconds}$ with less than $5\text{ MB}$ of memory overhead.
