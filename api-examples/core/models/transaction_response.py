from dataclasses import dataclass, field
from datetime import datetime
from .basic import *
from .enums import *

class Classification(CamelModel):
    action: str
    activity: str
class Transaction(CamelModel):
    identifier: str
    classification: Classification
    timestamp: Optional[datetime]
    platform: Optional[str] = None
    block_number: Optional[int] = None

class SubTransaction(CamelModel):
    amount: float
    balance_factor: int
    timestamp: datetime
    type: str
    belongs_to: InternalAccount
    sender: Account
    recipient: Account
    asset: Asset
    tx: Transaction
    platform: Platform

class SubTransactionResponse(CamelModel):
    total_count: int
    results: list[SubTransaction]

class GeneratedRewardsReportOutput(CamelModel):
    blockchain: str
    address: str
    date: datetime
    generated_rewards: float
    generated_commission: float
    action: str
    tags: list[str]
    asset: str
    hash: str

    
