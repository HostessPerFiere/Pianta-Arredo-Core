# SIM Overview

Specification ID: SIM-000

Version: 0.2-draft

Status: Draft

## Purpose

The Spatial Intelligence Model represents structured spatial
information independently from presentation and storage technology.

## Core hierarchy

Project

↓

Building

↓

Floor

↓

Space

↓

Room

## Related entities

A Project MAY also contain:

- Walls;
- Openings;
- Furniture;
- geometry references;
- validation results;
- analysis results;
- exports;
- revisions;
- metadata.

## Entity requirements

Every SIM entity MUST have:

- stable identifier;
- entity type;
- lifecycle state;
- creation metadata;
- version or revision context.

Spatial entities SHOULD also declare:

- coordinate reference;
- units;
- geometry reference;
- parent relationship.

## Separation of concerns

SIM represents domain meaning.

It MUST NOT depend on:

- rendering widgets;
- database row types;
- CAD-library classes;
- proprietary geometry objects;
- application screens.

## Geometry

SIM MAY store geometry directly or reference a geometry representation.

Geometry precision and tolerance MUST be explicit.

## Extensibility

Extensions MAY add metadata and specialised entities.

Extensions MUST preserve Core identifiers and relationship semantics.

## Serialisation

SIM MAY be serialised as JSON, YAML, database records or other formats.

Serialisation MUST preserve normative meaning.
