# Angular Architecture: Global Error Handling via ErrorHandler

## 1. Architectural Purpose & Problem Context
Custom global ErrorHandler, Sentry integration, and unhandled promise rejection logging.

---

## 2. Structural Blueprint & Component Lifecycle

```mermaid
flowchart TB
    Client[User Interaction] --> Component[Standalone Component with Signals]
    Component --> Facade[Feature Facade Service]
    Facade --> Store[SignalStore / NgRx ComponentStore]
    Facade --> HttpService[Angular HttpClient Service]
    HttpService --> Interceptor[HttpInterceptor Chain]
    Interceptor --> Backend[Enterprise API Gateway]
```

---

## 3. Production Patterns & Anti-Patterns

### Recommended Architecture Practice:
- Adopt modern Standalone Components and Signals for fine-grained reactivity without Zone.js overhead.
- Use Feature Facade services to decouple components from complex RxJS / NgRx state stores.

### Common Failure Modes:
- **RxJS Memory Leaks**: Subscribing to Observables inside components without `takeUntilDestroyed()` or async pipe, leaking component instances in memory.
- **Overusing NgRx Global Store**: Storing trivial local UI state in complex global Redux actions and reducers.
