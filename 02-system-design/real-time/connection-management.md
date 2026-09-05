# Connection Management at Scale (C10M)

## 1. Operating System & Kernel Tuning for 1M Concurrent Sockets
To support $1,000,000$ concurrent idle WebSocket connections on a cluster of Linux edge servers:

### 1. File Descriptor Ceilings (`/etc/security/limits.conf`)
Every open TCP connection requires a Linux file descriptor. Set hard limits to $>1\text{ Million}$:
```text
* soft nofile 1048576
* hard nofile 1048576
```

### 2. TCP Buffer Memory Tuning (`/etc/sysctl.conf`)
By default, Linux allocates up to $128\text{ KB}$ per socket buffer. $1\text{M}$ connections would consume $128\text{ GB RAM}$ in socket buffers alone. Tune default buffers to minimum:
```ini
net.ipv4.tcp_rmem = 4096 4096 16777216  # Min default 4KB read buffer
net.ipv4.tcp_wmem = 4096 4096 16777216  # Min default 4KB write buffer
net.core.somaxconn = 65535              # Backlog queue size
```
*At 4KB buffer per socket, 1M connections consume only **4 GB of kernel RAM**.*
