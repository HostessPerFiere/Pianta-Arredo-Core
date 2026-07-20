# Pianta-Arredo-Core — 05-guides-examples-and-releases.md

Documento consolidato per il GPT.

---

## File originale: `RELEASE-0.1-MANIFEST.md`

# Release 0.1 Manifest

Release: 0.1 — Foundation

Tag: `v0.1.0-foundation`

Status: Completed

## Packages

- Package A — Repository Foundation
- Package B — Core Documentation
- Package C — Architecture Decisions
- Package D — Service Specification
- Package E — Developer Experience

## Package manifests

- `PACKAGE-A-MANIFEST.md`
- `PACKAGE-B-MANIFEST.md`
- `PACKAGE-C-MANIFEST.md`
- `PACKAGE-D-MANIFEST.md`
- `PACKAGE-E-MANIFEST.md`

## Foundation documents

- `README.md`
- `PROJECT_PRINCIPLES.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `GOVERNANCE.md`
- `SUPPORT.md`
- `LICENSE`

## Documentation

- `docs/INDEX.md`
- `docs/00-vision.md`
- `docs/00b-spatial-intelligence-specification.md`
- `docs/01-architecture.md`
- `docs/02-data-model.md`
- `docs/02b-platform-strategy.md`
- `docs/03-system-glossary.md`
- `docs/04-domain-taxonomy.md`
- `docs/05-system-workflow.md`
- `docs/05b-system-state.md`
- `docs/05c-reference-architecture.md`
- `docs/06-geometry-service.md`
- `docs/07-validation-service.md`
- `docs/08-knowledge-service.md`
- `docs/09-export-service.md`
- `docs/10-api-principles.md`
- `docs/11-events.md`
- `docs/12-capabilities.md`
- `docs/13-plugin-system.md`
- `docs/14-ports-and-adapters.md`
- `docs/15-dependency-matrix.md`
- `docs/16-roadmap-architecture.md`

## Architecture Decisions

- `architecture/ADR-0001-layered-architecture.md`
- `architecture/ADR-0002-sis-sim-sie.md`
- `architecture/ADR-0003-domain-first.md`
- `architecture/ADR-0004-service-kernel-separation.md`
- `architecture/ADR-0005-export-adapters.md`
- `architecture/ADR-0006-engine-capabilities.md`
- `architecture/ADR-0007-event-bus.md`
- `architecture/ADR-0008-plugin-architecture.md`
- `architecture/ADR-0009-ports-adapters.md`
- `architecture/INDEX.md`

## Contracts

- `contracts/INDEX.md`
- `contracts/services/`
- `contracts/ports/`
- `contracts/events/`
- `contracts/capabilities/`

## Developer material

- `developer/INDEX.md`
- `developer/GettingStarted.md`
- `developer/ArchitectureGuide.md`
- `developer/CreateService.md`
- `developer/CreateAdapter.md`
- `developer/CreatePlugin.md`
- `developer/CodingStyle.md`
- `developer/Testing.md`
- `developer/FAQ.md`

## Schemas and diagrams

- `schemas/project.schema.json`
- `schemas/event.schema.json`
- `schemas/capability.schema.json`
- `diagrams/reference-architecture.mmd`
- `diagrams/system-workflow.mmd`
- `diagrams/project-state.mmd`

## Examples and tests

- `examples/basic-workflow/README.md`
- `tests/architecture/README.md`
- `tests/architecture/dependency-rules.md`

## Release condition

This release is considered complete when:

- all Package manifests are present;
- the release commit is pushed to `main`;
- the Git tag `v0.1.0-foundation` is published;
- the working tree is clean.


---

## File originale: `RELEASE-0.1-NOTES.md`

# Release 0.1 — Foundation

Release date: 2026-07-20

Tag: `v0.1.0-foundation`

Status: Completed

## Summary

Release 0.1 establishes the architectural, organisational and
documentation foundations of Pianta-Arredo-Core and the future Spatial
Intelligence Platform.

This release does not yet provide a production-ready implementation.

It defines the structure required to develop one coherently.

## Completed packages

### Package A — Repository Foundation

Added:

- repository structure;
- project principles;
- governance;
- contribution guidelines;
- security policy;
- GitHub templates;
- initial automation;
- top-level development areas.

### Package B — Core Documentation

Added documentation for:

- Spatial Intelligence Specification;
- workflow;
- project state;
- reference architecture;
- Geometry Service;
- Validation Service;
- Knowledge Service;
- Export Service;
- API principles;
- Events;
- Capabilities;
- Plugins;
- Ports and Adapters;
- dependency rules;
- architecture roadmap.

### Package C — Architecture Decisions

Added accepted ADRs for:

- layered architecture;
- SIS, SIM and SIE separation;
- domain-first design;
- Service and Kernel separation;
- Export Adapters;
- declared Capabilities;
- Event Bus;
- Plugin architecture;
- Ports and Adapters.

### Package D — Service Specification

Added draft contracts for:

- Geometry Service;
- Validation Service;
- Knowledge Service;
- Export Service;
- Geometry Port;
- Persistence Port;
- Event Bus Port;
- Export Port;
- project Events;
- geometry Events;
- validation Events;
- export Events;
- Capability catalogues.

### Package E — Developer Experience

Added:

- developer onboarding;
- architecture guide;
- Service, Adapter and Plugin guides;
- coding style;
- testing guide;
- developer FAQ;
- example workflow;
- JSON Schemas;
- Mermaid diagrams;
- initial architecture-test rules.

## Architectural baseline

Release 0.1 establishes the following baseline:

Spatial Intelligence Specification

↓

Spatial Intelligence Model

↓

Public Services

↓

Ports

↓

replaceable Kernels and Adapters

↓

Applications

## Important limitations

Release 0.1 contains draft contracts and documentation.

It does not yet include:

- a stable SIS version;
- a stable SIM version;
- executable Service implementations;
- a Geometry Kernel;
- compliance automation;
- production-ready exports;
- a complete Pianta-Arredo Application.

## Next release

Release 0.2 will focus on Core Specification:

- normative SIS structure;
- normative SIM foundation;
- shared identifiers;
- units and coordinate systems;
- contract versioning;
- error model;
- command model;
- machine-readable Service contracts;
- initial compliance rules.


---

## File originale: `RELEASE-0.2-MANIFEST.md`

# Release 0.2 Manifest

Release: 0.2 — Core Specification

Status: Completed

## Packages

- Package A — Specification Foundation
- Package B — SIM Core Entities
- Package C — Commands, Results and Errors
- Package D — Compliance Foundation
- Package E — Examples and Release Closure

## Tag

`v0.2.0-core-specification`


---

## File originale: `RELEASE-0.2-NOTES.md`

# Release 0.2 — Core Specification

Status: Completed

## Summary

Release 0.2 formalises the first draft of SIS and SIM.

## Main additions

- SIS overview, conformance and versioning;
- SIM identifiers, units and coordinate systems;
- Project, Building, Floor, Space and Room structure;
- Walls, Openings and Furniture;
- entity lifecycle;
- Command, Result and Error models;
- JSON Schemas;
- compliance profiles and test cases;
- synthetic example data.

## Limitations

Release 0.2 remains a draft specification.

It does not yet provide executable reference Services or a Geometry
Kernel.

## Next release

Release 0.3 will introduce the Reference Architecture and the first
executable skeleton.


---

## File originale: `RELEASE-0.2-PACKAGE-A-MANIFEST.md`

# Release 0.2 Package A Manifest

Release: 0.2 — Core Specification

Package: A — Specification Foundation

Status: Draft

## Created files

- `specification/INDEX.md`
- `specification/SIS/00-overview.md`
- `specification/SIS/01-conformance.md`
- `specification/SIS/02-versioning.md`
- `specification/SIM/00-overview.md`
- `specification/SIM/01-identifiers.md`
- `specification/SIM/02-units-and-coordinate-systems.md`
- `specification/SIM/03-project-structure.md`
- `specification/SIM/04-entity-lifecycle.md`
- `schemas/identifier.schema.json`
- `schemas/unit-system.schema.json`
- `schemas/coordinate-reference.schema.json`


---

## File originale: `RELEASE-0.2-PACKAGE-B-MANIFEST.md`

# RELEASE 0.2 PACKAGE B MANIFEST

Release: 0.2 — Core Specification

## Files

- `specification/SIM/05-building.md`
- `specification/SIM/06-floor.md`
- `specification/SIM/07-space-and-room.md`
- `specification/SIM/08-wall.md`
- `specification/SIM/09-opening.md`
- `specification/SIM/10-furniture.md`
- `schemas/building.schema.json`
- `schemas/floor.schema.json`
- `schemas/space.schema.json`
- `schemas/wall.schema.json`
- `schemas/opening.schema.json`


---

## File originale: `RELEASE-0.2-PACKAGE-C-MANIFEST.md`

# RELEASE 0.2 PACKAGE C MANIFEST

Release: 0.2 — Core Specification

## Files

- `specification/SIS/03-command-model.md`
- `specification/SIS/04-result-model.md`
- `specification/SIS/05-error-model.md`
- `contracts/errors/error-catalogue.md`
- `schemas/command.schema.json`
- `schemas/error.schema.json`
- `schemas/result.schema.json`


---

## File originale: `RELEASE-0.2-PACKAGE-D-MANIFEST.md`

# RELEASE 0.2 PACKAGE D MANIFEST

Release: 0.2 — Core Specification

## Files

- `compliance/INDEX.md`
- `compliance/core-model-profile.md`
- `compliance/test-cases/core-model-cases.md`
- `compliance/test-cases/versioning-cases.md`


---

## File originale: `RELEASE-0.2-PACKAGE-E-MANIFEST.md`

# RELEASE 0.2 PACKAGE E MANIFEST

Release: 0.2 — Core Specification

## Files

- `samples/release-0.2/minimal-project.json`
- `examples/release-0.2-model/README.md`
- `RELEASE-0.2-NOTES.md`
- `RELEASE-0.2-MANIFEST.md`


---

## File originale: `RELEASE-0.3-MANIFEST.md`

# Release 0.3 Manifest

Release: 0.3 — Reference Architecture

Status: Completed

## Main areas

- `implementation/python/`
- `tests/architecture/python-reference-rules.md`
- `examples/reference-architecture-python/`
- `RELEASE-0.3-NOTES.md`

## Tag

`v0.3.0-reference-architecture`


---

## File originale: `RELEASE-0.3-NOTES.md`

# Release 0.3 — Reference Architecture

Status: Completed

## Summary

Release 0.3 introduces the first executable reference architecture.

## Added

- Python package structure;
- public domain model types;
- structured results and errors;
- Geometry, Knowledge, Validation, Export and Workflow Services;
- Geometry, Knowledge, Export and Event Bus Ports;
- reference Adapters;
- Application composition root;
- unit tests;
- end-to-end workflow test;
- executable architecture checks;
- Python project configuration.

## Limitations

This release is an architectural skeleton.

It does not yet include a complete SIM implementation, persistent
storage, production geometry processing or CAD export.


---

## File originale: `RELEASE-0.4-MANIFEST.md`

# Release 0.4 Manifest

Release: 0.4 — Geometry and Validation Core

Status: Completed

## Main areas

- `implementation/python/src/spatial_intelligence/geometry/`
- `implementation/python/src/spatial_intelligence/validation/`
- `implementation/python/src/spatial_intelligence/capabilities/`
- `implementation/python/tests/`
- `docs/17-geometry-and-validation-core.md`

## Tag

`v0.4.0-geometry-validation-core`


---

## File originale: `RELEASE-0.4-NOTES.md`

# Release 0.4 — Geometry and Validation Core

Status: Completed

## Added

- Point2D, Segment2D and Polyline2D primitives;
- segment and polyline length calculations;
- closed-perimeter detection;
- signed and absolute polygon area;
- segment-intersection detection;
- wall-dimension validation;
- opening-to-host validation;
- perimeter closure and self-intersection validation;
- Capability registry;
- unit tests for geometry, validation and capabilities.

## Compatibility

Release 0.4 extends the Release 0.3 reference architecture without
changing its public Service contracts.

## Limitations

Geometry support remains two-dimensional and experimental.


---

## File originale: `RELEASE-0.5-MANIFEST.md`

# Release 0.5 Manifest

Release: 0.5 — Project Model and Persistence

Status: Completed

## Main areas

- `implementation/python/src/spatial_intelligence/persistence/`
- `implementation/python/src/spatial_intelligence/ports/project_repository.py`
- `implementation/python/src/spatial_intelligence/adapters/`
- `implementation/python/src/spatial_intelligence/services/project_service.py`
- `implementation/python/tests/`
- `docs/18-project-model-and-persistence.md`

## Tag

`v0.5.0-project-persistence`


---

## File originale: `RELEASE-0.5-NOTES.md`

# Release 0.5 — Project Model and Persistence

Status: Completed

## Added

- revision-aware ProjectRecord;
- ProjectRepositoryPort;
- in-memory Project repository;
- JSON file Project repository;
- Project save and load Service;
- revision conflict handling;
- persistence integration tests.

## Limitations

This release does not include a database Adapter, migrations,
authentication or distributed locking.


---

## File originale: `RELEASE-0.6-MANIFEST.md`

# Release 0.6 Manifest

Tag: `v0.6.0-interoperability`

Main areas:

- `spatial_intelligence/interoperability/`
- GeoJSON tests
- interoperability documentation


---

## File originale: `RELEASE-0.6-NOTES.md`

# Release 0.6 — Interoperability Core

        Status: Completed

        ## Added

        - GeoJSON Project export
- GeoJSON Wall import
- structured interoperability errors
- round-trip tests

        ## Limitations

        - Only straight two-dimensional Walls are supported
- DXF and SVG Adapters are reserved for later extensions


---

## File originale: `RELEASE-0.7-MANIFEST.md`

# Release 0.7 Manifest

Tag: `v0.7.0-spatial-analysis`

Main areas:

- `spatial_intelligence/analysis/`
- clearance tests
- spatial-analysis documentation


---

## File originale: `RELEASE-0.7-NOTES.md`

# Release 0.7 — Spatial Analysis Core

        Status: Completed

        ## Added

        - axis-aligned bounding boxes
- object-to-object clearance calculation
- minimum-clearance validation
- spatial-analysis tests

        ## Limitations

        - Rotated bounding boxes are not yet supported
- Clearance analysis is geometric and not regulatory advice


---

## File originale: `RELEASE-0.8-MANIFEST.md`

# Release 0.8 Manifest

Tag: `v0.8.0-events-plugins`

Main areas:

- `spatial_intelligence/events/`
- `spatial_intelligence/plugins/`
- Event and Plugin tests


---

## File originale: `RELEASE-0.8-NOTES.md`

# Release 0.8 — Events and Plugins

        Status: Completed

        ## Added

        - typed Event envelope
- in-process Event dispatcher
- Plugin descriptors
- Plugin capability discovery
- Event and Plugin tests

        ## Limitations

        - Event delivery is synchronous and in-process
- Dynamic package loading is not included


---

## File originale: `RELEASE-0.9-MANIFEST.md`

# Release 0.9 Manifest

Tag: `v0.9.0-production-hardening`

Main areas:

- `spatial_intelligence/config/`
- `spatial_intelligence/health/`
- runtime-hardening tests


---

## File originale: `RELEASE-0.9-NOTES.md`

# Release 0.9 — Production Hardening

        Status: Completed

        ## Added

        - environment-based runtime settings
- health-status model
- runtime health service
- hardening tests

        ## Limitations

        - Authentication and authorisation are not included
- External monitoring integrations are not included


---

## File originale: `RELEASE-1.0-MANIFEST.md`

# Release 1.0 Manifest

Tag: `v1.0.0-stable-foundation`

Completed release sequence:

- 0.1 Foundation
- 0.2 Core Specification
- 0.3 Reference Architecture
- 0.4 Geometry and Validation Core
- 0.5 Project Model and Persistence
- 0.6 Interoperability Core
- 0.7 Spatial Analysis Core
- 0.8 Events and Plugins
- 0.9 Production Hardening
- 1.0 Stable Foundation


---

## File originale: `RELEASE-1.0-NOTES.md`

# Release 1.0 — Stable Foundation

        Status: Completed

        ## Added

        - stable public application facade
- cumulative specification and implementation foundation
- versioned capability discovery
- health reporting
- complete automated regression suite

        ## Limitations

        - No graphical user interface is included
- No claim of legal or building-code compliance is made
- Advanced CAD, BIM and 3D kernels remain extensions


---

## File originale: `developer/ArchitectureGuide.md`

# Architecture Guide

Version: 0.1

Status: Draft

## Reference architecture

Application

↓

Workflow Service

↓

Domain Services

↓

Ports

↓

Kernels and Adapters

↓

External systems

## Public abstractions

### Service

A stable public contract.

### Kernel

A replaceable implementation of computational behaviour.

### Port

A technology-neutral boundary.

### Adapter

A connection between a Port and a concrete external technology.

### Capability

A discoverable feature declaration.

### Event

A completed fact about platform state.

## Dependency direction

Dependencies must point toward stable contracts.

Domain Services must not depend directly on:

- databases;
- file systems;
- CAD applications;
- cloud providers;
- AI vendors;
- user interfaces.

## Domain-first rule

Generic spatial concepts belong in the Core.

Residential, Office, Retail and other specialisations belong in
Plugins or Knowledge Packages.

## Service and Kernel rule

Applications invoke Services.

Applications must not depend directly on internal Kernel types.

## Export rule

SIM

↓

Export Service

↓

Abstract Export Model

↓

Export Adapter

## Event rule

Events use past-tense names and describe completed facts.

Commands and requests are not Events.

## Architecture review

A change requires architecture review when it:

- introduces a new public dependency;
- changes a Service contract;
- adds a Port;
- changes dependency direction;
- adds a new Plugin lifecycle rule;
- introduces a breaking schema change.


---

## File originale: `developer/CodingStyle.md`

# Coding Style

Version: 0.1

Status: Draft

## General principles

Code should be:

- readable;
- explicit;
- testable;
- deterministic where possible;
- independent from unnecessary frameworks.

## Naming

Use domain vocabulary from the glossary.

Avoid synonyms for established concepts.

Prefer:

- `project_id`;
- `room_boundary`;
- `validation_result`;
- `export_adapter`.

Avoid ambiguous names such as:

- `data`;
- `thing`;
- `manager`;
- `helper`.

## Public contracts

Public names should remain stable and descriptive.

Breaking renames require migration guidance.

## Units

Never hide units in undocumented assumptions.

Prefer explicit names such as:

- `length_mm`;
- `area_m2`;
- `angle_degrees`.

## Errors

Do not use plain strings as the only error representation.

Include machine-readable error codes.

## Comments

Comments should explain why, not restate obvious code.

## Formatting

Language-specific formatters and linters will be defined when reference
implementations are introduced.


---

## File originale: `developer/CreateAdapter.md`

# Create an Adapter

Version: 0.1

Status: Draft

## Purpose

An Adapter connects a public Port to a concrete external technology.

## Examples

- SQLite Persistence Adapter;
- PostgreSQL Persistence Adapter;
- SVG Export Adapter;
- DXF Export Adapter;
- OpenCascade Geometry Adapter;
- external AI provider Adapter.

## Required behaviour

An Adapter must:

- implement one published Port;
- declare supported Capabilities;
- avoid changing domain semantics;
- convert vendor-specific errors into public errors;
- preserve identifiers and traceability;
- report information loss;
- document security requirements.

## Input and output mapping

Mapping code belongs in the Adapter.

Domain Services must not import Adapter-specific types.

## Failure handling

Adapter failure must produce a structured result.

It must not silently corrupt the SIM or Project state.

## Testing

Every Adapter should have:

- unit tests;
- Port conformance tests;
- compatibility tests;
- failure-mode tests;
- representative sample files where applicable.

## Selection

Adapter selection belongs to the Application composition layer.


---

## File originale: `developer/CreatePlugin.md`

# Create a Plugin

Version: 0.1

Status: Draft

## Purpose

Plugins extend the platform without placing specialised behaviour in
the generic Core.

## Suitable Plugin content

A Plugin may provide:

- Knowledge Packages;
- Capabilities;
- validators;
- Export Adapters;
- persistence Adapters;
- commands;
- Events;
- application components.

## Required manifest fields

A Plugin manifest should declare:

- identifier;
- name;
- version;
- compatible SIS version;
- required Capabilities;
- provided Capabilities;
- dependencies;
- permissions;
- entry points;
- license.

## Isolation rules

A Plugin must:

- use public contracts;
- avoid direct access to undocumented internal state;
- declare all required permissions;
- fail without corrupting the Project;
- report unsupported behaviour explicitly.

## Example lifecycle

Discovered

↓

Validated

↓

Loaded

↓

Activated

↓

Deactivated

↓

Unloaded

## Compatibility

A Plugin must state which contract and platform versions it supports.

Breaking Plugin API changes require migration guidance.

## Current status

The Plugin SDK is planned for Release 0.5.

This guide currently defines architectural expectations only.


---

## File originale: `developer/CreateService.md`

# Create a Service

Version: 0.1

Status: Draft

## Purpose

A Service exposes stable public behaviour independently from a specific
implementation.

## Required contract sections

Every Service contract must define:

- purpose;
- operations;
- inputs;
- outputs;
- errors;
- Events;
- Capabilities;
- versioning;
- conformance expectations.

## Design rules

A Service must:

- use public domain types;
- avoid vendor-specific objects;
- define explicit units;
- define coordinate references where spatial data is involved;
- return structured errors;
- declare optional behaviour through Capabilities.

## Kernel relationship

A Kernel may implement one or more Service responsibilities.

Kernel implementation details must not leak into public responses.

## Service checklist

Before adding a Service, verify:

- the responsibility is not already covered;
- the boundary is domain-oriented;
- dependencies point toward Ports;
- operations are testable;
- Events represent completed facts;
- compatibility rules are documented.

## Naming

Use descriptive names such as:

- Geometry Service;
- Validation Service;
- Knowledge Service;
- Export Service.

Avoid vague names such as Manager, Utility or General Service.


---

## File originale: `developer/FAQ.md`

# Frequently Asked Questions

Version: 0.1

Status: Draft

## Is Pianta-Arredo-Core only an interior-design application?

No.

It is the current repository for a broader Spatial Intelligence
Platform.

Pianta-Arredo is the first planned Application.

## What is SIS?

SIS is the Spatial Intelligence Specification.

It defines normative concepts, contracts and compatibility rules.

## What is SIM?

SIM is the Spatial Intelligence Model.

It represents Projects, Buildings, Floors, Spaces, Rooms, Walls,
Openings and related spatial information.

## What is the difference between a Service and a Kernel?

A Service is a public contract.

A Kernel is a replaceable implementation.

## Why use Ports and Adapters?

They prevent the Core from depending directly on databases, file
formats, CAD products, cloud systems or AI providers.

## Are the current contracts stable?

No.

Release 0.1 contracts are Draft.

## Can proprietary standards be stored in the repository?

Not without appropriate permission.

The project may reference external standards and store original,
legally permitted interpretations.

## Does the platform replace a qualified professional?

No.

Structural, regulatory, safety and authorisation matters require
professional verification.


---

## File originale: `developer/GettingStarted.md`

# Getting Started

Version: 0.1

Status: Draft

## Purpose

This guide introduces contributors to Pianta-Arredo-Core and the
Spatial Intelligence Platform architecture.

## Prerequisites

Contributors should understand:

- Git and GitHub;
- Markdown;
- structured data formats such as JSON;
- basic software architecture concepts.

Implementation-specific prerequisites will be documented separately.

## Repository orientation

Start with:

1. `README.md`
2. `PROJECT_PRINCIPLES.md`
3. `docs/INDEX.md`
4. `architecture/INDEX.md`
5. `contracts/INDEX.md`

## Main repository areas

- `docs/`: conceptual and technical documentation;
- `architecture/`: accepted ADRs;
- `contracts/`: Services, Ports, Events and Capabilities;
- `specification/`: future stable SIS and SIM specifications;
- `implementation/`: reference implementations;
- `examples/`: small code and workflow examples;
- `samples/`: spatial datasets and publishable files;
- `tests/`: compliance, integration and architecture tests.

## Development sequence

Preferred contribution order:

1. identify the domain problem;
2. check the glossary and taxonomy;
3. review applicable ADRs;
4. define or update the contract;
5. add tests;
6. implement;
7. update documentation.

## First validation

Before opening a pull request:

- check repository status;
- review changed files;
- run available tests;
- confirm no sensitive spatial data is included;
- confirm no proprietary standards are reproduced.

## Current maturity

Release 0.1 defines foundations and draft contracts.

Public APIs and schemas may still change.


---

## File originale: `developer/INDEX.md`

# Developer Documentation Index

Version: 0.1

Status: Draft

## Guides

| Guide | File |
|---|---|
| Getting Started | `GettingStarted.md` |
| Architecture Guide | `ArchitectureGuide.md` |
| Create a Plugin | `CreatePlugin.md` |
| Create a Service | `CreateService.md` |
| Create an Adapter | `CreateAdapter.md` |
| Coding Style | `CodingStyle.md` |
| Testing Guide | `Testing.md` |
| FAQ | `FAQ.md` |

## Recommended reading order

1. Getting Started
2. Architecture Guide
3. Testing Guide
4. Create a Service
5. Create an Adapter
6. Create a Plugin
7. Coding Style
8. FAQ


---

## File originale: `developer/README.md`

# Developer

Developer onboarding guides.


---

## File originale: `developer/Testing.md`

# Testing Guide

Version: 0.1

Status: Draft

## Test categories

### Unit tests

Verify isolated behaviour.

### Contract tests

Verify public Service, Port, Event and Capability contracts.

### Integration tests

Verify collaboration between multiple components.

### Compliance tests

Verify conformance with SIS, SIM and public contracts.

### Architecture tests

Verify allowed dependency direction and module boundaries.

### Regression tests

Preserve previously corrected behaviour.

### Export tests

Verify generated artifacts and declared information loss.

## Determinism

Core geometry and validation tests should produce reproducible results.

## Spatial tolerances

Tests involving geometry must state their tolerance policy explicitly.

## Test data

Use synthetic, anonymised or authorised samples.

Never commit private floor plans or sensitive building information.

## Architecture rules

Initial rules include:

- Domain Model must not depend on Services;
- Services must not depend directly on Adapters;
- Geometry must not depend on Knowledge;
- Export must not modify SIM;
- UI must not define domain truth.

## Future automation

Language-specific test commands will be documented with the first
reference implementation.


---

## File originale: `docs/00-vision.md`

# Vision

## Pianta-Arredo Core

Pianta-Arredo Core is an open source Geometry and Interior Intelligence Platform.

Its purpose is to transform measurements, floor plans and spatial data into validated geometric models that can be used for CAD, BIM, interior design, automation and AI-assisted workflows.

The project is designed as an independent modular engine.

ChatGPT, web applications, desktop applications and external software integrations are considered interfaces or clients of the core platform.

## Mission

Pianta-Arredo Core aims to:

- acquire spatial data from manual measurements, floor plans, images and structured files;
- build a reliable and machine-readable geometric model;
- validate walls, openings, rooms, dimensions and spatial relationships;
- identify geometric inconsistencies before generating drawings or models;
- produce CAD-friendly and interoperable outputs;
- support interior layout studies and furniture placement;
- integrate with open source CAD, BIM, rendering and design tools;
- provide a reusable foundation for AI-assisted spatial design.

## Core principles

### 1. Geometry first

No downstream output should be considered reliable until the underlying geometry has been validated.

### 2. Engine first

The core engine must remain independent from ChatGPT, web interfaces, desktop applications or any single user interface.

### 3. Modular architecture

Each module must have a clearly defined responsibility and communicate through documented interfaces.

### 4. Open standards

The project should prefer open and interoperable formats whenever technically possible.

Initial target formats include:

- JSON
- YAML
- SVG
- DXF

Future formats may include:

- IFC
- glTF
- STEP

### 5. Replaceable components

Geometry, validation, export and integration backends should be replaceable without redesigning the entire platform.

### 6. Verifiable outputs

The project must distinguish between:

- provisional geometry;
- validated geometry;
- conceptual drawings;
- editable CAD models;
- executable or construction-ready documents.

Pianta-Arredo Core does not replace the work of licensed architects, engineers, surveyors or other qualified professionals.

## Initial scope

The first development objective is:

> From measured walls to a validated 2D floor plan.

The first stable workflow will:

1. receive wall and opening measurements;
2. normalize the input data;
3. build a geometric model;
4. verify closure and consistency;
5. report errors and tolerances;
6. generate a structured representation;
7. export a basic 2D floor plan.

## Long-term direction

Pianta-Arredo Core may evolve into a shared spatial intelligence platform supporting:

- CAD generation;
- BIM interoperability;
- floor plan recognition;
- computer vision;
- interior layout optimization;
- furniture catalog integration;
- Sweet Home 3D workflows;
- FreeCAD and OpenCascade integrations;
- API access;
- web and desktop applications.


---

## File originale: `docs/00b-spatial-intelligence-specification.md`

# Spatial Intelligence Specification (SIS)

## Purpose

The Spatial Intelligence Specification (SIS) defines the conceptual contract of the platform.

It is independent from any programming language, software implementation or user interface.

Its purpose is to ensure that every implementation of the Spatial Intelligence Engine behaves consistently.

---

# Scope

The SIS specifies:

- concepts
- relationships
- workflows
- interfaces
- terminology
- interoperability rules

The SIS does not specify algorithms.

The SIS does not prescribe implementation details.

---

# Core Components

The specification is composed of:

- Vision
- Architecture
- Spatial Intelligence Model (SIM)
- System Glossary
- Domain Taxonomy
- Workflow Specification
- API Principles
- Interoperability Rules

---

# Relationship with the SIM

The Spatial Intelligence Model defines the entities manipulated by the platform.

The SIS defines the expected behavior of those entities.

---

# Relationship with the SIE

The Spatial Intelligence Engine is an implementation of the SIS.

Different implementations may exist provided they conform to this specification.

---

# Design Principles

- Implementation independent
- Technology independent
- Domain extensible
- Backward compatible where possible
- Open and interoperable

---

# Conformance

An implementation is considered SIS-compliant if it:

- implements the required concepts
- preserves the semantics defined by the SIM
- respects the architectural principles
- follows the workflow contracts
- exposes compatible interfaces

---

# Long-Term Vision

The SIS aims to become a reusable specification for spatial intelligence systems across multiple industries.

It should enable interoperability between independent tools, applications and engines.


---

## File originale: `docs/01-architecture.md`

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


---

## File originale: `docs/02-data-model.md`

# Data Model

## Philosophy

Pianta-Arredo Core separates real-world concepts, geometric representation and export formats into independent models.

This separation allows the platform to evolve without coupling business logic to CAD engines or file formats.

---

# The Three Models

The platform defines three independent models:

1. Domain Model
2. Geometry Model
3. Export Model

---

# Domain Model

The Domain Model represents architectural concepts.

Examples:

- Project
- Building
- Floor
- Space
- Wall
- Opening
- Door
- Window
- Furniture
- Material

The Domain Model contains no geometric algorithms.

---

# Geometry Model

The Geometry Model represents mathematical entities.

Examples:

- Point
- Vector
- Line
- Arc
- Segment
- Polyline
- Polygon
- Plane
- Solid
- Bounding Box

The Geometry Model contains no architectural semantics.

---

# Export Model

The Export Model converts validated geometry into external formats.

Examples:

- DXF
- SVG
- IFC
- STEP
- glTF
- Sweet Home 3D

Each exporter is independent.

---

# Transformation Pipeline

Domain Model

↓

Geometry Model

↓

Validation

↓

Export Model

---

# Design Rules

Domain objects never depend on exporters.

Geometry objects never depend on UI.

Exporters never modify geometry.

Validation always operates on Geometry Model.

---

# Future Extensions

Additional domain entities may include:

- Electrical systems
- Plumbing
- HVAC
- Structural elements
- Lighting
- Accessibility
- Cost estimation

without changing the Geometry Model.


---

## File originale: `docs/02b-platform-strategy.md`

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


---

## File originale: `docs/03-system-glossary.md`

# System Glossary

## Purpose

This glossary defines the official terminology of the Spatial Intelligence Engine (SIE).

It represents the authoritative vocabulary for the entire platform.

Every architectural document, source file, API, workflow and software component must use these definitions consistently.

If a concept is defined here, its meaning must remain identical throughout the entire project.

If a concept is not present in this glossary, it does not officially exist within the platform.

Every new architectural concept must be introduced here before being used in documentation, source code or APIs.

---

# Spatial Intelligence Concepts

## Spatial Intelligence Engine (SIE)

The computational platform responsible for modeling, validating, analyzing and transforming spatial information.

The SIE contains all computational engines but no business-specific knowledge.

Applications and Domain Packages are built on top of the SIE.

---

## Spatial Intelligence Model (SIM)

The conceptual representation of physical spaces.

The SIM defines the objects manipulated by the Spatial Intelligence Engine.

Examples include:

- Project
- Building
- Floor
- Space
- Wall
- Opening
- Furniture

The SIM is independent from programming languages, CAD software and geometric libraries.

The SIE processes the SIM.

---

# Core Concepts

## Project

The highest-level container representing an entire spatial project.

A Project may contain one or more Buildings.

---

## Building

A physical construction composed of one or more Floors.

---

## Floor

A horizontal level within a Building.

A Floor contains one or more Spaces.

---

## Space

A bounded physical area.

Space is the fundamental domain object of the platform.

Examples:

- Room
- Office
- Corridor
- Exhibition Stand
- Retail Area
- Warehouse Zone
- Laboratory
- Hotel Suite

Every specialized environment is a Space.

---

## Room

A residential specialization of Space.

Every Room is a Space.

Not every Space is a Room.

---

# Architectural Elements

## Wall

A physical element delimiting one or more Spaces.

Walls may contain Openings.

---

## Opening

A generic interruption of a Wall.

Examples:

- Door
- Window
- Archway

---

## Door

A passable Opening connecting two Spaces or a Space with the exterior.

---

## Window

A non-passable Opening intended for natural light, ventilation or visibility.

---

## Corner

The intersection between two or more Walls.

Corners define the topology of a Space.

---

## Furniture

A movable object positioned inside a Space.

Furniture never modifies the topology of the building.

---

# Geometry Concepts

## Point

A position in space.

---

## Vector

A direction with magnitude.

---

## Edge

A geometric connection between two vertices.

---

## Face

A bounded geometric surface.

---

## Polygon

A closed planar shape composed of edges.

---

## Solid

A closed three-dimensional volume.

---

## Bounding Box

The minimum volume enclosing a geometric object.

Used for spatial indexing and collision detection.

---

# Platform Concepts

## Domain Model

The representation of real-world entities.

Contains architectural semantics.

Examples:

- Wall
- Room
- Building
- Furniture

The Domain Model contains no geometric algorithms.

---

## Geometry Model

The mathematical representation of spatial objects.

Contains only geometry.

Examples:

- Point
- Vector
- Polygon
- Solid

The Geometry Model contains no architectural meaning.

---

## Export Model

The representation used for generating external formats.

Examples:

- DXF
- SVG
- IFC
- STEP
- glTF
- Sweet Home 3D

Export Models never modify the Geometry Model.

---

# Workflow Concepts

## Workflow

A coordinated sequence of operations executed by the Workflow Engine.

Examples:

Input

↓

Validation

↓

Geometry

↓

Furniture

↓

Export

---

## Workflow Engine

The orchestration engine responsible for coordinating platform operations.

It decides:

- execution order
- dependencies
- engine invocation
- state transitions

The Workflow Engine performs no geometry calculations.

---

# Computational Engines

## Engine

An independent computational module responsible for one well-defined task.

Every Engine must satisfy the following principles:

- single responsibility
- independent testing
- replaceability
- well-defined interfaces

Examples:

- Geometry Engine
- Validation Engine
- Knowledge Engine
- Export Engine

---

## Geometry Kernel

The computational heart of the platform.

Responsible only for geometry and topology.

It knows nothing about:

- residential design
- furniture brands
- GPT
- user interfaces
- CAD software

---

## Validation Engine

Verifies the consistency and correctness of the Geometry Model.

It never modifies geometry.

It only reports validation results.

---

## Knowledge Engine

Contains business knowledge rather than computational geometry.

Examples:

- building standards
- accessibility rules
- residential constraints
- exhibition regulations
- office planning rules

The Knowledge Engine is replaceable and domain-independent.

---

## AI Orchestrator

Coordinates interactions with artificial intelligence systems.

May communicate with:

- GPT
- local language models
- OCR
- Computer Vision
- future AI services

The AI Orchestrator never contains business rules.

---

## Export Engine

Transforms validated geometry into external representations.

Examples:

- DXF
- IFC
- SVG
- STEP
- Sweet Home 3D
- glTF

---

# Extension Concepts

## Package

A domain-specific extension of the platform.

Packages extend the platform without modifying the Core.

Examples:

- Residential Package
- Office Package
- Retail Package
- Exhibition Package
- Hospitality Package
- Healthcare Package
- Industrial Package

Packages may depend on the SIE.

The SIE never depends on Packages.

---

## Application

A user-facing software built on top of the Spatial Intelligence Engine.

Examples:

- Pianta-Arredo
- Web Platform
- Desktop Application
- Mobile App
- REST API

Applications consume services provided by the SIE.

---

# Guiding Principles

The glossary is the authoritative source for project terminology.

Every architectural document must conform to these definitions.

Every source file should use this vocabulary consistently.

Every API should expose these concepts without ambiguity.

Every new concept must first be introduced into this glossary before becoming part of the platform.

Consistency of language is considered an architectural requirement, not a documentation task.


---

## File originale: `docs/04-domain-taxonomy.md`

# Domain Taxonomy

## Purpose

This document defines the hierarchical organization of the Spatial Intelligence Model (SIM).

While the System Glossary defines the meaning of concepts, the Domain Taxonomy defines the relationships between them.

The taxonomy is the canonical structural model of the platform.

---

# Taxonomy Principles

The taxonomy follows four principles:

- Generalization
- Specialization
- Composition
- Independence

Every new concept introduced into the Spatial Intelligence Model must have a defined position within this taxonomy.

---

# Spatial Intelligence Model

Project
└── Building
    ├── Floor
    │   ├── Space
    │   │   ├── Room
    │   │   ├── Office
    │   │   ├── Corridor
    │   │   ├── Retail Area
    │   │   ├── Exhibition Stand
    │   │   ├── Hotel Room
    │   │   ├── Warehouse Zone
    │   │   ├── Laboratory
    │   │   └── Generic Space
    │   │
    │   ├── Wall
    │   ├── Opening
    │   │   ├── Door
    │   │   ├── Window
    │   │   └── Archway
    │   │
    │   ├── Furniture
    │   ├── Material
    │   ├── Annotation
    │   └── Equipment
    │
    └── Site

---

# Domain Hierarchy

## Project

Contains one or more Buildings.

---

## Building

Contains one or more Floors.

---

## Floor

Contains one or more Spaces and architectural elements.

---

## Space

The primary spatial abstraction.

Every specialized environment derives from Space.

Examples:

- Room
- Office
- Retail Area
- Exhibition Stand
- Warehouse Zone

---

# Architectural Elements

Architectural Elements belong to Spaces.

They include:

- Walls
- Openings
- Furniture
- Materials
- Equipment

---

# Geometry Relationship

The Domain Taxonomy is independent from geometry.

A Wall is not a line.

A Room is not a polygon.

A Building is not a mesh.

Geometry is an implementation used to represent domain objects.

---

# Domain Packages

Additional industries extend the taxonomy through specialization.

Examples:

Residential Package

Space
└── Room
    ├── Bedroom
    ├── Kitchen
    ├── Bathroom
    ├── Living Room
    └── Laundry

---

Office Package

Space
└── Office
    ├── Meeting Room
    ├── Open Space
    ├── Reception
    └── Server Room

---

Retail Package

Space
└── Retail Area
    ├── Sales Area
    ├── Storage
    ├── Checkout
    └── Display Area

---

Exhibition Package

Space
└── Exhibition Stand
    ├── Demo Area
    ├── Meeting Area
    ├── Storage
    └── Hospitality Area

---

Healthcare Package

Space
└── Healthcare Space
    ├── Waiting Room
    ├── Examination Room
    ├── Operating Room
    └── Recovery Room

---

# Design Rules

The Core defines only generic concepts.

Domain Packages introduce specialized concepts.

The Core must never contain industry-specific terminology.

---

# Architectural Principle

Inheritance flows downward.

Dependencies flow downward.

Knowledge flows upward through abstraction.

The Spatial Intelligence Model must remain stable while Domain Packages evolve independently.


---

## File originale: `docs/05-system-workflow.md`

# System Workflow

Document ID: DOC-005

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

Depends on:

- DOC-001
- DOC-002
- DOC-003
- DOC-004

## Purpose

This document defines the main processing workflow of the Spatial
Intelligence Platform.

## Reference workflow

User or external system

↓

Application

↓

Workflow Service

↓

Knowledge Service

↓

Spatial Intelligence Model

↓

Geometry Service

↓

Validation Service

↓

Analysis

↓

Export Service

↓

Export Adapter

↓

Application output or external format

## Workflow stages

### Input acquisition

The Application receives measurements, imported data, user actions
or external project files.

### Normalisation

Inputs are converted into explicit units, identifiers, coordinates
and domain entities.

### Knowledge resolution

The Knowledge Service supplies applicable rules, defaults, domain
classifications and constraints.

### Model construction

The normalised information is represented in the Spatial Intelligence
Model.

### Geometry generation

The Geometry Service creates or updates geometric representations.

### Validation

The Validation Service checks structure, dimensions, topology,
consistency and applicable rules.

### Analysis

Optional analytical Services evaluate circulation, dimensions,
occupancy, accessibility or other declared Capabilities.

### Export

The Export Service prepares an abstract export representation.

A format-specific Adapter converts it into DXF, SVG, IFC, glTF,
Sweet Home 3D-compatible data or another supported format.

## Workflow principles

### Single direction

The principal workflow moves forward through explicit stages.

### Immutable stage outputs

Each stage should produce a new state or result rather than silently
mutating unrelated data.

### Deterministic execution

Equal validated inputs and configuration should produce reproducible
outputs.

### Replaceable Services

Public contracts must not depend on one Kernel implementation.

### Explicit failures

Errors must identify the responsible stage and preserve diagnostic
information.

### Event publication

Relevant state changes may publish Events without making the Event Bus
the only means of direct Service invocation.

## Example

A measured wall is entered by the user.

The Application normalises centimetres into the project unit.

The Workflow Service requests applicable wall rules.

The SIM stores the wall definition.

The Geometry Service generates its geometric representation.

The Validation Service checks length, thickness and connectivity.

The Export Service prepares the wall for an SVG Adapter.


---

## File originale: `docs/05b-system-state.md`

# System State

Document ID: DOC-005B

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This document defines the lifecycle states of a spatial project.

## Reference state machine

Draft

↓

Measured

↓

Normalized

↓

Validated

↓

Geometry Generated

↓

Analyzed

↓

Exported

↓

Published

## States

### Draft

Initial project information exists but may be incomplete.

### Measured

Raw dimensions, orientations and openings have been recorded.

### Normalized

Units, identifiers, coordinate references and input structures have
been standardised.

### Validated

Required validation checks have completed successfully or with
explicitly accepted warnings.

### Geometry Generated

Geometric representations have been created from the model.

### Analyzed

One or more analytical Capabilities have produced results.

### Exported

An export representation has been created through an Export Adapter.

### Published

A project version has been intentionally released, shared or made
available to another system.

## State transitions

A state transition must include:

- previous state;
- resulting state;
- triggering command;
- timestamp;
- actor or Service;
- relevant Events;
- validation result;
- version identifier.

## Invalid transitions

Implementations must reject transitions that violate required
dependencies.

Example:

A project cannot become Validated before it is Normalized.

## Revisions

Editing a Published or Exported project creates a new revision.

Previous states should remain recoverable when persistence supports
history.

## Undo and redo

Undo and redo should operate on explicit commands or project revisions,
not on undocumented mutations.

## Concurrent changes

Synchronisation systems must detect conflicting project revisions and
must not silently overwrite spatial data.

## State Events

Recommended Events include:

- ProjectCreated
- MeasurementRecorded
- ProjectNormalized
- ValidationCompleted
- GeometryGenerated
- AnalysisCompleted
- ExportCompleted
- ProjectPublished


---

## File originale: `docs/05c-reference-architecture.md`

# Reference Architecture

Document ID: DOC-005C

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This document presents the reference architecture of the platform.

## Architectural view

Application Layer

↓

Workflow Service

↓

Domain Services

- Knowledge Service
- Geometry Service
- Validation Service
- Export Service

↓

Ports

↓

Kernels and Adapters

↓

External systems and formats

## Cross-cutting components

Cross-cutting components include:

- Event Bus;
- logging;
- tracing;
- versioning;
- configuration;
- security;
- compliance tests.

## Public and private boundaries

### Public

Public contracts include:

- Service interfaces;
- request and response models;
- Events;
- Ports;
- Capabilities;
- error models.

### Private

Private implementation details include:

- algorithms;
- geometry library choices;
- internal caches;
- database drivers;
- rendering code;
- vendor-specific integrations.

## Service and Kernel distinction

A Service is the stable public contract.

A Kernel is one implementation of that contract.

Example:

Geometry Service

↓

Geometry Port

↓

OpenCascade Kernel

or

custom geometry Kernel

## Adapter distinction

Adapters translate between platform contracts and external systems.

Examples:

- DXF Export Adapter;
- SVG Export Adapter;
- Sweet Home 3D Adapter;
- SQLite Persistence Adapter;
- PostgreSQL Persistence Adapter.

## Architectural rule

Domain Services must not depend directly on user interfaces, file
systems, GitHub, databases, cloud providers or AI vendors.

These dependencies must be accessed through Ports.

## Event Bus

The Event Bus supports loose coupling and observability.

Direct synchronous Service calls remain valid when immediate results
are required.

## Applications

Applications assemble Services, Kernels and Adapters.

Pianta-Arredo is the first reference Application.


---

## File originale: `docs/06-geometry-service.md`

# Geometry Service

Document ID: DOC-006

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

The Geometry Service provides public operations for creating,
transforming and querying spatial geometry.

## Responsibilities

The Geometry Service is responsible for:

- vertices;
- segments;
- polylines;
- walls;
- openings;
- room boundaries;
- offsets;
- intersections;
- containment;
- adjacency;
- geometric measurements;
- coordinate transformations.

## Service contract

The public Service defines requests, responses, errors and declared
Capabilities.

The Geometry Kernel implements the algorithms.

## Example Capabilities

- CreateWall
- SplitWall
- MergeWalls
- OffsetWall
- CreateOpening
- GenerateRoomBoundary
- CalculateArea
- CalculatePerimeter
- DetectIntersection
- TransformCoordinates

## Input principles

Inputs must declare:

- units;
- coordinate reference;
- tolerances;
- geometry type;
- identifiers.

## Output principles

Outputs must be:

- deterministic;
- traceable to source entities;
- serialisable;
- independent from rendering technology.

## Tolerances

Geometry operations must not rely on undocumented floating-point
assumptions.

Tolerances must be explicit and configurable.

## Topology

Geometry and topology are related but distinct.

Geometry describes shape and position.

Topology describes relationships such as connection, containment and
adjacency.

## Kernel independence

The public Geometry Service must not expose proprietary Kernel types.

## Errors

Example errors include:

- InvalidCoordinate
- InvalidGeometry
- DegenerateSegment
- NonClosedBoundary
- SelfIntersection
- UnsupportedOperation
- ToleranceExceeded

## Non-responsibilities

The Geometry Service does not decide regulatory compliance, furniture
style, application presentation or export file syntax.


---

## File originale: `docs/07-validation-service.md`

# Validation Service

Document ID: DOC-007

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

The Validation Service evaluates the consistency and acceptability of
spatial models and operations.

## Validation categories

### Structural validation

Confirms required entities, identifiers and references.

### Dimensional validation

Checks lengths, areas, thicknesses, heights and tolerances.

### Geometric validation

Detects invalid geometry, intersections, gaps and degenerate forms.

### Topological validation

Checks connectivity, enclosure, containment and adjacency.

### Domain validation

Applies domain rules supplied by the Knowledge Service.

### Export validation

Confirms that a model can be represented by a selected Export Adapter.

## Results

A validation result contains:

- validation identifier;
- subject identifier;
- rule identifier;
- severity;
- message;
- location;
- evidence;
- suggested correction;
- status.

## Severity levels

- Information
- Warning
- Error
- Critical

## Validation Capabilities

Examples:

- ValidateTopology
- ValidateDimensions
- ValidateRoomClosure
- ValidateOpeningPlacement
- ValidateExportReadiness
- ValidateDomainRules

## Rule source

Domain rules should come from traceable Knowledge Packages rather than
being hidden inside validation code.

## Determinism

Equal inputs, rules and configuration should produce equal validation
results.

## Error handling

Validation failure is not the same as system failure.

Invalid project data should produce structured validation results.

Internal Service failure should produce a Service error.

## Professional review

Automated validation does not replace review by qualified professionals
for structural, regulatory, accessibility or safety decisions.


---

## File originale: `docs/08-knowledge-service.md`

# Knowledge Service

Document ID: DOC-008

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

The Knowledge Service provides versioned, traceable and queryable
domain knowledge to other Services.

## Knowledge examples

- residential planning rules;
- office planning rules;
- furniture dimensions;
- circulation guidance;
- accessibility criteria;
- domain taxonomies;
- export mappings;
- local project conventions.

## Knowledge Packages

Knowledge is grouped into Packages.

A Package contains:

- package identifier;
- version;
- jurisdiction or scope;
- source references;
- effective dates;
- rules;
- assumptions;
- limitations;
- compatibility information.

## Public operations

Example Capabilities:

- ResolveRule
- ListApplicableRules
- ResolveDefault
- ResolveClassification
- ExplainRule
- CompareKnowledgeVersions

## No hardcoded rules

Domain rules should not be embedded directly in unrelated Service code.

## Traceability

Every applied rule should be traceable to:

- Package;
- version;
- source;
- rule identifier;
- effective context.

## Conflicts

When multiple rules conflict, the Service must return an explicit
conflict result rather than silently selecting one.

## Legal and standards material

The repository must not reproduce proprietary standards without
permission.

Knowledge Packages may reference external sources and store original
project interpretations where legally permitted.

## AI use

AI may assist with rule interpretation, but AI-generated conclusions
remain provisional until verified against an authoritative source.


---

## File originale: `docs/09-export-service.md`

# Export Service

Document ID: DOC-009

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

The Export Service converts platform data into an abstract export
representation and delegates file-specific generation to Export
Adapters.

## Architecture

Spatial Intelligence Model

↓

Export Service

↓

Abstract Export Model

↓

Export Adapter

↓

External format

## Example Export Adapters

- DXF Adapter
- SVG Adapter
- IFC Adapter
- STEP Adapter
- glTF Adapter
- Sweet Home 3D Adapter
- JSON Adapter

## Responsibilities

The Export Service is responsible for:

- selecting export scope;
- preparing export entities;
- mapping semantic layers;
- validating export readiness;
- preserving identifiers;
- reporting unsupported features.

## Adapter responsibilities

An Export Adapter is responsible for:

- file syntax;
- format versions;
- encoding;
- format-specific units;
- layer mapping;
- external compatibility;
- file generation.

## Layer recommendations

Common export layers include:

- walls;
- openings;
- rooms;
- furniture;
- dimensions;
- text;
- references;
- analysis results.

## Loss reporting

If a target format cannot represent part of the model, the Adapter must
report the loss explicitly.

## Capabilities

Example Capabilities:

- Export2D
- Export3D
- ExportSemanticModel
- ExportDimensions
- ExportLayers
- ExportMetadata

## Verification

A generated file must not be described as compatible or ready for use
unless the relevant Adapter and output have been tested.


---

## File originale: `docs/10-api-principles.md`

# API Principles

Document ID: DOC-010

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This document defines principles for public APIs and Service contracts.

## Contract first

Public behaviour should be defined before implementation details.

## Explicit input and output

Every operation must define:

- request;
- response;
- errors;
- side effects;
- Events;
- required Capabilities;
- version.

## Stable identifiers

Entities, requests, results and Events should use stable identifiers.

## Units

APIs must never assume undocumented units.

## Coordinate systems

Spatial operations must declare the applicable coordinate reference.

## Idempotency

Operations that may be retried should define idempotency behaviour.

## Errors

Errors must be machine-readable and human-readable.

They should include:

- code;
- message;
- subject;
- context;
- recoverability;
- suggested action.

## Versioning

Public APIs must distinguish compatible changes from breaking changes.

## Pagination and filtering

Collection APIs should support predictable pagination and filtering
when result size may grow.

## Synchronous and asynchronous operations

Immediate operations may be synchronous.

Long-running operations should expose progress, cancellation and result
retrieval.

## Security

APIs must minimise access to sensitive spatial data.

## Vendor neutrality

Public contracts must not expose vendor-specific implementation types.

## Human readability

Contract definitions should remain understandable without proprietary
tooling.


---

## File originale: `docs/11-events.md`

# Events

Document ID: DOC-011

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Events communicate completed facts about the platform state.

## Event rule

Event names should use past tense.

Examples:

- WallCreated
- OpeningMoved
- ProjectNormalized
- ValidationCompleted
- GeometryGenerated
- ExportCompleted

## Event structure

Every Event should include:

- event identifier;
- event type;
- event version;
- timestamp;
- project identifier;
- subject identifier;
- correlation identifier;
- causation identifier;
- actor;
- payload.

## Domain Events

Domain Events describe meaningful spatial or project changes.

## Integration Events

Integration Events expose selected facts to external systems.

Internal Domain Events must not automatically become public Integration
Events.

## Ordering

Consumers must not assume global ordering unless an implementation
explicitly guarantees it.

## Delivery

The platform may support:

- in-process delivery;
- queued delivery;
- persistent delivery;
- external messaging.

## Duplicate delivery

Consumers should be prepared for duplicate Events where delivery is at
least once.

## Event compatibility

Event payloads must be versioned.

Compatible consumers should ignore unknown optional fields.

## Privacy

Events must not expose unnecessary spatial or personal information.


---

## File originale: `docs/12-capabilities.md`

# Capabilities

Document ID: DOC-012

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Capabilities declare what a Service, Kernel, Adapter or Plugin can do.

## Why Capabilities are required

Different implementations may support different operations.

Consumers must not infer support from product names or implementation
types.

## Capability descriptor

A Capability should declare:

- identifier;
- version;
- status;
- supported inputs;
- supported outputs;
- limits;
- required dependencies;
- known restrictions.

## Example Geometry Capabilities

- CreateWall
- SplitWall
- MergeWalls
- OffsetWall
- GenerateRoomBoundary
- CalculateArea

## Example Validation Capabilities

- ValidateTopology
- ValidateDimensions
- ValidateRoomClosure
- ValidateOpeningPlacement

## Example Knowledge Capabilities

- ResidentialRules
- OfficeRules
- AccessibilityRules
- ExplainRule

## Example Export Capabilities

- ExportDXF
- ExportSVG
- ExportIFC
- ExportGLTF
- ExportSweetHome3D

## Capability negotiation

Applications may query available Capabilities before invoking an
operation.

## Partial support

Partial support must be declared explicitly.

## Capability stability

Stable public Capabilities require versioning and compatibility rules.


---

## File originale: `docs/13-plugin-system.md`

# Plugin System

Document ID: DOC-013

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

The Plugin System allows the platform to support domain-specific or
implementation-specific extensions without placing them in the Core.

## Example Plugins

- Residential Plugin
- Office Plugin
- Retail Plugin
- Healthcare Plugin
- Accessibility Plugin
- Export Plugin
- Geometry Plugin

## Plugin contents

A Plugin may provide:

- Capabilities;
- Knowledge Packages;
- Validators;
- Adapters;
- application components;
- commands;
- Events;
- schemas.

## Plugin manifest

Every Plugin should declare:

- identifier;
- version;
- compatible SIS version;
- required Capabilities;
- provided Capabilities;
- permissions;
- entry points;
- dependencies;
- license.

## Isolation

Plugins must not directly modify internal state outside published
contracts.

## Security

Plugin permissions should follow least privilege.

## Compatibility

A Plugin must declare which platform and contract versions it supports.

## Failure handling

Plugin failure must not silently corrupt the project model.

## Core rule

Generic concepts belong in the Core.

Domain specialisation belongs in Plugins or Packages.


---

## File originale: `docs/14-ports-and-adapters.md`

# Ports and Adapters

Document ID: DOC-014

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Ports and Adapters isolate the domain and public Services from external
technology choices.

## Port

A Port is a contract required or exposed by the platform.

## Adapter

An Adapter connects a Port to a specific external technology.

## Examples

Persistence Port

↓

JSON Adapter

SQLite Adapter

PostgreSQL Adapter

Cloud Adapter

Geometry Port

↓

OpenCascade Adapter

custom Kernel Adapter

Export Port

↓

DXF Adapter

SVG Adapter

IFC Adapter

## Dependency direction

Domain Services depend on Ports.

Adapters depend on Ports.

Ports do not depend on Adapters.

## Core isolation

The Core must not directly depend on:

- file systems;
- databases;
- GitHub;
- ChatGPT;
- CAD products;
- cloud providers;
- messaging vendors.

## Adapter replacement

Replacing an Adapter should not require changing the public domain
contract.

## Testing

Ports should support test doubles and compliance suites.

## Configuration

Adapter selection belongs to the Application composition layer.


---

## File originale: `docs/15-dependency-matrix.md`

# Dependency Matrix

Document ID: DOC-015

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This document defines allowed high-level dependencies.

## Rule legend

Allowed means the source may depend on the target.

Forbidden means the dependency must not exist.

## Matrix

| Source | Domain Model | Workflow | Geometry | Validation | Knowledge | Export | Ports | Adapters | UI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Domain Model | — | No | No | No | No | No | No | No | No |
| Workflow | Yes | — | Yes | Yes | Yes | Yes | Yes | No | No |
| Geometry | Yes | No | — | No | No | No | Yes | No | No |
| Validation | Yes | No | Yes | — | Yes | No | Yes | No | No |
| Knowledge | Yes | No | No | No | — | No | Yes | No | No |
| Export | Yes | No | No | Yes | No | — | Yes | No | No |
| Ports | Yes | No | No | No | No | No | — | No | No |
| Adapters | Yes | No | No | No | No | No | Yes | — | No |
| UI | Yes | Yes | No | No | No | No | Yes | No | — |

## Key restrictions

Geometry must not depend on Knowledge.

Export must not modify the Spatial Intelligence Model.

Domain Model must not depend on Services.

Services must not depend directly on Adapters.

Adapters must not define domain rules.

UI must not become the source of domain truth.

## Architecture tests

Future implementations should enforce these rules automatically.


---

## File originale: `docs/16-roadmap-architecture.md`

# Architecture Roadmap

Document ID: DOC-016

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This document describes the intended architectural evolution.

## Release 0.1 — Foundation

- repository structure;
- documentation;
- governance;
- project principles;
- initial architectural vocabulary.

## Release 0.2 — Contracts

- SIS foundation;
- SIM foundation;
- Service contracts;
- Ports;
- Events;
- Capabilities;
- error model.

## Release 0.3 — Reference Architecture

- executable module boundaries;
- architecture tests;
- dependency enforcement;
- reference workflow;
- compliance skeleton.

## Release 0.4 — Reference Implementation

- first Geometry Kernel;
- first Validation implementation;
- first Knowledge Package;
- SVG and JSON Adapters;
- end-to-end tests.

## Release 0.5 — Plugin SDK

- plugin manifest;
- plugin lifecycle;
- capability negotiation;
- compatibility tests;
- possible specification repository separation.

## Release 0.6 — Assisted Intelligence

- AI Ports;
- OCR Adapter experiments;
- computer vision experiments;
- human verification workflow.

## Release 0.7 — Persistence

- project revisions;
- undo and redo;
- local persistence;
- synchronisation Ports;
- conflict handling.

## Release 0.8 — Beta

- Pianta-Arredo reference Application;
- real samples;
- Sweet Home 3D workflow;
- LibreCAD and DXF workflow.

## Release 0.9 — Stabilisation

- compatibility review;
- migration tools;
- compliance suites;
- performance benchmarks.

## Release 1.0 — Stable Platform

- stable SIS version;
- stable SIM version;
- documented public contracts;
- tested reference implementation.


---

## File originale: `docs/17-geometry-and-validation-core.md`

# Geometry and Validation Core

Version: 0.4

Status: Experimental reference implementation

## Scope

Release 0.4 introduces technology-neutral two-dimensional geometry
primitives and deterministic validation rules.

## Geometry primitives

- Point2D
- Segment2D
- Polyline2D

## Algorithms

- Euclidean segment length
- Polyline length
- Perimeter closure check
- Signed polygon area
- Absolute polygon area
- Segment intersection

## Validation rules

- Wall length must be positive
- Wall thickness must be positive
- Opening width must be positive
- Opening must fit within its host
- Room perimeter must be closed
- Room perimeter must not self-intersect

## Units

Geometry algorithms operate on consistent numeric coordinates.

The caller remains responsible for declaring and preserving the
associated unit system.

## Limitations

Release 0.4 does not yet implement arcs, curves, holes, constructive
solid geometry or production-grade numerical robustness.


---

## File originale: `docs/18-project-model-and-persistence.md`

# Project Model and Persistence

Version: 0.5

Status: Experimental reference implementation

## Scope

Release 0.5 introduces revision-aware Project persistence.

## Components

- ProjectRecord
- ProjectRepositoryPort
- InMemoryProjectRepository
- JsonProjectRepository
- ProjectService

## Revision rules

- A new Project starts at revision 1.
- Every successful update increments the revision.
- Clients MAY declare an expected revision.
- A mismatching expected revision produces RevisionConflict.
- Persistence Adapters MUST preserve Project identifiers.

## Limitations

JSON persistence is intended for development and interoperability
experiments, not concurrent production workloads.


---

## File originale: `docs/19-interoperability-core.md`

# Interoperability Core

Version: 0.6

Release 0.6 introduces a technology-neutral GeoJSON boundary.

Supported entities:

- Wall as GeoJSON LineString;
- Project metadata as FeatureCollection properties;
- explicit Wall thickness metadata.

GeoJSON is an exchange representation, not the internal
authoritative geometry model.


---

## File originale: `docs/20-spatial-analysis-core.md`

# Spatial Analysis Core

Version: 0.7

Release 0.7 introduces deterministic clearance analysis for
axis-aligned spatial objects.

The initial implementation supports:

- rectangular object envelopes;
- horizontal, vertical and diagonal clearance;
- minimum-clearance checks.

Rotated objects and navigable path planning remain outside
this release.


---

## File originale: `docs/21-events-and-plugins.md`

# Events and Plugins

Version: 0.8

Release 0.8 introduces an in-process Event dispatcher and a
technology-neutral Plugin registry.

Plugins declare identifiers, versions and Capabilities.

Plugin implementations remain outside public domain types and
must integrate through Ports and contracts.


---

## File originale: `docs/22-production-hardening.md`

# Production Hardening

Version: 0.9

Release 0.9 introduces deterministic runtime configuration
and health reporting.

It does not by itself certify production readiness.

Deployments remain responsible for security, persistence,
monitoring, backups and operational policy.


---

## File originale: `docs/23-stable-foundation.md`

# Stable Foundation

Version: 1.0

Release 1.0 establishes the first stable foundation of
Pianta-Arredo-Core.

Stable areas:

- specification structure;
- public Python package layout;
- domain and result foundations;
- Geometry and Validation Core;
- Project persistence Ports;
- GeoJSON interoperability;
- spatial clearance analysis;
- Events and Plugin registry;
- runtime configuration and health;
- public application facade.

Stable does not mean complete or suitable for every production
scenario. Domain extensions remain versioned independently.


---

## File originale: `docs/INDEX.md`

# Documentation Index

Document ID: DOC-INDEX

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This file is the entry point for project documentation.

## Foundation documents

| ID | File | Title | Status |
|---|---|---|---|
| DOC-000 | `00-vision.md` | Vision | Existing |
| DOC-000B | `00b-spatial-intelligence-specification.md` | Spatial Intelligence Specification | Draft |
| DOC-001 | `01-architecture.md` | Architecture | Existing |
| DOC-002 | `02-data-model.md` | Data Model | Existing |
| DOC-002B | `02b-platform-strategy.md` | Platform Strategy | Existing |
| DOC-003 | `03-system-glossary.md` | System Glossary | Existing |
| DOC-004 | `04-domain-taxonomy.md` | Domain Taxonomy | Existing |

## Core architecture documents

| ID | File | Title | Status |
|---|---|---|---|
| DOC-005 | `05-system-workflow.md` | System Workflow | Draft |
| DOC-005B | `05b-system-state.md` | System State | Draft |
| DOC-005C | `05c-reference-architecture.md` | Reference Architecture | Draft |
| DOC-006 | `06-geometry-service.md` | Geometry Service | Draft |
| DOC-007 | `07-validation-service.md` | Validation Service | Draft |
| DOC-008 | `08-knowledge-service.md` | Knowledge Service | Draft |
| DOC-009 | `09-export-service.md` | Export Service | Draft |
| DOC-010 | `10-api-principles.md` | API Principles | Draft |
| DOC-011 | `11-events.md` | Events | Draft |
| DOC-012 | `12-capabilities.md` | Capabilities | Draft |
| DOC-013 | `13-plugin-system.md` | Plugin System | Draft |
| DOC-014 | `14-ports-and-adapters.md` | Ports and Adapters | Draft |
| DOC-015 | `15-dependency-matrix.md` | Dependency Matrix | Draft |
| DOC-016 | `16-roadmap-architecture.md` | Architecture Roadmap | Draft |

## Documentation levels

### Stable specification

Located in `specification/`.

### Approved architecture

Located in `architecture/`.

### Proposals

Located in `rfc/`.

### Exploratory work

Located in `design/`.

### Temporary decisions

Located in `decisions/`.

## Reading order

Recommended sequence:

1. Vision
2. Project Principles
3. Architecture
4. Data Model
5. Glossary
6. Domain Taxonomy
7. System Workflow
8. Reference Architecture
9. Service documents
10. Ports, Events and Capabilities
11. Dependency Matrix
12. Architecture Roadmap


---

## File originale: `docs/README.md`

# Docs

General, conceptual and technical documentation.


---

## File originale: `docs/RELEASE-0.1-REVIEW.md`

# Release 0.1 Architecture Review

Review date: 2026-07-20

Release: 0.1 — Foundation

Status: Approved for closure

## Review scope

This review verifies that Release 0.1 establishes a coherent foundation
for future specification and implementation work.

## Accepted strengths

### Clear separation of concepts

The project distinguishes:

- SIS;
- SIM;
- Services;
- Kernels;
- Ports;
- Adapters;
- Events;
- Capabilities;
- Plugins.

### Domain-first architecture

Generic spatial concepts are separated from application-specific and
domain-specific specialisations.

### Vendor neutrality

Public contracts do not require one CAD product, geometry library,
database, cloud provider or AI system.

### Replaceability

Infrastructure and computational components are placed behind Ports and
public Service contracts.

### Documentation traceability

The repository distinguishes:

- stable specifications;
- accepted ADRs;
- RFC proposals;
- exploratory designs;
- temporary decisions.

## Known gaps

The following remain intentionally incomplete:

- normative SIS modules;
- normative SIM schema;
- command contracts;
- shared error taxonomy;
- compatibility policy;
- executable architecture tests;
- reference implementation;
- compliance automation.

## Risks

### Over-design risk

Future work must validate abstractions through a small vertical reference
implementation.

### Terminology drift

The glossary and document indexes must remain authoritative.

### Contract instability

Draft contracts must not be presented as stable APIs.

### Excessive Core growth

Domain specialisations must remain outside the generic Core.

## Release decision

Release 0.1 is approved as a Foundation release.

Release 0.2 should focus on formalising the specification rather than
introducing additional high-level architecture concepts.


---

## File originale: `examples/README.md`

# Examples

Small source-code examples.


---

## File originale: `examples/basic-workflow/README.md`

# Basic Spatial Workflow Example

Version: 0.1

Status: Conceptual example

## Scenario

Create one rectangular Room with one Door and export a simple
two-dimensional representation.

## Workflow

1. Create Project.
2. Create Building.
3. Create Floor.
4. Create Space.
5. Create Room.
6. Create four Walls.
7. Add one Door Opening.
8. Normalize units and coordinates.
9. Generate geometry.
10. Validate closure and dimensions.
11. Prepare export.
12. Invoke SVG Export Adapter.

## Example project state

Draft

↓

Measured

↓

Normalized

↓

Validated

↓

Geometry Generated

↓

Exported

## Example measurements

- Room width: 4000 mm
- Room depth: 3000 mm
- Wall thickness: 120 mm
- Door width: 900 mm
- Door offset from wall start: 500 mm

## Expected validation

- four connected Walls;
- one closed Room boundary;
- positive area;
- Door hosted by one Wall;
- no self-intersections.

## Expected result

The workflow produces:

- one SIM Project;
- one geometry result;
- one validation report;
- one abstract export model;
- one SVG artifact.

This example is conceptual until the reference implementation exists.


---

## File originale: `examples/reference-architecture-python/README.md`

# Python Reference Architecture Example

This example uses the Release 0.3 composition root.

```python
from spatial_intelligence.composition import build_application
from spatial_intelligence.domain import Project, Wall

