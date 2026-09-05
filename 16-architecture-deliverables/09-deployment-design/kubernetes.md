# Kubernetes Architecture Standards
* Separate namespaces per microservice and lifecycle environment; enforce PodDisruptionBudgets (`minAvailable: 1`).
