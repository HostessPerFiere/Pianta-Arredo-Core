# System Glossary

## Purpose

This glossary defines the official terminology of the Spatial Intelligence Engine (SIE).

It represents the authoritative vocabulary for the entire platform.

Every architectural document, source file, API, workflow and software component must use these definitions consistently.

If a concept is defined here, its meaning must remain identical throughout the entire project.

If a concept is not present in this glossary, it does not officially exist within the platform.

Every new architectural concept must be introduced here before being used in documentation, source code or APIs.

---

# Spatial Intelligence Concepts

## Spatial Intelligence Engine (SIE)

The computational platform responsible for modeling, validating, analyzing and transforming spatial information.

The SIE contains all computational engines but no business-specific knowledge.

Applications and Domain Packages are built on top of the SIE.

---

## Spatial Intelligence Model (SIM)

The conceptual representation of physical spaces.

The SIM defines the objects manipulated by the Spatial Intelligence Engine.

Examples include:

- Project
- Building
- Floor
- Space
- Wall
- Opening
- Furniture

The SIM is independent from programming languages, CAD software and geometric libraries.

The SIE processes the SIM.

---

# Core Concepts

## Project

The highest-level container representing an entire spatial project.

A Project may contain one or more Buildings.

---

## Building

A physical construction composed of one or more Floors.

---

## Floor

A horizontal level within a Building.

A Floor contains one or more Spaces.

---

## Space

A bounded physical area.

Space is the fundamental domain object of the platform.

Examples:

- Room
- Office
- Corridor
- Exhibition Stand
- Retail Area
- Warehouse Zone
- Laboratory
- Hotel Suite

Every specialized environment is a Space.

---

## Room

A residential specialization of Space.

Every Room is a Space.

Not every Space is a Room.

---

# Architectural Elements

## Wall

A physical element delimiting one or more Spaces.

Walls may contain Openings.

---

## Opening

A generic interruption of a Wall.

Examples:

- Door
- Window
- Archway

---

## Door

A passable Opening connecting two Spaces or a Space with the exterior.

---

## Window

A non-passable Opening intended for natural light, ventilation or visibility.

---

## Corner

The intersection between two or more Walls.

Corners define the topology of a Space.

---

## Furniture

A movable object positioned inside a Space.

Furniture never modifies the topology of the building.

---

# Geometry Concepts

## Point

A position in space.

---

## Vector

A direction with magnitude.

---

## Edge

A geometric connection between two vertices.

---

## Face

A bounded geometric surface.

---

## Polygon

A closed planar shape composed of edges.

---

## Solid

A closed three-dimensional volume.

---

## Bounding Box

The minimum volume enclosing a geometric object.

Used for spatial indexing and collision detection.

---

# Platform Concepts

## Domain Model

The representation of real-world entities.

Contains architectural semantics.

Examples:

- Wall
- Room
- Building
- Furniture

The Domain Model contains no geometric algorithms.

---

## Geometry Model

The mathematical representation of spatial objects.

Contains only geometry.

Examples:

- Point
- Vector
- Polygon
- Solid

The Geometry Model contains no architectural meaning.

---

## Export Model

The representation used for generating external formats.

Examples:

- DXF
- SVG
- IFC
- STEP
- glTF
- Sweet Home 3D

Export Models never modify the Geometry Model.

---

# Workflow Concepts

## Workflow

A coordinated sequence of operations executed by the Workflow Engine.

Examples:

Input

↓

Validation

↓

Geometry

↓

Furniture

↓

Export

---

## Workflow Engine

The orchestration engine responsible for coordinating platform operations.

It decides:

- execution order
- dependencies
- engine invocation
- state transitions

The Workflow Engine performs no geometry calculations.

---

# Computational Engines

## Engine

An independent computational module responsible for one well-defined task.

Every Engine must satisfy the following principles:

- single responsibility
- independent testing
- replaceability
- well-defined interfaces

Examples:

- Geometry Engine
- Validation Engine
- Knowledge Engine
- Export Engine

---

## Geometry Kernel

The computational heart of the platform.

Responsible only for geometry and topology.

It knows nothing about:

- residential design
- furniture brands
- GPT
- user interfaces
- CAD software

---

## Validation Engine

Verifies the consistency and correctness of the Geometry Model.

It never modifies geometry.

It only reports validation results.

---

## Knowledge Engine

Contains business knowledge rather than computational geometry.

Examples:

- building standards
- accessibility rules
- residential constraints
- exhibition regulations
- office planning rules

The Knowledge Engine is replaceable and domain-independent.

---

## AI Orchestrator

Coordinates interactions with artificial intelligence systems.

May communicate with:

- GPT
- local language models
- OCR
- Computer Vision
- future AI services

The AI Orchestrator never contains business rules.

---

## Export Engine

Transforms validated geometry into external representations.

Examples:

- DXF
- IFC
- SVG
- STEP
- Sweet Home 3D
- glTF

---

# Extension Concepts

## Package

A domain-specific extension of the platform.

Packages extend the platform without modifying the Core.

Examples:

- Residential Package
- Office Package
- Retail Package
- Exhibition Package
- Hospitality Package
- Healthcare Package
- Industrial Package

Packages may depend on the SIE.

The SIE never depends on Packages.

---

## Application

A user-facing software built on top of the Spatial Intelligence Engine.

Examples:

- Pianta-Arredo
- Web Platform
- Desktop Application
- Mobile App
- REST API

Applications consume services provided by the SIE.

---

# Guiding Principles

The glossary is the authoritative source for project terminology.

Every architectural document must conform to these definitions.

Every source file should use this vocabulary consistently.

Every API should expose these concepts without ambiguity.

Every new concept must first be introduced into this glossary before becoming part of the platform.

Consistency of language is considered an architectural requirement, not a documentation task.
