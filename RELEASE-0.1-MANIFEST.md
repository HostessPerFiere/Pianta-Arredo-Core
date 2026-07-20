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
