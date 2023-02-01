from re import sub


def clean_name(name: str) -> str:
    return sub("[^0-9a-zA-Z_]", "_", name)
