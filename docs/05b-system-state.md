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
