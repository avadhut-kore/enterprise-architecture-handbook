# Monolith Pruning & Legacy Codebase Retirement

## 1. Dead Code Elimination Lifecycle
Once traffic is 100% migrated to an extracted microservice and data parity is verified for 30 days:
1. **Disable Legacy Routing**: Update the API Facade to permanently route all traffic to the new service; remove the legacy route fallback.
2. **Quarantine Monolithic Code**: Mark the monolithic module as `@Deprecated` and remove read/write permissions from its database user.
3. **Prune Source Code**: Delete the controller, service, and data access classes from the monolithic repository.
4. **Drop Legacy Database Tables**: Take a final database backup, archive cold data, and drop deprecated tables to reclaim database memory and disk space.
