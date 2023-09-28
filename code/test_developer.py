""" Module to test developers. """
# standard imports
from pathlib import Path
import json
from typing import List

# internal imports
from interface import Developer, Organization


def test_valid_developers():
    """Test function for developers"""

    data_path = Path("../data/developers")
    for file in data_path.iterdir():
        with open(file, "r", encoding="utf-8") as file_pointer:
            file_content = json.load(file_pointer)
        dev = Developer.model_validate(file_content)

        file_name = file.name.replace(file.suffix, "")

        # Make sure file name is same as developer name
        # it can be case insensitve and ignore spaces
        assert file_name == dev.name.lower() or file_name == dev.name.lower().replace(
            " ", ""
        )


def test_valid_organizations_for_developers():
    """Test if developer entry has valid organization name."""

    organizatons: List[str] = []
    for file in Path("../data/organizations").iterdir():
        with open(file, "r", encoding="utf-8") as file_pointer:
            file_content = json.load(file_pointer)
        org = Organization.model_validate(file_content)
        organizatons.append(org.name)

    for file in Path("../data/developers").iterdir():
        with open(file, "r", encoding="utf-8") as file_pointer:
            file_content = json.load(file_pointer)

        dev = Developer.model_validate(file_content)
        if dev.organization is not None:
            assert dev.organization in organizatons
