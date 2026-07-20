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
