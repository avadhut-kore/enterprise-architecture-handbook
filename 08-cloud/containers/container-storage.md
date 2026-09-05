# Container Storage Architecture: Ephemeral Layers & Volumes

## Executive Summary

Containers are designed to be ephemeral. Data written to the container's default writable layer is lost when the container is destroyed. Managing state requires externalized storage volumes.

---

## 1. Storage Drivers & Volume Types

```mermaid
graph TD
    Container[Running Container Process]
    Container --> Writable[1. Ephemeral Writable Layer: Overlay2 Driver / Destroyed on Container Stop]
    Container --> BindMount[2. Bind Mount: Maps Host Directory /tmp/data to Container]
    Container --> NamedVol[3. Named Volume: Managed by Storage Driver in /var/lib/docker/volumes]
    Container --> CSI[4. CSI Volume: Cloud Block/File Storage EBS / Azure Disk / Persistent Disk]
```

---

## 2. Overlay2 Storage Driver Mechanics

- **Copy-on-Write (CoW)**: When a container modifies an existing file from an underlying image layer, the storage driver copies the file up to the container's thin writable layer before applying changes.
- **Architectural Consequence**: Heavy random disk I/O (e.g., database writes) on an Overlay2 CoW filesystem incurs severe performance degradation. **All database data files, transaction logs, and high-throughput logging sinks must be mounted to dedicated block storage volumes (EBS/Disk), completely bypassing the storage driver.**
