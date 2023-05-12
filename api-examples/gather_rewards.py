from core.graphql_functions import *
from data.demo import *
from datetime import datetime

def main():

    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    
    # # Get Internal Accounts
    get_internal_wallets(graphql_client)

    # # Create Internal Account
    for wallet in WALLETS_TO_CREATE:
        create_wallet(
            graphql_client,
            name=wallet['name'],
            parent_platform=wallet['parent_platform'],
            identifier=wallet['identifier']
        )

    # # Set Internal Account Tags
    set_internal_account_tags(
        graphql_client,
        WALLETS_TO_CREATE[0]["identifier"],
        WALLETS_TO_CREATE[0]["parent_platform"],
        ["test", "test2"]
    )
    
    # # Trigger Commit
    trigger_commit(graphql_client)

    # # Get Last Commits
    get_latests_commits(graphql_client)
    
    # # Get Asset Balances
    get_balances(graphql_client)

    # # Get Asset Balance (only Accured Rewards)
    get_claimable_rewards(graphql_client) # Also know as unavailable rewards
    
    # # Get Collected Rewards Transactions In Org Context
    get_transactions_data_in_org_context(
        graphql_client,
        start_date=datetime(2023, 1, 1),
        activity="STAKING REWARDS"
    )

    # Get Collected Rewards In Account Context By Identifier
    get_sub_transactions_data_in_account_context(
        graphql_client,
        start_date = datetime(2022, 1, 1),
        end_date= datetime(2023, 1, 31),
        activity="STAKING REWARDS",
        identifiers=[WALLETS_TO_CREATE[0]["identifier"]]
    )

    # Get Collected Rewards In Account Context By Tag
    get_sub_transactions_data_in_account_context(
        graphql_client,
        start_date = datetime(2023, 1, 1),
        end_date= datetime(2023, 1, 31),
        activity="STAKING REWARDS",
        tags=["test"]
    )

    # Get Polkadot Collected Rewards Data In Account Context By Tag & Validator
    get_sub_transactions_data_in_account_context(
        graphql_client,
        start_date = datetime(2023, 1, 1),
        end_date= datetime(2023, 1, 31),
        activity="STAKING REWARDS",
        tags=["POLKADOT 1"],
        senders=["14wFkAiTSxhUUdpkN37QMhZv6dYcURJVgSGwqDRd4TK2qhrL"],
        platforms=["polkadot"]
    )

if __name__ == "__main__":
    main()