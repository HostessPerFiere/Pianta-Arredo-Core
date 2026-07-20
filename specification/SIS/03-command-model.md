# SIS Command Model

        Specification ID: SIS-003

        Version: 0.2-draft

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines commands that request controlled changes to Project state.

        ## Normative requirements

        - A Command MUST have a command identifier.
- A Command MUST declare its contract version.
- A Command MUST identify the target Project.
- A Command SHOULD include correlation and actor information.
- Commands MUST be validated before state mutation.
- A successful Command SHOULD produce one or more Events.
- Commands MUST NOT be represented as completed Events.

        ## Versioning

        Compatible additions MAY introduce optional properties.

        Removing required behaviour or changing established meaning is a
        breaking change.

        ## Conformance

        Implementations claiming support MUST pass the applicable schema,
        contract and compliance tests.
