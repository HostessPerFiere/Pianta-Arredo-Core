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
