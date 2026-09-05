# Infrastructure Hardening & Immutable Golden Images

## Executive Summary

Manually logging into servers via SSH to patch operating systems creates configuration drift and introduces severe security vulnerabilities. Modern infrastructure mandates **Immutable Infrastructure**.

---

## Architectural Workflow:
1. **Automated Image Pipeline**: HashiCorp Packer builds base AMIs/VHDs weekly using the latest patched OS kernel.
2. **CIS Benchmark Level 2 Hardening**: Ansible applies CIS benchmarks (disabling legacy filesystems, removing compilers, configuring auditd).
3. **Automated Testing**: Testinfra validates that ports are closed and root logins are disabled.
4. **Immutable Deployment**: Production servers are replaced entirely via Auto Scaling rolling updates; zero in-place SSH patching permitted.
