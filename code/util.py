""" Module for storing utility functions. """

# standard imports
from pathlib import Path
import json
from typing import Optional, Dict


def read_file(file_path: Path) -> Optional[Dict]:
    """Reads from file."""

    if file_path.suffix == ".json":
        with open(file_path, "r", encoding="utf-8") as file_pointer:
            json_content = json.load(file_pointer)

        return json_content

    raise NotImplementedError(
        f"Reading file of type {file_path.suffix} is not implemented."
    )


def write_file(data: Dict, file_path: Path) -> None:
    """Writed to file."""

    if file_path.suffix == ".json":
        with open(file_path, "w", encoding="utf-8") as file_pointer:
            json.dump(data, file_pointer)
        return
    raise NotImplementedError(
        f"Writing file of type {file_path.suffix} is not implemented."
    )
