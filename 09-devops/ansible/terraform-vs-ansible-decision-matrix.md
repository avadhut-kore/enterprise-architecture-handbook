# Terraform vs Ansible Architecture Decision Matrix

A common architectural fallacy is asking: *"Should we use Terraform OR Ansible?"* In reality, they address fundamentally different layers of the technology stack.

## 1. Comparative Analysis

| Requirement / Layer | Terraform (Infrastructure Provisioner) | Ansible (Configuration Manager) | Architectural Synergy |
| :--- | :--- | :--- | :--- |
| **Primary Domain** | Cloud API resources (VPCs, Subnets, Databases, K8s clusters). | In-server configuration (Nginx configs, system users, kernel sysctl). | Terraform builds the house; Ansible paints the walls. |
| **State Model** | Explicit State File (`terraform.tfstate`) tracking real-world resources. | Stateless; queries live target servers directly during playbook execution. | Terraform tracks cloud lifecycle; Ansible mutates target hosts. |
| **Execution Architecture** | Client communicates with Cloud APIs over HTTPS. | Master connects to target servers via SSH/WinRM. | Complementary network paths. |
| **Immutable vs Mutable** | Ideal for Immutable Infrastructure (Bake AMI, deploy fresh VM/container).| Ideal for Mutable Infrastructure (Patch existing long-lived servers). | In modern cloud-native, Terraform + Packer often replaces Ansible entirely! |

## 2. The Modern Cloud-Native Shift
In pure container and Kubernetes environments, Ansible is largely redundant:
- **Terraform** provisions the cloud VPC, IAM, and EKS clusters.
- **Docker / Cloud Native Buildpacks** package application configuration into immutable containers.
- **Helm / GitOps** manages runtime configuration manifests.
Ansible remains essential for bare-metal datacenters, legacy VM patching, and network device automation (routers/switches).

## Related Resources
- [Terraform Architecture](../terraform/README.md)
- [Ansible Architecture](./ansible-architecture-and-configuration-management.md)
