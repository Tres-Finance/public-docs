from pydantic import BaseModel
from typing import Optional
from .enums import *
from datetime import datetime
from .basic import *

class StakingPositionMonitoringOutput(BaseModel):
    hash: Optional[str] =  None
    delegator_address: str
    position_name: Optional[str] = None
    platform: Optional[Platform] = None
    timestamp: Optional[datetime] = None
    block_number: Optional[int] = None
    token_symbol: str
    token_amount: float
    state: BalanceState

class BalanceOutput(CamelModel):
    blockchain: str
    validator_address: str
    timestamp: str
    block_number: int
    total_staked_native: float
    total_staked_fiat: float
    status: str

class InternalAccountOutput(CamelModel):
    platforms: list[str]
    total_fiat_value: float
    name: str
    tags: list[str]
    description: str
    identifier: str
    parent_platform: str