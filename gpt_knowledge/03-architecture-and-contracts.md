# Pianta-Arredo-Core — 03-architecture-and-contracts.md

Documento consolidato per il GPT.

---

## File originale: `api/README.md`

# Api

Public API descriptions.


---

## File originale: `architecture/ADR-0001-layered-architecture.md`




---

## File originale: `architecture/ADR-0002-sis-sim-sie.md`

# ADR-0002 — SIS, SIM and SIE Separation

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

The project needs to distinguish the normative specification, the
spatial data model and the software that executes spatial operations.

Using one term for all three would create ambiguity between rules,
data and implementation.

## Decision

The platform adopts three distinct concepts.

### Spatial Intelligence Specification — SIS

SIS defines normative concepts, contracts, compatibility rules and
conformance expectations.

### Spatial Intelligence Model — SIM

SIM represents spatial entities, relationships, geometry references,
project state and metadata.

### Spatial Intelligence Engine — SIE

SIE is the runtime platform formed by Services, Kernels, Adapters,
workflows and supporting infrastructure.

Public architecture should generally refer to Services rather than
exposing internal Engines or Kernels.

## Dependency direction

SIS

↓

SIM

↓

Services

↓

Kernels and Adapters

↓

Applications

Implementations conform to SIS.

SIS must not depend on one implementation.

## Consequences

Positive consequences:

- independent specification evolution;
- multiple possible implementations;
- clearer conformance testing;
- easier future repository separation.

Negative consequences:

- more terminology;
- additional version coordination;
- need for compatibility documentation.

## Alternatives considered

### One unified Core model

Rejected because normative rules and implementation details would
become inseparable.

### Implementation-first specification

Rejected because the first implementation would become the accidental
standard.

## Review trigger

Review before extracting SIS into the independent
Spatial-Intelligence-Specification repository.


---

## File originale: `architecture/ADR-0003-domain-first.md`

# ADR-0003 — Domain-First Design

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

Spatial applications may have different interfaces and technologies,
but they share concepts such as Projects, Buildings, Floors, Spaces,
Rooms, Walls, Openings and Furniture.

Allowing each Application to define these concepts independently would
create incompatible models.

## Decision

The platform adopts a domain-first approach.

Generic spatial concepts are defined before:

- user-interface components;
- database tables;
- CAD format mappings;
- rendering objects;
- AI prompts;
- application-specific workflows.

The Core contains generic concepts.

Domain Packages and Plugins provide specialisations such as:

- Residential;
- Office;
- Retail;
- Healthcare;
- Exhibition;
- Hospitality.

## Consequences

Positive consequences:

- shared vocabulary;
- reusable Services;
- consistent export and validation;
- reduced duplication between Applications.

Negative consequences:

- domain modelling requires early effort;
- some application-specific shortcuts are prohibited;
- disagreements require glossary and taxonomy updates.

## Alternatives considered

### UI-first modelling

Rejected because screens and controls would define the data model.

### Database-first modelling

Rejected because persistence concerns would shape domain concepts.

### Format-first modelling

Rejected because DXF, IFC or another format would impose its limitations
on the internal model.

## Review trigger

Review when a new domain cannot be represented without repeatedly
introducing exceptions into the generic model.


---

## File originale: `architecture/ADR-0004-service-kernel-separation.md`

# ADR-0004 — Service and Kernel Separation

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

Terms such as Geometry Engine or Validation Engine can ambiguously refer
to either a public contract or a concrete implementation.

Applications need stable interfaces even when algorithms or libraries
change.

## Decision

The platform distinguishes:

### Service

A Service is a public contract describing:

- requests;
- responses;
- errors;
- Capabilities;
- Events;
- behavioural guarantees.

### Kernel

A Kernel is a concrete implementation of one or more Service
responsibilities.

Example:

Geometry Service

↓

Geometry Port

↓

OpenCascade Kernel

or another compatible Kernel.

Public APIs must not expose proprietary Kernel types.

## Consequences

Positive consequences:

