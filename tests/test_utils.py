import pytest

from setuptools_openapi_generator.utils import get_name


@pytest.mark.parametrize(
    ("expected", "path"),
    [
        (
            "link-example",
            "https://raw.githubusercontent.com"
            "/OAI/OpenAPI-Specification/main/examples/v3.0/link-example.json",
        ),
        ("petstore", "api_definitions/petstore.json"),
        ("other", "other.json"),
    ],
)
def test_get_name_returns_name(expected: str, path: str):
    assert expected == get_name(path)
