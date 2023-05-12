from core.graphql_functions import *
from data.demo import *
from core.models import *
from core.csv import *
import dataclasses
def parse_output(balances: list[Balance]):
    output = []
    for balance in balances:
        output.append(
            BalanceOutput(
                blockchain=balance.asset.platform,
                validator_address=balance.belongs_to.identifier,
                timestamp=balance.created_at,
                block_height=balance.block_height,
                total_staked_native=balance.amount,
                total_staked_fiat=balance.fiat_value.value,
                status=balance.status
            )
        )

    return output

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
    
    # # Trigger Commit
    trigger_commit(graphql_client)

    # # Get Last Commits
    get_latests_commits(graphql_client)

    # # Get Balances which are under delegation / delegated to the validator
    res = get_balances(graphql_client, "delegated_to_account", include_pending=True)
    res = BalanceResponse.from_dict(res)
    output = parse_output(res.results)
    write_output(output)

if __name__ == "__main__":
    main()