- implementation replacement;
- stable Application contracts;
- easier testing with test doubles;
- support for multiple language implementations.

Negative consequences:

- mapping between public and internal types;
- additional interfaces;
- capability differences between Kernels.

## Alternatives considered

### Expose Kernel APIs directly

Rejected because consumers would depend on one implementation.

### Use Engine as both contract and implementation

Rejected because the abstraction boundary would remain unclear.

## Review trigger

Review if maintaining the separation introduces measurable complexity
without supporting more than one implementation.


---

## File originale: `architecture/ADR-0005-export-adapters.md`

# ADR-0005 — Export Adapters

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

The platform must export to multiple formats including DXF, SVG, IFC,
STEP, glTF, JSON and Sweet Home 3D-oriented workflows.

Implementing every format directly inside the Export Service would
couple the domain to external file syntax.

## Decision

Export is divided into two stages.

Spatial Intelligence Model

↓

Export Service

↓

Abstract Export Model

↓

Export Adapter

↓

External format

The Export Service selects and prepares semantic export content.

Each Export Adapter handles:

- file syntax;
- encoding;
- target version;
- unit conversion;
- layer mapping;
- format-specific limitations;
- output generation.

## Required behaviour

Adapters must report:

- unsupported entities;
- information loss;
- approximations;
- compatibility limitations;
- generated format version.

## Consequences

Positive consequences:

- new formats can be added independently;
- export logic remains testable;
- domain concepts are not shaped by one file format;
- format-specific limitations remain isolated.

Negative consequences:

- requires an Abstract Export Model;
- adapters may duplicate some mapping logic;
- conformance tests are needed for each format.

## Alternatives considered

### Direct format generation from SIM

Rejected because SIM would become coupled to every export format.

### One universal export library

Rejected because no single library is expected to support every target
format and semantic requirement.

## Review trigger

Review when the Abstract Export Model cannot represent common needs
shared across multiple Export Adapters.


---

## File originale: `architecture/ADR-0006-engine-capabilities.md`

# ADR-0006 — Declared Capabilities

Status: Accepted

Date: 2026-07-20

Decision owner: Spatial Intelligence Platform

## Context

Different Services, Kernels, Adapters and Plugins may support different
operations or levels of precision.

Applications must not assume that every implementation supports every
feature.

## Decision

Every replaceable component must publish explicit Capabilities.

A Capability descriptor includes:

- identifier;
- version;
- status;
- supported inputs;
- supported outputs;
- limits;
- required dependencies;
- known restrictions.

Example Geometry Capabilities:

- CreateWall;
- SplitWall;
- MergeWalls;
- OffsetWall;
- GenerateRoomBoundary;
- CalculateArea.

Example Validation Capabilities:

- ValidateTopology;
- ValidateDimensions;
- ValidateRoomClosure;
- ValidateOpeningPlacement.

Applications may negotiate Capabilities before invoking operations.

## Partial support

Partial support must be declared explicitly.

Unsupported operations must return structured errors.

## Consequences

Positive consequences:

- safer implementation replacement;
- runtime feature discovery;
- clearer compatibility;
- better plugin composition.

Negative consequences:

- capability catalogues require governance;
- negotiation adds complexity;
- version compatibility must be maintained.

## Alternatives considered

### Infer features from implementation name

Rejected because names do not provide reliable contracts.

### Fail only when an operation is called

Rejected because Applications need to plan workflows before execution.

## Review trigger

Review when the capability model becomes too granular or expensive to
negotiate.


---

## File originale: `architecture/ADR-0007-event-bus.md`

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


---

## File originale: `architecture/ADR-0008-plugin-architecture.md`

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


---

## File originale: `architecture/ADR-0009-ports-adapters.md`

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


---

## File originale: `architecture/INDEX.md`

# Architecture Decision Index

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Accepted decisions

