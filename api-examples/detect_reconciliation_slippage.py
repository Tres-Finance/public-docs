from core.graphql_functions import *
from data.stateless_demo import *
from core.models import *
from core.csv import *
from datetime import datetime, timedelta, timezone

WALLET_IDENTIFIER = ""
ASSET_IDENTIFIER = "native"
PLATFROM = Platform.ETHEREUM
START_DATE = datetime(year=2023, month=1, day=1, tzinfo=timezone.utc)
END_DATE = datetime(year=2023, month=6, day=1, tzinfo=timezone.utc)

def get_transactions(graphql_client, start_date: datetime, end_date: datetime, asset_identifier: str, wallet_identifier: str, platform: Platform):
    sub_transactions = []
    offset = 0
    while True:
        sub_transactions += get_sub_transactions_data_in_account_context(
            graphql_client,
            start_date=start_date,
            end_date=end_date,
            asset_identifiers=[asset_identifier],
            identifiers=[wallet_identifier],
            platforms=[platform],
            offset=offset
        )["results"]
        offset += 100
        if len(sub_transactions) < offset:
            break
    return sub_transactions

def get_historical_balance(graphql_client, platform: Platform, wallet_identifier: str, asset_identifier: str, timestamp: datetime) -> list[StatelessAssetBalanceChild]:
    return get_stateless_balances(
        graphql_client=graphql_client,
        asset_identifier=asset_identifier,
        wallet_identifiers=[wallet_identifier],
        platform=platform.name,
        timestamp=timestamp
    )

def main():

    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        access_token=ACCESS_TOKEN
    )

    sbxs = get_transactions(
        graphql_client, START_DATE, END_DATE,
        ASSET_IDENTIFIER, WALLET_IDENTIFIER, PLATFROM
    )

    for sbx in sbxs:
        balance = get_historical_balance(
            graphql_client, PLATFROM, WALLET_IDENTIFIER, ASSET_IDENTIFIER, datetime.fromisoformat(sbx["timestamp"])
        )[0]
        
        diff = float(balance.amount) - sbx["internalAccountRunningBalanceAfter"]
        if diff > 0.1:
            print(sbx["timestamp"], sbx["tx"]["identifier"], sbx["internalAccountRunningBalanceAfter"], diff, balance.amount)

if __name__ == "__main__":
    main()