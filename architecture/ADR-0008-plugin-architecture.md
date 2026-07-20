# ADR-0008 — Plugin Architecture

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

The platform must support residential, office, retail, healthcare and
other domains without placing every specialised rule or feature in the
Core.

## Decision

Generic concepts remain in the Core.

Specialised behaviour is delivered through Plugins or Knowledge
Packages.

Plugins may provide:

- Capabilities;
- Knowledge Packages;
- Validators;
- Adapters;
- schemas;
- commands;
- Events;
- application components.

Every Plugin must declare a manifest containing:

- identifier;
- version;
- compatible SIS version;
- required Capabilities;
- provided Capabilities;
- permissions;
- dependencies;
- entry points;
- license.

## Isolation

Plugins must interact through public contracts.

Plugins must not directly mutate undocumented internal state.

Plugin failure must not silently corrupt the project.

## Consequences

Positive consequences:

- smaller generic Core;
- domain extensibility;
- independent release cycles;
- community contributions.

Negative consequences:

- compatibility management;
- security risks;
- dependency conflicts;
- need for lifecycle rules.

## Alternatives considered

### Put every domain in Core

Rejected because the Core would become large and unstable.

### Independent applications with duplicated logic

Rejected because shared spatial concepts would diverge.

## Review trigger

Review before publishing the Plugin SDK in Release 0.5.
