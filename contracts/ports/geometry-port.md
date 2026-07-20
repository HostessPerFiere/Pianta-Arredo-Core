# Geometry Port

        Contract ID: PORT-GEO-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Connects the Geometry Service to a replaceable Geometry Kernel.

        ## Direction

        This Port is a public boundary between platform Services and replaceable
        infrastructure.

        Services depend on the Port.

        Adapters implement the Port.

        The Port must not depend on a concrete Adapter.

        ## Operations

        - create geometry
- transform geometry
- query geometry
- calculate measurements
- validate Kernel-level geometry
- declare Geometry Capabilities

        ## Candidate Adapters

        - OpenCascade Adapter
- custom computational geometry Adapter
- test geometry Adapter

        Adapter names do not alter the public Port contract.

        ## Input and output rules

        - use public identifiers;
        - declare versions;
        - avoid vendor-specific types;
        - return structured results;
        - preserve traceability;
        - report unsupported behaviour.

        ## Errors

        - KernelUnavailable
- UnsupportedGeometryOperation
- GeometryKernelFailure
- GeometryPrecisionFailure

        ## Security

        Adapters must use the minimum permissions required.

        Sensitive spatial data must not be transmitted or persisted unless
        explicitly authorised by the Application.

        ## Versioning

        Port versions follow public contract compatibility rules.

        ## Conformance

        An Adapter conforms only when it passes the applicable Port compliance
        suite and accurately declares its supported Capabilities.
