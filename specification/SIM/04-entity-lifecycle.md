# SIM Entity Lifecycle

Specification ID: SIM-004

Version: 0.2-draft

Status: Draft

## Purpose

This document defines lifecycle rules for SIM entities and revisions.

## Entity states

The initial entity lifecycle supports:

- Draft;
- Active;
- Superseded;
- Deleted.

## Draft

A Draft entity MAY be incomplete.

Draft entities MUST NOT be presented as validated unless they have a
separate successful validation result.

## Active

An Active entity is part of the current Project revision.

Active does not imply regulatory or professional approval.

## Superseded

A Superseded entity has been replaced by a newer revision or entity.

It SHOULD remain traceable when revision history is retained.

## Deleted

A Deleted entity is no longer active.

Deletion SHOULD preserve an audit reference where permitted.

## Creation metadata

Every entity SHOULD record:

- created timestamp;
- creating actor;
- source;
- initial revision identifier.

## Modification metadata

Modified entities SHOULD record:

- modified timestamp;
- modifying actor;
- revision identifier;
- change reason where available.

## Identity across revisions

An edited entity SHOULD retain its entity identifier.

Each persistent Project revision MUST have a distinct revision
identifier.

## Replacement

When one entity replaces another, the relationship SHOULD identify:

- previous entity or revision;
- replacement entity or revision;
- replacement reason;
- timestamp.

## Deletion and references

An entity MUST NOT be deleted silently when required references still
depend on it.

Implementations MUST either:

- reject deletion;
- update dependent references;
- mark references as unresolved;
- perform an explicitly declared cascading operation.

## Events

Recommended lifecycle Events include:

- EntityCreated;
- EntityActivated;
- EntitySuperseded;
- EntityDeleted;
- EntityRestored.
