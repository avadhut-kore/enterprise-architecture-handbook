# Legacy Systems Integration Architecture Library

## 1. Overview
Enterprise modernization rarely permits "rip and replace". Solution architects must integrate modern cloud-native systems with legacy mainframes, AS/400 midrange servers, COBOL batch engines, green-screen terminal emulators, and unmanaged legacy relational databases.

## 2. Directory Structure
- [legacy-integration.md](legacy-integration.md): Core architectural principles for legacy integration.
- [mainframe.md](mainframe.md): IBM z/OS mainframe architecture, CICS, IMS, and MIPS cost reduction.
- [cobol.md](cobol.md): Parsing and transforming COBOL copybooks and EBCDIC character sets.
- [terminal-systems.md](terminal-systems.md): Screen scraping vs. programmatic terminal emulation (TN3270 / TN5250).
- [database-integration.md](database-integration.md): Direct DB reads, CDC log scraping, and DB2/VSAM interfaces.
- [file-based-integration.md](file-based-integration.md): Managed File Transfer (MFT), fixed-width flat files, and SFTP.
- [batch-processing.md](batch-processing.md): Mainframe batch windows, JCL jobs, and modern event bridges.
- [message-based-integration.md](message-based-integration.md): IBM MQ (MQSeries) bridges to Apache Kafka and cloud brokers.
- [api-wrapping.md](api-wrapping.md): Wrapping legacy transactions with REST/gRPC microservice facades.
- [strangler-pattern.md](strangler-pattern.md): Incremental legacy replacement via the Strangler Fig pattern.
- [anti-corruption-layer.md](anti-corruption-layer.md): Preventing legacy domain models from corrupting modern services.
- [legacy-modernization.md](legacy-modernization.md): Migration pathways: Rehost, Refactor, Replatform, Replace.
- [coexistence.md](coexistence.md): Maintaining multi-year dual-run state consistency.
- [migration.md](migration.md): Phased cutover, data migration, and fallback rollbacks.
- [synchronization.md](synchronization.md): Bi-directional data synchronization and conflict resolution.
- [reconciliation.md](reconciliation.md): Automated legacy-to-cloud break detection.
- [reliability.md](reliability.md): Throttling, backpressure, and mainframe connection pooling.
- [observability.md](observability.md): Correlating distributed cloud traces with mainframe SMF logs.
- [security.md](security.md): RACF, ACF2, Top Secret security translation to modern OAuth2/mTLS.
- [reference-architecture.md](reference-architecture.md): Legacy Mainframe-to-Cloud Modernization Reference Architecture.
