# ADR-0003 — Domain-First Design

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

Spatial applications may have different interfaces and technologies,
but they share concepts such as Projects, Buildings, Floors, Spaces,
Rooms, Walls, Openings and Furniture.

Allowing each Application to define these concepts independently would
create incompatible models.

## Decision

The platform adopts a domain-first approach.

Generic spatial concepts are defined before:

- user-interface components;
- database tables;
- CAD format mappings;
- rendering objects;
- AI prompts;
- application-specific workflows.

The Core contains generic concepts.

Domain Packages and Plugins provide specialisations such as:

- Residential;
- Office;
- Retail;
- Healthcare;
- Exhibition;
- Hospitality.

## Consequences

Positive consequences:

- shared vocabulary;
- reusable Services;
- consistent export and validation;
- reduced duplication between Applications.

Negative consequences:

- domain modelling requires early effort;
- some application-specific shortcuts are prohibited;
- disagreements require glossary and taxonomy updates.

## Alternatives considered

### UI-first modelling

Rejected because screens and controls would define the data model.

### Database-first modelling

Rejected because persistence concerns would shape domain concepts.

### Format-first modelling

Rejected because DXF, IFC or another format would impose its limitations
on the internal model.

## Review trigger

Review when a new domain cannot be represented without repeatedly
introducing exceptions into the generic model.
