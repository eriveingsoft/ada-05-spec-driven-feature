"""Data access repository for loading customer data."""

import json
from pathlib import Path
from typing import Union

from src.domain import Customer


def load_customers(file_path: Union[str, Path] = "customers.json") -> list[Customer]:
    """Opens, reads, and loads customer data from a JSON file into Customer instances.

    Args:
        file_path: Path to the customer JSON file.

    Returns:
        List of Customer domain model instances.

    Raises:
        FileNotFoundError: If the specified JSON file does not exist.
        ValueError: If JSON syntax is invalid or root is not a list.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Customer data file not found: {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Corrupted or invalid JSON in {path}") from exc

    if not isinstance(data, list):
        raise ValueError(f"Customer data in {path} must be a list of objects")

    return [Customer.from_dict(item) for item in data]
