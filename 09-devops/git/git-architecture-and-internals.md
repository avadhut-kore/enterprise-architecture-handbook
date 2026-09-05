# Git Architecture and Internals

Git is fundamentally a content-addressable filesystem with a Directed Acyclic Graph (DAG) layer built on top. Understanding Git internals is essential for debugging merge anomalies, optimizing large repositories, and designing automated CI/CD runners.

## 1. The Four Core Git Object Types

```
┌─────────────────────────────────────────────────────────────┐
│                          COMMIT                             │
│ - Points to Tree object SHA                                 │
│ - Points to Parent Commit SHA(s)                            │
│ - Author, Committer, GPG Signature, Commit Message          │
├──────────────────────────────┬──────────────────────────────┤
│             TREE             │             BLOB             │
│ - Directory representation   │ - Raw file content payload   │
│ - Maps file names to SHA-1   │ - Content-addressed by hash  │
│   of Blobs or Subtrees       │ - Does NOT store file name   │
├──────────────────────────────┴──────────────────────────────┤
│                             TAG                             │
│ - Annotated cryptographic reference pointing to a Commit    │
└─────────────────────────────────────────────────────────────┘
```

## 2. Storage & Optimization Mechanics

- **Loose Objects vs Packfiles**: New objects are stored as loose compressed zlib files (`.git/objects/xx/yyy`). Running `git gc` or pushing to remote repacks loose objects into compressed `.pack` files with delta compression.
- **Git Shallow Clones (`--depth 1`)**: Vital for enterprise CI/CD runners to avoid downloading gigabytes of historical git history, reducing checkout time from minutes to seconds.
- **Git Sparse Checkout & Blobless Clones (`--filter=blob:none`)**: Enables scalable monorepo operations where developers only download file trees and fetch blobs on-demand.

## Related Resources
- [Branching Strategies Evaluation](./branching-strategies-evaluation.md)
- [Monorepo vs Polyrepo Architecture](./monorepo-vs-polyrepo-architecture.md)
