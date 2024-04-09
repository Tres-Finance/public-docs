from core.graphql_functions import *
from data.stateless_demo import *
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor
from retry import retry
import json
from pydantic import BaseModel
from csv import DictReader
FILE_PATH = "/tmp/input.csv"

class RowInput(BaseModel):
    status: str
    side: str
    cp: str
    size: str
    pair: str
    trader: str
    buy_sell: str
    price: float
    size_ccy: str
    conf: str
    notional_usd: float
    size_base: float
    size_quote: float
    ClOrdID: str
    datetime: datetime

def read_csv(file_path: str) -> list[RowInput]:
    rows = []
    data = open(FILE_PATH, "r").readlines()
    reader = DictReader(data)
    # Read CSV File into list of dictionaries, each dictionary represents a row
    for line in reader:
        rows.append(RowInput.parse_obj(line))

    return rows

def main():
    rows = read_csv(FILE_PATH)
    
    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        access_token=ACCESS_TOKEN
    )
    
    for row in rows:
        # Create Transaction Frame
        tx = create_manual_transaction(
            graphql_client,
            row.ClOrdID,
            row.datetime,
            Platform.MANUAL
        )
        tx_id = tx.get("id") # We want to hold the TRES Internal Transaction ID

        # For each transaction, we creating two sub transactions
        pairs = row.pair.split("/")
        create_manual_sub_transaction(
            graphql_client,
            tx_id,
            row.size_base,
            Currency.USD,
            row.notional_usd,
            pairs[0],
            INTERNAL_ACCOUNT_ID,
            Direction.INFLOW,
            "0" # This ID of the transfer itself
        )

        create_manual_sub_transaction(
            graphql_client,
            tx_id,
            row.size_quote,
            Currency.USD,
            row.notional_usd,
            pairs[1],
            INTERNAL_ACCOUNT_ID,
            Direction.OUTFLOW,
            "1" # This ID of the transfer itself
        )


if __name__ == "__main__":
    main()