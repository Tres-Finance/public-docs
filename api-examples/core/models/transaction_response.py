from pydantic import BaseModel
from functools import cached_property
from pydantic import root_validator
from datetime import datetime
from datetime import date as datetype
from .basic import *
from .enums import *

class Classification(CamelModel):
    action: str
    activity: str
class Transaction(CamelModel):
    identifier: str
    classification: Optional[Classification] = None
    timestamp: Optional[datetime]
    method_id: Optional[str] = None
    platform: Optional[str] = None
    block_number: Optional[int] = None

class SubTransaction(CamelModel):
    id: str
    balance_impact: Optional[float] = None
    amount: float
    balance_factor: int
    timestamp: datetime
    type: Optional[str] = None
    belongs_to: InternalAccount
    sender: Account
    recipient: Account
    asset: Optional[Asset] = None
    tx: Transaction
    platform: Optional[Platform] = None

    @root_validator
    def compute_balance_impact(cls, values):
        balance_impact = values["balance_factor"] * values["amount"]
        values["balance_impact"] = balance_impact
        return values

class SubTransactionResponse(CamelModel):
    total_count: int
    results: list[SubTransaction]

class GeneratedRewardsReportOutput(CamelModel):
    blockchain: Optional[str] = None
    address: str
    date: Optional[datetype] = None
    generated_rewards: float
    generated_commission: float
    action: str
    tags: Optional[list[str]] = []
    asset: str
    hash: str
    validator: str

    
