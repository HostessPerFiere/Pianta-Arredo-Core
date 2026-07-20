# Events

Document ID: DOC-011

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Events communicate completed facts about the platform state.

## Event rule

Event names should use past tense.

Examples:

- WallCreated
- OpeningMoved
- ProjectNormalized
- ValidationCompleted
- GeometryGenerated
- ExportCompleted

## Event structure

Every Event should include:

- event identifier;
- event type;
- event version;
- timestamp;
- project identifier;
- subject identifier;
- correlation identifier;
- causation identifier;
- actor;
- payload.

## Domain Events

Domain Events describe meaningful spatial or project changes.

## Integration Events

Integration Events expose selected facts to external systems.

Internal Domain Events must not automatically become public Integration
Events.

## Ordering

Consumers must not assume global ordering unless an implementation
explicitly guarantees it.

## Delivery

The platform may support:

- in-process delivery;
- queued delivery;
- persistent delivery;
- external messaging.

## Duplicate delivery

Consumers should be prepared for duplicate Events where delivery is at
least once.

## Event compatibility

Event payloads must be versioned.

Compatible consumers should ignore unknown optional fields.

## Privacy

Events must not expose unnecessary spatial or personal information.
