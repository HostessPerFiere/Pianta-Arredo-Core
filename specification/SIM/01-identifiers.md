# SIM Identifiers

Specification ID: SIM-001

Version: 0.2-draft

Status: Draft

## Purpose

This document defines identifier requirements for SIM entities and
related platform objects.

## Identifier requirements

Every persistent entity MUST have a stable identifier.

An identifier MUST:

- be non-empty;
- be unique within its declared scope;
- remain stable across serialisation;
- remain stable across export where supported;
- be treated as opaque by consumers.

## Opaque identifiers

Consumers MUST NOT infer business meaning from identifier structure.

An identifier such as:

`room-123`

MAY be readable, but consumers MUST NOT assume that `123` has semantic
meaning.

## Recommended format

UUID or another collision-resistant identifier format is RECOMMENDED.

Human-readable prefixes MAY be used.

Example:

`room_550e8400-e29b-41d4-a716-446655440000`

## Identifier types

The platform distinguishes:

- project identifier;
- entity identifier;
- revision identifier;
- Event identifier;
- correlation identifier;
- causation identifier;
- operation identifier;
- artifact identifier.

## Scope

Identifier uniqueness MUST be declared.

Typical scopes include:

- global;
- repository;
- Project;
- Event stream;
- export artifact.

## Revisions

Editing an entity SHOULD preserve the entity identifier.

The revision identifier MUST change when a new persistent revision is
created.

## Deleted entities

Deleted identifiers SHOULD NOT be reused within the same Project.

## External identifiers

Imported identifiers MAY be preserved as external references.

External identifiers MUST NOT replace the platform identifier unless
they satisfy all normative requirements.
