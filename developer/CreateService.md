# Create a Service

Version: 0.1

Status: Draft

## Purpose

A Service exposes stable public behaviour independently from a specific
implementation.

## Required contract sections

Every Service contract must define:

- purpose;
- operations;
- inputs;
- outputs;
- errors;
- Events;
- Capabilities;
- versioning;
- conformance expectations.

## Design rules

A Service must:

- use public domain types;
- avoid vendor-specific objects;
- define explicit units;
- define coordinate references where spatial data is involved;
- return structured errors;
- declare optional behaviour through Capabilities.

## Kernel relationship

A Kernel may implement one or more Service responsibilities.

Kernel implementation details must not leak into public responses.

## Service checklist

Before adding a Service, verify:

- the responsibility is not already covered;
- the boundary is domain-oriented;
- dependencies point toward Ports;
- operations are testable;
- Events represent completed facts;
- compatibility rules are documented.

## Naming

Use descriptive names such as:

- Geometry Service;
- Validation Service;
- Knowledge Service;
- Export Service.

Avoid vague names such as Manager, Utility or General Service.
