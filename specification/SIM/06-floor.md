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
