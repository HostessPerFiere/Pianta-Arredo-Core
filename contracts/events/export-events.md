# Export Event Catalogue

Contract ID: EVT-EXP-001

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Defines Events describing export preparation and generation.

## Event rules

- Event names use past tense.
- Events describe completed facts.
- Payloads are versioned.
- Consumers must tolerate unknown optional fields.
- Sensitive data must be minimised.
- Duplicate delivery may occur.
- Global ordering must not be assumed.


## ExportPrepared

An abstract export model has been prepared.

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

## ExportCompleted

An export artifact has been generated.

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

## ExportFailed

An export operation has failed.

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
