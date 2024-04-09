from core.graphql_functions import *
from data.stateless_demo import *
from core.models import *
from core.csv import *
from datetime import datetime, timedelta
POLYGON_POS_CONTRACTS = ["0x5e3ef299fddf15eaa0432e6e66473ace8c13d908"]
POLYOGN_APPLICATION = "polygon-staking"

def get_withdrawals(graphql_client, start_date: datetime, end_date: datetime, delegators: list[str], contracts: list[str]):
    sub_transactions = []
    offset = 0
    while True:
        try:
            sub_transactions += get_sub_transactions_data_in_account_context(
                graphql_client,
                start_date=start_date,
                end_date=end_date,
                senders=contracts,
                identifiers=delegators,
                offset=offset
            ).get("results", [])
            offset += 100
            if len(sub_transactions) < offset:
                break
        except Exception as e:
            print(e)
            import pdb; pdb.set_trace()

    return [parse_sbx_to_event(SubTransaction.parse_obj(sub_transaction), BalanceState.WITHDRAWN) for sub_transaction in sub_transactions]


def get_deposits(graphql_client, start_date: datetime, end_date: datetime, delegators: list[str], contracts: list[str]):
    sub_transactions = []
    offset = 0
    while True:
        sub_transactions += get_sub_transactions_data_in_account_context(
            graphql_client,
            start_date=start_date,
            end_date=end_date,
            recipients=contracts,
            identifiers=delegators,
            offset=offset
        )["results"]
        offset += 100
        if len(sub_transactions) < offset:
            break

    return [parse_sbx_to_event(SubTransaction.parse_obj(sub_transaction), BalanceState.DEPOSITED) for sub_transaction in sub_transactions]


def parse_sbx_to_event(subtx: SubTransaction, state: BalanceState) -> StakingPositionMonitoringOutput:
    return StakingPositionMonitoringOutput(
        delegator_address=subtx.belongs_to.identifier,
        position_name=state,
        platform=subtx.platform,
        timestamp=subtx.timestamp,
        block_number=subtx.tx.block_number,
        token_symbol=subtx.asset.symbol,
        token_amount=float(subtx.amount),
        state=state,
        hash=subtx.tx.identifier
    )

def parse_position_to_event(position: StatelessPosition, delegator: str, timestamp: datetime) ->  list[StakingPositionMonitoringOutput]:
    res: list[StakingPositionMonitoringOutput] = []
    for child in position.children:
        res.append(StakingPositionMonitoringOutput(
            delegator_address=delegator,
            position_name=position.display_name,
            platform=position.platform,
            timestamp=timestamp,
            block_number=position.block_number,
            token_symbol=child.symbol,
            token_amount=float(child.amount),
            state=child.state
        ))

    return res

def get_polygon_position(graphql_client, delegator: str, timestamp: datetime) -> list[StatelessPosition]:
    return get_stateless_positions(
        graphql_client=graphql_client,
        wallet_identifiers=[delegator],
        platform="ETHEREUM",
        application=POLYOGN_APPLICATION,
        timestamp=timestamp
    )

def get_number_of_days(start_date: datetime, end_date: datetime) -> int:
    return (end_date - start_date).days

def main():

    # Login
    graphql_client = get_graphql_client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN)
    
    days = get_number_of_days(POLYGON_START_DATE, POLYGON_END_DATE)

    output: list[StakingPositionMonitoringOutput] = []

    for index in range(days + 1):
        date_to_test = POLYGON_START_DATE + timedelta(days=index)
        for delegator in POLYGON_DELEGATORS:
            positions = get_polygon_position(graphql_client, delegator, date_to_test)
            for position in positions:
                output.extend(parse_position_to_event(position, delegator, date_to_test))

    sbxs: list[StakingPositionMonitoringOutput] = get_withdrawals(graphql_client, POLYGON_START_DATE, POLYGON_END_DATE, POLYGON_DELEGATORS, POLYGON_POS_CONTRACTS)
    sbxs.extend(get_deposits(graphql_client, POLYGON_START_DATE, POLYGON_END_DATE, POLYGON_DELEGATORS, POLYGON_POS_CONTRACTS))
    output.extend(sbxs)

    checked_delegators_dates = set()
    # We want to get state 1m before the withdrawal / deposit
    for sbx in sbxs:
        if (sbx.delegator_address, sbx.timestamp) in checked_delegators_dates:
            continue

        date_to_test = sbx.timestamp - timedelta(minutes=1)
        positions = get_polygon_position(graphql_client, sbx.delegator_address, date_to_test)
        for position in positions:
            output.extend(parse_position_to_event(position, sbx.delegator_address, date_to_test))

        checked_delegators_dates.add((sbx.delegator_address, sbx.timestamp))

    for delegator in POLYGON_DELEGATORS:
        for state in [BalanceState.WITHDRAWN, BalanceState.DEPOSITED]:
            output.append(
                StakingPositionMonitoringOutput(
                    delegator_address=delegator,
                    state=state,
                    token_symbol="MATIC",
                    token_amount=0
                )
            )
    write_output(output)

if __name__ == "__main__":
    main()