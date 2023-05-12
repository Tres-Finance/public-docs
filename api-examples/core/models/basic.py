from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase
from datetime import datetime
from dataclasses_json import config
from dateutil.parser import parse
from pytz import UTC
from typing import Optional

class StringSerializer:
    @staticmethod
    def decode(date_string: Optional[str]) -> Optional[datetime]:
        return parse(date_string) if date_string else None

    @staticmethod
    def encode(date: Optional[datetime], str_format: str) -> Optional[str]:
        return date.strftime(str_format) if date else None


class ISOSerializer(StringSerializer):
    @staticmethod
    def encode(date: Optional[datetime], str_format='') -> Optional[str]:
        return datetime.isoformat(date) if date else None

iso_datetime_config = config(decoder=ISOSerializer.decode, encoder=ISOSerializer.encode)

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FiatValue:
    value: float
    fiat_currency: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class InternalAccount:
    identifier: str
    name: Optional[str] = None
    tags: Optional[list[str]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Account:
    identifier: str
    platform: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Asset:
    symbol: str
    name: str
    platform: Optional[str] = None
