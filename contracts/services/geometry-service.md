# Geometry Service Contract

        Contract ID: SVC-GEO-001

        Version: 0.1

        Status: Draft

        Owner: Spatial Intelligence Platform

        ## Purpose

        Defines public operations for creating, transforming and querying spatial geometry.

        ## Public operations

        - CreateGeometry
- UpdateGeometry
- SplitWall
- MergeWalls
- CreateOpening
- GenerateRoomBoundary
- CalculateMeasurements
- TransformCoordinates

        ## Inputs

        - project identifier
- subject identifier
- geometry request
- units
- coordinate reference
- tolerance policy

        Every request must declare its contract version and project context.

        Spatial requests must explicitly declare units, coordinate reference
        and tolerances where applicable.

        ## Outputs

        - geometry result
- topology references
- measurements
- diagnostics
- generated Events

        Outputs must use public contract types and must not expose proprietary
        Kernel or Adapter objects.

        ## Errors

        - InvalidCoordinate
- InvalidGeometry
- DegenerateSegment
- NonClosedBoundary
- SelfIntersection
- ToleranceExceeded
- CapabilityNotSupported

        Errors must contain:

        - machine-readable code;
        - human-readable message;
        - affected subject;
        - operation identifier;
        - recoverability;
        - suggested action where available.

        ## Events

        - GeometryCreated
- GeometryUpdated
- WallSplit
- WallsMerged
- RoomBoundaryGenerated

        Events describe completed facts. Requests and commands are not Events.

        ## Capabilities

        - CreateWall
- SplitWall
- MergeWalls
- OffsetWall
- CreateOpening
- GenerateRoomBoundary
- CalculateArea
- TransformCoordinates

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
