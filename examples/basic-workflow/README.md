# Basic Spatial Workflow Example

Version: 0.1

Status: Conceptual example

## Scenario

Create one rectangular Room with one Door and export a simple
two-dimensional representation.

## Workflow

1. Create Project.
2. Create Building.
3. Create Floor.
4. Create Space.
5. Create Room.
6. Create four Walls.
7. Add one Door Opening.
8. Normalize units and coordinates.
9. Generate geometry.
10. Validate closure and dimensions.
11. Prepare export.
12. Invoke SVG Export Adapter.

## Example project state

Draft

↓

Measured

↓

Normalized

↓

Validated

↓

Geometry Generated

↓

Exported

## Example measurements

- Room width: 4000 mm
- Room depth: 3000 mm
- Wall thickness: 120 mm
- Door width: 900 mm
- Door offset from wall start: 500 mm

## Expected validation

- four connected Walls;
- one closed Room boundary;
- positive area;
- Door hosted by one Wall;
- no self-intersections.

## Expected result

The workflow produces:

- one SIM Project;
- one geometry result;
- one validation report;
- one abstract export model;
- one SVG artifact.

This example is conceptual until the reference implementation exists.
