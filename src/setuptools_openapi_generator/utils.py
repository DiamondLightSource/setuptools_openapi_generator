from pathlib import Path
from re import sub


def get_name(path: str) -> str:
    return Path(path).stem


def clean_name(name: str) -> str:
    return sub("^[^a-zA-Z]|[^0-9a-zA-Z]", "_", name)
