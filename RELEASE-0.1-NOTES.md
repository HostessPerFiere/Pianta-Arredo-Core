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
