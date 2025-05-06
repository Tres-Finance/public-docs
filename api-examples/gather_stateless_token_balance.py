from core.graphql_functions import *
from data.stateless_demo import *
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
PLATFORM = "SOLANA"
WAELLET_IDENTIFIER = "25mYnjJ2MXHZH6NvTTdA63JvjgRVcuiaj6MRiEQNs1Dq"
START_DATE = datetime(2025, 1, 28)
END_DATE = datetime(2025, 1, 31)

output = []

def handle_balance(graphql_client, balance_to_test: str, start_date: datetime):
    res = get_stateless_balances(graphql_client, [WAELLET_IDENTIFIER], PLATFORM, start_date, balance_to_test)
    for balance in res:
        balance = balance.dict()
        balance["date"] = start_date.isoformat()
        balance["asset_identifier"] = balance_to_test
        output.append(balance)
        print(json.dumps(balance))
        with open("output.txt", "w") as f:
            f.write(json.dumps(output))
    if not res:
        with open("missing_balances.txt", "a") as f:
            f.write(balance_to_test + "\n")
    print(start_date)

def date_range(start_date: datetime, end_date: datetime):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def main():

    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )

    _executor = ThreadPoolExecutor(max_workers=1)
    for date in date_range(START_DATE, END_DATE):
        for balance_to_test in BALANCE_IDENTIFIERS_TO_TEST:
            _executor.submit(handle_balance, graphql_client=graphql_client,
            balance_to_test=balance_to_test,
            start_date=date
        )

if __name__ == "__main__":
    main()