""" Module to test developers. """
# standard imports
from pathlib import Path
from typing import List

# internal imports
from interface import Developer, Organization
from util import read_file


def test_valid_developers():
    """Test function for developers"""

    for file in Path("../data/developers").iterdir():
        dev = Developer.model_validate(read_file(file))
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
        org = Organization.model_validate(read_file(file))
        organizatons.append(org.name)

    for file in Path("../data/developers").iterdir():
        dev = Developer.model_validate(read_file(file))
        if dev.organization is not None:
            assert dev.organization in organizatons
