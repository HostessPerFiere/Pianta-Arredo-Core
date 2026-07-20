# Python Reference Architecture Example

This example uses the Release 0.3 composition root.

```python
from spatial_intelligence.composition import build_application
from spatial_intelligence.domain import Project, Wall

services = build_application()

project = Project(
    project_id="project_001",
    name="Example",
    walls=(
        Wall(
            wall_id="wall_001",
            start=(0.0, 0.0),
            end=(4000.0, 0.0),
            thickness_mm=120.0,
        ),
    ),
)

result = services.workflow.validate_and_export(project)
```

The workflow validates the Project, exports JSON and publishes an
`ExportCompleted` Event.
