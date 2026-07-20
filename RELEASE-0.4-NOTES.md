# Release 0.4 — Geometry and Validation Core

Status: Completed

## Added

- Point2D, Segment2D and Polyline2D primitives;
- segment and polyline length calculations;
- closed-perimeter detection;
- signed and absolute polygon area;
- segment-intersection detection;
- wall-dimension validation;
- opening-to-host validation;
- perimeter closure and self-intersection validation;
- Capability registry;
- unit tests for geometry, validation and capabilities.

## Compatibility

Release 0.4 extends the Release 0.3 reference architecture without
changing its public Service contracts.

## Limitations

Geometry support remains two-dimensional and experimental.
