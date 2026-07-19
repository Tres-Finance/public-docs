# Tres API — Staking Data

Endpoints in the 'Staking Data' section of the public Tres API collection (7 requests).

## Staking Data Report - By Validator

`POST {{backend}}/graphql`

<h2 id="general-notes">General Notes</h2>
<ol>
<li><p>The Staking Data Report endpoint provides data for the staking yields based on the given parameters.</p>
</li>
<li><p>The yields are divided into rewards and commissions. Rewards are generated from delegation operations, while commissions are earned from validation activities.</p>
</li>
<li><p>You can query the data divided by validator or get a summary of the overall data.</p>
</li>
</ol>
<h3 id="schemas-explanation">Schemas Explanation</h3>
<ol>
<li><p><strong>StakingData</strong>: This schema represents the overall staking data report and contains two main sections:</p>
<ul>
<li><p><strong>summary</strong>: Provides a summary of staking data by type.</p>
</li>
<li><p><strong>byValidator</strong>: Breaks down staking data by individual validators.</p>
</li>
</ul>
</li>
<li><p><strong>StakingDataByType</strong>: This schema represents staking data categorized by reward type. It contains two main lists:</p>
<ul>
<li><p><strong>reward</strong>: List of staking data entries representing rewards.</p>
</li>
<li><p><strong>commission</strong>: List of staking data entries representing commissions. Note that this field is optional and may not be supported for all platforms.</p>
</li>
</ul>
</li>
<li><p><strong>StakingDataEntry</strong>: This schema represents individual staking data entries. Each entry contains information such as:</p>
<ul>
<li><p><strong>start</strong>: The start datetime for the staking data entry.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data entry.</p>
</li>
<li><p><strong>generatedRewards</strong>: The total rewards generated during the specified period.</p>
</li>
<li><p><strong>locked</strong>: The amount of staked tokens that are currently locked.</p>
</li>
<li><p><strong>claimable</strong>: The amount of rewards that are claimable.</p>
</li>
<li><p><strong>apr</strong>: The annual percentage rate (APR) of staking rewards.</p>
</li>
<li><p><strong>stakingLedger</strong>: A list of sub-transactions representing staking activities.</p>
</li>
<li><p><strong>validatorIdentifier</strong>: The identifier of the validator (if applicable).</p>
</li>
<li><p><strong>rewardType</strong>: The type of reward received, which can be one of the following options:</p>
<ul>
<li><p><strong>REGULAR</strong>: Regular staking rewards.</p>
</li>
<li><p><strong>BLOCK</strong>: Rewards for block production.</p>
</li>
<li><p><strong>CONSENSUS</strong>: Rewards for participating in consensus mechanisms.</p>
</li>
<li><p><strong>MEV</strong>: Rewards from miner extractable value.</p>
</li>
<li><p><strong>EXECUTION_LAYER</strong>: Rewards from execution layer activities.</p>
</li>
</ul>
</li>
</ul>
</li>
</ol>
<h3 id="request-variables-explanation">Request Variables Explanation</h3>
<ul>
<li><p><strong>platform</strong>: The platform (e.g., Ethereum, Cosmos) for which staking data is being queried.</p>
</li>
<li><p><strong>identifier</strong>: The identifier (e.g., address) of the entity (e.g., validator, delegator) for which staking data is being queried.</p>
</li>
<li><p><strong>start</strong>: The start datetime for the staking data report.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data report.</p>
</li>
<li><p><strong>assetIdentifier</strong>: The identifier of the asset for which staking data is being queried (default: the native asset of the platform).</p>
</li>
<li><p><strong>excludeZeroRewards</strong>: A boolean flag indicating whether to exclude entries with zero rewards from the report (default: False).</p>
</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
query Test(
  $platform: Platform!,
  $identifier: String!,
  $start: Date!,
  $end: Date!,
  $assetIdentifier: String
  $excludeZeroRewards: Boolean
  $useDb: Boolean
  $yieldType: StakingYieldType
  $ignoreMissingDataErrors: Boolean
) {
    stakingData(
      platform: $platform,
      identifier: $identifier,
      start: $start,
      end: $end,
      assetIdentifier: $assetIdentifier
      excludeZeroRewards: $excludeZeroRewards,
      yieldType: $yieldType
      useDb: $useDb
      ignoreMissingDataErrors: $ignoreMissingDataErrors
    ) {
      start
      end
      assetIdentifier
      internalAccountName
      internalAccountTags
      identifier
      totalCount
      platform
      data {
      byValidator {
        start
        end
        claimable
        generatedRewards
        locked
        apr
        yieldType
        validatorIdentifier
        unlocking
        createdAt
        updatedAt
        metadata {
            __typename    
            ... on SolanaStakingMetadata   { slotsPerEpoch epochs { epoch commission rewardTx timestamp start end } }
            ... on AvalancheStakingMetadata { rewardPeriods { nodeId rewardType rewardTxHash start end } }
        }
      }
    }
  }
}
```

**Variables:**
```json
{
    "platform":"CARDANO",
    "start":"2025-01-01",
    "end":"2025-01-02",
    "identifier":"addr1vygqp3jeftgjdvvv2qfc5xfcflu5hr33aecwxtm0tcl9yngzfsp7v",
    "yieldType":"REWARD",
    "ignoreMissingDataErrors": true
}
```

**Sample response (200):**
```json
{
    "data": {
        "stakingData": {
            "start": "2024-05-12",
            "end": "2024-05-16",
            "assetIdentifier": "uosmo",
            "internalAccountName": "osmovaloper1q4mlwtw3ncve72na65xacck557wcknc8j0lmke",
            "internalAccountTags": [
                "OSMOSIS VALIDATOR"
            ],
            "identifier": "osmo1q4mlwtw3ncve72na65xacck557wcknc8gchcp7",
            "totalCount": 4,
            "platform": "OSMOSIS",
            "data": {
                "byValidator": [
                    {
                        "start": "2024-05-12T00:00:00",
                        "end": "2024-05-13T00:00:00",
                        "claimable": "3040.925622",
                        "generatedRewards": "62.846892",
                        "locked": "2298474.661468",
                        "apr": "0.998015",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-13T00:00:00",
                        "end": "2024-05-14T00:00:00",
                        "claimable": "3103.772514",
                        "generatedRewards": "69.006121",
                        "locked": "2299059.081288",
                        "apr": "1.095545",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-14T00:00:00",
                        "end": "2024-05-15T00:00:00",
                        "claimable": "3172.778635",
                        "generatedRewards": "69.812247",
                        "locked": "2299430.354248",
                        "apr": "1.108164",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-15T00:00:00",
                  
[TRUNCATED]
```

## Staking Data Report - Aggregated

`POST {{backend}}/graphql`

<h2 id="general-notes">General Notes</h2>
<ol>
<li><p>The Staking Data Report endpoint provides data for the staking yields based on the given parameters.</p>
</li>
<li><p>The yields are divided into rewards and commissions. Rewards are generated from delegation operations, while commissions are earned from validation activities.</p>
</li>
<li><p>You can query the data divided by validator or get a summary of the overall data.</p>
</li>
</ol>
<h3 id="schemas-explanation">Schemas Explanation</h3>
<ol>
<li><p><strong>StakingData</strong>: This schema represents the overall staking data report and contains two main sections:</p>
<ul>
<li><p><strong>summary</strong>: Provides a summary of staking data by type.</p>
</li>
<li><p><strong>byValidator</strong>: Breaks down staking data by individual validators.</p>
</li>
</ul>
</li>
<li><p><strong>StakingDataByType</strong>: This schema represents staking data categorized by reward type. It contains two main lists:</p>
<ul>
<li><p><strong>reward</strong>: List of staking data entries representing rewards.</p>
</li>
<li><p><strong>commission</strong>: List of staking data entries representing commissions. Note that this field is optional and may not be supported for all platforms.</p>
</li>
</ul>
</li>
<li><p><strong>StakingDataEntry</strong>: This schema represents individual staking data entries. Each entry contains information such as:</p>
<ul>
<li><p><strong>start</strong>: The start datetime for the staking data entry.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data entry.</p>
</li>
<li><p><strong>generatedRewards</strong>: The total rewards generated during the specified period.</p>
</li>
<li><p><strong>locked</strong>: The amount of staked tokens that are currently locked.</p>
</li>
<li><p><strong>claimable</strong>: The amount of rewards that are claimable.</p>
</li>
<li><p><strong>apr</strong>: The annual percentage rate (APR) of staking rewards.</p>
</li>
<li><p><strong>stakingLedger</strong>: A list of sub-transactions representing staking activities.</p>
</li>
<li><p><strong>validatorIdentifier</strong>: The identifier of the validator (if applicable).</p>
</li>
<li><p><strong>rewardType</strong>: The type of reward received, which can be one of the following options:</p>
<ul>
<li><p><strong>REGULAR</strong>: Regular staking rewards.</p>
</li>
<li><p><strong>BLOCK</strong>: Rewards for block production.</p>
</li>
<li><p><strong>CONSENSUS</strong>: Rewards for participating in consensus mechanisms.</p>
</li>
<li><p><strong>MEV</strong>: Rewards from miner extractable value.</p>
</li>
<li><p><strong>EXECUTION_LAYER</strong>: Rewards from execution layer activities.</p>
</li>
</ul>
</li>
</ul>
</li>
</ol>
<h3 id="request-variables-explanation">Request Variables Explanation</h3>
<ul>
<li><p><strong>platform</strong>: The platform (e.g., Ethereum, Cosmos) for which staking data is being queried.</p>
</li>
<li><p><strong>identifier</strong>: The identifier (e.g., address) of the entity (e.g., validator, delegator) for which staking data is being queried.</p>
</li>
<li><p><strong>start</strong>: The start datetime for the staking data report.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data report.</p>
</li>
<li><p><strong>assetIdentifier</strong>: The identifier of the asset for which staking data is being queried (default: the native asset of the platform).</p>
</li>
<li><p><strong>excludeZeroRewards</strong>: A boolean flag indicating whether to exclude entries with zero rewards from the report (default: False).</p>
</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
query StakingRewardsByPlatformAssetYieldType(
    $belongsToIdentifier: String!,
    $startDate: Date!,
    $endDate: Date!,
    $currency: String
  ) {
    stakingYieldRecord(
      belongsTo_Identifier: $belongsToIdentifier,
      startDate_Gte: $startDate,
      endDate_Lte: $endDate,
      currency: $currency,
      groupBy: ["platform", "yieldType", "asset_Identifier"],
      aggregations: [
        { field: generatedRewards, function: SUM, alias: "totalGeneratedRewards" },
        { field: generatedRewards, function: COUNT, alias: "recordCount" }
      ]
    ) {
      totalCount
      groupedAggregations {
        groupKey
        results {
          alias
          field
          function
          value
        }
      }
      aggregationPageInfo {
        totalCount
        distinctColumnCount
      }
    }
  }
```

**Variables:**
```json
{
    "belongsToIdentifier": "CyzVd8xyNjUsnPu3ra5fDPW2vja8zXpVbMoEk8hU5n9g",
    "startDate": "2026-01-01",
    "endDate": "2025-01-05"
  }
```

**Sample response (200):**
```json
{
    "data": {
        "stakingData": {
            "start": "2024-05-12",
            "end": "2024-05-16",
            "assetIdentifier": "uosmo",
            "internalAccountName": "osmovaloper1q4mlwtw3ncve72na65xacck557wcknc8j0lmke",
            "internalAccountTags": [
                "OSMOSIS VALIDATOR"
            ],
            "identifier": "osmo1q4mlwtw3ncve72na65xacck557wcknc8gchcp7",
            "totalCount": 4,
            "platform": "OSMOSIS",
            "data": {
                "byValidator": [
                    {
                        "start": "2024-05-12T00:00:00",
                        "end": "2024-05-13T00:00:00",
                        "claimable": "3040.925622",
                        "generatedRewards": "62.846892",
                        "locked": "2298474.661468",
                        "apr": "0.998015",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-13T00:00:00",
                        "end": "2024-05-14T00:00:00",
                        "claimable": "3103.772514",
                        "generatedRewards": "69.006121",
                        "locked": "2299059.081288",
                        "apr": "1.095545",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-14T00:00:00",
                        "end": "2024-05-15T00:00:00",
                        "claimable": "3172.778635",
                        "generatedRewards": "69.812247",
                        "locked": "2299430.354248",
                        "apr": "1.108164",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-15T00:00:00",
                  
[TRUNCATED]
```

## Staking Data Report - Aggregated Copy

`POST {{backend}}/graphql`

<h2 id="general-notes">General Notes</h2>
<ol>
<li><p>The Staking Data Report endpoint provides data for the staking yields based on the given parameters.</p>
</li>
<li><p>The yields are divided into rewards and commissions. Rewards are generated from delegation operations, while commissions are earned from validation activities.</p>
</li>
<li><p>You can query the data divided by validator or get a summary of the overall data.</p>
</li>
</ol>
<h3 id="schemas-explanation">Schemas Explanation</h3>
<ol>
<li><p><strong>StakingData</strong>: This schema represents the overall staking data report and contains two main sections:</p>
<ul>
<li><p><strong>summary</strong>: Provides a summary of staking data by type.</p>
</li>
<li><p><strong>byValidator</strong>: Breaks down staking data by individual validators.</p>
</li>
</ul>
</li>
<li><p><strong>StakingDataByType</strong>: This schema represents staking data categorized by reward type. It contains two main lists:</p>
<ul>
<li><p><strong>reward</strong>: List of staking data entries representing rewards.</p>
</li>
<li><p><strong>commission</strong>: List of staking data entries representing commissions. Note that this field is optional and may not be supported for all platforms.</p>
</li>
</ul>
</li>
<li><p><strong>StakingDataEntry</strong>: This schema represents individual staking data entries. Each entry contains information such as:</p>
<ul>
<li><p><strong>start</strong>: The start datetime for the staking data entry.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data entry.</p>
</li>
<li><p><strong>generatedRewards</strong>: The total rewards generated during the specified period.</p>
</li>
<li><p><strong>locked</strong>: The amount of staked tokens that are currently locked.</p>
</li>
<li><p><strong>claimable</strong>: The amount of rewards that are claimable.</p>
</li>
<li><p><strong>apr</strong>: The annual percentage rate (APR) of staking rewards.</p>
</li>
<li><p><strong>stakingLedger</strong>: A list of sub-transactions representing staking activities.</p>
</li>
<li><p><strong>validatorIdentifier</strong>: The identifier of the validator (if applicable).</p>
</li>
<li><p><strong>rewardType</strong>: The type of reward received, which can be one of the following options:</p>
<ul>
<li><p><strong>REGULAR</strong>: Regular staking rewards.</p>
</li>
<li><p><strong>BLOCK</strong>: Rewards for block production.</p>
</li>
<li><p><strong>CONSENSUS</strong>: Rewards for participating in consensus mechanisms.</p>
</li>
<li><p><strong>MEV</strong>: Rewards from miner extractable value.</p>
</li>
<li><p><strong>EXECUTION_LAYER</strong>: Rewards from execution layer activities.</p>
</li>
</ul>
</li>
</ul>
</li>
</ol>
<h3 id="request-variables-explanation">Request Variables Explanation</h3>
<ul>
<li><p><strong>platform</strong>: The platform (e.g., Ethereum, Cosmos) for which staking data is being queried.</p>
</li>
<li><p><strong>identifier</strong>: The identifier (e.g., address) of the entity (e.g., validator, delegator) for which staking data is being queried.</p>
</li>
<li><p><strong>start</strong>: The start datetime for the staking data report.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data report.</p>
</li>
<li><p><strong>assetIdentifier</strong>: The identifier of the asset for which staking data is being queried (default: the native asset of the platform).</p>
</li>
<li><p><strong>excludeZeroRewards</strong>: A boolean flag indicating whether to exclude entries with zero rewards from the report (default: False).</p>
</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
query {
  stakingYieldRecord(
    belongsTo_Identifier: "4xJkaGHvLZZmrqy4jgmxh4N3EuUCE9y8JDBniA8hqfX9"
    startDate_Gte: "2025-01-01"
    endDate_Lte: "2026-06-23"
    yieldType: "jito_tip"
    groupBy: ["validator_identifier"]
    aggregationLimit: 500     # <= 10000; 500 > 361 so all groups in one page
    aggregationOffset: 0      # advance by aggregationLimit to page if needed
    aggregations: [{ field: generatedRewards, function: SUM, alias: "t" }]
  ) {
    aggregationPageInfo { totalCount }
    groupedAggregations {
      groupKey
      results { alias value }
    }
  }
}
```

**Variables:**
```json
{
    "belongsToIdentifier": "CyzVd8xyNjUsnPu3ra5fDPW2vja8zXpVbMoEk8hU5n9g",
    "startDate": "2026-01-01",
    "endDate": "2025-01-05"
  }
```

**Sample response (200):**
```json
{
    "data": {
        "stakingData": {
            "start": "2024-05-12",
            "end": "2024-05-16",
            "assetIdentifier": "uosmo",
            "internalAccountName": "osmovaloper1q4mlwtw3ncve72na65xacck557wcknc8j0lmke",
            "internalAccountTags": [
                "OSMOSIS VALIDATOR"
            ],
            "identifier": "osmo1q4mlwtw3ncve72na65xacck557wcknc8gchcp7",
            "totalCount": 4,
            "platform": "OSMOSIS",
            "data": {
                "byValidator": [
                    {
                        "start": "2024-05-12T00:00:00",
                        "end": "2024-05-13T00:00:00",
                        "claimable": "3040.925622",
                        "generatedRewards": "62.846892",
                        "locked": "2298474.661468",
                        "apr": "0.998015",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-13T00:00:00",
                        "end": "2024-05-14T00:00:00",
                        "claimable": "3103.772514",
                        "generatedRewards": "69.006121",
                        "locked": "2299059.081288",
                        "apr": "1.095545",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-14T00:00:00",
                        "end": "2024-05-15T00:00:00",
                        "claimable": "3172.778635",
                        "generatedRewards": "69.812247",
                        "locked": "2299430.354248",
                        "apr": "1.108164",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-15T00:00:00",
                  
[TRUNCATED]
```

## Staking Data Report - By Validator Copy

`POST {{backend}}/graphql`

<h2 id="general-notes">General Notes</h2>
<ol>
<li><p>The Staking Data Report endpoint provides data for the staking yields based on the given parameters.</p>
</li>
<li><p>The yields are divided into rewards and commissions. Rewards are generated from delegation operations, while commissions are earned from validation activities.</p>
</li>
<li><p>You can query the data divided by validator or get a summary of the overall data.</p>
</li>
</ol>
<h3 id="schemas-explanation">Schemas Explanation</h3>
<ol>
<li><p><strong>StakingData</strong>: This schema represents the overall staking data report and contains two main sections:</p>
<ul>
<li><p><strong>summary</strong>: Provides a summary of staking data by type.</p>
</li>
<li><p><strong>byValidator</strong>: Breaks down staking data by individual validators.</p>
</li>
</ul>
</li>
<li><p><strong>StakingDataByType</strong>: This schema represents staking data categorized by reward type. It contains two main lists:</p>
<ul>
<li><p><strong>reward</strong>: List of staking data entries representing rewards.</p>
</li>
<li><p><strong>commission</strong>: List of staking data entries representing commissions. Note that this field is optional and may not be supported for all platforms.</p>
</li>
</ul>
</li>
<li><p><strong>StakingDataEntry</strong>: This schema represents individual staking data entries. Each entry contains information such as:</p>
<ul>
<li><p><strong>start</strong>: The start datetime for the staking data entry.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data entry.</p>
</li>
<li><p><strong>generatedRewards</strong>: The total rewards generated during the specified period.</p>
</li>
<li><p><strong>locked</strong>: The amount of staked tokens that are currently locked.</p>
</li>
<li><p><strong>claimable</strong>: The amount of rewards that are claimable.</p>
</li>
<li><p><strong>apr</strong>: The annual percentage rate (APR) of staking rewards.</p>
</li>
<li><p><strong>stakingLedger</strong>: A list of sub-transactions representing staking activities.</p>
</li>
<li><p><strong>validatorIdentifier</strong>: The identifier of the validator (if applicable).</p>
</li>
<li><p><strong>rewardType</strong>: The type of reward received, which can be one of the following options:</p>
<ul>
<li><p><strong>REGULAR</strong>: Regular staking rewards.</p>
</li>
<li><p><strong>BLOCK</strong>: Rewards for block production.</p>
</li>
<li><p><strong>CONSENSUS</strong>: Rewards for participating in consensus mechanisms.</p>
</li>
<li><p><strong>MEV</strong>: Rewards from miner extractable value.</p>
</li>
<li><p><strong>EXECUTION_LAYER</strong>: Rewards from execution layer activities.</p>
</li>
</ul>
</li>
</ul>
</li>
</ol>
<h3 id="request-variables-explanation">Request Variables Explanation</h3>
<ul>
<li><p><strong>platform</strong>: The platform (e.g., Ethereum, Cosmos) for which staking data is being queried.</p>
</li>
<li><p><strong>identifier</strong>: The identifier (e.g., address) of the entity (e.g., validator, delegator) for which staking data is being queried.</p>
</li>
<li><p><strong>start</strong>: The start datetime for the staking data report.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data report.</p>
</li>
<li><p><strong>assetIdentifier</strong>: The identifier of the asset for which staking data is being queried (default: the native asset of the platform).</p>
</li>
<li><p><strong>excludeZeroRewards</strong>: A boolean flag indicating whether to exclude entries with zero rewards from the report (default: False).</p>
</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
query Test(
  $platform: Platform!,
  $identifier: String!,
  $start: Date!,
  $end: Date!,
  $assetIdentifier: String
  $excludeZeroRewards: Boolean
  $useDb: Boolean
  $yieldType: StakingYieldType
  $ignoreMissingDataErrors: Boolean
) {
    stakingData(
      platform: $platform,
      identifier: $identifier,
      start: $start,
      end: $end,
      assetIdentifier: $assetIdentifier
      excludeZeroRewards: $excludeZeroRewards,
      yieldType: $yieldType
      useDb: $useDb
      ignoreMissingDataErrors: $ignoreMissingDataErrors
    ) {
      start
      end
      assetIdentifier
      internalAccountName
      internalAccountTags
      identifier
      totalCount
      platform
      data {
      byValidator {
        start
        end
        claimable
        generatedRewards
        locked
        apr
        yieldType
        validatorIdentifier
        unlocking
        createdAt
        updatedAt
      }
    }
  }
}
```

**Variables:**
```json
{
    "platform":"CARDANO",
    "start":"2025-01-01",
    "end":"2025-01-02",
    "identifier":"addr1vygqp3jeftgjdvvv2qfc5xfcflu5hr33aecwxtm0tcl9yngzfsp7v",
    "yieldType":"REWARD",
    "ignoreMissingDataErrors": true
}
```

**Sample response (200):**
```json
{
    "data": {
        "stakingData": {
            "start": "2024-05-12",
            "end": "2024-05-16",
            "assetIdentifier": "uosmo",
            "internalAccountName": "osmovaloper1q4mlwtw3ncve72na65xacck557wcknc8j0lmke",
            "internalAccountTags": [
                "OSMOSIS VALIDATOR"
            ],
            "identifier": "osmo1q4mlwtw3ncve72na65xacck557wcknc8gchcp7",
            "totalCount": 4,
            "platform": "OSMOSIS",
            "data": {
                "byValidator": [
                    {
                        "start": "2024-05-12T00:00:00",
                        "end": "2024-05-13T00:00:00",
                        "claimable": "3040.925622",
                        "generatedRewards": "62.846892",
                        "locked": "2298474.661468",
                        "apr": "0.998015",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-13T00:00:00",
                        "end": "2024-05-14T00:00:00",
                        "claimable": "3103.772514",
                        "generatedRewards": "69.006121",
                        "locked": "2299059.081288",
                        "apr": "1.095545",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-14T00:00:00",
                        "end": "2024-05-15T00:00:00",
                        "claimable": "3172.778635",
                        "generatedRewards": "69.812247",
                        "locked": "2299430.354248",
                        "apr": "1.108164",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-15T00:00:00",
                  
[TRUNCATED]
```

## Staking Data Report - Total Daily

`POST {{backend}}/graphql`

<h2 id="general-notes">General Notes</h2>
<ol>
<li>The Staking Data Report endpoint provides data for the staking yields based on the given parameters.</li>
<li>The yields are divided into rewards and commissions. Rewards are generated from delegation operations, while commissions are earned from validation activities.</li>
<li>You can query the data divided by validator or get a summary of the overall data.</li>
</ol>
<h3 id="schemas-explanation">Schemas Explanation</h3>
<ol>
<li><strong>StakingData</strong>: This schema represents the overall staking data report and contains two main sections:<ul>
<li><strong>summary</strong>: Provides a summary of staking data by type.</li>
<li><strong>byValidator</strong>: Breaks down staking data by individual validators.</li>
</ul>
</li>
<li><strong>StakingDataByType</strong>: This schema represents staking data categorized by reward type. It contains two main lists:<ul>
<li><strong>reward</strong>: List of staking data entries representing rewards.</li>
<li><strong>commission</strong>: List of staking data entries representing commissions. Note that this field is optional and may not be supported for all platforms.</li>
</ul>
</li>
<li><strong>StakingDataEntry</strong>: This schema represents individual staking data entries. Each entry contains information such as:<ul>
<li><strong>start</strong>: The start datetime for the staking data entry.</li>
<li><strong>end</strong>: The end datetime for the staking data entry.</li>
<li><strong>generatedRewards</strong>: The total rewards generated during the specified period.</li>
<li><strong>locked</strong>: The amount of staked tokens that are currently locked.</li>
<li><strong>claimable</strong>: The amount of rewards that are claimable.</li>
<li><strong>apr</strong>: The annual percentage rate (APR) of staking rewards.</li>
<li><strong>stakingLedger</strong>: A list of sub-transactions representing staking activities.</li>
<li><strong>validatorIdentifier</strong>: The identifier of the validator (if applicable).</li>
<li><strong>rewardType</strong>: The type of reward received, which can be one of the following options:<ul>
<li><strong>REGULAR</strong>: Regular staking rewards.</li>
<li><strong>BLOCK</strong>: Rewards for block production.</li>
<li><strong>CONSENSUS</strong>: Rewards for participating in consensus mechanisms.</li>
<li><strong>MEV</strong>: Rewards from miner extractable value.</li>
<li><strong>EXECUTION_LAYER</strong>: Rewards from execution layer activities.</li>
</ul>
</li>
</ul>
</li>
</ol>
<h3 id="request-variables-explanation">Request Variables Explanation</h3>
<ul>
<li><p><strong>organization</strong>: The organization for which staking data is being queried.</p>
</li>
<li><p><strong>platform</strong>: The platform (e.g., Ethereum, Cosmos) for which staking data is being queried.</p>
</li>
<li><p><strong>identifier</strong>: The identifier (e.g., address) of the entity (e.g., validator, delegator) for which staking data is being queried.</p>
</li>
<li><p><strong>start</strong>: The start datetime for the staking data report.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data report.</p>
</li>
<li><p><strong>assetIdentifier</strong>: The identifier of the asset for which staking data is being queried (default: the native asset of the platform).</p>
</li>
<li><p><strong>excludeZeroRewards</strong>: A boolean flag indicating whether to exclude entries with zero rewards from the report (default: False).</p>
</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
query Test(
  $platform: Platform!,
  $identifier: String!,
  $start: Date!,
  $end: Date!,
  $assetIdentifier: String
  $excludeZeroRewards: Boolean
  $useDb: Boolean
  $yieldType: StakingYieldType
  $ignoreMissingDataErrors: Boolean
) {
    stakingData(
      platform: $platform,
      identifier: $identifier,
      start: $start,
      end: $end,
      assetIdentifier: $assetIdentifier
      excludeZeroRewards: $excludeZeroRewards,
      yieldType: $yieldType
      useDb: $useDb
      ignoreMissingDataErrors: $ignoreMissingDataErrors
    ) {
      start
      end
      assetIdentifier
      internalAccountName
      internalAccountTags
      identifier
      totalCount
      platform
      data {
      summary {
        start
        end
        claimable
        generatedRewards
        locked
        apr
        yieldType
        unlocking
        createdAt
        updatedAt
      }
    }
  }
}
```

**Variables:**
```json
{
  "platform": "SUI",
  "assetIdentifier": "0x2::sui::sui",
  "identifier": "0xa62197444b71ba63354ab65518c692ad4777179285a7150e4dc62f7b34415e1c",
  "start": "2024-05-12",
  "end": "2024-05-16",
  "yieldType": "COMMISSION",
  "ignoreMissingDataErrors": false
}
```

**Sample response (200):**
```json
{
    "data": {
        "stakingData": {
            "start": "2024-05-12",
            "end": "2024-05-16",
            "assetIdentifier": "uosmo",
            "internalAccountName": "osmovaloper1q4mlwtw3ncve72na65xacck557wcknc8j0lmke",
            "internalAccountTags": [
                "OSMOSIS VALIDATOR"
            ],
            "identifier": "osmo1q4mlwtw3ncve72na65xacck557wcknc8gchcp7",
            "totalCount": 4,
            "platform": "OSMOSIS",
            "data": {
                "summary": [
                    {
                        "start": "2024-05-12T00:00:00",
                        "end": "2024-05-13T00:00:00",
                        "claimable": "3040.925622",
                        "generatedRewards": "62.846892",
                        "locked": "2298474.661468",
                        "apr": "0.9980147253548204804568624372",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-13T00:00:00",
                        "end": "2024-05-14T00:00:00",
                        "claimable": "3103.772514",
                        "generatedRewards": "69.006121",
                        "locked": "2299059.081288",
                        "apr": "1.095545319822289050557540132",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
                        "start": "2024-05-14T00:00:00",
                        "end": "2024-05-15T00:00:00",
                        "claimable": "3172.778635",
                        "generatedRewards": "69.812247",
                        "locked": "2299430.354248",
                        "apr": "1.108164468122514491215425786",
                        "yieldType": "COMMISSION",
                        "validatorIdentifier": null
                    },
                    {
              
[TRUNCATED]
```

## Staking Data Report w/ Data Breakdown

`POST {{backend}}/graphql`

<h2 id="general-notes">General Notes</h2>
<ol>
<li>The Staking Data Report endpoint provides data for the staking yields based on the given parameters.</li>
<li>The yields are divided into rewards and commissions. Rewards are generated from delegation operations, while commissions are earned from validation activities.</li>
<li>You can query the data divided by validator or get a summary of the overall data.</li>
</ol>
<h3 id="schemas-explanation">Schemas Explanation</h3>
<ol>
<li><strong>StakingData</strong>: This schema represents the overall staking data report and contains two main sections:<ul>
<li><strong>summary</strong>: Provides a summary of staking data by type.</li>
<li><strong>byValidator</strong>: Breaks down staking data by individual validators.</li>
</ul>
</li>
<li><strong>StakingDataByType</strong>: This schema represents staking data categorized by reward type. It contains two main lists:<ul>
<li><strong>reward</strong>: List of staking data entries representing rewards.</li>
<li><strong>commission</strong>: List of staking data entries representing commissions. Note that this field is optional and may not be supported for all platforms.</li>
</ul>
</li>
<li><strong>StakingDataEntry</strong>: This schema represents individual staking data entries. Each entry contains information such as:<ul>
<li><strong>start</strong>: The start datetime for the staking data entry.</li>
<li><strong>end</strong>: The end datetime for the staking data entry.</li>
<li><strong>generatedRewards</strong>: The total rewards generated during the specified period.</li>
<li><strong>locked</strong>: The amount of staked tokens that are currently locked.</li>
<li><strong>claimable</strong>: The amount of rewards that are claimable.</li>
<li><strong>apr</strong>: The annual percentage rate (APR) of staking rewards.</li>
<li><strong>stakingLedger</strong>: A list of sub-transactions representing staking activities.</li>
<li><strong>validatorIdentifier</strong>: The identifier of the validator (if applicable).</li>
<li><strong>rewardType</strong>: The type of reward received, which can be one of the following options:<ul>
<li><strong>REGULAR</strong>: Regular staking rewards.</li>
<li><strong>BLOCK</strong>: Rewards for block production.</li>
<li><strong>CONSENSUS</strong>: Rewards for participating in consensus mechanisms.</li>
<li><strong>MEV</strong>: Rewards from miner extractable value.</li>
<li><strong>EXECUTION_LAYER</strong>: Rewards from execution layer activities.</li>
</ul>
</li>
</ul>
</li>
</ol>
<h3 id="request-variables-explanation">Request Variables Explanation</h3>
<ul>
<li><p><strong>organization</strong>: The organization for which staking data is being queried.</p>
</li>
<li><p><strong>platform</strong>: The platform (e.g., Ethereum, Cosmos) for which staking data is being queried.</p>
</li>
<li><p><strong>identifier</strong>: The identifier (e.g., address) of the entity (e.g., validator, delegator) for which staking data is being queried.</p>
</li>
<li><p><strong>start</strong>: The start datetime for the staking data report.</p>
</li>
<li><p><strong>end</strong>: The end datetime for the staking data report.</p>
</li>
<li><p><strong>assetIdentifier</strong>: The identifier of the asset for which staking data is being queried (default: the native asset of the platform).</p>
</li>
<li><p><strong>excludeZeroRewards</strong>: A boolean flag indicating whether to exclude entries with zero rewards from the report (default: False).</p>
</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
query Test(
  $platform: Platform!,
  $identifier: String!,
  $start: Date!,
  $end: Date!,
  $assetIdentifier: String
  $excludeZeroRewards: Boolean
  $useDb: Boolean
  $yieldType: StakingYieldType
  $ignoreMissingDataErrors: Boolean
  $roundDecimals: Boolean
) {
    stakingData(
      platform: $platform,
      identifier: $identifier,
      start: $start,
      end: $end,
      assetIdentifier: $assetIdentifier
      excludeZeroRewards: $excludeZeroRewards,
      yieldType: $yieldType
      useDb: $useDb
      roundDecimals: $roundDecimals
      ignoreMissingDataErrors: $ignoreMissingDataErrors
    ) {
      start
      end
      assetIdentifier
      internalAccountName
      identifier
      totalCount
      platform
      data {
      byValidator {
        metadata {
            ... on SolanaStakingMetadata   { slotsPerEpoch epochs { epoch commission rewardTx timestamp start end } }
            ... on AvalancheStakingMetadata { rewardPeriods { nodeId rewardType rewardTxHash start end } }
        }
        start
        end
        claimable
        generatedRewards
        locked
        unlocking
        apr
        yieldType
        validatorIdentifier
        stakingLedger {
            originalRecipient {
                identifier
            }
            tx {
                identifier
                methodId
            }
            amount
            balanceFactor
        }
      }
    }
  }
}
```

**Variables:**
```json
{
    "platform":"SOLANA",
    "start":"2026-06-01",
    "end":"2026-06-05",
    "identifier":"3f892jCZzS5o53621v6dhEtyArXbuXTiq8xbjgcN3C1N",
    "assetIdentifier": "native",
    "yieldType":"REWARD",
    "roundDecimals": false
}
```

**Sample response (200):**
```json
{
    "data": {
        "stakingData": {
            "start": "2024-07-01",
            "end": "2024-07-24",
            "assetIdentifier": "native",
            "internalAccountName": "d8e9f36be65aa12b37706a2f54130652194074d7c5d462d6f91506b819f00433",
            "internalAccountTags": [
                "DELEGATOR"
            ],
            "identifier": "d8e9f36be65aa12b37706a2f54130652194074d7c5d462d6f91506b819f00433",
            "totalCount": 23,
            "platform": "NEAR",
            "data": {
                "byValidator": [
                    {
                        "start": "2024-07-01T00:00:00",
                        "end": "2024-07-02T00:00:00",
                        "claimable": "0",
                        "generatedRewards": "241.62734",
                        "locked": "881367.22464",
                        "apr": "10.006496",
                        "yieldType": "REWARD",
                        "validatorIdentifier": "aca87218e28c41f5a693dee3dff12238.poolv1.near",
                        "stakingLedger": [
                            {
                                "timestamp": "2024-07-02T00:00:00+00:00",
                                "tx": {
                                    "methodId": "accrued_rewards",
                                    "classification": {
                                        "action": "near-staking-total-position-balance-diff-aca87218e28c41f5a693dee3dff12238.poolv1.near"
                                    },
                                    "identifier": "not-available-2024-07-01 00:00:00+00:00-2024-07-02 00:00:00+00:00"
                                },
                                "amount": "241.6273400957689307963128",
                                "balanceFactor": 1,
                                "recipient": {
                                    "identifier": "d8e9f36be65aa12b37706a2f54130652194074d7c5d462d6f91506b819f00433"
                                }
                           
[TRUNCATED]
```

## Staking Yield Options

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query Test($resolveStatus: Boolean){
   stakingYieldOptions(resolveStatus: $resolveStatus){
    platform
    yieldType
    assetOptions {
        asset {
            name
            identifier
        }
        internalAccountOptions {
            internalAccount {
                name
                id
                identifier
            }
            earliest
            latest
            status
        }
    }
  }
  }
```

**Variables:**
```json
{
    "resolveStatus": true
}
```

**Sample response (200):**
```json
{
    "data": {
        "stakingYieldOptions": [
            {
                "platform": "DYDX",
                "yieldType": "COMMISSION",
                "assetOptions": [
                    {
                        "asset": {
                            "name": "dYdX",
                            "identifier": "adydx",
                            "symbol": "DYDX"
                        },
                        "internalAccountOptions": [
                            {
                                "internalAccount": {
                                    "name": "Dydx Chain Wallet",
                                    "identifier": "dydx16pj5gljqnqs0ajxakccfjhu05yczp9870tkh0z"
                                },
                                "earliest": "2023-10-26",
                                "latest": "2024-07-01"
                            }
                        ]
                    },
                    {
                        "asset": {
                            "name": "uusdc",
                            "identifier": "uusdc",
                            "symbol": "USDC"
                        },
                        "internalAccountOptions": [
                            {
                                "internalAccount": {
                                    "name": "Dydx Chain Wallet",
                                    "identifier": "dydx16pj5gljqnqs0ajxakccfjhu05yczp9870tkh0z"
                                },
                                "earliest": "2023-10-26",
                                "latest": "2024-03-18"
                            }
                        ]
                    }
                ]
            },
            {
                "platform": "DYDX",
                "yieldType": "REWARD",
                "assetOptions": [
                    {
                        "asset": {
                            "name": "dYdX",
                            "identifier": "adydx",
                      
[TRUNCATED]
```

**Sample response (200):**
```json
{
    "data": {
        "stakingYieldOptions": [
            {
                "platform": "KAVA",
                "yieldType": "REWARD",
                "assetOptions": [
                    {
                        "asset": {
                            "name": "Kava",
                            "identifier": "ukava"
                        },
                        "internalAccountOptions": [
                            {
                                "internalAccount": {
                                    "name": "CDC - month - 19jwaj",
                                    "id": 495380,
                                    "identifier": "kava19jwajksrajg7w6072fy7euy96nkjnayflrzkpz"
                                },
                                "earliest": "2024-03-01",
                                "latest": "2024-08-27"
                            }
                        ]
                    }
                ]
            },
            {
                "platform": "DYDX",
                "yieldType": "REWARD",
                "assetOptions": [
                    {
                        "asset": {
                            "name": "dYdX",
                            "identifier": "adydx"
                        },
                        "internalAccountOptions": [
                            {
                                "internalAccount": {
                                    "name": "DYDX-EC - 12xvq2",
                                    "id": 462522,
                                    "identifier": "dydx12xvq20j56kz6vzhwphxm97mupga40fmvj54306"
                                },
                                "earliest": "2023-12-10",
                                "latest": "2024-08-27"
                            },
                            {
                                "internalAccount": {
                                    "name": "PN - month - 1yp9ev",
                                    "id": 462523,
                 
[TRUNCATED]
```
