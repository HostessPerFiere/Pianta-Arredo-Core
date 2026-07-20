# ADR-0004 — Service and Kernel Separation

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

Terms such as Geometry Engine or Validation Engine can ambiguously refer
to either a public contract or a concrete implementation.

Applications need stable interfaces even when algorithms or libraries
change.

## Decision

The platform distinguishes:

### Service

A Service is a public contract describing:

- requests;
- responses;
- errors;
- Capabilities;
- Events;
- behavioural guarantees.

### Kernel

A Kernel is a concrete implementation of one or more Service
responsibilities.

Example:

Geometry Service

↓

Geometry Port

↓

OpenCascade Kernel

or another compatible Kernel.

Public APIs must not expose proprietary Kernel types.

## Consequences

Positive consequences:

- implementation replacement;
- stable Application contracts;
- easier testing with test doubles;
- support for multiple language implementations.

Negative consequences:

- mapping between public and internal types;
- additional interfaces;
- capability differences between Kernels.

## Alternatives considered

### Expose Kernel APIs directly

Rejected because consumers would depend on one implementation.

### Use Engine as both contract and implementation

Rejected because the abstraction boundary would remain unclear.

## Review trigger

Review if maintaining the separation introduces measurable complexity
without supporting more than one implementation.
