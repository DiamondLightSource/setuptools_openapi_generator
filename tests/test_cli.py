import subprocess
import sys

from setuptools_openapi_generator import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "setuptools_openapi_generator", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
