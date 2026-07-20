# Pianta-Arredo-Core — 01-overview-and-governance.md

Documento consolidato per il GPT.

---

## File originale: `CODE_OF_CONDUCT.md`

# Code of Conduct

The project is committed to respectful, constructive and inclusive
collaboration.

Participants should:

- communicate professionally;
- discuss ideas instead of attacking people;
- welcome different experience levels;
- provide actionable feedback;
- respect privacy, copyright and confidentiality.

Harassment, discrimination, threats, publication of private information
and abusive communication are not accepted.

Architectural disagreements should be resolved through evidence,
tests, prototypes, RFCs and documented trade-offs.


---

## File originale: `CONTRIBUTING.md`

# Contributing

Thank you for contributing to Pianta-Arredo-Core.

Before contributing, read:

1. `PROJECT_PRINCIPLES.md`
2. `README.md`
3. relevant documentation
4. applicable ADRs and RFCs

## Decision path

- minor correction: pull request
- temporary decision: `decisions/`
- significant proposal: `rfc/`
- approved architectural decision: `architecture/`
- stable normative behaviour: `specification/`

## Pull requests

Pull requests should:

- address one focused concern;
- explain motivation and trade-offs;
- identify affected contracts;
- include tests where appropriate;
- update documentation;
- avoid unrelated changes.

## Suggested commit prefixes

- `docs:`
- `spec:`
- `arch:`
- `feat:`
- `fix:`
- `test:`
- `build:`
- `chore:`

Do not commit private floor plans, confidential data,
proprietary standards or unlicensed assets.


---

## File originale: `GOVERNANCE.md`

# Governance

Pianta-Arredo-Core currently follows a maintainer-led model.

Maintainers are responsible for:

- architectural coherence
- contribution review
- release management
- security reports
- ADR approval
- RFC promotion
- specification maintenance

## Decision hierarchy

1. Project Principles
2. Stable Specifications
3. Approved ADRs
4. Accepted RFCs
5. Temporary Decisions
6. Implementation-specific choices

Governance may evolve as the contributor community grows.


---

## File originale: `LICENSE`

MIT License

Copyright (c) 2026 Pianta-Arredo-Core contributors

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files, to deal
in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons
to whom the Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---

## File originale: `README.md`

# Pianta-Arredo-Core

Open Source Geometry & Spatial Intelligence Platform.

Pianta-Arredo-Core is the initial repository for an open-source
Spatial Intelligence Platform designed to represent, validate,
analyse and export spatial information.

Pianta-Arredo is the first planned application built on this foundation.

## Current release

- Release: 0.1 — Foundation
- Package: A — Repository Foundation
- Status: Early development

## Architectural model

The platform is organised around:

- Spatial Intelligence Specification (SIS)
- Spatial Intelligence Model (SIM)
- Services
- replaceable Kernels
- Ports
- Adapters
- Capabilities
- Events
- Plugins
- Compliance tests

## Core principles

Geometry First.

Domain Before UI.

Specification Before Implementation.

AI as an assistant, never as the source of truth.

## Repository areas

- `docs/`: project documentation
- `architecture/`: approved ADRs
- `specification/`: stable specifications
- `contracts/`: Services, Events, Ports and Capabilities
- `implementation/`: reference implementations
- `knowledge/`: versioned domain knowledge
- `compliance/`: conformance tests
- `rfc/`: proposals under discussion
- `design/`: experimental design documents
- `decisions/`: temporary decisions
- `playground/`: prototypes and experiments

## License

MIT License. See `LICENSE`.

## Project status

**Current release:** 0.1 — Foundation  
**Release status:** Completed  
**Stable production version:** Not yet available

Release 0.1 establishes repository structure, architecture decisions,
draft Service contracts, developer documentation, schemas and initial
architecture rules.

See `RELEASE-0.1-NOTES.md` for the complete release summary.

<!-- RELEASE-0.2-STATUS:START -->
## Current specification status

**Latest completed release:** 0.2 — Core Specification  
**Specification maturity:** Draft  
**Production readiness:** Not yet production-ready

Release 0.2 defines the first formal SIS and SIM foundation.

See `RELEASE-0.2-NOTES.md`.
<!-- RELEASE-0.2-STATUS:END -->

<!-- RELEASE-0.3-STATUS:START -->
## Reference implementation status

**Latest completed release:** 0.3 — Reference Architecture  
**Implementation maturity:** Experimental  
**Production readiness:** Not production-ready

Release 0.3 introduces the first executable Python architecture skeleton.

See `RELEASE-0.3-NOTES.md`.
<!-- RELEASE-0.3-STATUS:END -->

<!-- RELEASE-0.4-STATUS:START -->
## Geometry and validation status

**Latest completed release:** 0.4 — Geometry and Validation Core  
**Geometry maturity:** Experimental  
**Production readiness:** Not production-ready

Release 0.4 introduces executable 2D geometry primitives,
deterministic validation rules and a Capability registry.

See `RELEASE-0.4-NOTES.md`.
<!-- RELEASE-0.4-STATUS:END -->

<!-- RELEASE-0.5-STATUS:START -->
## Project persistence status

**Latest completed release:** 0.5 — Project Model and Persistence  
**Persistence maturity:** Experimental  
**Production readiness:** Not production-ready

Release 0.5 introduces revision-aware in-memory and JSON
persistence.

See `RELEASE-0.5-NOTES.md`.
<!-- RELEASE-0.5-STATUS:END -->

<!-- RELEASE-0-6-0-STATUS:START -->
## Release 0.6.0 status

**Release:** Interoperability Core  
**Status:** Completed  
**Package version:** `0.6.0`

See `RELEASE-0.6-NOTES.md`.
<!-- RELEASE-0-6-0-STATUS:END -->

