# Architecture

## Overview

Pianta-Arredo Core follows a layered architecture designed to separate user interfaces, application orchestration and computational engines.

The platform is intentionally interface-independent.

ChatGPT is not the core.

A future desktop application is not the core.

A future web application is not the core.

Everything communicates with the Core through the Application Layer.

---

# Architecture

```
Users
    │
    ▼
Presentation Layer
    │
    ▼
Application Layer
    │
    ▼
Core Layer
    │
    ▼
Infrastructure & Integrations
```

---

# Layer 1 — Presentation

The Presentation Layer is responsible only for interacting with users.

Examples:

- ChatGPT
- Web UI
- Desktop UI
- Mobile UI
- REST API
- CLI

Responsibilities

- collect user input
- display results
- upload files
- authentication
- localization

Must NOT

- perform geometry
- validate models
- generate CAD
- access OpenCascade directly

---

# Layer 2 — Application

The Application Layer coordinates every operation.

Main components

- Workflow Engine
- AI Orchestrator
- Task Manager

Responsibilities

- execute workflows
- coordinate engines
- manage execution order
- manage project state
- collect results

Must NOT

- perform geometry calculations
- create CAD entities
- manipulate meshes
- export files directly

---

# Layer 3 — Core

The Core Layer contains every computational engine.

This layer represents the heart of the platform.

Main components

- Geometry Kernel
- Validation Engine
- CAD Engine
- Furniture Engine
- Export Engine
- Vision Engine
- Catalog Engine

Responsibilities

- geometry
- validation
- topology
- room recognition
- CAD generation
- furniture placement
- export generation

Must NEVER depend on

- ChatGPT
- Web UI
- Desktop UI
- API implementation

---

# Infrastructure

Infrastructure contains external software.

Examples

- OpenCascade
- FreeCAD
- Sweet Home 3D
- LibreCAD
- Blender
- OpenCV
- Tesseract
- PostgreSQL
- GitHub

Infrastructure components can be replaced without redesigning the platform.

---

# Dependency Rule

Dependencies always point downwards.

Presentation

↓

Application

↓

Core

↓

Infrastructure

Never the opposite.

---

# Design Principles

## Separation of Concerns

Each module has one responsibility.

## Dependency Inversion

High-level modules never depend on UI technologies.

## Replaceable Components

Every engine should be replaceable.

## Testability

Every engine must be independently testable.

## Open Standards

The platform should prefer interoperable formats.

---

# Future Evolution

Future releases may introduce:

- BIM Engine
- Simulation Engine
- Structural Engine
- Cost Estimation Engine
- AI Planning Engine

without changing the existing architecture.