| ADR | Title | Status |
|---|---|---|
| ADR-0001 | Layered Architecture | Accepted |
| ADR-0002 | SIS, SIM and SIE Separation | Accepted |
| ADR-0003 | Domain-First Design | Accepted |
| ADR-0004 | Service and Kernel Separation | Accepted |
| ADR-0005 | Export Adapters | Accepted |
| ADR-0006 | Declared Capabilities | Accepted |
| ADR-0007 | Event Bus | Accepted |
| ADR-0008 | Plugin Architecture | Accepted |
| ADR-0009 | Ports and Adapters Architecture | Accepted |

## Decision lifecycle

Proposed

↓

Under Review

↓

Accepted

↓

Superseded or Deprecated

## Repository distinction

Temporary operational decisions belong in `decisions/`.

Significant proposals under discussion belong in `rfc/`.

Accepted architectural decisions belong in `architecture/`.

Stable normative behaviour belongs in `specification/`.

## Naming

ADR filenames use:

`ADR-NNNN-short-title.md`

ADR numbers are never reused.


---

## File originale: `architecture/README.md`

# Architecture

Approved Architecture Decision Records.


---

## File originale: `contracts/INDEX.md`

# Contract Index

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Services

| Contract | File |
|---|---|
| Geometry Service | `services/geometry-service.md` |
| Validation Service | `services/validation-service.md` |
| Knowledge Service | `services/knowledge-service.md` |
| Export Service | `services/export-service.md` |

## Ports

| Contract | File |
|---|---|
| Geometry Port | `ports/geometry-port.md` |
| Persistence Port | `ports/persistence-port.md` |
| Event Bus Port | `ports/event-bus-port.md` |
| Export Port | `ports/export-port.md` |

## Events

| Catalogue | File |
|---|---|
| Project Events | `events/project-events.md` |
| Geometry Events | `events/geometry-events.md` |
| Validation Events | `events/validation-events.md` |
| Export Events | `events/export-events.md` |

## Capabilities

| Catalogue | File |
|---|---|
| Geometry Capabilities | `capabilities/geometry-capabilities.md` |
| Validation Capabilities | `capabilities/validation-capabilities.md` |
| Knowledge Capabilities | `capabilities/knowledge-capabilities.md` |
| Export Capabilities | `capabilities/export-capabilities.md` |

## Contract maturity

All Package D contracts are Draft.

They become normative only after review and promotion into the stable
specification.

## Rules

- Services define public behaviour.
- Kernels implement Service responsibilities.
- Ports define replaceable boundaries.
- Adapters implement Ports.
- Events describe completed facts.
- Capabilities declare supported behaviour.


---

## File originale: `contracts/README.md`

# Contracts

Public contracts.


---

## File originale: `contracts/capabilities/README.md`

# Capabilities

Declared Capabilities.


---

## File originale: `contracts/capabilities/export-capabilities.md`

# Export Capability Catalogue

        Contract ID: CAP-EXP-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines discoverable export features.

        ## Capability descriptor

        Every Capability declaration includes:

        - identifier;
        - version;
        - status;
        - supported inputs;
        - supported outputs;
        - limits;
        - dependencies;
        - restrictions.

        ## Catalogue

        | Capability | Description | Status |
        |---|---|---|
        | `Export2D` | Export two-dimensional representations. | Draft |
| `Export3D` | Export three-dimensional representations. | Draft |
| `ExportSemanticModel` | Preserve semantic spatial entities. | Draft |
| `ExportDimensions` | Export dimensions and measurement annotations. | Draft |
| `ExportLayers` | Preserve or map semantic layers. | Draft |
| `ExportMetadata` | Export project and entity metadata. | Draft |
| `ReportInformationLoss` | Report unsupported or approximated content. | Draft |

        ## Negotiation

        Applications may query Capabilities before constructing a workflow.

        Partial support must be declared explicitly.

        ## Unsupported behaviour

        An unavailable Capability must produce a structured
        `CapabilityNotSupported` error.

        ## Versioning

        Capability identifiers are stable.

        Behavioural breaking changes require a new major Capability version.

        ## Conformance

        A component may declare a Capability only when its corresponding
        compliance tests pass.


