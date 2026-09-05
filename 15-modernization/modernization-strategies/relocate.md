# The "Relocate" Strategy: Hypervisor-Level Migration

## 1. Architectural Definition
**Relocate** shifts existing virtualized servers from on-premise hypervisors directly to a cloud-hosted software-defined datacenter running the same virtualization stack (e.g., VMware on AWS, Azure VMware Solution, Google Cloud VMware Engine).

---

## 2. Key Capabilities
- **Zero VM Format Conversion**: No conversion of VMDK to AMI/VHD.
- **Live vMotion Across Direct Connect**: Workloads can be live-migrated over high-bandwidth private circuits with zero application downtime.
- **Consistent Operational Tooling**: Existing SysAdmin staff continue using familiar vCenter, NSX, and vSAN management consoles.
- **Preserved Network Topologies**: Extended Layer-2 networks allow virtual machines to retain their exact on-premise IP addresses in the cloud.