<!-- RELEASE-0-7-0-STATUS:START -->
## Release 0.7.0 status

**Release:** Spatial Analysis Core  
**Status:** Completed  
**Package version:** `0.7.0`

See `RELEASE-0.7-NOTES.md`.
<!-- RELEASE-0-7-0-STATUS:END -->

<!-- RELEASE-0-8-0-STATUS:START -->
## Release 0.8.0 status

**Release:** Events and Plugins  
**Status:** Completed  
**Package version:** `0.8.0`

See `RELEASE-0.8-NOTES.md`.
<!-- RELEASE-0-8-0-STATUS:END -->

<!-- RELEASE-0-9-0-STATUS:START -->
## Release 0.9.0 status

**Release:** Production Hardening  
**Status:** Completed  
**Package version:** `0.9.0`

See `RELEASE-0.9-NOTES.md`.
<!-- RELEASE-0-9-0-STATUS:END -->

<!-- RELEASE-1-0-0-STATUS:START -->
## Release 1.0.0 status

**Release:** Stable Foundation  
**Status:** Completed  
**Package version:** `1.0.0`

See `RELEASE-1.0-NOTES.md`.
<!-- RELEASE-1-0-0-STATUS:END -->


---

## File originale: `ROADMAP.md`

# Roadmap

## Release 0.1 — Foundation

Establish:

- repository structure
- governance
- project principles
- documentation foundations
- architectural decision process
- GitHub templates
- initial automation

Packages:

- Package A — Repository Foundation
- Package B — Core Documentation
- Package C — Architecture Decisions
- Package D — Service Specification
- Package E — Developer Experience

## Release 0.2 — Core Specification

Define SIS, SIM, Services, Ports, Adapters, Events, Capabilities,
errors and versioning.

## Release 0.3 — Reference Architecture

Add architecture tests, dependency rules and executable skeletons.

## Release 0.4 — Reference Implementation

Implement the first vertical workflow:

measurement input → SIM → geometry → validation → export.

## Release 0.5 — Plugin SDK

Define plugin contracts and evaluate separating the specification
into the independent repository:

`Spatial-Intelligence-Specification`

## Release 0.6 — Assisted Intelligence

Explore AI, OCR and computer vision through replaceable adapters.

## Release 0.7 — Persistence and Synchronisation

Add state history, persistence, versioning and optional cloud adapters.

## Release 0.8 — Beta

Integrate the first complete Pianta-Arredo workflow.

## Release 0.9 — Stabilisation

Focus on compatibility, migration and compliance.

## Release 1.0 — Stable Platform

Publish stable Spatial Intelligence contracts and a reference implementation.

## Release 0.1 — Foundation

Status: Completed

Completed packages:

- Package A — Repository Foundation
- Package B — Core Documentation
- Package C — Architecture Decisions
- Package D — Service Specification
- Package E — Developer Experience

<!-- RELEASE-0.2-STATUS:START -->
## Release 0.2 — Core Specification

Status: Completed

Completed packages:

- Package A — Specification Foundation
- Package B — SIM Core Entities
- Package C — Commands, Results and Errors
- Package D — Compliance Foundation
- Package E — Examples and Release Closure
<!-- RELEASE-0.2-STATUS:END -->

<!-- RELEASE-0.3-STATUS:START -->
## Release 0.3 — Reference Architecture

Status: Completed

Added:

- executable Python package structure;
- public Service skeletons;
- Ports and reference Adapters;
- composition root;
- unit and end-to-end tests;
- executable architecture checks.
<!-- RELEASE-0.3-STATUS:END -->

<!-- RELEASE-0.4-STATUS:START -->
## Release 0.4 — Geometry and Validation Core

Status: Completed

Added:

- executable 2D geometry primitives;
- length and area algorithms;
- perimeter closure validation;
- segment-intersection validation;
- Wall and Opening validation;
- Capability registry;
- expanded automated tests.
<!-- RELEASE-0.4-STATUS:END -->

<!-- RELEASE-0.5-STATUS:START -->
## Release 0.5 — Project Model and Persistence

Status: Completed

Added:

- revision-aware Project records;
- Project Repository Port;
- in-memory persistence;
- JSON file persistence;
- save and load Service;
- revision conflict handling;
- persistence tests.
<!-- RELEASE-0.5-STATUS:END -->

<!-- RELEASE-0-6-0-ROADMAP:START -->
## Release 0.6.0 — Interoperability Core

Status: Completed
<!-- RELEASE-0-6-0-ROADMAP:END -->

<!-- RELEASE-0-7-0-ROADMAP:START -->
## Release 0.7.0 — Spatial Analysis Core

Status: Completed
<!-- RELEASE-0-7-0-ROADMAP:END -->

<!-- RELEASE-0-8-0-ROADMAP:START -->
## Release 0.8.0 — Events and Plugins

Status: Completed
<!-- RELEASE-0-8-0-ROADMAP:END -->

<!-- RELEASE-0-9-0-ROADMAP:START -->
## Release 0.9.0 — Production Hardening

Status: Completed
<!-- RELEASE-0-9-0-ROADMAP:END -->

<!-- RELEASE-1-0-0-ROADMAP:START -->
## Release 1.0.0 — Stable Foundation

Status: Completed
<!-- RELEASE-1-0-0-ROADMAP:END -->


---

## File originale: `SECURITY.md`

# Security Policy

The project is currently in an early development phase.

Do not publish exploitable security details in public issues.

Report vulnerabilities privately through the repository security
reporting tools when available.

Floor plans, access routes, infrastructure details, addresses and
occupancy data may be sensitive.

Repository samples must be synthetic, anonymised, publicly licensed
or explicitly authorised.

