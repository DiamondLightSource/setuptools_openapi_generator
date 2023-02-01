from pathlib import Path

from openapi_python_generator.common import HTTPLibrary

from setuptools_openapi_generator.config import Configuration


def test_load_config_from_toml():
    assert Configuration(
        library=HTTPLibrary.httpx,
        basedir=Path("src/sample_project/apis/"),
        sources={
            Path("api_definitions/link-example.json"),
            Path("api_definitions/petstore.json"),
        },
    ) == Configuration.from_toml(toml_path="tests/sample_project/pyproject.toml")
