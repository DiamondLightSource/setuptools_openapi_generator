setuptools_openapi_generator
============================

|code_ci| |docs_ci| |coverage| |pypi_version| |license|

A setuptools extension for generating RESTful clients from OpenAPI schema at build time,
allowing for easy use of the API with static type checking.

============== ==============================================================
PyPI           ``pip install setuptools_openapi_generator``
Source code    https://github.com/garryod/setuptools_openapi_generator
Documentation  https://garryod.github.io/setuptools_openapi_generator
Releases       https://github.com/garryod/setuptools_openapi_generator/releases
============== ==============================================================

To generate an API client in your project, simply add `setuptools_openapi_generator`
to the `build-system.requires` section of your `pyproject.toml`. 

Client generation can be configured via a `tool` entry in the `pyproject.toml` as below:

.. code-block:: toml

    [tool.setuptools_openapi_generator]
    library = "httpx"
    basedir = "src/sample_project/apis/"
    sources = ["api_definitions/link-example.json", "api_definitions/petstore.json"]
    
The above example will generate two API clients, at `src/sample_project/apis/link_example`
and src/sample_project/apis/petstore" respectively.

.. |code_ci| image:: https://github.com/garryod/setuptools_openapi_generator/actions/workflows/code.yml/badge.svg?branch=main
    :target: https://github.com/garryod/setuptools_openapi_generator/actions/workflows/code.yml
    :alt: Code CI

.. |docs_ci| image:: https://github.com/garryod/setuptools_openapi_generator/actions/workflows/docs.yml/badge.svg?branch=main
    :target: https://github.com/garryod/setuptools_openapi_generator/actions/workflows/docs.yml
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/garryod/setuptools_openapi_generator/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/garryod/setuptools_openapi_generator
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/setuptools_openapi_generator.svg
    :target: https://pypi.org/project/setuptools_openapi_generator
    :alt: Latest PyPI version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

See https://garryod.github.io/setuptools_openapi_generator for more detailed documentation.
