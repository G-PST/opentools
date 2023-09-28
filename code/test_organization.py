""" Module to test organizations. """
# standard imports
from pathlib import Path 
import json

# internal imports
from interface import Organization

def test_organization():
    """ Test function for organizations. """

    data_path = Path('../data/organizations')
    for file in data_path.iterdir():

        with open(file, "r", encoding="utf-8") as file_pointer:
            file_content = json.load(file_pointer)
        org = Organization.model_validate(file_content)

        file_name = file.name.replace(file.suffix, '')

        # Make sure file name is same as developer name
        # it can be case insensitve and ignore spaces
        assert file_name == org.name.lower() or \
            file_name == org.name.lower().replace(' ', '')