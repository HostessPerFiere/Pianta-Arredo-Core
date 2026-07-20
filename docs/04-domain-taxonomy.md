# Domain Taxonomy

## Purpose

This document defines the hierarchical organization of the Spatial Intelligence Model (SIM).

While the System Glossary defines the meaning of concepts, the Domain Taxonomy defines the relationships between them.

The taxonomy is the canonical structural model of the platform.

---

# Taxonomy Principles

The taxonomy follows four principles:

- Generalization
- Specialization
- Composition
- Independence

Every new concept introduced into the Spatial Intelligence Model must have a defined position within this taxonomy.

---

# Spatial Intelligence Model

Project
└── Building
    ├── Floor
    │   ├── Space
    │   │   ├── Room
    │   │   ├── Office
    │   │   ├── Corridor
    │   │   ├── Retail Area
    │   │   ├── Exhibition Stand
    │   │   ├── Hotel Room
    │   │   ├── Warehouse Zone
    │   │   ├── Laboratory
    │   │   └── Generic Space
    │   │
    │   ├── Wall
    │   ├── Opening
    │   │   ├── Door
    │   │   ├── Window
    │   │   └── Archway
    │   │
    │   ├── Furniture
    │   ├── Material
    │   ├── Annotation
    │   └── Equipment
    │
    └── Site

---

# Domain Hierarchy

## Project

Contains one or more Buildings.

---

## Building

Contains one or more Floors.

---

## Floor

Contains one or more Spaces and architectural elements.

---

## Space

The primary spatial abstraction.

Every specialized environment derives from Space.

Examples:

- Room
- Office
- Retail Area
- Exhibition Stand
- Warehouse Zone

---

# Architectural Elements

Architectural Elements belong to Spaces.

They include:

- Walls
- Openings
- Furniture
- Materials
- Equipment

---

# Geometry Relationship

The Domain Taxonomy is independent from geometry.

A Wall is not a line.

A Room is not a polygon.

A Building is not a mesh.

Geometry is an implementation used to represent domain objects.

---

# Domain Packages

Additional industries extend the taxonomy through specialization.

Examples:

Residential Package

Space
└── Room
    ├── Bedroom
    ├── Kitchen
    ├── Bathroom
    ├── Living Room
    └── Laundry

---

Office Package

Space
└── Office
    ├── Meeting Room
    ├── Open Space
    ├── Reception
    └── Server Room

---

Retail Package

Space
└── Retail Area
    ├── Sales Area
    ├── Storage
    ├── Checkout
    └── Display Area

---

Exhibition Package

Space
└── Exhibition Stand
    ├── Demo Area
    ├── Meeting Area
    ├── Storage
    └── Hospitality Area

---

Healthcare Package

Space
└── Healthcare Space
    ├── Waiting Room
    ├── Examination Room
    ├── Operating Room
    └── Recovery Room

---

# Design Rules

The Core defines only generic concepts.

Domain Packages introduce specialized concepts.

The Core must never contain industry-specific terminology.

---

# Architectural Principle

Inheritance flows downward.

Dependencies flow downward.

Knowledge flows upward through abstraction.

The Spatial Intelligence Model must remain stable while Domain Packages evolve independently.
