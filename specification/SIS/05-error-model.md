# SIS Error Model

        Specification ID: SIS-005

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines the shared public error representation.

        ## Normative requirements

        - Every error MUST have a machine-readable code.
- Every error MUST have a human-readable message.
- Errors SHOULD identify the affected subject.
- Errors MUST declare recoverability when known.
- Validation failures MUST remain distinct from internal system failures.
- Vendor-specific errors MUST be translated at Adapter boundaries.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.
