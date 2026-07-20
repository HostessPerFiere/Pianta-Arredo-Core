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
