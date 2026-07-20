# Dependency Matrix

Document ID: DOC-015

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This document defines allowed high-level dependencies.

## Rule legend

Allowed means the source may depend on the target.

Forbidden means the dependency must not exist.

## Matrix

| Source | Domain Model | Workflow | Geometry | Validation | Knowledge | Export | Ports | Adapters | UI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Domain Model | — | No | No | No | No | No | No | No | No |
| Workflow | Yes | — | Yes | Yes | Yes | Yes | Yes | No | No |
| Geometry | Yes | No | — | No | No | No | Yes | No | No |
| Validation | Yes | No | Yes | — | Yes | No | Yes | No | No |
| Knowledge | Yes | No | No | No | — | No | Yes | No | No |
| Export | Yes | No | No | Yes | No | — | Yes | No | No |
| Ports | Yes | No | No | No | No | No | — | No | No |
| Adapters | Yes | No | No | No | No | No | Yes | — | No |
| UI | Yes | Yes | No | No | No | No | Yes | No | — |

## Key restrictions

Geometry must not depend on Knowledge.

Export must not modify the Spatial Intelligence Model.

Domain Model must not depend on Services.

Services must not depend directly on Adapters.

Adapters must not define domain rules.

UI must not become the source of domain truth.

## Architecture tests

Future implementations should enforce these rules automatically.
