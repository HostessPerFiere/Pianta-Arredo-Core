# Vision

## Pianta-Arredo Core

Pianta-Arredo Core is an open source Geometry and Interior Intelligence Platform.

Its purpose is to transform measurements, floor plans and spatial data into validated geometric models that can be used for CAD, BIM, interior design, automation and AI-assisted workflows.

The project is designed as an independent modular engine.

ChatGPT, web applications, desktop applications and external software integrations are considered interfaces or clients of the core platform.

## Mission

Pianta-Arredo Core aims to:

- acquire spatial data from manual measurements, floor plans, images and structured files;
- build a reliable and machine-readable geometric model;
- validate walls, openings, rooms, dimensions and spatial relationships;
- identify geometric inconsistencies before generating drawings or models;
- produce CAD-friendly and interoperable outputs;
- support interior layout studies and furniture placement;
- integrate with open source CAD, BIM, rendering and design tools;
- provide a reusable foundation for AI-assisted spatial design.

## Core principles

### 1. Geometry first

No downstream output should be considered reliable until the underlying geometry has been validated.

### 2. Engine first

The core engine must remain independent from ChatGPT, web interfaces, desktop applications or any single user interface.

### 3. Modular architecture

Each module must have a clearly defined responsibility and communicate through documented interfaces.

### 4. Open standards

The project should prefer open and interoperable formats whenever technically possible.

Initial target formats include:

- JSON
- YAML
- SVG
- DXF

Future formats may include:

- IFC
- glTF
- STEP

### 5. Replaceable components

Geometry, validation, export and integration backends should be replaceable without redesigning the entire platform.

### 6. Verifiable outputs

The project must distinguish between:

- provisional geometry;
- validated geometry;
- conceptual drawings;
- editable CAD models;
- executable or construction-ready documents.

Pianta-Arredo Core does not replace the work of licensed architects, engineers, surveyors or other qualified professionals.

## Initial scope

The first development objective is:

> From measured walls to a validated 2D floor plan.

The first stable workflow will:

1. receive wall and opening measurements;
2. normalize the input data;
3. build a geometric model;
4. verify closure and consistency;
5. report errors and tolerances;
6. generate a structured representation;
7. export a basic 2D floor plan.

## Long-term direction

Pianta-Arredo Core may evolve into a shared spatial intelligence platform supporting:

- CAD generation;
- BIM interoperability;
- floor plan recognition;
- computer vision;
- interior layout optimization;
- furniture catalog integration;
- Sweet Home 3D workflows;
- FreeCAD and OpenCascade integrations;
- API access;
- web and desktop applications.
