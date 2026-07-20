# Architecture Tests

Version: 0.1

Status: Draft

## Purpose

Architecture tests protect module boundaries and dependency direction.

They are different from unit tests.

Unit tests verify behaviour.

Architecture tests verify structural rules.

## Initial targets

Future executable tests should verify:

- Domain Model does not depend on Services;
- Services do not depend directly on Adapters;
- Geometry does not depend on Knowledge;
- Export does not mutate SIM;
- UI does not define domain entities;
- Plugins use public contracts;
- public contracts do not expose vendor-specific types.

## Current status

Release 0.1 defines the rules in documentation.

Executable enforcement will be added with the first reference
implementation.
