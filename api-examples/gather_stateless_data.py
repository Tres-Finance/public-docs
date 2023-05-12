from core.graphql_functions import *
from data.stateless_demo import *
from datetime import datetime

def main():

    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    
    for position_to_test in POSITIONS_TO_TEST:
        print(get_stateless_positions(
            graphql_client=graphql_client,
            wallet_identifiers=position_to_test["wallet_identifiers"],
            platform=position_to_test["platform"],
            application=position_to_test.get("application")
        ))

if __name__ == "__main__":
    main()