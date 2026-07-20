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
