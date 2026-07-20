# Validation Service Contract

        Contract ID: SVC-VAL-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines structured validation of spatial models, geometry, topology, dimensions and domain rules.

        ## Public operations

        - ValidateProject
- ValidateEntity
- ValidateTopology
- ValidateDimensions
- ValidateRoomClosure
- ValidateOpeningPlacement
- ValidateExportReadiness

        ## Inputs

        - project or entity identifier
- validation profile
- knowledge package references
- severity threshold
- tolerance policy

        Every request must declare its contract version and project context.

        Spatial requests must explicitly declare units, coordinate reference
        and tolerances where applicable.

        ## Outputs

        - validation report
- rule results
- severity summary
- evidence
- suggested corrections

        Outputs must use public contract types and must not expose proprietary
        Kernel or Adapter objects.

        ## Errors

        - ValidationProfileNotFound
- KnowledgePackageUnavailable
- InvalidValidationRequest
- ValidationExecutionFailed
- CapabilityNotSupported

        Errors must contain:

        - machine-readable code;
        - human-readable message;
        - affected subject;
        - operation identifier;
        - recoverability;
        - suggested action where available.

        ## Events

        - ValidationStarted
- ValidationCompleted
- ValidationFailed

        Events describe completed facts. Requests and commands are not Events.

        ## Capabilities

        - ValidateTopology
- ValidateDimensions
- ValidateRoomClosure
- ValidateOpeningPlacement
- ValidateDomainRules
- ValidateExportReadiness

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
