# ADR-0006 — Declared Capabilities

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

Different Services, Kernels, Adapters and Plugins may support different
operations or levels of precision.

Applications must not assume that every implementation supports every
feature.

## Decision

Every replaceable component must publish explicit Capabilities.

A Capability descriptor includes:

- identifier;
- version;
- status;
- supported inputs;
- supported outputs;
- limits;
- required dependencies;
- known restrictions.

Example Geometry Capabilities:

- CreateWall;
- SplitWall;
- MergeWalls;
- OffsetWall;
- GenerateRoomBoundary;
- CalculateArea.

Example Validation Capabilities:

- ValidateTopology;
- ValidateDimensions;
- ValidateRoomClosure;
- ValidateOpeningPlacement.

Applications may negotiate Capabilities before invoking operations.

## Partial support

Partial support must be declared explicitly.

Unsupported operations must return structured errors.

## Consequences

Positive consequences:

- safer implementation replacement;
- runtime feature discovery;
- clearer compatibility;
- better plugin composition.

Negative consequences:

- capability catalogues require governance;
- negotiation adds complexity;
- version compatibility must be maintained.

## Alternatives considered

### Infer features from implementation name

Rejected because names do not provide reliable contracts.

### Fail only when an operation is called

Rejected because Applications need to plan workflows before execution.

## Review trigger

Review when the capability model becomes too granular or expensive to
negotiate.
