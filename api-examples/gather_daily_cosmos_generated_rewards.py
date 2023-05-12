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
                hash=sbx.tx.identifier
            )
        )

    return output

def get_all_sub_transactions(graphql_client, start_date: datetime, end_date: datetime, platform: str):
    sub_transactions = []
    offset = 0
    while True:
        sub_transactions += get_sub_transactions_data_in_account_context(
            graphql_client,
            start_date=start_date,
            end_date=end_date,
            activities=["STAKING REWARDS", "ACCRUED STAKING REWARDS"],
            platforms=[platform],
            offset=offset
        )["results"]
        offset += 100
        if len(sub_transactions) < offset:
            break

    return [SubTransaction.from_dict(sub_transaction) for sub_transaction in sub_transactions]

def main():

    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    
    start_date = datetime(2023, 3, 26)
    end_date = datetime(2023, 4, 7)
    platform = "cosmos"
    sub_transactions = get_all_sub_transactions(graphql_client, start_date, end_date, platform)
    res = SubTransactionResponse(
        results=sub_transactions,
        total_count=len(sub_transactions)
    )

    output = parse_output(res.results)
    write_output(output)

if __name__ == "__main__":
    main()