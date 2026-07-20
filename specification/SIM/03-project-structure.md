# SIM Project Structure

Specification ID: SIM-003

Version: 0.2-draft

Status: Draft

## Purpose

This document defines the normative containment structure of a SIM
Project.

## Project

A Project is the root aggregate.

A Project MUST contain:

- project identifier;
- name;
- lifecycle state;
- unit system;
- coordinate reference;
- revision context.

A Project MAY contain one or more Buildings.

## Building

A Building represents a physical or conceptual building container.

A Building MUST belong to one Project.

A Building MAY contain one or more Floors.

## Floor

A Floor represents a vertical level or storey.

A Floor MUST belong to one Building.

A Floor SHOULD declare:

- elevation;
- height;
- local coordinate reference;
- order or level designation.

## Space

A Space is a generic bounded or conceptual spatial region.

A Space MUST belong to one Floor unless an extension explicitly
defines a multi-floor Space.

## Room

A Room is a Space specialisation intended to represent an enclosed or
functionally defined area.

A Room MAY reference:

- boundary;
- Walls;
- Openings;
- use classification;
- area;
- volume;
- adjacency relationships.

## Wall

A Wall is a spatial boundary element.

A Wall SHOULD declare:

- start and end geometry;
- thickness;
- height;
- host Floor;
- connected Walls;
- hosted Openings.

## Opening

An Opening represents a Door, Window or another interruption in a host
element.

An Opening MUST reference its host when the host is known.

## Furniture

Furniture represents movable or placed spatial objects.

Furniture MUST NOT be treated as a structural element unless explicitly
specialised.

## Parent relationships

Every contained entity MUST reference its parent or be discoverable
through an equivalent normative relationship.

## Cross-references

Cross-references MUST use stable identifiers.

Circular containment is forbidden.