---

## File originale: `contracts/capabilities/geometry-capabilities.md`

# Geometry Capability Catalogue

        Contract ID: CAP-GEO-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines discoverable Geometry Service and Kernel features.

        ## Capability descriptor

        Every Capability declaration includes:

        - identifier;
        - version;
        - status;
        - supported inputs;
        - supported outputs;
        - limits;
        - dependencies;
        - restrictions.

        ## Catalogue

        | Capability | Description | Status |
        |---|---|---|
        | `CreateWall` | Create a Wall geometry representation. | Draft |
| `SplitWall` | Split a Wall at one or more positions. | Draft |
| `MergeWalls` | Merge compatible Wall segments. | Draft |
| `OffsetWall` | Create a parallel Wall offset. | Draft |
| `CreateOpening` | Create a Door or Window opening. | Draft |
| `GenerateRoomBoundary` | Generate a closed Room boundary. | Draft |
| `CalculateArea` | Calculate area using declared units and tolerance. | Draft |
| `TransformCoordinates` | Transform geometry between coordinate references. | Draft |

        ## Negotiation

        Applications may query Capabilities before constructing a workflow.

        Partial support must be declared explicitly.

        ## Unsupported behaviour

        An unavailable Capability must produce a structured
        `CapabilityNotSupported` error.

        ## Versioning

        Capability identifiers are stable.

        Behavioural breaking changes require a new major Capability version.

        ## Conformance

        A component may declare a Capability only when its corresponding
        compliance tests pass.


---

## File originale: `contracts/capabilities/knowledge-capabilities.md`

# Knowledge Capability Catalogue

        Contract ID: CAP-KNW-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines discoverable Knowledge Service operations.

        ## Capability descriptor

        Every Capability declaration includes:

        - identifier;
        - version;
        - status;
        - supported inputs;
        - supported outputs;
        - limits;
        - dependencies;
        - restrictions.

        ## Catalogue

        | Capability | Description | Status |
        |---|---|---|
        | `ResolveRule` | Resolve an applicable rule. | Draft |
| `ListApplicableRules` | List rules for a project context. | Draft |
| `ResolveDefault` | Resolve a versioned default value. | Draft |
| `ResolveClassification` | Resolve a domain classification. | Draft |
| `ExplainRule` | Return traceability and explanation. | Draft |
| `CompareKnowledgeVersions` | Compare two Knowledge Package versions. | Draft |

        ## Negotiation

        Applications may query Capabilities before constructing a workflow.

        Partial support must be declared explicitly.

        ## Unsupported behaviour

        An unavailable Capability must produce a structured
        `CapabilityNotSupported` error.

        ## Versioning

        Capability identifiers are stable.

        Behavioural breaking changes require a new major Capability version.

        ## Conformance

        A component may declare a Capability only when its corresponding
        compliance tests pass.


---

## File originale: `contracts/capabilities/validation-capabilities.md`

# Validation Capability Catalogue

        Contract ID: CAP-VAL-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines discoverable validation operations.

        ## Capability descriptor

        Every Capability declaration includes:

        - identifier;
        - version;
        - status;
        - supported inputs;
        - supported outputs;
        - limits;
        - dependencies;
        - restrictions.

        ## Catalogue

        | Capability | Description | Status |
        |---|---|---|
        | `ValidateTopology` | Validate spatial connectivity and enclosure. | Draft |
| `ValidateDimensions` | Validate dimensions and tolerances. | Draft |
| `ValidateRoomClosure` | Verify that a Room boundary is closed. | Draft |
| `ValidateOpeningPlacement` | Validate Doors and Windows on host Walls. | Draft |
| `ValidateDomainRules` | Apply rules supplied by Knowledge Packages. | Draft |
| `ValidateExportReadiness` | Verify readiness for a target export. | Draft |

        ## Negotiation

        Applications may query Capabilities before constructing a workflow.

        Partial support must be declared explicitly.

        ## Unsupported behaviour

        An unavailable Capability must produce a structured
        `CapabilityNotSupported` error.

        ## Versioning

        Capability identifiers are stable.

        Behavioural breaking changes require a new major Capability version.

        ## Conformance

        A component may declare a Capability only when its corresponding
        compliance tests pass.


