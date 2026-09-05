# Terraform Portability: Dispelling the "Write Once" Myth

## Executive Summary

A pervasive misconception among IT leadership is that using HashiCorp Terraform or OpenTofu enables "writing infrastructure once and running it on AWS, Azure, or GCP." 

> **The Reality**: Terraform provides a **consistent workflow** (plan, apply, state), but **zero code portability** across cloud providers.

---

## 1. Provider Syntax Divergence

A simple virtual machine declaration cannot be shared across cloud providers:

```hcl
# AWS EC2 Instance
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"
  subnet_id     = var.subnet_id
}

# Azure Virtual Machine
resource "azurerm_linux_virtual_machine" "web" {
  name                = "web-vm"
  resource_group_name = var.rg_name
  size                = "Standard_B2s"
  admin_username      = "adminuser"
  network_interface_ids = [var.nic_id]
}

# GCP Compute Instance
resource "google_compute_instance" "web" {
  name         = "web-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }
}
```

---

## 2. Recommended Enterprise IaC Architecture

1. **Do Not Build Pseudo-Generic Modules**:
   - Avoid creating massive monolithic modules attempting to abstract `compute_instance` across AWS and Azure. The resulting abstraction is leaky, unmaintainable, and breaks whenever a provider releases new features.
2. **Layered Module Design**:
   - Author separate provider-specific implementation modules (`modules/aws/networking`, `modules/azure/networking`).
   - Standardize only the **module output contracts** (e.g., both modules output `vpc_id`, `private_subnet_ids`, `cidr_block`) so that downstream application deployment modules consume consistent variable names.
