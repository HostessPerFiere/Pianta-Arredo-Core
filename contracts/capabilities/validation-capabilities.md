# Validation Capability Catalogue

        Contract ID: CAP-VAL-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines discoverable validation operations.

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
        | `ValidateTopology` | Validate spatial connectivity and enclosure. | Draft |
| `ValidateDimensions` | Validate dimensions and tolerances. | Draft |
| `ValidateRoomClosure` | Verify that a Room boundary is closed. | Draft |
| `ValidateOpeningPlacement` | Validate Doors and Windows on host Walls. | Draft |
| `ValidateDomainRules` | Apply rules supplied by Knowledge Packages. | Draft |
| `ValidateExportReadiness` | Verify readiness for a target export. | Draft |

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
