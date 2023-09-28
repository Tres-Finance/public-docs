from core.graphql_functions import *
from data.demo import *
from core.models import *
from core.csv import *
import dataclasses
def parse_output(internal_accounts: list[InternalAccount]):
    output = []
    for ia in internal_accounts:
        output.append(
            InternalAccountOutput(
                name=ia.name or ia.identifier,
                platforms=ia.platforms or [],
                identifier=ia.identifier,
                parent_platform=ia.parent_platform or "",
                tags=ia.tags or [],
                total_fiat_value=ia.totalFiatValue or 0,
                description=ia.description or ""
            )
        )
    return output

def main():
    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    )
    
    # # Get Internal Accounts
    internal_accounts = get_internal_wallets(graphql_client)
    output = parse_output(internal_accounts)
    write_output(output)

if __name__ == "__main__":
    main()