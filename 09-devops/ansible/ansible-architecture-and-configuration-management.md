# Ansible Architecture and Configuration Management

Unlike Terraform, which excels at provisioning cloud infrastructure resources, Ansible specializes in configuring operating systems, installing packages, and managing software configuration inside VMs and bare-metal servers.

## 1. Core Principles
- **Agentless Execution**: Connects via native SSH (Linux) or WinRM (Windows) using Python on the target host; zero agent software to install, patch, or maintain.
- **Idempotent Tasks**: Tasks define desired state. If a package is already installed or a config file already matches, Ansible makes no changes.
- **Role Reusability**: Package tasks, handlers, variables, and templates into modular, versioned roles (`ansible-galaxy`).

## Related Resources
- [Terraform vs Ansible Decision Matrix](./terraform-vs-ansible-decision-matrix.md)
- [Infrastructure as Code](../infrastructure-as-code/README.md)
