# Export Port

        Contract ID: PORT-EXP-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Connects the Export Service to format-specific Export Adapters.

        ## Direction

        This Port is a public boundary between platform Services and replaceable
        infrastructure.

        Services depend on the Port.

        Adapters implement the Port.

        The Port must not depend on a concrete Adapter.

        ## Operations

        - list supported formats
- validate abstract export model
- generate target artifact
- report information loss
- declare Export Capabilities

        ## Candidate Adapters

        - DXF Adapter
- SVG Adapter
- IFC Adapter
- STEP Adapter
- glTF Adapter
- Sweet Home 3D Adapter
- JSON Adapter

        Adapter names do not alter the public Port contract.

        ## Input and output rules

        - use public identifiers;
        - declare versions;
        - avoid vendor-specific types;
        - return structured results;
        - preserve traceability;
        - report unsupported behaviour.

        ## Errors

        - UnsupportedExportFormat
- UnsupportedExportEntity
- ExportEncodingFailed
- TargetVersionUnsupported
- ExportArtifactWriteFailed

        ## Security

        Adapters must use the minimum permissions required.

        Sensitive spatial data must not be transmitted or persisted unless
        explicitly authorised by the Application.

        ## Versioning

        Port versions follow public contract compatibility rules.

        ## Conformance

        An Adapter conforms only when it passes the applicable Port compliance
        suite and accurately declares its supported Capabilities.
