# Getting Started

Version: 0.1

Status: Draft

## Purpose

This guide introduces contributors to Pianta-Arredo-Core and the
Spatial Intelligence Platform architecture.

## Prerequisites

Contributors should understand:

- Git and GitHub;
- Markdown;
- structured data formats such as JSON;
- basic software architecture concepts.

Implementation-specific prerequisites will be documented separately.

## Repository orientation

Start with:

1. `README.md`
2. `PROJECT_PRINCIPLES.md`
3. `docs/INDEX.md`
4. `architecture/INDEX.md`
5. `contracts/INDEX.md`

## Main repository areas

- `docs/`: conceptual and technical documentation;
- `architecture/`: accepted ADRs;
- `contracts/`: Services, Ports, Events and Capabilities;
- `specification/`: future stable SIS and SIM specifications;
- `implementation/`: reference implementations;
- `examples/`: small code and workflow examples;
- `samples/`: spatial datasets and publishable files;
- `tests/`: compliance, integration and architecture tests.

## Development sequence

Preferred contribution order:

1. identify the domain problem;
2. check the glossary and taxonomy;
3. review applicable ADRs;
4. define or update the contract;
5. add tests;
6. implement;
7. update documentation.

## First validation

Before opening a pull request:

- check repository status;
- review changed files;
- run available tests;
- confirm no sensitive spatial data is included;
- confirm no proprietary standards are reproduced.

## Current maturity

Release 0.1 defines foundations and draft contracts.

Public APIs and schemas may still change.
