# SIS Conformance

Specification ID: SIS-001

Version: 0.2-draft

Status: Draft

## Purpose

This document defines how implementations declare conformance with SIS.

## Conformance statement

A conforming implementation MUST declare:

- supported SIS version;
- supported SIM version;
- implemented Services;
- implemented Ports;
- declared Capabilities;
- known limitations;
- applicable extensions;
- compliance-suite version.

## Conformance levels

### Schema Conformance

Data satisfies the applicable machine-readable schemas.

### Model Conformance

SIM entities and relationships satisfy normative model rules.

### Service Conformance

Public Service behaviour satisfies the applicable Service contracts.

### Adapter Conformance

An Adapter satisfies the applicable Port contract.

### Capability Conformance

A declared Capability passes its required tests.

### Full Platform Conformance

The implementation satisfies all REQUIRED requirements for its declared
profile.

## Conformance profiles

Implementations MAY declare profiles such as:

- Core Model Profile;
- Geometry Profile;
- Validation Profile;
- Export Profile;
- Application Profile.

A profile MUST list its required documents and tests.

## Partial implementations

Partial implementations are permitted.

They MUST NOT claim unsupported Capabilities.

Unsupported behaviour MUST produce a structured error.

## Compliance evidence

Conformance evidence SHOULD include:

- test-suite version;
- execution date;
- implementation version;
- test results;
- excluded optional tests;
- known deviations.

## Non-conformance

An implementation is non-conforming when it:

- violates a REQUIRED rule;
- declares unsupported Capabilities;
- exposes incompatible public behaviour;
- silently ignores required validation;
- produces invalid normative data.

## Certification

Release 0.2 defines self-declared conformance only.

Independent certification MAY be introduced later.
