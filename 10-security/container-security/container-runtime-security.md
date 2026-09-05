# Container Runtime Security & eBPF (Falco)

## Executive Summary

Static scanning cannot detect zero-day attacks or malicious insider behavior. Runtime security uses **Extended Berkeley Packet Filter (eBPF)** to inspect kernel system calls (syscalls) in real time without modifying application code.

---

## 1. Falco Behavioral Rules Example
Detecting an unauthorized shell spawned inside a container:
```yaml
- rule: Terminal Shell Spawned in Container
  desc: A shell was spawned inside a running production container
  condition: >
    spawned_process and container and
    shell_procs and not user_known_shell_procs
  output: >
    ALERT: Shell spawned in container (user=%user.name pod=%k8s.pod.name 
    ns=%k8s.ns.name image=%container.image.repository cmd=%proc.cmdline)
  priority: CRITICAL
  tags: [container, mitre_execution]
```
