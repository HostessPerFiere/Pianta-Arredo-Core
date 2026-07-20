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
