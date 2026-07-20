# Data Model

## Philosophy

Pianta-Arredo Core separates real-world concepts, geometric representation and export formats into independent models.

This separation allows the platform to evolve without coupling business logic to CAD engines or file formats.

---

# The Three Models

The platform defines three independent models:

1. Domain Model
2. Geometry Model
3. Export Model

---

# Domain Model

The Domain Model represents architectural concepts.

Examples:

- Project
- Building
- Floor
- Space
- Wall
- Opening
- Door
- Window
- Furniture
- Material

The Domain Model contains no geometric algorithms.

---

# Geometry Model

The Geometry Model represents mathematical entities.

Examples:

- Point
- Vector
- Line
- Arc
- Segment
- Polyline
- Polygon
- Plane
- Solid
- Bounding Box

The Geometry Model contains no architectural semantics.

---

# Export Model

The Export Model converts validated geometry into external formats.

Examples:

- DXF
- SVG
- IFC
- STEP
- glTF
- Sweet Home 3D

Each exporter is independent.

---

# Transformation Pipeline

Domain Model

↓

Geometry Model

↓

Validation

↓

Export Model

---

# Design Rules

Domain objects never depend on exporters.

Geometry objects never depend on UI.

Exporters never modify geometry.

Validation always operates on Geometry Model.

---

# Future Extensions

Additional domain entities may include:

- Electrical systems
- Plumbing
- HVAC
- Structural elements
- Lighting
- Accessibility
- Cost estimation

without changing the Geometry Model.
