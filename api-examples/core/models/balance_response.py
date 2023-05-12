from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from .basic import *

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Balance:
    name: str
    id: str
    created_at: str
    amount: float
    state: str
    belongs_to: InternalAccount
    asset: Asset
    fiat_value: FiatValue
    block_height: int
    status: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BalanceResponse:
    total_count: int
    results : list[Balance]

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BalanceOutput:
    blockchain: str
    validator_address: str
    timestamp: str
    block_height: int
    total_staked_native: float
    total_staked_fiat: float
    status: str
