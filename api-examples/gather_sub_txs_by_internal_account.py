from core.graphql_functions import *
from data.stateless_demo import *
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor
from retry import retry
import json
from core.csv.csv import write_output

belongs_to_identifiers = [
    "ADDRESS"
]

def get_sub_txs(graphql_client: GraphQLClient, tx_identifiers: list[str]) -> list[SubTransaction]:
    res =  get_sub_transactions_data_in_account_context(graphql_client=graphql_client,
            limit=10000, belongs_to_identifiers=belongs_to_identifiers
    )
    return res

output = []

identifiers = [
]

def main():

    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        access_token=ACCESS_TOKEN
    )
    # _executor = ThreadPoolExecutor(max_workers=10)
    _executor = ThreadPoolExecutor(max_workers=1)
    futures = []
    futures.append(_executor.submit(get_sub_txs, graphql_client, identifiers))
    res = futures[0].result()
    write_output(res["results"])


if __name__ == "__main__":
    main()