# Export Service

Document ID: DOC-009

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

The Export Service converts platform data into an abstract export
representation and delegates file-specific generation to Export
Adapters.

## Architecture

Spatial Intelligence Model

↓

Export Service

↓

Abstract Export Model

↓

Export Adapter

↓

External format

## Example Export Adapters

- DXF Adapter
- SVG Adapter
- IFC Adapter
- STEP Adapter
- glTF Adapter
- Sweet Home 3D Adapter
- JSON Adapter

## Responsibilities

The Export Service is responsible for:

- selecting export scope;
- preparing export entities;
- mapping semantic layers;
- validating export readiness;
- preserving identifiers;
- reporting unsupported features.

## Adapter responsibilities

An Export Adapter is responsible for:

- file syntax;
- format versions;
- encoding;
- format-specific units;
- layer mapping;
- external compatibility;
- file generation.

## Layer recommendations

Common export layers include:

- walls;
- openings;
- rooms;
- furniture;
- dimensions;
- text;
- references;
- analysis results.

## Loss reporting

If a target format cannot represent part of the model, the Adapter must
report the loss explicitly.

## Capabilities

Example Capabilities:

- Export2D
- Export3D
- ExportSemanticModel
- ExportDimensions
- ExportLayers
- ExportMetadata

## Verification

A generated file must not be described as compatible or ready for use
unless the relevant Adapter and output have been tested.
