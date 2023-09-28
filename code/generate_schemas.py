""" Module for generating schemas frpm pydantic models. """

# standard imports
from pathlib import Path
from typing import List

# third-party imports
from pydantic import BaseModel
import pydantic

# internal imports
from interface import (
    ProgrammingLanguage,
    Licenses,
    Developer,
    Organization,
    SoftwareTool,
)
from util import read_file, write_file

# pylint:disable=missing-class-docstring
# pylint:disable=missing-function-docstring


class SchemaItemModel(BaseModel):
    """Interface for schema item."""

    name: str
    model: pydantic._internal._model_construction.ModelMetaclass

    class Config:
        arbitrary_types_allowed = True


class SchemaManager:
    def __init__(self, schema_folder: str = ".vscode"):
        self.schema_folder = Path(schema_folder)
        self.schemas: List[SchemaItemModel] = []

    def add_schema(self, name: str, model: BaseModel):
        self.schemas.append(SchemaItemModel(name=name, model=model))

    def generate_and_save_schemas(self):
        if not self.schema_folder.exists():
            self.schema_folder.mkdir()

        for schema in self.schemas:
            json_schema = schema.model.model_json_schema()
            schema_file = self.schema_folder / f"{schema.name}.json"
            write_file(json_schema, schema_file)

if __name__ == "__main__":

    schema_manager = SchemaManager(schema_folder="../schemas")
    schema_manager.add_schema("programming_languages", ProgrammingLanguage)
    schema_manager.add_schema("licenses", Licenses)
    schema_manager.add_schema("developers", Developer)
    schema_manager.add_schema("software_tool", SoftwareTool)
    schema_manager.add_schema("organization", Organization)
    schema_manager.generate_and_save_schemas()