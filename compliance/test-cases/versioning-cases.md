# Versioning Compliance Cases

Version: 0.2-draft

Status: Draft

## Cases

### VER-001 — Unknown optional property

Compatible consumers SHOULD ignore unknown optional properties.

### VER-002 — Missing required property

Missing required properties MUST fail validation.

### VER-003 — Breaking type change

Changing a stable property's type requires a new major version.

### VER-004 — Capability accuracy

An implementation MUST NOT declare a Capability that fails its
required tests.
