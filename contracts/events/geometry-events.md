# Geometry Event Catalogue

Contract ID: EVT-GEO-001

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Defines Events describing completed geometry changes.

## Event rules

- Event names use past tense.
- Events describe completed facts.
- Payloads are versioned.
- Consumers must tolerate unknown optional fields.
- Sensitive data must be minimised.
- Duplicate delivery may occur.
- Global ordering must not be assumed.


## GeometryCreated

A geometric representation has been created.

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

## GeometryUpdated

An existing geometric representation has changed.

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

## WallSplit

A Wall has been split into multiple segments.

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

## WallsMerged

Compatible Wall segments have been merged.

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

## RoomBoundaryGenerated

A Room boundary has been generated.

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
