# Persistence Port

        Contract ID: PORT-PER-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines storage and retrieval of Projects, revisions, Events and model snapshots.

        ## Direction

        This Port is a public boundary between platform Services and replaceable
        infrastructure.

        Services depend on the Port.

        Adapters implement the Port.

        The Port must not depend on a concrete Adapter.

        ## Operations

        - save project
- load project
- save revision
- list revisions
- load revision
- delete permitted data
- check optimistic concurrency

        ## Candidate Adapters

        - JSON file Adapter
- SQLite Adapter
- PostgreSQL Adapter
- cloud persistence Adapter
- in-memory test Adapter

        Adapter names do not alter the public Port contract.

        ## Input and output rules

        - use public identifiers;
        - declare versions;
        - avoid vendor-specific types;
        - return structured results;
        - preserve traceability;
        - report unsupported behaviour.

        ## Errors

        - ProjectNotFound
- RevisionConflict
- PersistenceUnavailable
- PersistenceWriteFailed
- PersistenceReadFailed

        ## Security

        Adapters must use the minimum permissions required.

        Sensitive spatial data must not be transmitted or persisted unless
        explicitly authorised by the Application.

        ## Versioning

        Port versions follow public contract compatibility rules.

        ## Conformance

        An Adapter conforms only when it passes the applicable Port compliance
        suite and accurately declares its supported Capabilities.
