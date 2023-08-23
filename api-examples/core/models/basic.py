from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import StrEnum

from pydantic import BaseModel
from humps import camelize

def to_camel(string):
    return camelize(string)


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class FiatValue(CamelModel):
    value: float
    fiat_currency: str

class InternalAccount(CamelModel):
    identifier: str
    name: Optional[str] = None
    tags: Optional[list[str]] = None

class Account(CamelModel):
    identifier: str
    platform: Optional[str] = None

class Asset(CamelModel):
    symbol: Optional[str] = None
    name: Optional[str] = None
    platform: Optional[str] = None