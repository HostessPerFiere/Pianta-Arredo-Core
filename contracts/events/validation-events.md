# Validation Event Catalogue

Contract ID: EVT-VAL-001

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Defines Events describing validation execution and results.

## Event rules

- Event names use past tense.
- Events describe completed facts.
- Payloads are versioned.
- Consumers must tolerate unknown optional fields.
- Sensitive data must be minimised.
- Duplicate delivery may occur.
- Global ordering must not be assumed.


## ValidationStarted

A validation operation has started.

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

## ValidationCompleted

A validation operation has completed.

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

## ValidationFailed

A validation operation could not be completed.

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
