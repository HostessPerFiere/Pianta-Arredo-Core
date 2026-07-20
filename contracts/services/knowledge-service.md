# Knowledge Service Contract

        Contract ID: SVC-KNW-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines access to versioned, traceable domain knowledge and rule packages.

        ## Public operations

        - ResolveRule
- ListApplicableRules
- ResolveDefault
- ResolveClassification
- ExplainRule
- CompareKnowledgeVersions

        ## Inputs

        - project context
- domain classification
- jurisdiction or scope
- effective date
- knowledge package version
- rule query

        Every request must declare its contract version and project context.

        Spatial requests must explicitly declare units, coordinate reference
        and tolerances where applicable.

        ## Outputs

        - resolved rules
- source references
- assumptions
- conflicts
- applicability explanation

        Outputs must use public contract types and must not expose proprietary
        Kernel or Adapter objects.

        ## Errors

        - KnowledgePackageNotFound
- RuleNotFound
- RuleConflict
- UnsupportedJurisdiction
- KnowledgeVersionMismatch

        Errors must contain:

        - machine-readable code;
        - human-readable message;
        - affected subject;
        - operation identifier;
        - recoverability;
        - suggested action where available.

        ## Events

        - KnowledgePackageLoaded
- RuleResolved
- RuleConflictDetected

        Events describe completed facts. Requests and commands are not Events.

        ## Capabilities

        - ResolveRule
- ListApplicableRules
- ResolveDefault
- ResolveClassification
- ExplainRule
- CompareKnowledgeVersions

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
