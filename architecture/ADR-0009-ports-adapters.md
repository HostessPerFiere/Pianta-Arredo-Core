# ADR-0009 — Ports and Adapters Architecture

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

The Core must support different databases, file systems, geometry
libraries, CAD integrations, cloud providers and AI systems.

Direct dependencies on these technologies would create vendor lock-in.

## Decision

The platform adopts Ports and Adapters.

A Port is a contract required or exposed by the platform.

An Adapter connects a Port to a specific external technology.

Examples:

Persistence Port

↓

JSON Adapter

SQLite Adapter

PostgreSQL Adapter

Cloud Adapter

Geometry Port

↓

OpenCascade Adapter

custom Kernel Adapter

AI Assistance Port

↓

provider-specific Adapter

## Dependency rule

Domain Services depend on Ports.

Adapters depend on Ports.

Ports do not depend on Adapters.

Adapter selection belongs to the Application composition layer.

## Core restrictions

The Core must not directly depend on:

- file systems;
- databases;
- GitHub;
- ChatGPT;
- CAD products;
- cloud providers;
- messaging vendors.

## Consequences

Positive consequences:

- technology replacement;
- easier testing;
- reduced vendor lock-in;
- multiple deployment options.

Negative consequences:

- more interfaces;
- configuration complexity;
- mapping overhead;
- risk of overly generic Ports.

## Alternatives considered

### Direct infrastructure dependencies

Rejected because domain code would be tied to selected technologies.

### One universal infrastructure abstraction

Rejected because unrelated technologies require different contracts.

## Review trigger

Review whenever a Port becomes strongly shaped by one Adapter.
