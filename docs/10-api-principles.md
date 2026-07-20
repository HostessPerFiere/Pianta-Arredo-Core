# API Principles

Document ID: DOC-010

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This document defines principles for public APIs and Service contracts.

## Contract first

Public behaviour should be defined before implementation details.

## Explicit input and output

Every operation must define:

- request;
- response;
- errors;
- side effects;
- Events;
- required Capabilities;
- version.

## Stable identifiers

Entities, requests, results and Events should use stable identifiers.

## Units

APIs must never assume undocumented units.

## Coordinate systems

Spatial operations must declare the applicable coordinate reference.

## Idempotency

Operations that may be retried should define idempotency behaviour.

## Errors

Errors must be machine-readable and human-readable.

They should include:

- code;
- message;
- subject;
- context;
- recoverability;
- suggested action.

## Versioning

Public APIs must distinguish compatible changes from breaking changes.

## Pagination and filtering

Collection APIs should support predictable pagination and filtering
when result size may grow.

## Synchronous and asynchronous operations

Immediate operations may be synchronous.

Long-running operations should expose progress, cancellation and result
retrieval.

## Security

APIs must minimise access to sensitive spatial data.

## Vendor neutrality

Public contracts must not expose vendor-specific implementation types.

## Human readability

Contract definitions should remain understandable without proprietary
tooling.
