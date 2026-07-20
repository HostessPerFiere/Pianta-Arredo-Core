# Pianta-Arredo-Core — 02-specification-and-schemas.md

Documento consolidato per il GPT.

---

## File originale: `compliance/INDEX.md`

# Compliance Index

Version: 0.2-draft

Status: Draft

## Profiles

- Core Model Profile
- Geometry Profile
- Validation Profile
- Export Profile

## Compliance areas

- schema validation;
- identifier stability;
- unit declaration;
- coordinate-reference declaration;
- Service contract behaviour;
- Capability accuracy;
- Event compatibility;
- Adapter conformance.

## Current maturity

Release 0.2 defines compliance requirements and test cases.

Automated execution is planned for Release 0.3.


---

## File originale: `compliance/README.md`

# Compliance

Specification and implementation conformance suites.


---

## File originale: `compliance/core-model-profile.md`

# Core Model Compliance Profile

Version: 0.2-draft

Status: Draft

## Required support

A conforming implementation MUST support:

- Project;
- Building;
- Floor;
- Space;
- Room;
- Wall;
- Opening;
- stable identifiers;
- explicit units;
- coordinate references;
- entity lifecycle;
- structured results and errors.

## Required evidence

- schema-validation results;
- test-suite version;
- implementation version;
- known deviations;
- declared optional Capabilities.


---

## File originale: `compliance/test-cases/core-model-cases.md`

# Core Model Compliance Cases

Version: 0.2-draft

Status: Draft

## Cases

### CM-001 — Valid Project

A Project with valid identifier, unit system and coordinate reference
MUST be accepted.

### CM-002 — Missing identifier

An entity without a required identifier MUST be rejected.

### CM-003 — Unknown unit

An unsupported unit without an extension declaration MUST be rejected.

### CM-004 — Circular containment

Circular Project containment MUST be rejected.

### CM-005 — Invalid Wall thickness

Zero or negative Wall thickness MUST be rejected.

### CM-006 — Invalid Opening host

An Opening referencing an unavailable host MUST produce a validation
error.

### CM-007 — Revision conflict

A Command with an obsolete expected revision MUST return
`RevisionConflict`.


---

## File originale: `compliance/test-cases/versioning-cases.md`

# Versioning Compliance Cases

Version: 0.2-draft

Status: Draft

## Cases

### VER-001 — Unknown optional property

Compatible consumers SHOULD ignore unknown optional properties.

### VER-002 — Missing required property

Missing required properties MUST fail validation.

### VER-003 — Breaking type change

Changing a stable property's type requires a new major version.

### VER-004 — Capability accuracy

An implementation MUST NOT declare a Capability that fails its
required tests.


---

## File originale: `schemas/README.md`

# Schemas

Machine-readable validation schemas.


---

