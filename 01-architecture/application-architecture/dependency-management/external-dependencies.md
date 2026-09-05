# External Dependencies & Cloud SDK Isolation

## 1. The Threat of Vendor SDK Contamination

If an application imports AWS SDK (`AmazonS3Client`) or Azure Blob Storage directly into domain use cases:
- Mocking and testing becomes tedious and fragile.
- Migrating cloud providers or running local integration tests requires cloud emulators (LocalStack).
- The domain becomes coupled to vendor-specific exception classes and API quirks.

---

## 2. The Port-and-Adapter Solution

```mermaid
flowchart LR
    subgraph CoreApplication [Core Application]
        UseCase[UploadInvoiceUseCase] --> IStorageService[Interface: IFileStoragePort]
    end

    subgraph InfrastructureTier [Infrastructure Adapters]
        IStorageService <|.. S3Adapter[AwsS3StorageAdapter]
        IStorageService <|.. AzureAdapter[AzureBlobStorageAdapter]
        IStorageService <|.. LocalDiskAdapter[LocalDiskStorageAdapter]
    end
```
