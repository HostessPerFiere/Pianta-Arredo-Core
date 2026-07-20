# Units and Coordinate Systems

Specification ID: SIM-002

Version: 0.2-draft

Status: Draft

## Purpose

This document defines how SIM represents measurements, units,
coordinates and tolerances.

## Explicit units

Spatial values MUST NOT rely on undocumented implicit units.

Every Project MUST declare a unit system.

## Supported base length units

The initial Core supports:

- millimetres: `mm`
- centimetres: `cm`
- metres: `m`

Implementations MAY support additional units through extensions.

## Recommended internal unit

Millimetres are RECOMMENDED for architectural dimensions.

This recommendation does not require all implementations to store
values internally as millimetres.

## Angles

Supported angle units are:

- degrees;
- radians.

Angle unit MUST be explicit.

## Areas and volumes

Derived units MUST correspond to the declared length unit or be
explicitly specified.

Examples:

- square metres: `m2`;
- cubic metres: `m3`.

## Coordinate reference

Every spatial geometry context MUST declare:

- coordinate-reference identifier;
- dimensionality;
- axis order;
- origin;
- orientation;
- unit.

## Local coordinate systems

Projects MAY use a local Cartesian coordinate system.

A local system SHOULD define:

- origin at `(0, 0)` or `(0, 0, 0)`;
- positive X direction;
- positive Y direction;
- positive Z direction when applicable;
- north or reference orientation when known.

## Global coordinate systems

Geographic or projected coordinate systems MAY be used through an
identified external reference.

## Transformations

Coordinate transformations MUST declare:

- source reference;
- target reference;
- transformation method;
- precision;
- possible information loss.

## Tolerances

Geometry operations MUST use explicit tolerance policies.

A tolerance policy SHOULD include:

- linear tolerance;
- angular tolerance;
- area tolerance where applicable;
- rounding policy.

## Precision

Implementations MUST NOT claim higher precision than their source data
or Kernel supports.
