# Docker & Container Architecture

This module establishes architecture standards for container packaging, runtime isolation, multi-stage builds, and production image hardening.

## Contents

- [Docker Architecture and Container Internals](./docker-architecture-and-container-internals.md) — Linux cgroups, namespaces, overlayfs, containerd, and OCI runtime specifications.
- [Production Dockerfile Optimization](./production-dockerfile-optimization.md) — Multi-stage builds, non-root execution, distroless images, minimal attack surfaces, and layer caching.
- [Container Architecture Decisions](./container-architecture-decisions.md) — Decision framework: Container vs VM vs Serverless, one process vs multi-process, distroless vs full OS.

## Core Tenet
Containers are not lightweight virtual machines. They are isolated processes sharing the host Linux kernel constrained by cgroups and namespaces.
