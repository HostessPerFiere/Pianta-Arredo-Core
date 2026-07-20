# Project Model and Persistence

Version: 0.5

Status: Experimental reference implementation

## Scope

Release 0.5 introduces revision-aware Project persistence.

## Components

- ProjectRecord
- ProjectRepositoryPort
- InMemoryProjectRepository
- JsonProjectRepository
- ProjectService

## Revision rules

- A new Project starts at revision 1.
- Every successful update increments the revision.
- Clients MAY declare an expected revision.
- A mismatching expected revision produces RevisionConflict.
- Persistence Adapters MUST preserve Project identifiers.

## Limitations

JSON persistence is intended for development and interoperability
experiments, not concurrent production workloads.
