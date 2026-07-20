# Dependency Rules

Version: 0.1

Status: Draft

## Allowed direction

Application

↓

Services

↓

Domain Model and Ports

↑

Adapters and Kernels

## Rules

### Rule ARCH-001

Domain Model must not import Service modules.

### Rule ARCH-002

Service modules must not import concrete Adapter modules.

### Rule ARCH-003

Geometry modules must not depend on Knowledge implementations.

### Rule ARCH-004

Export components must not modify SIM state during export.

### Rule ARCH-005

User-interface modules must not define canonical domain entities.

### Rule ARCH-006

Plugins must access the platform through published contracts.

### Rule ARCH-007

Public contracts must not expose proprietary infrastructure types.

### Rule ARCH-008

Adapter selection must occur in the Application composition layer.

## Enforcement

Each rule should later be associated with:

- an automated test;
- an owner;
- a severity;
- an exception process;
- an ADR reference.
