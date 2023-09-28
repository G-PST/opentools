""" Module to test licenses. """
# standard imports
from pathlib import Path
import json

# internal imports
from interface import Licenses


def test_licenses():
    """Test function for licenses. """

    data_path = Path("../data/licenses")
    for file in data_path.iterdir():
        with open(file, "r", encoding="utf-8") as file_pointer:
            file_content = json.load(file_pointer)
        licen = Licenses.model_validate(file_content)

        file_name = file.name.replace(file.suffix, '')

        # Make sure file name is same as developer name
        # it can be case insensitve and ignore spaces
        assert file_name == licen.spdx_id.lower()

        
