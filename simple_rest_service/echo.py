from typing import Optional


def echo(in_string: str, prefix: Optional[str] = None) -> str:
    prefix = prefix or "echoed: "
    return f"{prefix}{in_string}"
