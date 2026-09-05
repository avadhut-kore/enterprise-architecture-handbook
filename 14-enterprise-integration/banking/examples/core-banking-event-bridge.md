# Implementation Example: Core Banking Event Bridge

## 1. Architecture Context
This component reads account balance changes from a mainframe DB2 database via Change Data Capture (CDC), transforms the legacy EBCDIC data into a CloudEvent JSON structure, and streams it to Kafka to update distributed read caches.

## 2. Debezium CDC to Kafka Configuration
```json
{
  "name": "core-banking-db2-cdc-source",
  "config": {
    "connector.class": "io.debezium.connector.db2.Db2Connector",
    "tasks.max": "1",
    "database.hostname": "mainframe.bank.internal",
    "database.port": "50000",
    "database.user": "db2_cdc_agent",
    "database.password": "${vault:secret/db2_password}",
    "database.dbname": "COREBANK",
    "table.include.list": "BANKING.ACCOUNT_BALANCES",
    "topic.prefix": "core-ledger",
    "tombstones.on.delete": "false"
  }
}
```
