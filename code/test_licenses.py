""" Module to test licenses. """
# standard imports
from pathlib import Path

# internal imports
from interface import Licenses
from util import read_file


def test_licenses():
    """Test function for licenses."""

    for file in Path("../data/licenses").iterdir():
        licen = Licenses.model_validate(read_file(file))
        file_name = file.name.replace(file.suffix, "")

        # Make sure file name is same as developer name
        # it can be case insensitve and ignore spaces
        assert file_name == licen.spdx_id.lower()
