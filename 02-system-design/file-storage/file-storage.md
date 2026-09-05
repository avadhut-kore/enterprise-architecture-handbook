# File Storage (NFS / EFS) Architecture

## 1. POSIX Shared Filesystems
Network Attached Storage (NAS) provides a traditional hierarchical filesystem accessible concurrently across thousands of compute nodes over NFS or SMB protocols:
* **Advantages**: Full POSIX compatibility (`open`, `read`, `write`, directory locking).
* **Disadvantages**: Slower performance and significantly higher cost per gigabyte ($\approx 10\times$ more expensive than cloud object storage).
