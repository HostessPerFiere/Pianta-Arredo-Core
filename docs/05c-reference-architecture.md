# Reference Architecture

Document ID: DOC-005C

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This document presents the reference architecture of the platform.

## Architectural view

Application Layer

↓

Workflow Service

↓

Domain Services

- Knowledge Service
- Geometry Service
- Validation Service
- Export Service

↓

Ports

↓

Kernels and Adapters

↓

External systems and formats

## Cross-cutting components

Cross-cutting components include:

- Event Bus;
- logging;
- tracing;
- versioning;
- configuration;
- security;
- compliance tests.

## Public and private boundaries

### Public

Public contracts include:

- Service interfaces;
- request and response models;
- Events;
- Ports;
- Capabilities;
- error models.

### Private

Private implementation details include:

- algorithms;
- geometry library choices;
- internal caches;
- database drivers;
- rendering code;
- vendor-specific integrations.

## Service and Kernel distinction

A Service is the stable public contract.

A Kernel is one implementation of that contract.

Example:

Geometry Service

↓

Geometry Port

↓

OpenCascade Kernel

or

custom geometry Kernel

## Adapter distinction

Adapters translate between platform contracts and external systems.

Examples:

- DXF Export Adapter;
- SVG Export Adapter;
- Sweet Home 3D Adapter;
- SQLite Persistence Adapter;
- PostgreSQL Persistence Adapter.

## Architectural rule

Domain Services must not depend directly on user interfaces, file
systems, GitHub, databases, cloud providers or AI vendors.

These dependencies must be accessed through Ports.

## Event Bus

The Event Bus supports loose coupling and observability.

Direct synchronous Service calls remain valid when immediate results
are required.

## Applications

Applications assemble Services, Kernels and Adapters.

Pianta-Arredo is the first reference Application.
