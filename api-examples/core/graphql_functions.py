import json
from .graphqlclient import GraphQLClient
from .graphql_queries import *
import logging
from typing import Optional
from datetime import datetime, timedelta
from .models.stateless_response import StatelessPosition, StatelessAssetBalanceChild
from .models.transaction_response import SubTransaction
from .models.basic import InternalAccount

def get_graphql_client(
    client_id: str | None = None,
    client_secret: str | None = None,
    access_token: str | None = None
) -> GraphQLClient:

    graphql_client = GraphQLClient(endpoint="https://api.prod.tres.finance/graphql")
    if not access_token:
        access_token = get_access_token(graphql_client, client_id, client_secret)
    
    graphql_client.inject_token(f'Bearer {access_token}', 'Authorization')

    logging.info(f"GraphQL client created with access token: {access_token}")
    
    return graphql_client

def execute_grahpql_query(
    graphql_client: GraphQLClient,
    query: str,
    variables: dict
) -> dict:
    logging.info(f"\n\nExecuting query: {query}")
    logging.info(f"Executing variables: {json.dumps(variables)}")
    data = json.loads(graphql_client.execute(query=query, variables=variables))
    logging.info(f"Got response: {json.dumps(data)}\n\n")
    return data

def get_access_token(
    graphql_client: GraphQLClient,
    client_id: str,
    client_secret: str
) -> str:
    
    variables = dict(
        clientId=client_id,
        clientSecret=client_secret
    )

    return execute_grahpql_query(
        graphql_client, LOGIN_MUTATION, variables
    )["data"]["getApiKey"]["token"]["access_token"]

def set_internal_account_tags(
    graphql_client: GraphQLClient,
    identifier: str,
    parent_platform: str,
    tags: list
):
    variables = dict(
        identifier=identifier,
        parentPlatform=parent_platform,
        tags=tags
    )
    response = execute_grahpql_query(
        graphql_client, SET_INTERNAL_ACCOUNT_TAGS_MUTATION, variables
    )["data"]["setInternalAccountTags"]["internalAccount"]
    return response

def create_wallet(
    graphql_client: GraphQLClient,
    name: str,
    parent_platform: str,
    identifier: str,
):
    variables = dict(
        name=name,
        parentPlatform=parent_platform,
        identifier=identifier
    )
    response = execute_grahpql_query(
        graphql_client, CREATE_WALLET_MUTATION, variables
    )["data"]["updateInternalAccount"]["internalAccount"]
    return response

def get_internal_wallets(
    graphql_client: GraphQLClient,
):
    variables = dict()
    response = execute_grahpql_query(
        graphql_client, GET_INTERNAL_WALLETS_QUERY, variables
    )["data"]["internalAccount"]
    return [InternalAccount.parse_obj(ia) for ia in response["results"]]

def trigger_commit(
    graphql_client: GraphQLClient
):
    response = execute_grahpql_query(
        graphql_client, TRIGGER_COMMITMENT_MUTATION, {}
    )["data"]["triggerCommit"]
    return response

def get_latests_commits(
    graphql_client: GraphQLClient,
):
    variables = dict(
        limit=100,
        offset=0
    )
    response = execute_grahpql_query(
        graphql_client, GET_LATESTS_COMMITS_QUERY, variables
    )["data"]["collectAudit"]
    return response

def get_balances(
    graphql_client: GraphQLClient,
    state: str = None,
    limit: int = 100,
    offset: int = 0,
    include_pending: bool = False,
    parent_balance_isnull: bool = False
):
    variables = dict(
        limit=limit,
        offset=offset,
        parentBalance_Isnull=parent_balance_isnull,
        state=state,
        includePending=include_pending
    )
    response = execute_grahpql_query(
        graphql_client, ASSET_BALACE_QUERY, variables
    )["data"]["assetBalance"]
    return response

