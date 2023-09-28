""" Module to test languages. """
# standard imports
from pathlib import Path 
import json

# internal imports
from interface import ProgrammingLanguage

def test_languages():
    """ Test function for programming languages. """

    data_path = Path('../data/languages')
    for file in data_path.iterdir():

        with open(file, "r", encoding="utf-8") as file_pointer:
            file_content = json.load(file_pointer)
        lang = ProgrammingLanguage.model_validate(file_content)

        file_name = file.name.replace(file.suffix, '')

        # Make sure file name is same as developer name
        # it can be case insensitve and ignore spaces
        assert file_name == lang.name.lower() or \
            file_name == lang.name.lower().replace(' ', '')