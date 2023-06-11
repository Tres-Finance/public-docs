from pydantic import BaseModel
from .basic import *
from .enums import *

class StatelessAssetBalanceChild(CamelModel):
    wallet_identifier: str
    state: BalanceState
    original_amount: str
    amount: str
    asset_identifier: Optional[str] = None
    symbol: Optional[str] = None

class StatelessPosition(CamelModel):
    wallet_identifier: str
    display_name: str
    platform: Platform
    position_type: PositionType
    block_number: int | None
    children: list[StatelessAssetBalanceChild]

class StatelessAssetDetails(CamelModel):
    decimals: int
    symbol: str