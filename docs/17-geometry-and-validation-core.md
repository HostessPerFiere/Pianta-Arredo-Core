# Geometry and Validation Core

Version: 0.4

Status: Experimental reference implementation

## Scope

Release 0.4 introduces technology-neutral two-dimensional geometry
primitives and deterministic validation rules.

## Geometry primitives

- Point2D
- Segment2D
- Polyline2D

## Algorithms

- Euclidean segment length
- Polyline length
- Perimeter closure check
- Signed polygon area
- Absolute polygon area
- Segment intersection

## Validation rules

- Wall length must be positive
- Wall thickness must be positive
- Opening width must be positive
- Opening must fit within its host
- Room perimeter must be closed
- Room perimeter must not self-intersect

## Units

Geometry algorithms operate on consistent numeric coordinates.

The caller remains responsible for declaring and preserving the
associated unit system.

## Limitations

Release 0.4 does not yet implement arcs, curves, holes, constructive
solid geometry or production-grade numerical robustness.
