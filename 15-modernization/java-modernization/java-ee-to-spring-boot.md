# Java EE (Jakarta EE) to Spring Boot Migration

## 1. Component Mapping Matrix

| Java EE / Jakarta EE Primitive | Spring Boot Cloud-Native Equivalent |
| :--- | :--- |
| `@Stateless` / `@Stateful` Session Bean | `@Service` / Stateless Spring Bean |
| Message-Driven Bean (`@MessageDriven`) | `@KafkaListener` / `@JmsListener` |
| `persistence.xml` & JPA EntityManager | Spring Data JPA / Hibernate `JpaRepository` |
| JAX-RS / `@Path` / Servlets | Spring MVC `@RestController` / `@GetMapping` |
| JNDI DataSource Lookup | Spring Boot `application.yml` HikariCP connection pool |
