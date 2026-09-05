# Interface Boundaries & Interface Segregation

## 1. The Interface Segregation Principle (ISP)

> **Clients should not be forced to depend upon interfaces that they do not use.**

---

## 2. Fat vs Role Interfaces

```
Antipattern: The "Fat" Repository Interface
interface IUserRepository {
    User GetById(Guid id);
    void Save(User user);
    void UpdatePasswordHash(Guid id, string hash);
    void IncrementFailedLogins(Guid id);
    List<UserReportDto> GetAnnualComplianceReport(); // Leaks reporting into core repo!
}

Architectural Target: Role-Based Segregation
interface IUserReader { User GetById(Guid id); }
interface IUserWriter { void Save(User user); }
interface IUserComplianceReporter { List<UserReportDto> GetAnnualComplianceReport(); }
```
