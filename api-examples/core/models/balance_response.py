from .basic import *

class Balance(CamelModel):
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


class BalanceResponse(CamelModel):
    total_count: int
    results : list[Balance]

class BalanceOutput(CamelModel):
    blockchain: str
    validator_address: str
    timestamp: str
    block_height: int
    total_staked_native: float
    total_staked_fiat: float
    status: str
