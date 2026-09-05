# Security Runbook: Enterprise Ransomware Containment

## Executive Summary

1. **Sever Network Interconnects**: Immediately disable DirectConnect / ExpressRoute BGP sessions to prevent ransomware lateral movement into cloud landing zones.
2. **Isolate Compromised Subnets**: Update Security Groups to drop all inbound and outbound traffic to affected VMs/clusters.
3. **Restore from Immutable WORM Backups**: Re-provision clean virtual machines from trusted golden images; restore databases from immutable S3 Object Lock backups.
