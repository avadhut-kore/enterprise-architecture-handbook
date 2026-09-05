# The "Rehost" Strategy: Lift-and-Shift Migration

## 1. Architectural Definition
**Rehost** (colloquially termed "Lift-and-Shift") migrates application virtual machines, operating systems, and databases from on-premise infrastructure directly to cloud Virtual Machines (AWS EC2, Azure VMs, Google Compute Engine) with zero changes to application code, architecture, or configuration.

---

## 2. When to Use Rehost
- **Impending Datacenter Termination**: When a physical datacenter lease expires within 6 to 9 months and business continuity requires immediate evacuation.
- **Hardware Refresh Avoidance**: When on-premise SAN storage or servers reach end-of-life and capital expenditure for renewal is denied.
- **First Step of a Phased Modernization**: Moving workloads to the cloud first to gain cloud-native telemetry, backup, and network connectivity before undertaking refactoring.

---

## 3. Trade-Offs & Anti-Patterns
- **Pros**: Fastest time-to-cloud; lowest initial engineering risk; automated block-level migration tools (AWS Application Migration Service, Azure Migrate).
- **Cons**: Carries technical debt into the cloud; does not exploit cloud scalability or elasticity; running unoptimized 24/7 over-provisioned VMs often results in higher operational costs than on-premise hosting.
