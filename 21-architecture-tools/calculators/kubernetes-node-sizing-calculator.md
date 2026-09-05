# Kubernetes Node Sizing & Pod Density Calculator

## Formula
$$\text{Nodes Required} = \max\left(\frac{\sum \text{Pod CPU Requests}}{\text{Allocatable vCPU per Node}}, \frac{\sum \text{Pod Memory Requests}}{\text{Allocatable RAM per Node}}\right) \times (1 + \text{Surge Headroom})$$

- Note: Worker nodes reserve 5–10% of physical capacity for OS and kubelet overhead (`kube-reserved` and `system-reserved`).
