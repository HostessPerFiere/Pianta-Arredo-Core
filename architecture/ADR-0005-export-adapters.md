# ADR-0005 — Export Adapters

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

The platform must export to multiple formats including DXF, SVG, IFC,
STEP, glTF, JSON and Sweet Home 3D-oriented workflows.

Implementing every format directly inside the Export Service would
couple the domain to external file syntax.

## Decision

Export is divided into two stages.

Spatial Intelligence Model

↓

Export Service

↓

Abstract Export Model

↓

Export Adapter

↓

External format

The Export Service selects and prepares semantic export content.

Each Export Adapter handles:

- file syntax;
- encoding;
- target version;
- unit conversion;
- layer mapping;
- format-specific limitations;
- output generation.

## Required behaviour

Adapters must report:

- unsupported entities;
- information loss;
- approximations;
- compatibility limitations;
- generated format version.

## Consequences

Positive consequences:

- new formats can be added independently;
- export logic remains testable;
- domain concepts are not shaped by one file format;
- format-specific limitations remain isolated.

Negative consequences:

- requires an Abstract Export Model;
- adapters may duplicate some mapping logic;
- conformance tests are needed for each format.

## Alternatives considered

### Direct format generation from SIM

Rejected because SIM would become coupled to every export format.

### One universal export library

Rejected because no single library is expected to support every target
format and semantic requirement.

## Review trigger

Review when the Abstract Export Model cannot represent common needs
shared across multiple Export Adapters.
