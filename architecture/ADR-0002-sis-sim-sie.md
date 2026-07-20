# ADR-0002 — SIS, SIM and SIE Separation

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

The project needs to distinguish the normative specification, the
spatial data model and the software that executes spatial operations.

Using one term for all three would create ambiguity between rules,
data and implementation.

## Decision

The platform adopts three distinct concepts.

### Spatial Intelligence Specification — SIS

SIS defines normative concepts, contracts, compatibility rules and
conformance expectations.

### Spatial Intelligence Model — SIM

SIM represents spatial entities, relationships, geometry references,
project state and metadata.

### Spatial Intelligence Engine — SIE

SIE is the runtime platform formed by Services, Kernels, Adapters,
workflows and supporting infrastructure.

Public architecture should generally refer to Services rather than
exposing internal Engines or Kernels.

## Dependency direction

SIS

↓

SIM

↓

Services

↓

Kernels and Adapters

↓

Applications

Implementations conform to SIS.

SIS must not depend on one implementation.

## Consequences

Positive consequences:

- independent specification evolution;
- multiple possible implementations;
- clearer conformance testing;
- easier future repository separation.

Negative consequences:

- more terminology;
- additional version coordination;
- need for compatibility documentation.

## Alternatives considered

### One unified Core model

Rejected because normative rules and implementation details would
become inseparable.

### Implementation-first specification

Rejected because the first implementation would become the accidental
standard.

## Review trigger

Review before extracting SIS into the independent
Spatial-Intelligence-Specification repository.