services = build_application()

project = Project(
    project_id="project_001",
    name="Example",
    walls=(
        Wall(
            wall_id="wall_001",
            start=(0.0, 0.0),
            end=(4000.0, 0.0),
            thickness_mm=120.0,
        ),
    ),
)

result = services.workflow.validate_and_export(project)
```

The workflow validates the Project, exports JSON and publishes an
`ExportCompleted` Event.


---

## File originale: `examples/release-0.2-model/README.md`

# Release 0.2 Model Example

This example demonstrates the specification sequence:

Project

↓

Building

↓

Floor

↓

Room

↓

Walls and Opening

The example is normative only where it references explicit SIS or SIM
requirements.

Sample data is synthetic and contains no private floor plan.


---

## File originale: `samples/README.md`

# Samples

Synthetic or publishable spatial samples.


---

## File originale: `samples/release-0.2/minimal-project.json`

{
  "schemaVersion": "0.2-draft",
  "projectId": "project_demo_001",
  "name": "Minimal Apartment Example",
  "state": "Normalized",
  "unitSystem": {
    "length": "mm",
    "angle": "degrees",
    "area": "m2",
    "volume": "m3"
  },
  "coordinateReference": {
    "coordinateReferenceId": "crs_local_001",
    "type": "local-cartesian",
    "dimensions": 2,
    "axisOrder": [
      "x",
      "y"
    ],
    "unit": "mm",
    "origin": [
      0,
      0
    ],
    "orientationDegrees": 0,
    "externalReference": null
  }
}

