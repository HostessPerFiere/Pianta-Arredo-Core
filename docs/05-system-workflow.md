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
