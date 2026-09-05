# Configuration Validation & Startup Gates

## 1. Fail-Fast Startup Validation
Applications must validate all configuration on boot:
```csharp
// Example Architectural Validation Guard
public record DatabaseConfig(string ConnectionString, int MaxPoolSize)
{
    public void Validate() {
        if (string.IsNullOrWhiteSpace(ConnectionString)) 
            throw new ConfigurationException("ConnectionString is required.");
        if (MaxPoolSize <= 0 || MaxPoolSize > 500)
            throw new ConfigurationException("MaxPoolSize must be between 1 and 500.");
    }
}
```
If configuration is invalid, crash immediately (`exit(1)`) to halt faulty rollouts in CI/CD.
