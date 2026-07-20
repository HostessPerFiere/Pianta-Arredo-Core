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
