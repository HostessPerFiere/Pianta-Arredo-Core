# Core Model Compliance Cases

Version: 0.2-draft

Status: Draft

## Cases

### CM-001 — Valid Project

A Project with valid identifier, unit system and coordinate reference
MUST be accepted.

### CM-002 — Missing identifier

An entity without a required identifier MUST be rejected.

### CM-003 — Unknown unit

An unsupported unit without an extension declaration MUST be rejected.

### CM-004 — Circular containment

Circular Project containment MUST be rejected.

### CM-005 — Invalid Wall thickness

Zero or negative Wall thickness MUST be rejected.

### CM-006 — Invalid Opening host

An Opening referencing an unavailable host MUST produce a validation
error.

### CM-007 — Revision conflict

A Command with an obsolete expected revision MUST return
`RevisionConflict`.