---

## File originale: `contracts/errors/error-catalogue.md`

# Error Catalogue

Version: 0.2-draft

Status: Draft

## Core errors

| Code | Meaning |
|---|---|
| `InvalidRequest` | Request structure or values are invalid |
| `EntityNotFound` | Referenced entity does not exist |
| `RevisionConflict` | Project revision is no longer current |
| `CapabilityNotSupported` | Requested Capability is unavailable |
| `ValidationFailed` | Domain or geometric validation failed |
| `AdapterUnavailable` | Required Adapter cannot be used |
| `InternalFailure` | Unexpected implementation failure |

## Rules

Error codes are stable public identifiers.

Implementations MAY add extension errors.

Extension errors MUST NOT redefine Core error meanings.


---

## File originale: `contracts/events/README.md`

# Events

Domain Event contracts.


---

## File originale: `contracts/events/export-events.md`

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


---

## File originale: `contracts/events/geometry-events.md`

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


---

## File originale: `contracts/events/project-events.md`

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


---

## File originale: `contracts/events/validation-events.md`

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


---

## File originale: `contracts/ports/README.md`

# Ports

Platform Ports.


---

## File originale: `contracts/ports/event-bus-port.md`

# Event Bus Port

        Contract ID: PORT-EVT-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines publication and subscription of domain and integration Events.

        ## Direction

        This Port is a public boundary between platform Services and replaceable
        infrastructure.

        Services depend on the Port.

        Adapters implement the Port.

        The Port must not depend on a concrete Adapter.

        ## Operations

        - publish Event
- publish Event batch
- subscribe by Event type
- unsubscribe
- acknowledge delivery when supported
- declare delivery guarantees

        ## Candidate Adapters

        - in-process Event Bus Adapter
- persistent queue Adapter
- external message broker Adapter
- test Event Bus Adapter

        Adapter names do not alter the public Port contract.

        ## Input and output rules

        - use public identifiers;
        - declare versions;
        - avoid vendor-specific types;
        - return structured results;
        - preserve traceability;
        - report unsupported behaviour.

        ## Errors

        - EventPublicationFailed
- EventSubscriptionFailed
- UnsupportedDeliveryGuarantee
- InvalidEventEnvelope

        ## Security

        Adapters must use the minimum permissions required.

        Sensitive spatial data must not be transmitted or persisted unless
        explicitly authorised by the Application.

        ## Versioning

        Port versions follow public contract compatibility rules.

        ## Conformance

        An Adapter conforms only when it passes the applicable Port compliance
        suite and accurately declares its supported Capabilities.


---

## File originale: `contracts/ports/export-port.md`

# Export Port

        Contract ID: PORT-EXP-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Connects the Export Service to format-specific Export Adapters.

        ## Direction

        This Port is a public boundary between platform Services and replaceable
        infrastructure.

        Services depend on the Port.

        Adapters implement the Port.

        The Port must not depend on a concrete Adapter.

        ## Operations

        - list supported formats
- validate abstract export model
- generate target artifact
- report information loss
- declare Export Capabilities

        ## Candidate Adapters

        - DXF Adapter
- SVG Adapter
- IFC Adapter
- STEP Adapter
- glTF Adapter
- Sweet Home 3D Adapter
- JSON Adapter

        Adapter names do not alter the public Port contract.

        ## Input and output rules

        - use public identifiers;
        - declare versions;
        - avoid vendor-specific types;
        - return structured results;
        - preserve traceability;
        - report unsupported behaviour.

        ## Errors

        - UnsupportedExportFormat
