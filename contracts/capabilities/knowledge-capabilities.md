# Knowledge Capability Catalogue

        Contract ID: CAP-KNW-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines discoverable Knowledge Service operations.

        ## Capability descriptor

        Every Capability declaration includes:

        - identifier;
        - version;
        - status;
        - supported inputs;
        - supported outputs;
        - limits;
        - dependencies;
        - restrictions.

        ## Catalogue

        | Capability | Description | Status |
        |---|---|---|
        | `ResolveRule` | Resolve an applicable rule. | Draft |
| `ListApplicableRules` | List rules for a project context. | Draft |
| `ResolveDefault` | Resolve a versioned default value. | Draft |
| `ResolveClassification` | Resolve a domain classification. | Draft |
| `ExplainRule` | Return traceability and explanation. | Draft |
| `CompareKnowledgeVersions` | Compare two Knowledge Package versions. | Draft |

        ## Negotiation

        Applications may query Capabilities before constructing a workflow.

        Partial support must be declared explicitly.

        ## Unsupported behaviour

        An unavailable Capability must produce a structured
        `CapabilityNotSupported` error.

        ## Versioning

        Capability identifiers are stable.

        Behavioural breaking changes require a new major Capability version.

        ## Conformance

        A component may declare a Capability only when its corresponding
        compliance tests pass.
