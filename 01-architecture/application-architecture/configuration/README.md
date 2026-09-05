# Application Configuration Architecture

Configuration management defines how runtime parameters, credentials, feature switches, and environment behaviors are loaded, validated, secured, and updated across enterprise software deployments.

---

## The Four Categories of Runtime Data

```
+--------------------+-----------------------+-----------------------+-----------------------+
| Category           | Definition            | Sensitivity           | Mutation Frequency    |
+--------------------+-----------------------+-----------------------+-----------------------+
| Configuration      | Non-sensitive params  | Low (Checked into Git)| Low (Deploy-time)     |
|                    | (URLs, Timeouts)      |                       |                       |
+--------------------+-----------------------+-----------------------+-----------------------+
| Secrets            | Sensitive credentials | High (Vault, KMS)     | Low (90-day rotation) |
|                    | (API Keys, DB Passwds)|                       |                       |
+--------------------+-----------------------+-----------------------+-----------------------+
| Feature Flags      | Conditional toggles   | Low (LaunchDarkly, DB)| High (Runtime flip)   |
|                    | (Rollout percentages) |                       |                       |
+--------------------+-----------------------+-----------------------+-----------------------+
| Runtime State      | In-memory domain data | High (Encrypted)      | Real-time (Millisecond|
|                    | (Active shopping cart)|                       | transactions)         |
+--------------------+-----------------------+-----------------------+-----------------------+
```

---

## Documents in this Section
- [Configuration Principles](configuration-principles.md)
- [Environment Configuration](environment-configuration.md)
- [Feature Flags](feature-flags.md)
- [Secret Configuration](secret-configuration.md)
- [Configuration Validation](configuration-validation.md)
- [Configuration Versioning](configuration-versioning.md)
- [Configuration Drift](configuration-drift.md)
- [Dynamic Configuration](dynamic-configuration.md)
- [Configuration Security](configuration-security.md)