- UnsupportedExportEntity
- ExportEncodingFailed
- TargetVersionUnsupported
- ExportArtifactWriteFailed

        ## Security

        Adapters must use the minimum permissions required.

        Sensitive spatial data must not be transmitted or persisted unless
        explicitly authorised by the Application.

        ## Versioning

        Port versions follow public contract compatibility rules.

        ## Conformance

        An Adapter conforms only when it passes the applicable Port compliance
        suite and accurately declares its supported Capabilities.


---

## File originale: `contracts/ports/geometry-port.md`

# Geometry Port

        Contract ID: PORT-GEO-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Connects the Geometry Service to a replaceable Geometry Kernel.

        ## Direction

        This Port is a public boundary between platform Services and replaceable
        infrastructure.

        Services depend on the Port.

        Adapters implement the Port.

        The Port must not depend on a concrete Adapter.

        ## Operations

        - create geometry
- transform geometry
- query geometry
- calculate measurements
- validate Kernel-level geometry
- declare Geometry Capabilities

        ## Candidate Adapters

        - OpenCascade Adapter
- custom computational geometry Adapter
- test geometry Adapter

        Adapter names do not alter the public Port contract.

        ## Input and output rules

        - use public identifiers;
        - declare versions;
        - avoid vendor-specific types;
        - return structured results;
        - preserve traceability;
        - report unsupported behaviour.

        ## Errors

        - KernelUnavailable
- UnsupportedGeometryOperation
- GeometryKernelFailure
- GeometryPrecisionFailure

        ## Security

        Adapters must use the minimum permissions required.

        Sensitive spatial data must not be transmitted or persisted unless
        explicitly authorised by the Application.

        ## Versioning

        Port versions follow public contract compatibility rules.

        ## Conformance

        An Adapter conforms only when it passes the applicable Port compliance
        suite and accurately declares its supported Capabilities.


---

## File originale: `contracts/ports/persistence-port.md`

# Persistence Port

        Contract ID: PORT-PER-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines storage and retrieval of Projects, revisions, Events and model snapshots.

        ## Direction

        This Port is a public boundary between platform Services and replaceable
        infrastructure.

        Services depend on the Port.

        Adapters implement the Port.

        The Port must not depend on a concrete Adapter.

        ## Operations

        - save project
- load project
- save revision
- list revisions
- load revision
- delete permitted data
- check optimistic concurrency

        ## Candidate Adapters

        - JSON file Adapter
- SQLite Adapter
- PostgreSQL Adapter
- cloud persistence Adapter
- in-memory test Adapter

        Adapter names do not alter the public Port contract.

        ## Input and output rules

        - use public identifiers;
        - declare versions;
        - avoid vendor-specific types;
        - return structured results;
        - preserve traceability;
        - report unsupported behaviour.

        ## Errors

        - ProjectNotFound
- RevisionConflict
- PersistenceUnavailable
- PersistenceWriteFailed
- PersistenceReadFailed

        ## Security

        Adapters must use the minimum permissions required.

        Sensitive spatial data must not be transmitted or persisted unless
        explicitly authorised by the Application.

        ## Versioning

        Port versions follow public contract compatibility rules.

        ## Conformance

        An Adapter conforms only when it passes the applicable Port compliance
        suite and accurately declares its supported Capabilities.


---

## File originale: `contracts/services/README.md`

# Services

Public Service contracts.


---

## File originale: `contracts/services/export-service.md`

# Export Service Contract

        Contract ID: SVC-EXP-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines creation of abstract export representations and delegation to format-specific Export Adapters.

        ## Public operations

        - PrepareExport
- ValidateExportReadiness
- ListExportFormats
- ExecuteExport
- ReportInformationLoss

        ## Inputs

        - project identifier
- export scope
- target format
- target version
- unit policy
- layer mapping
- Adapter identifier

        Every request must declare its contract version and project context.

        Spatial requests must explicitly declare units, coordinate reference
        and tolerances where applicable.

        ## Outputs

        - abstract export model
- generated artifact reference
- format metadata
- warnings
- information-loss report

        Outputs must use public contract types and must not expose proprietary
        Kernel or Adapter objects.

        ## Errors

        - ExportFormatNotSupported
