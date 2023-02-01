from pathlib import Path
from typing import List

from openapi_python_generator.generate_data import generate_data
from setuptools import Distribution

from setuptools_openapi_generator.config import Configuration
from setuptools_openapi_generator.utils import clean_name, get_name


def _generate_clients(configuration: Configuration):
    generated_apis: List[str] = list()
    for source in sorted(configuration.sources):
        module_name = clean_name(get_name(source))
        generate_data(
            source,
            configuration.basedir.joinpath(module_name),
            configuration.library,
        )
        generated_apis.append(module_name)
    with open(configuration.basedir.joinpath("__init__.py"), "w+") as init_file:
        init_file.writelines(f"from {api} import *\n" for api in generated_apis)


def generate_clients(distribution: Distribution):
    TOML_PATH = Path("pyproject.toml")
    configuration = Configuration.from_toml(TOML_PATH)
    _generate_clients(configuration)
