# Export Service Contract

        Contract ID: SVC-EXP-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines creation of abstract export representations and delegation to format-specific Export Adapters.

        ## Public operations

        - PrepareExport
- ValidateExportReadiness
- ListExportFormats
- ExecuteExport
- ReportInformationLoss

        ## Inputs

        - project identifier
- export scope
- target format
- target version
- unit policy
- layer mapping
- Adapter identifier

        Every request must declare its contract version and project context.

        Spatial requests must explicitly declare units, coordinate reference
        and tolerances where applicable.

        ## Outputs

        - abstract export model
- generated artifact reference
- format metadata
- warnings
- information-loss report

        Outputs must use public contract types and must not expose proprietary
        Kernel or Adapter objects.

        ## Errors

        - ExportFormatNotSupported
- ExportAdapterUnavailable
- ExportValidationFailed
- InformationLossNotAccepted
- ExportGenerationFailed

        Errors must contain:

        - machine-readable code;
        - human-readable message;
        - affected subject;
        - operation identifier;
        - recoverability;
        - suggested action where available.

        ## Events

        - ExportPrepared
- ExportCompleted
- ExportFailed

        Events describe completed facts. Requests and commands are not Events.

        ## Capabilities

        - Export2D
- Export3D
- ExportSemanticModel
- ExportDimensions
- ExportLayers
- ExportMetadata

        Consumers should query declared Capabilities before invoking optional
        operations.

        ## Versioning

        Compatible additions may introduce optional fields or new operations.

        Breaking changes require a new major contract version and migration
        guidance.

        ## Conformance

        An implementation conforms to this Service contract only when:

        - required operations are implemented;
        - declared Capabilities are accurate;
        - public errors follow the contract;
        - applicable compliance tests pass;
        - unsupported behaviour is reported explicitly.
