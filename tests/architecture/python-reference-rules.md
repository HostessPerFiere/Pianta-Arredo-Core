# Python Reference Architecture Rules

Version: 0.3

Status: Active

## Rules

- `domain` MUST NOT import `services`, `ports` or `adapters`.
- `contracts` MUST NOT import `adapters`.
- `ports` MAY import public domain types.
- `services` MAY depend on `domain`, `contracts` and `ports`.
- `services` MUST NOT import concrete Adapters.
- `adapters` MUST implement public Ports structurally.
- `composition` MAY import Services and Adapters.
- tests MAY import any public reference module.

## Enforcement

Release 0.3 documents these rules and includes executable import checks.
