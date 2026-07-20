# Capabilities

Document ID: DOC-012

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Capabilities declare what a Service, Kernel, Adapter or Plugin can do.

## Why Capabilities are required

Different implementations may support different operations.

Consumers must not infer support from product names or implementation
types.

## Capability descriptor

A Capability should declare:

- identifier;
- version;
- status;
- supported inputs;
- supported outputs;
- limits;
- required dependencies;
- known restrictions.

## Example Geometry Capabilities

- CreateWall
- SplitWall
- MergeWalls
- OffsetWall
- GenerateRoomBoundary
- CalculateArea

## Example Validation Capabilities

- ValidateTopology
- ValidateDimensions
- ValidateRoomClosure
- ValidateOpeningPlacement

## Example Knowledge Capabilities

- ResidentialRules
- OfficeRules
- AccessibilityRules
- ExplainRule

## Example Export Capabilities

- ExportDXF
- ExportSVG
- ExportIFC
- ExportGLTF
- ExportSweetHome3D

## Capability negotiation

Applications may query available Capabilities before invoking an
operation.

## Partial support

Partial support must be declared explicitly.

## Capability stability

Stable public Capabilities require versioning and compatibility rules.
