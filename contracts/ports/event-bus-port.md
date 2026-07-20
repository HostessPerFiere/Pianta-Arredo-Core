# Event Bus Port

        Contract ID: PORT-EVT-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines publication and subscription of domain and integration Events.

        ## Direction

        This Port is a public boundary between platform Services and replaceable
        infrastructure.

        Services depend on the Port.

        Adapters implement the Port.

        The Port must not depend on a concrete Adapter.

        ## Operations

        - publish Event
- publish Event batch
- subscribe by Event type
- unsubscribe
- acknowledge delivery when supported
- declare delivery guarantees

        ## Candidate Adapters

        - in-process Event Bus Adapter
- persistent queue Adapter
- external message broker Adapter
- test Event Bus Adapter

        Adapter names do not alter the public Port contract.

        ## Input and output rules

        - use public identifiers;
        - declare versions;
        - avoid vendor-specific types;
        - return structured results;
        - preserve traceability;
        - report unsupported behaviour.

        ## Errors

        - EventPublicationFailed
- EventSubscriptionFailed
- UnsupportedDeliveryGuarantee
- InvalidEventEnvelope

        ## Security

        Adapters must use the minimum permissions required.

        Sensitive spatial data must not be transmitted or persisted unless
        explicitly authorised by the Application.

        ## Versioning

        Port versions follow public contract compatibility rules.

        ## Conformance

        An Adapter conforms only when it passes the applicable Port compliance
        suite and accurately declares its supported Capabilities.
