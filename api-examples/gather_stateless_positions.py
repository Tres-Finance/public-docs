from core.graphql_functions import *
from data.stateless_demo import *
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor
from retry import retry
import json

# @retry(tries=3, delay=30)
def get_position(graphql_client: GraphQLClient, position_to_test: dict, start_date: datetime) -> list[StatelessPosition]:
    res =  get_stateless_positions(graphql_client=graphql_client,
        wallet_identifiers=position_to_test["wallet_identifiers"],
        platform=position_to_test["platform"],
        application=position_to_test.get("application"),
        timestamp=start_date
    )
    return res

output = []

def handle_position(graphql_client, position_to_test: dict, start_date: datetime):
    res = get_position(graphql_client, position_to_test, start_date)
    for position in res:
        for child in position.children:
            child = child.dict()
            child["date"] = start_date.isoformat()
            child["tag"] = position_to_test.get("tag")
            child["display_name"] = position.display_name
            child["validator"] = position.extras.validator_address
            output.append(child)
            print(json.dumps(child))
            with open("output.txt", "w") as f:
                f.write(json.dumps(output))
    print(start_date)
    

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
    for position_to_test in POSITIONS_TO_TEST:
        start_date = datetime(2024, 3, 1, tzinfo=timezone.utc)
        while start_date <= datetime(2024, 4, 1, tzinfo=timezone.utc):
            futures.append(_executor.submit(handle_position, graphql_client, position_to_test, start_date))
            start_date += timedelta(days=1)

    for future in futures:
        future.result()


if __name__ == "__main__":
    main()