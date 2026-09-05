# API Boundary Rules

## 1. Controller Hygiene
Ensure controllers do not directly inject `DbContext` or repository instances, but communicate strictly through MediatR/Command Handlers.
