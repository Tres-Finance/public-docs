from datetime import datetime, UTC
POSITIONS_TO_TEST = [
    dict(platform="NEAR", wallet_identifiers=["continue.poolv1.near"]),
    dict(platform="COSMOS", wallet_identifiers=["cosmos13nvnv6q8d3yg7tjeahjzljkqu0y27s8yqd2guk", "cosmos1c4k24jzduc365kywrsvf5ujz4ya6mwymy8vq4q"]),
    dict(platform="CELO", wallet_identifiers=["0xdadbd6cfb29b054adc9c4c2ef0f21f0bbdb44871","0x971f723194796dbF04DcFe361ED584CaE9bf94A0"]),
    dict(platform="ETHEREUM2", wallet_identifiers=["0xa86ab2d8c2d43ae5f83573f924b3b8b4e0f8594f5823e0245fa150155840d91265c60e549a34492363132e8eb96b5519"]),
    dict(platform="POLKADOT", wallet_identifiers=["1h9DxxTwWFDrKJgG9mEbdLqVJTnbs5H67Tfo6RLromTpjcr"]),
    dict(platform="FLOW", wallet_identifiers=["0x02aef436ae96cec3", "0xf5224874d6729085"]),
    dict(platform="SUI", wallet_identifiers=["0xa62197444b71ba63354ab65518c692ad4777179285a7150e4dc62f7b34415e1c"]),
    dict(platform="EVMOS", wallet_identifiers=["evmos1h62qm8qcctvcdd8t3jwm9jcc9cwleqjg77uwze"]),
    dict(platform="CARDANO", wallet_identifiers=["pool1dqzprrl8305mlysnh85znqpe22lg0q2d9zest7jjhugajuf46kv"]),
    dict(platform="ETHEREUM", wallet_identifiers=["0xda43d85b8d419a9c51bbf0089c9bd5169c23f2f9", "0x971f723194796dbF04DcFe361ED584CaE9bf94A0"], application="livepeer"),
    dict(platform="ETHEREUM", wallet_identifiers=["0xd87a811d823da10761c27d324d4d462b07052ea9", "0x997ff3cddd8d7d80c8cde23c6665a41eb9425a28", "0x971f723194796dbF04DcFe361ED584CaE9bf94A0"], application="polygon-staking"),
    dict(platform="EVMOS", wallet_identifiers=["evmos1h62qm8qcctvcdd8t3jwm9jcc9cwleqjg77uwze"]),
]

POLYGON_DELEGATORS: list[str] = [
    "0x997ff3cddd8d7d80c8cde23c6665a41eb9425a28"
]

POLYGON_START_DATE = datetime(2023, 4, 1, tzinfo=UTC)
POLYGON_END_DATE = datetime(2023, 5, 1, tzinfo=UTC)
CLIENT_ID = ""
CLIENT_SECRET = ""
ACCESS_TOKEN = ""