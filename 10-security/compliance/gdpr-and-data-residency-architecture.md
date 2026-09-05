# GDPR & Data Sovereignty Architecture

## Executive Summary

- **Geographic Data Pinning**: Configure cloud storage buckets and database read replicas strictly within European Union regions (`eu-west-1`, `eu-central-1`).
- **Preventing Cross-Border Replication**: Enforce Cloud Service Control Policies (SCPs) that restrict resource creation exclusively to approved sovereign regions.
