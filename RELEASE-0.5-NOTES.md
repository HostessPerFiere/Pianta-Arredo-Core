# Release 0.5 — Project Model and Persistence

Status: Completed

## Added

- revision-aware ProjectRecord;
- ProjectRepositoryPort;
- in-memory Project repository;
- JSON file Project repository;
- Project save and load Service;
- revision conflict handling;
- persistence integration tests.

## Limitations

This release does not include a database Adapter, migrations,
authentication or distributed locking.
