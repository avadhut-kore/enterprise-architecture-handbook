# Object Storage Architecture

## 1. Flat Namespace & Metadata Architecture
Unlike hierarchical file systems with nested directory trees, object storage organizes data in a flat namespace:
$$\text{Object} = \text{Unique Key} + \text{Binary Data} + \text{Metadata} + \text{Version ID}$$
* Key: `users/123/profile.jpg` (The slashes are merely string characters in the key, not physical OS directories).
* Scaling: Because there are no filesystem directory locks or inode tables, object stores scale horizontally to exabytes of data across thousands of commodity storage nodes.
