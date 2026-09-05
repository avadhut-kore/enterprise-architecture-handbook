# Block Storage Architecture

## 1. Low-Latency Raw Block Access
Block storage presents raw blocks directly to the operating system as an unformatted block device (e.g., `/dev/nvme0n1`).
* **IOPS & Low Latency**: Provides the lowest possible latency ($<1\text{ ms}$) and highest random IOPS ($250,000+\text{ IOPS}$).
* **Single Instance Attachment**: Typically attaches to exactly one virtual machine host at a time (e.g., AWS EBS), making it unsuitable for multi-node shared media pools.
