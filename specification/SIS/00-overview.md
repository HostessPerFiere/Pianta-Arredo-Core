# SIS Overview

Specification ID: SIS-000

Version: 0.2-draft

Status: Draft

## Purpose

The Spatial Intelligence Specification defines the normative public
behaviour of the platform.

SIS is independent from:

- programming languages;
- geometry libraries;
- databases;
- CAD applications;
- rendering systems;
- cloud providers;
- AI providers;
- user-interface frameworks.

## Scope

SIS defines:

- normative vocabulary;
- public concepts;
- identifiers;
- units;
- coordinate systems;
- entity lifecycle;
- Service contracts;
- Ports;
- Events;
- Capabilities;
- errors;
- versioning;
- conformance.

## Relationship with SIM

SIS defines rules.

SIM represents spatial information governed by those rules.

SIS

↓

SIM

↓

Services

↓

Kernels and Adapters

## Normative and non-normative material

Normative material defines requirements.

Non-normative material provides examples, explanations or guidance.

Every specification document SHOULD identify which sections are
normative.

## Implementation independence

An implementation MAY use any internal architecture that satisfies the
public requirements and compliance tests.

Public contracts MUST NOT expose implementation-specific types unless
explicitly standardised.

## Extensibility

Extensions MAY introduce new domain concepts or Capabilities.

Extensions MUST NOT redefine the meaning of stable Core concepts.

## Security and privacy

Implementations MUST treat spatial data as potentially sensitive.

Public contracts SHOULD minimise unnecessary disclosure of:

- addresses;
- access routes;
- occupancy information;
- infrastructure details;
- personal data.

## Professional responsibility

SIS does not replace professional verification for structural,
regulatory, accessibility, fire-safety or authorisation matters.
