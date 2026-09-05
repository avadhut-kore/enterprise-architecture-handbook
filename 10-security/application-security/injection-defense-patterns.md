# Injection Defense Architecture (SQL, Command, LDAP)

## Executive Summary

Injection occurs when untrusted user input is concatenated directly into an interpreter (SQL engine, OS shell, LDAP directory) instead of being treated as literal data.

---

## 1. Absolute Rule: Prohibition of Dynamic Concatenation

```csharp
// FATAL VULNERABILITY: Raw String Concatenation
var query = "SELECT * FROM Users WHERE Email = '" + userInput + "'";

// SECURE ARCHITECTURE: Compile-Time Parameterized Query
var query = "SELECT * FROM Users WHERE Email = @email";
command.Parameters.AddWithValue("@email", userInput);
```

### Command Injection Defense:
- **Never invoke the shell**: Ban `exec()`, `system()`, and `eval()`.
- Use structured process execution APIs where command and arguments are passed as discrete arrays:
  ```python
  # SECURE: Passes arguments as an array; no shell interpretation possible
  subprocess.run(["/usr/bin/convert", input_file, output_file], shell=False)
  ```
