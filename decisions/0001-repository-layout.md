# Decision 0001 — Repository Layout

Status: Active temporary decision

Release: 0.1

Date: 2026-07-20

## Decision

Pianta-Arredo-Core initially contains specification, architecture,
contracts, implementations and application-oriented material in one
repository.

The repository is organised so that the stable specification can
later be extracted into:

`Spatial-Intelligence-Specification`

## Reason

A single repository reduces complexity during the foundation stage
while preserving a future separation path.

## Review trigger

Review during Release 0.5 or earlier when independent implementations
require a separately versioned specification.
