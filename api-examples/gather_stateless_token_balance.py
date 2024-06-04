from core.graphql_functions import *
from data.stateless_demo import *
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def main():

    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    
    _executor = ThreadPoolExecutor(max_workers=10)
    for position_to_test in POSITIONS_TO_TEST:
        _executor.submit(get_stateless_positions, graphql_client=graphql_client,
            wallet_identifiers=position_to_test["wallet_identifiers"],
            platform=position_to_test["platform"],
            application=position_to_test.get("application")
        )

if __name__ == "__main__":
    main()