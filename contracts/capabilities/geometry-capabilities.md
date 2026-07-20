# Geometry Capability Catalogue

        Contract ID: CAP-GEO-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines discoverable Geometry Service and Kernel features.

        ## Capability descriptor

        Every Capability declaration includes:

        - identifier;
        - version;
        - status;
        - supported inputs;
        - supported outputs;
        - limits;
        - dependencies;
        - restrictions.

        ## Catalogue

        | Capability | Description | Status |
        |---|---|---|
        | `CreateWall` | Create a Wall geometry representation. | Draft |
| `SplitWall` | Split a Wall at one or more positions. | Draft |
| `MergeWalls` | Merge compatible Wall segments. | Draft |
| `OffsetWall` | Create a parallel Wall offset. | Draft |
| `CreateOpening` | Create a Door or Window opening. | Draft |
| `GenerateRoomBoundary` | Generate a closed Room boundary. | Draft |
| `CalculateArea` | Calculate area using declared units and tolerance. | Draft |
| `TransformCoordinates` | Transform geometry between coordinate references. | Draft |

        ## Negotiation

        Applications may query Capabilities before constructing a workflow.

        Partial support must be declared explicitly.

        ## Unsupported behaviour

        An unavailable Capability must produce a structured
        `CapabilityNotSupported` error.

        ## Versioning

        Capability identifiers are stable.

        Behavioural breaking changes require a new major Capability version.

        ## Conformance

        A component may declare a Capability only when its corresponding
        compliance tests pass.
