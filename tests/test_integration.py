from pathlib import Path

from setuptools_openapi_generator.config import Configuration
from setuptools_openapi_generator.integration import _generate_clients


def test_clinets_are_generated():
    TOML_PATH = Path("tests/sample_project/pyproject.toml")
    configuration = Configuration.from_toml(TOML_PATH)
    _generate_clients(configuration, TOML_PATH.parent)
