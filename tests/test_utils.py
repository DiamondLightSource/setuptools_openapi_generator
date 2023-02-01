import pytest

from setuptools_openapi_generator.utils import clean_name, get_name


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


@pytest.mark.parametrize(
    "name",
    [
        "ufhwahidhuhiuhdiuawh",
        "y753rhqblhbey2q078",
        "/7*+4684+17+/7+7+9",
        "4/+9b5047+4117+v",
    ],
)
def test_clean_name_returns_valid_identifier(name: str):
    assert clean_name(name).isidentifier()
