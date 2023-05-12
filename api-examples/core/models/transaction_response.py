from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase
from datetime import datetime
from .basic import *

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Classification:
    action: str
    activity: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Transaction:
    identifier: str
    classification: Classification
    timestamp: Optional[datetime] = field(metadata=iso_datetime_config, default=None)
    platform: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SubTransaction:
    amount: float
    balance_factor: int
    timestamp: datetime = field(metadata=iso_datetime_config)
    type: str
    belongs_to: InternalAccount
    sender: Account
    recipient: Account
    asset: Asset
    tx: Transaction
    platform: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SubTransactionResponse:
    total_count: int
    results: list[SubTransaction]

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GeneratedRewardsReportOutput:
    blockchain: str
    address: str
    date: datetime
    generated_rewards: float
    generated_commission: float
    action: str
    tags: list[str]
    asset: str
    hash: str

    
