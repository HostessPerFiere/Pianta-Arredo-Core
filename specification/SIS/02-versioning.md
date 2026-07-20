# SIS Versioning

Specification ID: SIS-002

Version: 0.2-draft

Status: Draft

## Purpose

This document defines versioning rules for specifications, contracts,
schemas, Events and Capabilities.

## Version format

Stable public versions SHOULD use:

MAJOR.MINOR.PATCH

Draft versions MAY use suffixes such as:

- `0.2-draft`
- `0.2-preview.1`
- `1.0-rc.1`

## Major version

A MAJOR version changes when compatibility is intentionally broken.

Examples:

- removing a required field;
- changing the meaning of an existing field;
- changing identifier semantics;
- changing required Service behaviour.

## Minor version

A MINOR version changes for compatible additions.

Examples:

- adding an optional field;
- adding a new Capability;
- adding a new optional operation;
- adding a new Event type.

## Patch version

A PATCH version changes for compatible corrections.

Examples:

- editorial clarification;
- schema correction that does not alter valid data;
- test correction;
- non-normative example correction.

## Schema compatibility

New optional properties MAY be compatible.

Removing required properties is breaking.

Changing a property's type is normally breaking.

Tightening validation rules MAY be breaking.

## Event compatibility

Event consumers SHOULD ignore unknown optional properties.

Event producers MUST preserve required field meaning within a major
version.

## Capability compatibility

Capability identifiers MUST remain stable.

A breaking behavioural change requires a new major Capability version.

## Deprecation

Deprecation MUST document:

- deprecated item;
- replacement;
- reason;
- deprecation version;
- planned removal version;
- migration guidance.

## Migration

Breaking changes MUST include migration guidance when practical.

## Version negotiation

Services and Applications SHOULD be able to determine whether their
supported versions are compatible before executing a workflow.
