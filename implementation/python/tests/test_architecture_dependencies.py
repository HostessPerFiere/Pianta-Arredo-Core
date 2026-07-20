from pathlib import Path


SOURCE = (
    Path(__file__).parents[1]
    / "src"
    / "spatial_intelligence"
)


def read_module(relative_path: str) -> str:
    return (SOURCE / relative_path).read_text(encoding="utf-8")


def test_domain_does_not_import_services_or_adapters() -> None:
    content = read_module("domain/models.py")

    assert "spatial_intelligence.services" not in content
    assert "spatial_intelligence.adapters" not in content


def test_services_do_not_import_concrete_adapters() -> None:
    for path in (SOURCE / "services").glob("*.py"):
        content = path.read_text(encoding="utf-8")
        assert "spatial_intelligence.adapters" not in content


def test_ports_do_not_import_adapters() -> None:
    for path in (SOURCE / "ports").glob("*.py"):
        content = path.read_text(encoding="utf-8")
        assert "spatial_intelligence.adapters" not in content
