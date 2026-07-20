# Export Capability Catalogue

        Contract ID: CAP-EXP-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines discoverable export features.

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
        | `Export2D` | Export two-dimensional representations. | Draft |
| `Export3D` | Export three-dimensional representations. | Draft |
| `ExportSemanticModel` | Preserve semantic spatial entities. | Draft |
| `ExportDimensions` | Export dimensions and measurement annotations. | Draft |
| `ExportLayers` | Preserve or map semantic layers. | Draft |
| `ExportMetadata` | Export project and entity metadata. | Draft |
| `ReportInformationLoss` | Report unsupported or approximated content. | Draft |

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
