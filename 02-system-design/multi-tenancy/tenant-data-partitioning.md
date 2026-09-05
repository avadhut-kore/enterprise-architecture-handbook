# Tenant Data Partitioning

## 1. Composite Sharding Keys
In distributed NoSQL and sharded SQL databases:
$$\text{Partition Key} = (\text{tenant\_id}, \text{entity\_id})$$
* Guarantees that all data for a single tenant is co-located on the same physical shard or partition, enabling single-partition queries and eliminating distributed cross-shard scans.
