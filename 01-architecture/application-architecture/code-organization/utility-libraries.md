# Utility Libraries: Eliminating "Utils" Junk Drawers

## 1. Architectural Guidance
- **Prohibit Generic Class Names**: Ban `Helper`, `Utils`, `Common`, `Manager`, and `Handler` unless qualified by specific domain intent.
- **Prefer Extension Methods or Domain Types**: Instead of `StringUtils.ValidateEmail(str)`, create a strongly typed `EmailAddress` Value Object that validates itself upon construction.