- ExportAdapterUnavailable
- ExportValidationFailed
- InformationLossNotAccepted
- ExportGenerationFailed

        Errors must contain:

        - machine-readable code;
        - human-readable message;
        - affected subject;
        - operation identifier;
        - recoverability;
        - suggested action where available.

        ## Events

        - ExportPrepared
- ExportCompleted
- ExportFailed

        Events describe completed facts. Requests and commands are not Events.

        ## Capabilities

        - Export2D
- Export3D
- ExportSemanticModel
- ExportDimensions
- ExportLayers
- ExportMetadata

        Consumers should query declared Capabilities before invoking optional
        operations.

        ## Versioning

        Compatible additions may introduce optional fields or new operations.

        Breaking changes require a new major contract version and migration
        guidance.

        ## Conformance

        An implementation conforms to this Service contract only when:

        - required operations are implemented;
        - declared Capabilities are accurate;
        - public errors follow the contract;
        - applicable compliance tests pass;
        - unsupported behaviour is reported explicitly.


---

## File originale: `contracts/services/geometry-service.md`

# Geometry Service Contract

        Contract ID: SVC-GEO-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines public operations for creating, transforming and querying spatial geometry.

        ## Public operations

        - CreateGeometry
- UpdateGeometry
- SplitWall
- MergeWalls
- CreateOpening
- GenerateRoomBoundary
- CalculateMeasurements
- TransformCoordinates

        ## Inputs

        - project identifier
- subject identifier
- geometry request
- units
- coordinate reference
- tolerance policy

        Every request must declare its contract version and project context.

        Spatial requests must explicitly declare units, coordinate reference
        and tolerances where applicable.

        ## Outputs

        - geometry result
- topology references
- measurements
- diagnostics
- generated Events

        Outputs must use public contract types and must not expose proprietary
        Kernel or Adapter objects.

        ## Errors

        - InvalidCoordinate
- InvalidGeometry
- DegenerateSegment
- NonClosedBoundary
- SelfIntersection
- ToleranceExceeded
- CapabilityNotSupported

        Errors must contain:

        - machine-readable code;
        - human-readable message;
        - affected subject;
        - operation identifier;
        - recoverability;
        - suggested action where available.

        ## Events

        - GeometryCreated
- GeometryUpdated
- WallSplit
- WallsMerged
- RoomBoundaryGenerated

        Events describe completed facts. Requests and commands are not Events.

        ## Capabilities

        - CreateWall
- SplitWall
- MergeWalls
- OffsetWall
- CreateOpening
- GenerateRoomBoundary
- CalculateArea
- TransformCoordinates

        Consumers should query declared Capabilities before invoking optional
        operations.

        ## Versioning

        Compatible additions may introduce optional fields or new operations.

        Breaking changes require a new major contract version and migration
        guidance.

        ## Conformance

        An implementation conforms to this Service contract only when:

        - required operations are implemented;
        - declared Capabilities are accurate;
        - public errors follow the contract;
        - applicable compliance tests pass;
        - unsupported behaviour is reported explicitly.


---

## File originale: `contracts/services/knowledge-service.md`

# Knowledge Service Contract

        Contract ID: SVC-KNW-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines access to versioned, traceable domain knowledge and rule packages.

        ## Public operations

        - ResolveRule
- ListApplicableRules
- ResolveDefault
- ResolveClassification
- ExplainRule
- CompareKnowledgeVersions

        ## Inputs

        - project context
- domain classification
- jurisdiction or scope
- effective date
- knowledge package version
- rule query

        Every request must declare its contract version and project context.

        Spatial requests must explicitly declare units, coordinate reference
        and tolerances where applicable.

        ## Outputs

        - resolved rules
- source references
- assumptions
- conflicts
- applicability explanation

        Outputs must use public contract types and must not expose proprietary
        Kernel or Adapter objects.

        ## Errors

        - KnowledgePackageNotFound
