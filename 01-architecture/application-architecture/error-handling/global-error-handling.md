# Global Error Handling Middleware

## 1. Ingress Filter Architecture
Implement a single global exception middleware at the edge of the API pipeline (ASP.NET Core `UseExceptionHandler`, Express error middleware, Spring `@ControllerAdvice`) to catch any unhandled escapees.
