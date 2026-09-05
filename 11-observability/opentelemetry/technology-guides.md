# Enterprise Technology Instrumentation Guides

## 1. Executive Summary
This document provides production-tested architectural instrumentation patterns across the major enterprise runtimes: **.NET, Java, Python, Node.js, Web Browsers, and Mobile Applications**.

---

## 2. .NET 8 / C# Enterprise Pattern

```csharp
// Program.cs - ASP.NET Core 8 Web API
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;
using OpenTelemetry.Metrics;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenTelemetry()
    .ConfigureResource(resource => resource
        .AddService(serviceName: "checkout-service", serviceVersion: "1.0.0")
        .AddAttributes(new Dictionary<string, object> {
            ["deployment.environment"] = builder.Environment.EnvironmentName
        }))
    .WithTracing(tracing => tracing
        .AddAspNetCoreInstrumentation(opts => {
            opts.RecordException = true;
            // Sanitize dynamic route paths to preserve low cardinality
            opts.Filter = httpContext => !httpContext.Request.Path.StartsWithSegments("/health");
        })
        .AddHttpClientInstrumentation()
        .AddEntityFrameworkCoreInstrumentation()
        .AddOtlpExporter(opts => {
            opts.Endpoint = new Uri("http://localhost:4317"); // Localhost Node Agent
            opts.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.Grpc;
        }))
    .WithMetrics(metrics => metrics
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddRuntimeInstrumentation()
        .AddOtlpExporter());
```

---

## 3. Java 21 / Spring Boot 3 Enterprise Pattern

```xml
<!-- pom.xml -->
<dependency>
    <groupId>io.opentelemetry</groupId>
    <artifactId>opentelemetry-api</artifactId>
    <version>1.38.0</version>
</dependency>
```

```java
// Production Service Instrumentation using OTel API
@Service
public class PaymentProcessingService {
    private static final Tracer TRACER = GlobalOpenTelemetry.getTracer("com.enterprise.payment");

    public PaymentConfirmation processPayment(PaymentRequest request) {
        Span span = TRACER.spanBuilder("AuthorizeCardPayment")
                          .setSpanKind(SpanKind.INTERNAL)
                          .startSpan();

        try (Scope scope = span.makeCurrent()) {
            span.setAttribute("payment.method", request.getMethod());
            span.setAttribute("payment.amount", request.getAmount().doubleValue());

            PaymentConfirmation confirmation = externalGatewayClient.authorize(request);
            span.setAttribute("payment.authorization_code", confirmation.getAuthCode());
            span.setStatus(StatusCode.OK);
            return confirmation;
        } catch (PaymentDeclinedException ex) {
            span.setStatus(StatusCode.ERROR, "Payment declined by issuing bank");
            span.recordException(ex);
            throw ex;
        } finally {
            span.end();
        }
    }
}
```

---

## 4. Python 3.11 / FastAPI Enterprise Pattern

```python
# main.py - FastAPI Enterprise Setup
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

resource = Resource.create({
    "service.name": "inventory-api",
    "deployment.environment": "production"
})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="localhost:4317", insecure=True))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

app = FastAPI()

# Auto-instrument FastAPI routes and SQLAlchemy
FastAPIInstrumentor.instrument_app(app)
SQLAlchemyInstrumentor().instrument()
```

---

## 5. Node.js / TypeScript Enterprise Pattern

```typescript
// instrumentation.ts - Executed before application code
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-grpc';
import { Resource } from '@opentelemetry/resources';
import { SEMRESATTRS_SERVICE_NAME } from '@opentelemetry/semantic-conventions';

const sdk = new NodeSDK({
  resource: new Resource({
    [SEMRESATTRS_SERVICE_NAME]: 'notification-service',
  }),
  traceExporter: new OTLPTraceExporter({
    url: 'grpc://localhost:4317',
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      // Disable noisy fs / DNS auto-spans
      '@opentelemetry/instrumentation-fs': { enabled: false },
    }),
  ],
});

sdk.start();
```
