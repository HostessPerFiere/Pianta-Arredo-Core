# Changelog

## Unreleased

Planned:

- Core documentation
- Architecture Decision Records
- Service specifications
- SIS and SIM foundations
- event and contract catalogues

## 0.1.0-foundation-a — 2026-07-20

Added:

- repository foundation
- project principles
- roadmap
- governance documents
- GitHub templates
- initial repository validation workflow
- approved directory structure

## [0.1.0-foundation] — 2026-07-20

### Added

- repository foundation and governance;
- project principles and contribution guidance;
- core architecture documentation;
- accepted Architecture Decision Records;
- draft Service and Port contracts;
- Event and Capability catalogues;
- developer onboarding documentation;
- JSON Schemas;
- Mermaid architecture diagrams;
- architecture-test rules;
- Package manifests and Release 0.1 documentation.

### Status

Release 0.1 is a Foundation release.

It does not provide a stable production implementation.

<!-- RELEASE-0.2-CHANGELOG:START -->
## [0.2.0-core-specification]

### Added

- formal SIS foundation;
- formal SIM foundation;
- identifiers, units and coordinate references;
- Building, Floor, Space, Room, Wall, Opening and Furniture models;
- Command, Result and Error contracts;
- machine-readable JSON Schemas;
- compliance profiles and test cases;
- synthetic model example.

### Status

Draft specification completed.

No production reference implementation is included.
<!-- RELEASE-0.2-CHANGELOG:END -->

<!-- RELEASE-0.3-CHANGELOG:START -->
## [0.3.0-reference-architecture]

### Added

- first executable Python reference architecture;
- domain model skeleton;
- Service and Port implementations;
- reference Adapters;
- composition root;
- unit, integration and architecture tests;
- project configuration for pytest, Ruff and mypy.

### Status

Experimental reference architecture completed.
<!-- RELEASE-0.3-CHANGELOG:END -->

<!-- RELEASE-0.4-CHANGELOG:START -->
## [0.4.0-geometry-validation-core]

### Added

- Point2D, Segment2D and Polyline2D;
- length, closure and polygon-area algorithms;
- segment-intersection detection;
- deterministic Wall, Opening and perimeter validation;
- Capability registry;
- geometry and validation test suites.

### Status

Experimental Geometry and Validation Core completed.
<!-- RELEASE-0.4-CHANGELOG:END -->

<!-- RELEASE-0.5-CHANGELOG:START -->
## [0.5.0-project-persistence]

### Added

- ProjectRecord with revision metadata;
- ProjectRepositoryPort;
- in-memory and JSON persistence Adapters;
- ProjectService;
- revision conflict handling;
- persistence tests.

### Status

Experimental Project persistence completed.
<!-- RELEASE-0.5-CHANGELOG:END -->

<!-- RELEASE-0-6-0-CHANGELOG:START -->
## [0.6.0] — Interoperability Core

Status: Completed
<!-- RELEASE-0-6-0-CHANGELOG:END -->

<!-- RELEASE-0-7-0-CHANGELOG:START -->
## [0.7.0] — Spatial Analysis Core

Status: Completed
<!-- RELEASE-0-7-0-CHANGELOG:END -->
