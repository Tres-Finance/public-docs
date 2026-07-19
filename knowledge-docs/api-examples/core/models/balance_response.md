# API example: balance response

Runnable example script `core/models/balance_response.py` from the public-docs repo (api-examples/).

```python
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
    block_number: int
    status: str


class BalanceResponse(CamelModel):
    total_count: int
    results : list[Balance]
```
