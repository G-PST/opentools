""" This module contains all the interfaces for data models used."""

# standard imports
from typing import Optional, List

# third-party imports
from pydantic import BaseModel


class ProgrammingLanguage(BaseModel):
    """Interface for programming language."""

    name: str
    description: Optional[str] = None


class Licenses(BaseModel):
    """Interface for opensource licenses."""

    name: str
    spdx_id: str


class Organization(BaseModel):
    """Interface for organization."""

    name: str
    description: Optional[str] = None
    url: Optional[str] = None


class Developer(BaseModel):
    """Interface for developer/contributor."""

    name: str
    email: Optional[str]  = None
    organization: Optional[str]  = None


class SoftwareTool(BaseModel):
    """ Interface for software tool. """
    name: str 
    language: str | List[str]
    developer: str | List[str]
    license: str | List[str]
    description: Optional[str] = None
