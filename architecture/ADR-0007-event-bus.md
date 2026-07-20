# ADR-0007 — Event Bus

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

The platform requires observability, plugin integration, asynchronous
workflows and loose coupling between some components.

Direct calls alone would make secondary reactions difficult to extend.

## Decision

The platform introduces an Event Bus for publishing domain and
integration Events.

Examples include:

- WallCreated;
- ValidationRequested;
- ValidationCompleted;
- GeometryGenerated;
- ExportCompleted;
- ProjectPublished.

Events describe completed facts and use past-tense names.

## Boundaries

The Event Bus does not replace every direct Service call.

Direct calls remain appropriate when:

- an immediate response is required;
- an operation is part of one explicit transaction;
- failure must be returned synchronously.

Events are appropriate for:

- notifications;
- plugins;
- audit trails;
- background work;
- integration;
- observability.

## Consequences

Positive consequences:

- loose coupling;
- extensibility;
- plugin support;
- asynchronous processing;
- better auditability.

Negative consequences:

- ordering complexity;
- duplicate delivery handling;
- eventual consistency;
- harder debugging without tracing.

## Alternatives considered

### Direct calls only

Rejected because extensions would require modifying existing Services.

### Event-only architecture

Rejected because simple synchronous operations would become
unnecessarily complex.

## Review trigger

Review when the first persistent or distributed Event Bus is
implemented.
