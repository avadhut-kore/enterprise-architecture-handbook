# Modern Python Enterprise Architecture (Python 3.12+)

This directory establishes architectural standards, runtime design patterns, and engineering trade-offs for modern enterprise applications built on **Python 3.12+**.

> [!IMPORTANT]
> **Architecture, Not Syntax**: This documentation evaluates the CPython execution model, the Global Interpreter Lock (GIL) and free-threaded Python (PEP 703), asyncio event loop saturation, memory management with PyMalloc, Pydantic type boundaries, and ASGI/WSGI gateway topology.

---

## Subsystem Navigation

| Subsystem | Scope & Focus |
| :--- | :--- |
| [Architecture](architecture/) | FastAPI vs Django, asyncio event loop, Clean & Hexagonal Python |
| [API Engineering](api/) | Pydantic v2 validation, OpenAPI 3.0 generation, RFC 7807 problem details |
| [Data Access](data/) | SQLAlchemy 2.0 async ORM, connection pool sizing, Alembic migrations |
| [Resilience](resilience/) | Circuit breakers, timeouts, retries, and backpressure in async systems |
| [Testing Architecture](testing/) | Pytest fixtures, Testcontainers Python, import-linter architecture tests |
| [Performance](performance/) | Asyncio concurrency, multiprocessing vs multithreading, memory profiling |
| [Security](security/) | OAuth2/OIDC, JWT verification, input sanitization, secret management |
