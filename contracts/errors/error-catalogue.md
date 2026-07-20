# Error Catalogue

Version: 0.2-draft

Status: Draft

## Core errors

| Code | Meaning |
|---|---|
| `InvalidRequest` | Request structure or values are invalid |
| `EntityNotFound` | Referenced entity does not exist |
| `RevisionConflict` | Project revision is no longer current |
| `CapabilityNotSupported` | Requested Capability is unavailable |
| `ValidationFailed` | Domain or geometric validation failed |
| `AdapterUnavailable` | Required Adapter cannot be used |
| `InternalFailure` | Unexpected implementation failure |

## Rules

Error codes are stable public identifiers.

Implementations MAY add extension errors.

Extension errors MUST NOT redefine Core error meanings.
