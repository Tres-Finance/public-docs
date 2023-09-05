from pydantic import BaseModel
from typing import Optional
from .enums import *
from datetime import datetime
class StakingPositionMonitoringOutput(BaseModel):
    hash: Optional[str] =  None
    delegator_address: str
    position_name: str
    platform: Optional[Platform] = None
    timestamp: datetime
    block_number: Optional[int] = None
    token_symbol: str
    token_amount: float
    state: BalanceState

