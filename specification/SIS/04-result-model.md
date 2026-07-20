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
