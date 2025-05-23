from pydantic import BaseModel
from .basic import *
from .enums import *

class StatelessAssetBalanceChild(CamelModel):
    wallet_identifier: str
    state: BalanceState
    original_amount: str | float
    amount: Optional[str] = None
    asset_identifier: Optional[str] = None
    symbol: Optional[str] = None

class Extras(CamelModel):
    validator_address: Optional[str]

class StatelessPosition(CamelModel):
    wallet_identifier: str
    display_name: str
    platform: Platform
    position_type: PositionType
    block_number: int | None
    children: list[StatelessAssetBalanceChild]
    extras: Extras | None = None

class StatelessAssetDetails(CamelModel):
    decimals: int
    symbol: str