LOGIN_MUTATION = """mutation LoginMutation($clientId: String!, $clientSecret: String!) {
        getApiKey(clientId: $clientId, clientSecret: $clientSecret) {
            token
        }
    }"""

CREATE_WALLET_MUTATION = """mutation CreateWalletMutation(
        $name: String!,
        $parentPlatform: String!,
        $identifier: String!,
        $enforceCollectTransactions: Boolean
    ) {
    updateInternalAccount(
        name: $name,
        parentPlatform: $parentPlatform,
        identifier: $identifier,
        enforceCollectTransactions: $enforceCollectTransactions
        ) {
            internalAccount {
                identifier
            }
        }
    }"""

GET_INTERNAL_WALLETS_QUERY = """query GetAccountById($limit: Int, $offset: Int) {
    internalAccount(
        limit: $limit
        offset: $offset
    ) {
        totalCount
        results {
            name
            identifier
            platforms
            parentPlatform
            totalFiatValue
            tags
        }
    }
}"""

TRIGGER_COMMITMENT_MUTATION = """mutation TriggerCommit {
    triggerCommit {
        status
        message
    }
}"""

GET_LATESTS_COMMITS_QUERY = """query GetLastSuccessCommit($status: String, $offset: Int, $limit: Int) {
    collectAudit(status: $status, offset: $offset, limit: $limit) {
        results {
            commitId
            createdAt
            status
            updatedAt
            progress
            numOfTransactionsCreated
        }
    }
}"""

ASSET_BALACE_QUERY = """query AssetBalanceQuery($includePending: Boolean, $limit: Int, $offset: Int, $currency: String, $internalAccount: String, $parentBalance_Isnull: Boolean, $asset_Name_Icontains: String, $state: String) {
    assetBalance(includePending: $includePending, limit: $limit, offset: $offset, currency: $currency, belongsTo_Identifier: $internalAccount, parentBalance_Isnull: $parentBalance_Isnull,
    asset_Name_Icontains: $asset_Name_Icontains, state: $state) {
        totalCount
        results {
        name
        id
        createdAt
        asset {
            symbol
            name
            platform
        }
        amount   
        state
        status
        blockNumber
        belongsTo {
            identifier
            name
            tags
        }
        childBalances {
            asset {
                symbol
            }
            state
            amount
        }
        fiatValue {
            value
            fiatCurrency
        }
        }
    }
}"""

TRANSACTIONS_DATA_QUERY = """
query readTxsQuery($limit: Int, $offset: Int,
    $classification_Activity: String, $identifier_In: [String],
    $timestamp_Gt: DateTime, $timestamp_Lt: DateTime,
    $children_Recipient_Identifier_In: [String]) {
  transaction(
    limit: $limit
    offset: $offset
    classification_Activity: $classification_Activity
    identifier_In: $identifier_In
    timestamp_Gt: $timestamp_Gt
    timestamp_Lt: $timestamp_Lt
    children_Recipient_Identifier_In: $children_Recipient_Identifier_In
    
  ) {
    results {
      id
      success
      timestamp
      children {
          asset {
              symbol
          }
          amount
          balanceFactor
      }
      identifier
      platform
      classification {
        action
        activity
        action
      }
    }
  }
}"""

TRANSACTIONS_STATS_QUERY = """query readTxsQuery($limit: Int, $offset: Int, $classification_Activity: String, $identifier_In: [String], $timestamp_Gt: DateTime, $timestamp_Lt: DateTime) {
  transaction(
    limit: $limit
    offset: $offset
    classification_Activity: $classification_Activity
    identifier_In: $identifier_In
    timestamp_Gt: $timestamp_Gt
    timestamp_Lt: $timestamp_Lt
  ) {
      stats
    }
}"""

SET_INTERNAL_ACCOUNT_TAGS_MUTATION = """
mutation MyMutation(
    $tags: [String]!,
    $parentPlatform: String!,
    $identifier: String!,
) {
  setInternalAccountTags(
      parentPlatform: $parentPlatform,
      identifier: $identifier,
      tags: $tags
    ) {
    internalAccount {
      identifier
      tags
    }
  }
}
"""

GET_STATELESS_POSITIONS_MUTATION = """
mutation MyMutation($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
      results {
        walletIdentifier
        displayName
        blockNumber
        platform
        positionType
        children {
            amount
            originalAmount
            walletIdentifier
            assetIdentifier
            state
            symbol
        }
      }
  }
}
"""

GET_STATELESS_BALANCES_MUTATION = """
mutation MyMutation($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $assetIdentifier: String!) {
  getStatelessTokenBalance(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, assetIdentifier: $assetIdentifier) {
      results {
        amount
        originalAmount
        walletIdentifier
        state
      }
  }
}
"""

SUB_TRANSACTIONS_DATA_QUERY = """
query GetSubTxs(
    $asset_Identifier_In: [String]
    $limit: Int, $offset: Int, $belongsTo_Identifier_In: [String], $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $tags_Overlap: [String],
    $sender_Identifier_In: [String], $platform_In: [String], $tx_Classification_Activity_In: [String], $recipient_Identifier_In: [String]
) {
 subTransaction(
    limit: $limit, offset: $offset, belongsTo_Identifier_In: $belongsTo_Identifier_In, recipient_Identifier_In: $recipient_Identifier_In,
    timestamp_Gt: $timestamp_Gt, tags_Overlap: $tags_Overlap, sender_Identifier_In: $sender_Identifier_In, timestamp_Lt: $timestamp_Lt,
    platform_In: $platform_In, tx_Classification_Activity_In: $tx_Classification_Activity_In, asset_Identifier_In: $asset_Identifier_In) {
   totalCount
   results {
    amount
    balanceFactor
    id
    type
    timestamp
    belongsTo {
        identifier
    }
    asset {
        symbol
    }
    tx {
        identifier
        blockNumber
        methodId
    }
    recipient {
        identifier
    }
    sender {
        identifier
    }
   }
 }
}
"""