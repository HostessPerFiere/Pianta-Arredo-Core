# Platform Strategy

## Purpose

Pianta-Arredo Core is an open-source platform implementing a Spatial Intelligence Engine (SIE).

The engine is designed to model, validate, analyze and transform physical spaces independently of any specific industry or user interface.

Pianta-Arredo is the first application built on top of this platform.

---

# Vision

The long-term objective is to provide a reusable engine capable of supporting multiple professional domains involving physical spaces.

The engine should remain domain-independent.

Business rules belong to specialized packages.

---

# Platform Layers

Spatial Intelligence Engine

↓

Domain Packages

↓

Applications

---

# Spatial Intelligence Engine

The engine is responsible for:

- geometric modeling
- topology
- validation
- spatial reasoning
- workflow orchestration
- export
- integrations

The engine contains no domain-specific knowledge.

---

# Domain Packages

A Domain Package specializes the engine for a specific field.

Each package provides:

- business rules
- workflows
- validation rules
- catalogs
- templates
- terminology

Examples:

- Residential Package
- Office Package
- Retail Package
- Exhibition Package
- Hospitality Package
- Healthcare Package
- Industrial Package

Packages may depend on the engine.

The engine must never depend on packages.

---

# Applications

Applications provide user interaction.

Examples:

- Pianta-Arredo
- Web Platform
- Desktop Application
- Mobile App
- API Service

Applications may combine one or more Domain Packages.

---

# Dependency Rule

Applications

↓

Domain Packages

↓

Spatial Intelligence Engine

Never the opposite.

---

# Extensibility

New industries should be supported by creating new Domain Packages.

No modification of the engine should be required for introducing a new business domain.

---

# Open Architecture

The platform encourages:

- open standards
- replaceable components
- modular development
- independent testing
- community contributions

---

# Commercial Strategy

The engine remains the common technological foundation.

Commercial value is created through:

- specialized applications
- professional workflows
- premium integrations
- enterprise services
- industry-specific packages

This separation allows the platform to evolve without coupling business strategy to the core architecture.
