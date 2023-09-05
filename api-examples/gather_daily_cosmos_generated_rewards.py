from core.graphql_functions import *
from data.demo import *
from datetime import datetime
from core.models import *
from core.csv import *

def parse_output(sbxs: list[SubTransaction]):
    output = []
    for sbx in sbxs:
        output.append(
            GeneratedRewardsReportOutput(
                blockchain=sbx.platform,
                address=sbx.belongs_to.identifier,
                date=sbx.timestamp.date(),
                generated_rewards=sbx.amount * sbx.balance_factor if sbx.type == 'REWARD' else 0,
                generated_commission=sbx.amount * sbx.balance_factor if sbx.type == 'COMMISSION' else 0,
                tags=sbx.belongs_to.tags,
                action=sbx.tx.classification.action,
                asset=sbx.asset.symbol,
                hash=sbx.tx.identifier,
                validator=sbx.sender.identifier
            )
        )

    return output
def main():

    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 9, 1)
    platform = "cosmos"
    sub_transactions = get_all_sub_transactions(
        graphql_client, start_date, end_date, platform, ["STAKING REWARDS", "ACCRUED STAKING REWARDS"]
    )
    res = SubTransactionResponse(
        results=sub_transactions,
        total_count=len(sub_transactions)
    )

    output = parse_output(res.results)
    write_output(output)

if __name__ == "__main__":
    main()