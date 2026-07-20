# Architecture Guide

Version: 0.1

Status: Draft

## Reference architecture

Application

↓

Workflow Service

↓

Domain Services

↓

Ports

↓

Kernels and Adapters

↓

External systems

## Public abstractions

### Service

A stable public contract.

### Kernel

A replaceable implementation of computational behaviour.

### Port

A technology-neutral boundary.

### Adapter

A connection between a Port and a concrete external technology.

### Capability

A discoverable feature declaration.

### Event

A completed fact about platform state.

## Dependency direction

Dependencies must point toward stable contracts.

Domain Services must not depend directly on:

- databases;
- file systems;
- CAD applications;
- cloud providers;
- AI vendors;
- user interfaces.

## Domain-first rule

Generic spatial concepts belong in the Core.

Residential, Office, Retail and other specialisations belong in
Plugins or Knowledge Packages.

## Service and Kernel rule

Applications invoke Services.

Applications must not depend directly on internal Kernel types.

## Export rule

SIM

↓

Export Service

↓

Abstract Export Model

↓

Export Adapter

## Event rule

Events use past-tense names and describe completed facts.

Commands and requests are not Events.

## Architecture review

A change requires architecture review when it:

- introduces a new public dependency;
- changes a Service contract;
- adds a Port;
- changes dependency direction;
- adds a new Plugin lifecycle rule;
- introduces a breaking schema change.
