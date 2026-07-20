# Coding Style

Version: 0.1

Status: Draft

## General principles

Code should be:

- readable;
- explicit;
- testable;
- deterministic where possible;
- independent from unnecessary frameworks.

## Naming

Use domain vocabulary from the glossary.

Avoid synonyms for established concepts.

Prefer:

- `project_id`;
- `room_boundary`;
- `validation_result`;
- `export_adapter`.

Avoid ambiguous names such as:

- `data`;
- `thing`;
- `manager`;
- `helper`.

## Public contracts

Public names should remain stable and descriptive.

Breaking renames require migration guidance.

## Units

Never hide units in undocumented assumptions.

Prefer explicit names such as:

- `length_mm`;
- `area_m2`;
- `angle_degrees`.

## Errors

Do not use plain strings as the only error representation.

Include machine-readable error codes.

## Comments

Comments should explain why, not restate obvious code.

## Formatting

Language-specific formatters and linters will be defined when reference
implementations are introduced.