def get_claimable_rewards(
    graphql_client: GraphQLClient,
):
    variables = dict(
        limit=100,
        offset=0,
        state="claimable", # We want to get only claimable rewards
        parentBalance_Isnull=False # We want to get child balances
    )
    response = execute_grahpql_query(
        graphql_client, ASSET_BALACE_QUERY, variables
    )["data"]["assetBalance"]
    return response

def get_transactions_data_in_org_context(
    graphql_client: GraphQLClient,
    start_date: datetime = None,
    end_date: datetime = None,
    activity: str = None
):
    variables = dict(
        limit=100,
        offset=0,
        classification_Activity=activity,
        timestamp_Gt=start_date.isoformat() if start_date else None,
        timestamp_Lt=end_date.isoformat() if end_date else None,
    )
    response = execute_grahpql_query(
        graphql_client, TRANSACTIONS_DATA_QUERY, variables
    )["data"]["transaction"]
    return response

def get_sub_transactions_data_in_account_context(
    graphql_client: GraphQLClient,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    activities: Optional[list[str]] = None,
    tags: Optional[list[str]] = None,
    identifiers: Optional[list[str]] = None,
    senders: Optional[list[str]] = None,
    recipients: Optional[list[str]] = None,
    platforms: Optional[list[str]] = None,
    asset_identifiers: Optional[list[str]] = None,
    offset: int = 0,
    limit: int = 100
):
    variables = dict(
        limit=limit,
        offset=offset,
        tx_Classification_Activity_In=activities if activities else None,
        timestamp_Gt=start_date.isoformat() if start_date else None,
        timestamp_Lt=end_date.isoformat() if end_date else None,
        tags_Overlap=tags if tags else None,
        belongsTo_Identifier_In=identifiers if identifiers else None,
        sender_Identifier_In=senders if senders else None,
        recipient_Identifier_In=recipients if recipients else None,
        platform_In=platforms if platforms else None,
        asset_Identifier_In=asset_identifiers if asset_identifiers else None,
    )
    response = execute_grahpql_query(
        graphql_client, SUB_TRANSACTIONS_DATA_QUERY, variables
    )["data"]["subTransaction"]
    return response


def get_stateless_positions(
    graphql_client: GraphQLClient,
    wallet_identifiers: list[str],
    platform: str,
    application: str = None,
    timestamp: datetime = None
) -> list[StatelessPosition]:
    variables = dict(
        walletIdentifiers=wallet_identifiers,
        platform=platform,
        application=application,
        timestamp=timestamp.isoformat() if timestamp else None
    )
    response = execute_grahpql_query(
        graphql_client, GET_STATELESS_POSITIONS_QUEEY, variables
    )["data"]["getStatelessWalletsPositions"]
    return [StatelessPosition.parse_obj(position) for position in response if position["children"]]


def get_stateless_balances(
    graphql_client: GraphQLClient,
    wallet_identifiers: list[str],
    platform: str,
    timestamp: datetime = None,
    asset_identifier: str = None
) -> list[StatelessAssetBalanceChild]:
    variables = dict(
        walletIdentifiers=wallet_identifiers,
        platform=platform,
        assetIdentifier=asset_identifier,
        timestamp=timestamp.isoformat().replace("+00:00", "") if timestamp else None
    )
    response = execute_grahpql_query(
        graphql_client, GET_STATELESS_BALANCES_QUERY, variables
    )["data"]["getStatelessTokenBalance"]["results"]
    return [StatelessAssetBalanceChild.parse_obj(balance) for balance in response]


def get_all_sub_transactions(graphql_client, start_date: datetime, end_date: datetime, platform: str, activities: list[str] | None, identifiers: list[str] | None = None):
    sub_transactions = []
    offset = 0
    while True:
        sub_transactions += get_sub_transactions_data_in_account_context(
            graphql_client,
            start_date=start_date,
            end_date=end_date,
            activities=activities if activities else None,
            platforms=[platform],
            identifiers=identifiers if identifiers else None,
            offset=offset
        )["results"]

        offset += 100
        if len(sub_transactions) < offset:
            break

    return [SubTransaction.parse_obj(sub_transaction) for sub_transaction in sub_transactions]