## File originale: `schemas/building.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/building.schema.json",
  "title": "SIM Building",
  "type": "object",
  "required": [
    "buildingId",
    "projectId",
    "name",
    "state"
  ],
  "properties": {
    "buildingId": {
      "$ref": "identifier.schema.json"
    },
    "projectId": {
      "$ref": "identifier.schema.json"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "state": {
      "type": "string",
      "enum": [
        "Draft",
        "Active",
        "Superseded",
        "Deleted"
      ]
    },
    "address": {
      "type": [
        "object",
        "null"
      ]
    },
    "metadata": {
      "type": "object"
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/capability.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/capability.schema.json",
  "title": "Spatial Intelligence Capability",
  "type": "object",
  "required": [
    "capabilityId",
    "version",
    "status",
    "supportedInputs",
    "supportedOutputs"
  ],
  "properties": {
    "capabilityId": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "status": {
      "type": "string",
      "enum": [
        "Draft",
        "Experimental",
        "Stable",
        "Deprecated"
      ]
    },
    "supportedInputs": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "supportedOutputs": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "limits": {
      "type": "object"
    },
    "dependencies": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "restrictions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/command.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/command.schema.json",
  "title": "Spatial Intelligence Command",
  "type": "object",
  "required": [
    "commandId",
    "commandType",
    "commandVersion",
    "projectId",
    "correlationId",
    "payload"
  ],
  "properties": {
    "commandId": {
      "$ref": "identifier.schema.json"
    },
    "commandType": {
      "type": "string",
      "minLength": 1
    },
    "commandVersion": {
      "type": "string",
      "minLength": 1
    },
    "projectId": {
      "$ref": "identifier.schema.json"
    },
    "correlationId": {
      "$ref": "identifier.schema.json"
    },
    "actor": {
      "type": [
        "string",
        "null"
      ]
    },
    "expectedRevisionId": {
      "type": [
        "string",
        "null"
      ]
    },
    "payload": {
      "type": "object"
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/coordinate-reference.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/coordinate-reference.schema.json",
  "title": "Spatial Intelligence Coordinate Reference",
  "type": "object",
  "required": [
    "coordinateReferenceId",
    "type",
    "dimensions",
    "axisOrder",
    "unit"
  ],
  "properties": {
    "coordinateReferenceId": {
      "$ref": "identifier.schema.json"
    },
    "type": {
      "type": "string",
      "enum": [
        "local-cartesian",
        "projected",
        "geographic",
        "custom"
      ]
    },
    "dimensions": {
      "type": "integer",
      "enum": [
        2,
        3
      ]
    },
    "axisOrder": {
      "type": "array",
      "minItems": 2,
      "maxItems": 3,
      "items": {
        "type": "string",
        "enum": [
          "x",
          "y",
          "z",
          "longitude",
          "latitude",
          "elevation"
        ]
      }
    },
    "unit": {
      "type": "string",
      "enum": [
        "mm",
        "cm",
        "m",
        "degrees"
      ]
    },
    "origin": {
      "type": "array",
      "minItems": 2,
      "maxItems": 3,
      "items": {
        "type": "number"
      }
    },
    "orientationDegrees": {
      "type": "number"
    },
    "externalReference": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/error.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/error.schema.json",
  "title": "Spatial Intelligence Error",
  "type": "object",
  "required": [
    "code",
    "message",
    "recoverable"
  ],
  "properties": {
    "code": {
      "type": "string",
      "minLength": 1
    },
    "message": {
      "type": "string",
      "minLength": 1
    },
    "subjectId": {
      "type": [
        "string",
        "null"
      ]
    },
    "operationId": {
      "type": [
        "string",
        "null"
      ]
    },
    "recoverable": {
      "type": "boolean"
    },
    "suggestedAction": {
      "type": [
        "string",
        "null"
      ]
    },
    "details": {
      "type": "object"
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/event.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/event.schema.json",
  "title": "Spatial Intelligence Event",
  "type": "object",
  "required": [
    "eventId",
    "eventType",
    "eventVersion",
    "occurredAt",
    "projectId",
    "correlationId",
    "payload"
  ],
  "properties": {
    "eventId": {
      "type": "string",
      "minLength": 1
    },
    "eventType": {
      "type": "string",
      "minLength": 1
    },
    "eventVersion": {
      "type": "string",
      "minLength": 1
    },
    "occurredAt": {
      "type": "string",
      "format": "date-time"
    },
    "projectId": {
      "type": "string",
      "minLength": 1
    },
    "subjectId": {
      "type": [
        "string",
        "null"
      ]
    },
    "correlationId": {
      "type": "string",
      "minLength": 1
    },
    "causationId": {
      "type": [
        "string",
        "null"
      ]
    },
    "actor": {
      "type": [
        "string",
        "null"
      ]
    },
    "payload": {
      "type": "object"
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/floor.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/floor.schema.json",
  "title": "SIM Floor",
  "type": "object",
  "required": [
    "floorId",
    "buildingId",
    "name",
    "state"
  ],
  "properties": {
    "floorId": {
      "$ref": "identifier.schema.json"
    },
    "buildingId": {
      "$ref": "identifier.schema.json"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "elevation": {
      "type": [
        "number",
        "null"
      ]
    },
    "height": {
      "type": [
        "number",
        "null"
      ],
      "exclusiveMinimum": 0
    },
    "state": {
      "type": "string",
      "enum": [
        "Draft",
        "Active",
        "Superseded",
        "Deleted"
      ]
    },
    "coordinateReferenceId": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/identifier.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/identifier.schema.json",
  "title": "Spatial Intelligence Identifier",
  "description": "Opaque, non-empty identifier used by SIS and SIM.",
  "type": "string",
  "minLength": 1,
  "maxLength": 255,
  "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]*$"
}


---

## File originale: `schemas/opening.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/opening.schema.json",
  "title": "SIM Opening",
  "type": "object",
  "required": [
    "openingId",
    "openingType",
    "hostId",
    "offset",
    "width",
    "height",
    "unit",
    "state"
  ],
  "properties": {
    "openingId": {
      "$ref": "identifier.schema.json"
    },
    "openingType": {
      "type": "string",
      "enum": [
        "Door",
        "Window",
        "Passage",
        "Custom"
      ]
    },
    "hostId": {
      "$ref": "identifier.schema.json"
    },
    "offset": {
      "type": "number",
      "minimum": 0
    },
    "width": {
      "type": "number",
      "exclusiveMinimum": 0
    },
    "height": {
      "type": "number",
      "exclusiveMinimum": 0
    },
    "unit": {
      "type": "string",
      "enum": [
        "mm",
        "cm",
        "m"
      ]
    },
    "state": {
      "type": "string",
      "enum": [
        "Draft",
        "Active",
        "Superseded",
        "Deleted"
      ]
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/project.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/project.schema.json",
  "title": "Spatial Intelligence Project",
  "type": "object",
  "required": [
    "schemaVersion",
    "projectId",
    "name",
    "state",
    "unitSystem"
  ],
  "properties": {
    "schemaVersion": {
      "type": "string",
      "pattern": "^0\\.1$"
    },
    "projectId": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "state": {
      "type": "string",
      "enum": [
        "Draft",
        "Measured",
        "Normalized",
        "Validated",
        "GeometryGenerated",
        "Analyzed",
        "Exported",
        "Published"
      ]
    },
    "unitSystem": {
      "type": "object",
      "required": [
        "length"
      ],
      "properties": {
        "length": {
          "type": "string",
          "enum": [
            "mm",
            "cm",
            "m"
          ]
        },
        "angle": {
          "type": "string",
          "enum": [
            "degrees",
            "radians"
          ]
        }
      },
      "additionalProperties": false
    },
    "metadata": {
      "type": "object"
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/result.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/result.schema.json",
  "title": "Spatial Intelligence Result",
  "type": "object",
  "required": [
    "operationId",
    "success",
    "errors",
    "warnings"
  ],
  "properties": {
    "operationId": {
      "$ref": "identifier.schema.json"
    },
    "success": {
      "type": "boolean"
    },
    "data": {},
    "errors": {
      "type": "array",
      "items": {
        "$ref": "error.schema.json"
      }
    },
    "warnings": {
      "type": "array",
      "items": {
        "$ref": "error.schema.json"
      }
    },
    "eventIds": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/space.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/space.schema.json",
  "title": "SIM Space",
  "type": "object",
  "required": [
    "spaceId",
    "floorId",
    "spaceType",
    "state"
  ],
  "properties": {
    "spaceId": {
      "$ref": "identifier.schema.json"
    },
    "floorId": {
      "$ref": "identifier.schema.json"
    },
    "spaceType": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": [
        "string",
        "null"
      ]
    },
    "boundaryGeometryId": {
      "type": [
        "string",
        "null"
      ]
    },
    "state": {
      "type": "string",
      "enum": [
        "Draft",
        "Active",
        "Superseded",
        "Deleted"
      ]
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/unit-system.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/unit-system.schema.json",
  "title": "Spatial Intelligence Unit System",
  "type": "object",
  "required": [
    "length",
    "angle"
  ],
  "properties": {
    "length": {
      "type": "string",
      "enum": [
        "mm",
        "cm",
        "m"
      ]
    },
    "angle": {
      "type": "string",
      "enum": [
        "degrees",
        "radians"
      ]
    },
    "area": {
      "type": "string",
      "enum": [
        "mm2",
        "cm2",
        "m2"
      ]
    },
    "volume": {
      "type": "string",
      "enum": [
        "mm3",
        "cm3",
        "m3"
      ]
    }
  },
  "additionalProperties": false
}


---

## File originale: `schemas/wall.schema.json`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/spatial-intelligence/wall.schema.json",
  "title": "SIM Wall",
  "type": "object",
  "required": [
    "wallId",
    "floorId",
    "start",
    "end",
    "thickness",
    "unit",
    "state"
  ],
  "properties": {
    "wallId": {
      "$ref": "identifier.schema.json"
    },
    "floorId": {
      "$ref": "identifier.schema.json"
    },
    "start": {
      "type": "array",
      "minItems": 2,
      "maxItems": 3,
      "items": {
        "type": "number"
      }
    },
    "end": {
      "type": "array",
      "minItems": 2,
      "maxItems": 3,
      "items": {
        "type": "number"
      }
    },
    "thickness": {
      "type": "number",
      "exclusiveMinimum": 0
    },
    "height": {
      "type": [
        "number",
        "null"
      ],
      "exclusiveMinimum": 0
    },
    "unit": {
      "type": "string",
      "enum": [
        "mm",
        "cm",
        "m"
      ]
    },
    "state": {
      "type": "string",
      "enum": [
        "Draft",
        "Active",
        "Superseded",
        "Deleted"
      ]
    }
  },
  "additionalProperties": false
}


---

## File originale: `specification/INDEX.md`

# Spatial Intelligence Specification Index

Specification version: 0.2-draft

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

This index is the entry point for the normative specification work
introduced by Release 0.2.

The specification is divided into:

- Spatial Intelligence Specification — SIS
- Spatial Intelligence Model — SIM
- public contracts
- machine-readable schemas
- compliance requirements

## SIS documents

| ID | File | Title | Status |
|---|---|---|---|
| SIS-000 | `SIS/00-overview.md` | SIS Overview | Draft |
| SIS-001 | `SIS/01-conformance.md` | Conformance | Draft |
| SIS-002 | `SIS/02-versioning.md` | Versioning | Draft |

## SIM documents

| ID | File | Title | Status |
|---|---|---|---|
| SIM-000 | `SIM/00-overview.md` | SIM Overview | Draft |
| SIM-001 | `SIM/01-identifiers.md` | Identifiers | Draft |
| SIM-002 | `SIM/02-units-and-coordinate-systems.md` | Units and Coordinate Systems | Draft |
| SIM-003 | `SIM/03-project-structure.md` | Project Structure | Draft |
| SIM-004 | `SIM/04-entity-lifecycle.md` | Entity Lifecycle | Draft |

## Machine-readable schemas

- `schemas/identifier.schema.json`
- `schemas/unit-system.schema.json`
- `schemas/coordinate-reference.schema.json`

## Normative language

The keywords MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD,
SHOULD NOT, RECOMMENDED, MAY and OPTIONAL indicate requirement levels.

## Maturity

All Release 0.2 Package A documents are Draft.

Draft specifications must not be presented as stable production
contracts.


---

## File originale: `specification/README.md`

# Specification

Stable Spatial Intelligence specifications.


---

## File originale: `specification/SIM/00-overview.md`

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


---

## File originale: `specification/SIM/01-identifiers.md`

# SIM Identifiers

Specification ID: SIM-001

Version: 0.2-draft

Status: Draft

## Purpose

This document defines identifier requirements for SIM entities and
related platform objects.

## Identifier requirements

Every persistent entity MUST have a stable identifier.

An identifier MUST:

- be non-empty;
- be unique within its declared scope;
- remain stable across serialisation;
- remain stable across export where supported;
- be treated as opaque by consumers.

## Opaque identifiers

Consumers MUST NOT infer business meaning from identifier structure.

An identifier such as:

`room-123`

MAY be readable, but consumers MUST NOT assume that `123` has semantic
meaning.

## Recommended format

UUID or another collision-resistant identifier format is RECOMMENDED.

Human-readable prefixes MAY be used.

Example:

`room_550e8400-e29b-41d4-a716-446655440000`

## Identifier types

The platform distinguishes:

- project identifier;
- entity identifier;
- revision identifier;
- Event identifier;
- correlation identifier;
- causation identifier;
- operation identifier;
- artifact identifier.

## Scope

Identifier uniqueness MUST be declared.

Typical scopes include:

- global;
- repository;
- Project;
- Event stream;
- export artifact.

## Revisions

Editing an entity SHOULD preserve the entity identifier.

The revision identifier MUST change when a new persistent revision is
created.

## Deleted entities

Deleted identifiers SHOULD NOT be reused within the same Project.

## External identifiers

Imported identifiers MAY be preserved as external references.

External identifiers MUST NOT replace the platform identifier unless
they satisfy all normative requirements.


---

## File originale: `specification/SIM/02-units-and-coordinate-systems.md`

# Units and Coordinate Systems

Specification ID: SIM-002

Version: 0.2-draft

Status: Draft

## Purpose

This document defines how SIM represents measurements, units,
coordinates and tolerances.

## Explicit units

Spatial values MUST NOT rely on undocumented implicit units.

Every Project MUST declare a unit system.

## Supported base length units

The initial Core supports:

- millimetres: `mm`
- centimetres: `cm`
- metres: `m`

Implementations MAY support additional units through extensions.

## Recommended internal unit

Millimetres are RECOMMENDED for architectural dimensions.

This recommendation does not require all implementations to store
values internally as millimetres.

## Angles

Supported angle units are:

- degrees;
- radians.

Angle unit MUST be explicit.

## Areas and volumes

Derived units MUST correspond to the declared length unit or be
explicitly specified.

Examples:

- square metres: `m2`;
- cubic metres: `m3`.

## Coordinate reference

Every spatial geometry context MUST declare:

- coordinate-reference identifier;
- dimensionality;
- axis order;
- origin;
- orientation;
- unit.

## Local coordinate systems

Projects MAY use a local Cartesian coordinate system.

A local system SHOULD define:

- origin at `(0, 0)` or `(0, 0, 0)`;
- positive X direction;
- positive Y direction;
- positive Z direction when applicable;
- north or reference orientation when known.

## Global coordinate systems

Geographic or projected coordinate systems MAY be used through an
identified external reference.

## Transformations

Coordinate transformations MUST declare:

- source reference;
- target reference;
- transformation method;
- precision;
- possible information loss.

## Tolerances

Geometry operations MUST use explicit tolerance policies.

A tolerance policy SHOULD include:

- linear tolerance;
- angular tolerance;
- area tolerance where applicable;
- rounding policy.

## Precision

Implementations MUST NOT claim higher precision than their source data
or Kernel supports.


---

## File originale: `specification/SIM/03-project-structure.md`

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


---

## File originale: `specification/SIM/04-entity-lifecycle.md`

# SIM Entity Lifecycle

Specification ID: SIM-004

Version: 0.2-draft

Status: Draft

## Purpose

This document defines lifecycle rules for SIM entities and revisions.

## Entity states

The initial entity lifecycle supports:

- Draft;
- Active;
- Superseded;
- Deleted.

## Draft

A Draft entity MAY be incomplete.

Draft entities MUST NOT be presented as validated unless they have a
separate successful validation result.

## Active

An Active entity is part of the current Project revision.

Active does not imply regulatory or professional approval.

## Superseded

A Superseded entity has been replaced by a newer revision or entity.

It SHOULD remain traceable when revision history is retained.

## Deleted

A Deleted entity is no longer active.

Deletion SHOULD preserve an audit reference where permitted.

## Creation metadata

Every entity SHOULD record:

- created timestamp;
- creating actor;
- source;
- initial revision identifier.

## Modification metadata

Modified entities SHOULD record:

- modified timestamp;
- modifying actor;
- revision identifier;
- change reason where available.

## Identity across revisions

An edited entity SHOULD retain its entity identifier.

Each persistent Project revision MUST have a distinct revision
identifier.

## Replacement

When one entity replaces another, the relationship SHOULD identify:

- previous entity or revision;
- replacement entity or revision;
- replacement reason;
- timestamp.

## Deletion and references

An entity MUST NOT be deleted silently when required references still
depend on it.

Implementations MUST either:

- reject deletion;
- update dependent references;
- mark references as unresolved;
- perform an explicitly declared cascading operation.

## Events

Recommended lifecycle Events include:

- EntityCreated;
- EntityActivated;
- EntitySuperseded;
- EntityDeleted;
- EntityRestored.


---

## File originale: `specification/SIM/05-building.md`

# SIM Building

        Specification ID: SIM-005

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines the Building entity and its relationship with Projects and Floors.

        ## Normative requirements

        - A Building MUST have a stable identifier.
- A Building MUST belong to exactly one Project.
- A Building MAY contain one or more Floors.
- A Building SHOULD declare a name or designation.
- A Building MAY declare address metadata without making it mandatory.
- Sensitive location data MUST be handled according to project privacy policy.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.


---

## File originale: `specification/SIM/06-floor.md`

# SIM Floor

        Specification ID: SIM-006

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines the Floor entity as a level within a Building.

        ## Normative requirements

        - A Floor MUST belong to exactly one Building.
- A Floor MUST have a stable identifier.
- A Floor SHOULD declare elevation.
- A Floor SHOULD declare usable height when known.
- A Floor MAY use a local coordinate reference.
- Floor order MUST NOT be inferred only from display names.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.


---

## File originale: `specification/SIM/07-space-and-room.md`

# SIM Space and Room

        Specification ID: SIM-007

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines generic Spaces and the Room specialisation.

        ## Normative requirements

        - A Space MUST belong to one Floor unless an extension defines otherwise.
- A Room MUST be represented as a Space specialisation.
- A Room MAY reference a closed boundary.
- A Room SHOULD declare use classification when known.
- Calculated area MUST declare units and tolerance.
- A Room MUST NOT be considered geometrically closed without validation.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.


---

## File originale: `specification/SIM/08-wall.md`

# SIM Wall

        Specification ID: SIM-008

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines Walls as spatial boundary elements.

        ## Normative requirements

        - A Wall MUST have a stable identifier.
- A Wall MUST belong to a Floor or equivalent spatial context.
- A Wall SHOULD reference start and end geometry.
- Wall thickness MUST declare units.
- Wall height SHOULD be explicit when known.
- Hosted Openings MUST reference their host Wall.
- A Wall MUST NOT expose proprietary Geometry Kernel objects.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.


---

## File originale: `specification/SIM/09-opening.md`

# SIM Opening

        Specification ID: SIM-009

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines Doors, Windows and other hosted openings.

        ## Normative requirements

        - An Opening MUST have a stable identifier.
- An Opening SHOULD reference a host element.
- Opening width and height MUST declare units.
- Opening position MUST be expressed relative to a declared reference.
- Door swing MAY be represented as optional geometry or metadata.
- An Opening outside its host extent MUST produce a validation result.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.


---

## File originale: `specification/SIM/10-furniture.md`

# SIM Furniture

        Specification ID: SIM-010

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines movable or placed spatial objects.

        ## Normative requirements

        - Furniture MUST have a stable identifier.
- Furniture MUST reference a parent Space or Floor context.
- Furniture dimensions MUST declare units.
- Furniture MAY reference a catalogue product.
- Catalogue references MUST remain separate from geometry identity.
- Furniture MUST NOT be treated as structural unless explicitly specialised.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.


---

## File originale: `specification/SIM/README.md`

# Sim

Spatial Intelligence Model modules.


---

## File originale: `specification/SIS/00-overview.md`

# SIS Overview

Specification ID: SIS-000

Version: 0.2-draft

Status: Draft

## Purpose

The Spatial Intelligence Specification defines the normative public
behaviour of the platform.

SIS is independent from:

- programming languages;
- geometry libraries;
- databases;
- CAD applications;
- rendering systems;
- cloud providers;
- AI providers;
- user-interface frameworks.

## Scope

SIS defines:

- normative vocabulary;
- public concepts;
- identifiers;
- units;
- coordinate systems;
- entity lifecycle;
- Service contracts;
- Ports;
- Events;
- Capabilities;
- errors;
- versioning;
- conformance.

## Relationship with SIM

SIS defines rules.

SIM represents spatial information governed by those rules.

SIS

↓

SIM

↓

Services

↓

Kernels and Adapters

## Normative and non-normative material

Normative material defines requirements.

Non-normative material provides examples, explanations or guidance.

Every specification document SHOULD identify which sections are
normative.

## Implementation independence

An implementation MAY use any internal architecture that satisfies the
public requirements and compliance tests.

Public contracts MUST NOT expose implementation-specific types unless
explicitly standardised.

## Extensibility

Extensions MAY introduce new domain concepts or Capabilities.

Extensions MUST NOT redefine the meaning of stable Core concepts.

## Security and privacy

Implementations MUST treat spatial data as potentially sensitive.

Public contracts SHOULD minimise unnecessary disclosure of:

- addresses;
- access routes;
- occupancy information;
- infrastructure details;
- personal data.

## Professional responsibility

SIS does not replace professional verification for structural,
regulatory, accessibility, fire-safety or authorisation matters.


---

## File originale: `specification/SIS/01-conformance.md`

# SIS Conformance

Specification ID: SIS-001

Version: 0.2-draft

Status: Draft

## Purpose

This document defines how implementations declare conformance with SIS.

## Conformance statement

A conforming implementation MUST declare:

- supported SIS version;
- supported SIM version;
- implemented Services;
- implemented Ports;
- declared Capabilities;
- known limitations;
- applicable extensions;
- compliance-suite version.

## Conformance levels

### Schema Conformance

Data satisfies the applicable machine-readable schemas.

### Model Conformance

SIM entities and relationships satisfy normative model rules.

### Service Conformance

Public Service behaviour satisfies the applicable Service contracts.

### Adapter Conformance

An Adapter satisfies the applicable Port contract.

### Capability Conformance

A declared Capability passes its required tests.

### Full Platform Conformance

The implementation satisfies all REQUIRED requirements for its declared
profile.

## Conformance profiles

Implementations MAY declare profiles such as:

- Core Model Profile;
- Geometry Profile;
- Validation Profile;
- Export Profile;
- Application Profile.

A profile MUST list its required documents and tests.

## Partial implementations

Partial implementations are permitted.

They MUST NOT claim unsupported Capabilities.

Unsupported behaviour MUST produce a structured error.

## Compliance evidence

Conformance evidence SHOULD include:

- test-suite version;
- execution date;
- implementation version;
- test results;
- excluded optional tests;
- known deviations.

## Non-conformance

An implementation is non-conforming when it:

- violates a REQUIRED rule;
- declares unsupported Capabilities;
- exposes incompatible public behaviour;
- silently ignores required validation;
- produces invalid normative data.

## Certification

Release 0.2 defines self-declared conformance only.

Independent certification MAY be introduced later.


---

## File originale: `specification/SIS/02-versioning.md`

# SIS Versioning

Specification ID: SIS-002

Version: 0.2-draft

Status: Draft

## Purpose

This document defines versioning rules for specifications, contracts,
schemas, Events and Capabilities.

## Version format

Stable public versions SHOULD use:

MAJOR.MINOR.PATCH

Draft versions MAY use suffixes such as:

- `0.2-draft`
- `0.2-preview.1`
- `1.0-rc.1`

## Major version

A MAJOR version changes when compatibility is intentionally broken.

Examples:

- removing a required field;
- changing the meaning of an existing field;
- changing identifier semantics;
- changing required Service behaviour.

## Minor version

A MINOR version changes for compatible additions.

Examples:

- adding an optional field;
- adding a new Capability;
- adding a new optional operation;
- adding a new Event type.

## Patch version

A PATCH version changes for compatible corrections.

Examples:

- editorial clarification;
- schema correction that does not alter valid data;
- test correction;
- non-normative example correction.

## Schema compatibility

New optional properties MAY be compatible.

Removing required properties is breaking.

Changing a property's type is normally breaking.

Tightening validation rules MAY be breaking.

## Event compatibility

Event consumers SHOULD ignore unknown optional properties.

Event producers MUST preserve required field meaning within a major
version.

## Capability compatibility

Capability identifiers MUST remain stable.

A breaking behavioural change requires a new major Capability version.

## Deprecation

Deprecation MUST document:

- deprecated item;
- replacement;
- reason;
- deprecation version;
- planned removal version;
- migration guidance.

## Migration

Breaking changes MUST include migration guidance when practical.

## Version negotiation

Services and Applications SHOULD be able to determine whether their
supported versions are compatible before executing a workflow.


---

## File originale: `specification/SIS/03-command-model.md`

# SIS Command Model

        Specification ID: SIS-003

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines commands that request controlled changes to Project state.

        ## Normative requirements

        - A Command MUST have a command identifier.
- A Command MUST declare its contract version.
- A Command MUST identify the target Project.
- A Command SHOULD include correlation and actor information.
- Commands MUST be validated before state mutation.
- A successful Command SHOULD produce one or more Events.
- Commands MUST NOT be represented as completed Events.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.


---

## File originale: `specification/SIS/04-result-model.md`

# SIS Result Model

        Specification ID: SIS-004

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines structured operation results.

        ## Normative requirements

        - Every public operation MUST return a structured result.
- A result MUST declare success or failure.
- A successful result MAY contain data and emitted Event references.
- A failed result MUST contain one or more structured errors.
- Warnings MUST remain distinct from fatal errors.
- Results MUST preserve operation and correlation identifiers.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.


---

## File originale: `specification/SIS/05-error-model.md`

# SIS Error Model

        Specification ID: SIS-005

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines the shared public error representation.

        ## Normative requirements

        - Every error MUST have a machine-readable code.
- Every error MUST have a human-readable message.
- Errors SHOULD identify the affected subject.
- Errors MUST declare recoverability when known.
- Validation failures MUST remain distinct from internal system failures.
- Vendor-specific errors MUST be translated at Adapter boundaries.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.


---

## File originale: `specification/SIS/README.md`

# Sis

Spatial Intelligence Specification modules.

