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
