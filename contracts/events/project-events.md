# Project Event Catalogue

Contract ID: EVT-PRJ-001

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Defines Events describing project lifecycle and state transitions.

## Event rules

- Event names use past tense.
- Events describe completed facts.
- Payloads are versioned.
- Consumers must tolerate unknown optional fields.
- Sensitive data must be minimised.
- Duplicate delivery may occur.
- Global ordering must not be assumed.


## ProjectCreated

A new Project has been created.

Minimum payload:

- eventId;
- eventType;
- eventVersion;
- occurredAt;
- projectId;
- subjectId;
- correlationId;
- causationId;
- actor;
- payload.

## ProjectNormalized

Project inputs have been normalised.

Minimum payload:

- eventId;
- eventType;
- eventVersion;
- occurredAt;
- projectId;
- subjectId;
- correlationId;
- causationId;
- actor;
- payload.

## ProjectStateChanged

The Project has entered a new lifecycle state.

Minimum payload:

- eventId;
- eventType;
- eventVersion;
- occurredAt;
- projectId;
- subjectId;
- correlationId;
- causationId;
- actor;
- payload.

## ProjectPublished

A Project revision has been intentionally published.

Minimum payload:

- eventId;
- eventType;
- eventVersion;
- occurredAt;
- projectId;
- subjectId;
- correlationId;
- causationId;
- actor;
- payload.


## Compatibility

Removing or changing the meaning of a required field is a breaking
change.

New optional fields are compatible additions.

## Conformance

Producers and consumers must pass applicable event schema and
compatibility tests.