- RuleNotFound
- RuleConflict
- UnsupportedJurisdiction
- KnowledgeVersionMismatch

        Errors must contain:

        - machine-readable code;
        - human-readable message;
        - affected subject;
        - operation identifier;
        - recoverability;
        - suggested action where available.

        ## Events

        - KnowledgePackageLoaded
- RuleResolved
- RuleConflictDetected

        Events describe completed facts. Requests and commands are not Events.

        ## Capabilities

        - ResolveRule
- ListApplicableRules
- ResolveDefault
- ResolveClassification
- ExplainRule
- CompareKnowledgeVersions

        Consumers should query declared Capabilities before invoking optional
        operations.

        ## Versioning

        Compatible additions may introduce optional fields or new operations.

        Breaking changes require a new major contract version and migration
        guidance.

        ## Conformance

        An implementation conforms to this Service contract only when:

        - required operations are implemented;
        - declared Capabilities are accurate;
        - public errors follow the contract;
        - applicable compliance tests pass;
        - unsupported behaviour is reported explicitly.


---

## File originale: `contracts/services/validation-service.md`

# Validation Service Contract

        Contract ID: SVC-VAL-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines structured validation of spatial models, geometry, topology, dimensions and domain rules.

        ## Public operations

        - ValidateProject
- ValidateEntity
- ValidateTopology
- ValidateDimensions
- ValidateRoomClosure
- ValidateOpeningPlacement
- ValidateExportReadiness

        ## Inputs

        - project or entity identifier
- validation profile
- knowledge package references
- severity threshold
- tolerance policy

        Every request must declare its contract version and project context.

        Spatial requests must explicitly declare units, coordinate reference
        and tolerances where applicable.

        ## Outputs

        - validation report
- rule results
- severity summary
- evidence
- suggested corrections

        Outputs must use public contract types and must not expose proprietary
        Kernel or Adapter objects.

        ## Errors

        - ValidationProfileNotFound
- KnowledgePackageUnavailable
- InvalidValidationRequest
- ValidationExecutionFailed
- CapabilityNotSupported

        Errors must contain:

        - machine-readable code;
        - human-readable message;
        - affected subject;
        - operation identifier;
        - recoverability;
        - suggested action where available.

        ## Events

        - ValidationStarted
- ValidationCompleted
- ValidationFailed

        Events describe completed facts. Requests and commands are not Events.

        ## Capabilities

        - ValidateTopology
- ValidateDimensions
- ValidateRoomClosure
- ValidateOpeningPlacement
- ValidateDomainRules
- ValidateExportReadiness

        Consumers should query declared Capabilities before invoking optional
        operations.

        ## Versioning

        Compatible additions may introduce optional fields or new operations.

        Breaking changes require a new major contract version and migration
        guidance.

        ## Conformance

        An implementation conforms to this Service contract only when:

        - required operations are implemented;
        - declared Capabilities are accurate;
        - public errors follow the contract;
        - applicable compliance tests pass;
        - unsupported behaviour is reported explicitly.


---

## File originale: `decisions/0001-repository-layout.md`

# Decision 0001 — Repository Layout

Status: Active temporary decision

Release: 0.1

Date: 2026-07-20

## Decision

Pianta-Arredo-Core initially contains specification, architecture,
contracts, implementations and application-oriented material in one
repository.

The repository is organised so that the stable specification can
later be extracted into:

`Spatial-Intelligence-Specification`

## Reason

A single repository reduces complexity during the foundation stage
while preserving a future separation path.

## Review trigger

Review during Release 0.5 or earlier when independent implementations
require a separately versioned specification.


---

## File originale: `decisions/0002-platform-naming.md`

# Decision 0002 — Platform Naming

Status: Active temporary decision

Release: 0.1

Date: 2026-07-20

## Decision

The current repository remains named:

`Pianta-Arredo-Core`

`Spatial Intelligence Platform` is the architectural platform name.

Pianta-Arredo is the first planned application.

## Review trigger

Reconsider repository naming during Release 0.5.


---

## File originale: `diagrams/README.md`

# Diagrams

Diagram source files.

