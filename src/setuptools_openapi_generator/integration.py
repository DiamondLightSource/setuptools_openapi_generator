from pathlib import Path
from typing import List

from openapi_python_generator.generate_data import generate_data
from setuptools import Distribution

from setuptools_openapi_generator.config import Configuration
from setuptools_openapi_generator.utils import clean_name


def _generate_clients(configuration: Configuration, project_dir: Path):
    generated_apis: List[str] = list()
    for source in sorted(configuration.sources):
        module_name = clean_name(source.stem)
        generate_data(
            project_dir.joinpath(source),
            project_dir.joinpath(configuration.basedir, module_name),
            configuration.library,
        )
        generated_apis.append(module_name)
    with open(
        project_dir.joinpath(configuration.basedir, "__init__.py"), "x"
    ) as init_file:
        init_file.writelines(f"from {api} import *\n" for api in generated_apis)


def generate_clients(distribution: Distribution):
    TOML_PATH = Path("pyproject.toml")
    configuration = Configuration.from_toml(TOML_PATH)
    _generate_clients(configuration, TOML_PATH.parent)
