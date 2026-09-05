# Right to be Forgotten & Distributed Erasure Architecture

## Executive Summary

When an erasure request is received:
1. An event (`UserErasureRequested`) is published to Kafka.
2. Microservices consume the event and purge user records from transactional databases.
3. Customer-specific KMS keys are destroyed, cryptographically shredding all historical backups.
