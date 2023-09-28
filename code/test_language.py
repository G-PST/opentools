""" Module to test languages. """
# standard imports
from pathlib import Path

# internal imports
from interface import ProgrammingLanguage
from util import read_file


def test_languages():
    """Test function for programming languages."""

    for file in Path("../data/languages").iterdir():
        lang = ProgrammingLanguage.model_validate(read_file(file))
        file_name = file.name.replace(file.suffix, "")

        # Make sure file name is same as developer name
        # it can be case insensitve and ignore spaces
        assert file_name == lang.name.lower() or file_name == lang.name.lower().replace(
            " ", ""
        )
