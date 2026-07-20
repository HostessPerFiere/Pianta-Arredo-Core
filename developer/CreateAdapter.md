# Create an Adapter

Version: 0.1

Status: Draft

## Purpose

An Adapter connects a public Port to a concrete external technology.

## Examples

- SQLite Persistence Adapter;
- PostgreSQL Persistence Adapter;
- SVG Export Adapter;
- DXF Export Adapter;
- OpenCascade Geometry Adapter;
- external AI provider Adapter.

## Required behaviour

An Adapter must:

- implement one published Port;
- declare supported Capabilities;
- avoid changing domain semantics;
- convert vendor-specific errors into public errors;
- preserve identifiers and traceability;
- report information loss;
- document security requirements.

## Input and output mapping

Mapping code belongs in the Adapter.

Domain Services must not import Adapter-specific types.

## Failure handling

Adapter failure must produce a structured result.

It must not silently corrupt the SIM or Project state.

## Testing

Every Adapter should have:

- unit tests;
- Port conformance tests;
- compatibility tests;
- failure-mode tests;
- representative sample files where applicable.

## Selection

Adapter selection belongs to the Application composition layer.
