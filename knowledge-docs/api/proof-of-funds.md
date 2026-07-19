# Tres API — Proof of Funds

Endpoints in the 'Proof of Funds' section of the public Tres API collection (14 requests).

## Aggregate Account Balances

`POST {{backend}}/pof/account-balances`

**Auth:** bearer

**Request body:**
```json
{
  "pipeline": [
    {
      "$match": {
        "$expr": {
          "$eq": [
            "$timestamp",
            {
              "$dateFromString": {
                "dateString": "2026-04-01T00:00:00.000+00:00"
              }
            }
          ]
        },
        "network": "bitcoin"
      }
    }
  ]
}
```

## Find Account Balances

`POST {{backend}}/pof/find-account-balances`

<p>Fetches raw account-balance snapshots for an organization.<br />All body fields are optional.</p>
<hr />
<h2 id="example-request-body">Example Request Body</h2>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code class="language-json">{
  "accountAddress": "WALLET_ADDRESS", // Use "accountAddress" or "accountAddresses"
  "accountAddresses": [
    "WALLET_ADDRESS_1",
    "WALLET_ADDRESS_2"
  ],
  "networks": ["ethereum", "bitcoin"],
  "timestamps": ["2026-06-01T00:00:00.000Z", "2026-06-02T00:00:00.000Z"], // Use "timestamps" or "startDate"/"endDate"
  "startDate": "2026-06-01T00:00:00.000Z",
  "endDate": "2026-06-08T23:59:59.999Z",
  "tokenAddresses": [
    "0x0000000000000000000000000000000000000000",
    "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
  ],
  "symbols": ["ETH", "USDC"],
  "sources": ["fireblocks", "coinbase"],
  "sourceOriginIds": ["vault-123", "vault-456"],
  "sourceAddressNames": ["Treasury Wallet", "Ops Wallet"],
  "limit": 100,
  "offset": 0
}

</code></pre>
<hr />
<h2 id="field-reference">Field Reference</h2>
<div class="click-to-expand-wrapper is-table-wrapper"><table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>accountAddress</code></td>
<td><code>string</code></td>
<td>Match a single wallet address (exact match).</td>
</tr>
<tr>
<td><code>accountAddresses</code></td>
<td><code>string[]</code></td>
<td>Match any wallet in the list.</td>
</tr>
<tr>
<td><code>networks</code></td>
<td><code>string[]</code></td>
<td>Filter by chain. Use standardized lowercase names (<code>"ethereum"</code>, <code>"bitcoin"</code>, <code>"solana"</code>, …).</td>
</tr>
<tr>
<td><code>timestamps</code></td>
<td><code>Date[]</code> (ISO string or epoch ms)</td>
<td>Match exact snapshot timestamps.</td>
</tr>
<tr>
<td><code>startDate</code></td>
<td><code>Date</code></td>
<td>Start of a timestamp range.</td>
</tr>
<tr>
<td><code>endDate</code></td>
<td><code>Date</code></td>
<td>End of a timestamp range.</td>
</tr>
<tr>
<td><code>tokenAddresses</code></td>
<td><code>string[]</code></td>
<td>Keep only token entries whose <code>tokenAddress</code> is in the list.</td>
</tr>
<tr>
<td><code>symbols</code></td>
<td><code>string[]</code></td>
<td>Keep only token entries whose <code>symbol</code> is in the list.</td>
</tr>
<tr>
<td><code>sources</code></td>
<td><code>string[]</code></td>
<td>Filter by data source / custodian integration.</td>
</tr>
<tr>
<td><code>sourceOriginIds</code></td>
<td><code>string[]</code></td>
<td>Filter by source-side origin id (e.g. vault id).</td>
</tr>
<tr>
<td><code>sourceAddressNames</code></td>
<td><code>string[]</code></td>
<td>Filter by human-readable address name.</td>
</tr>
<tr>
<td><code>limit</code></td>
<td><code>number</code></td>
<td>Page size. Default <code>1000</code>, intended ceiling <code>20000</code>.</td>
</tr>
<tr>
<td><code>offset</code></td>
<td><code>number</code></td>
<td>Number of documents to skip. Default <code>0</code>.</td>
</tr>
</tbody>
</table>
</div><hr />
<h2 id="important-combination-rules--gotchas">Important Combination Rules &amp; Gotchas</h2>
<p>These matter because some fields <strong>override</strong> each other rather than narrowing together:</p>
<p><strong><code>accountAddresses</code></strong> <strong>overrides</strong> <strong><code>accountAddress</code>****.</strong><br />Both write to the same <code>accountAddress</code> match key, and <code>accountAddresses</code> is applied second. Use one or the other.</p>
<p><strong><code>startDate</code><strong><strong>/</strong></strong><code>endDate</code></strong> <strong>override</strong> <strong><code>timestamps</code>****.</strong><br />Don't mix exact timestamps with a date range - pick one strategy:</p>
<ul>
<li><p>Exact snapshots → use <code>timestamps</code></p>
</li>
<li><p>A time window → use <code>startDate</code> + <code>endDate</code></p>
</li>
</ul>
<p><strong><code>tokenAddresses</code></strong> <strong>+</strong> <strong><code>symbols</code></strong> <strong>are AND-ed at the token level.</strong><br />When both are present, a balance entry inside a document must match both (its <code>tokenAddress</code> is in <code>tokenAddresses</code> <strong>and</strong> its <code>symbol</code> is in <code>symbols</code>) to be kept. They filter the inner <code>balances[]</code> array, not which documents are returned — a document with no matching tokens is still returned, but with an empty <code>balances</code> array.</p>
<p><strong>Token filters reshape, they don't drop documents.</strong><br /><code>tokenAddresses</code>/<code>symbols</code> only trim each document's <code>balances[]</code>. To restrict which accounts/networks come back, use <code>accountAddresses</code>/<code>networks</code>.</p>

**Auth:** bearer

**Request body:**
```json
{
    "accountAddresses": ["WALLET_ADDRESS"],
    "startDate": "2026-01-01T00:00:00.000Z",
    "endDate": "2026-06-01T00:00:00.000Z"
}
```

## Aggregated Token Balances

`POST {{backend}}/pof/aggregated-token-balances`

<p>Returns token balances aggregated across your accounts, per snapshot date. You can optionally roll them up (sum) by network, symbol, or source.</p>
<h2 id="field-reference">Field reference</h2>
<div class="click-to-expand-wrapper is-table-wrapper"><table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>networks</code></td>
<td>string[]</td>
<td>Only include balances on these chains. Use lowercase names (<code>"ethereum"</code>, <code>"bitcoin"</code>, <code>"solana"</code>, …).</td>
</tr>
<tr>
<td><code>symbols</code></td>
<td>string[]</td>
<td>Only include these token symbols (e.g. <code>"ETH"</code>, <code>"USDC"</code>).</td>
</tr>
<tr>
<td><code>timestamps</code></td>
<td>string[] (ISO date or epoch ms)</td>
<td>Return balances for these exact snapshot dates. Mutually exclusive with <code>startDate</code>/<code>endDate</code>.</td>
</tr>
<tr>
<td><code>startDate</code></td>
<td>string</td>
<td>Start of a date range (inclusive). Mutually exclusive with <code>timestamps</code>.</td>
</tr>
<tr>
<td><code>endDate</code></td>
<td>string</td>
<td>End of a date range (inclusive). Mutually exclusive with <code>timestamps</code>.</td>
</tr>
<tr>
<td><code>sources</code></td>
<td>string[]</td>
<td>Only include balances from these sources/custodians (e.g. <code>"fireblocks"</code>).</td>
</tr>
<tr>
<td><code>limit</code></td>
<td>number</td>
<td>Max number of results to return. Default 1000, maximum 20000 (exceeding it is rejected).</td>
</tr>
<tr>
<td><code>offset</code></td>
<td>number</td>
<td>Number of results to skip, for paging. Default 0.</td>
</tr>
<tr>
<td><code>groupBy</code></td>
<td>network / symbol / source</td>
<td>"symbol"</td>
</tr>
</tbody>
</table>
</div><h2 id="time-selector--pick-one">Time selector — pick one</h2>
<p>A typical request using a date range:</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code class="language-json">{
  "startDate": "2026-06-01T00:00:00.000Z",
  "endDate": "2026-06-08T23:59:59.999Z"
}

</code></pre>
<p>Or specific snapshot dates:</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code class="language-json">{
  "timestamps": ["2026-06-01T00:00:00.000Z", "2026-06-02T00:00:00.000Z"]
}

</code></pre>
<h2 id="whats-required-vs-optional">What's required vs optional</h2>
<p>Almost all fields are optional — include only the filters you need. The one requirement is a time selector: you must provide either <code>timestamps</code> or a date range (<code>startDate</code> / <code>endDate</code>), but not both.</p>
<ul>
<li><p>Provide both → request is rejected (<code>Cannot provide both timestamps and startDate/endDate</code>).</p>
</li>
<li><p>Provide neither → request is rejected (<code>Must provide either timestamps or startDate/endDate</code>).</p>
</li>
</ul>
<h2 id="example-request-body-all-possible-fields">Example request body (all possible fields)</h2>
<blockquote>
<p>In a real request pick <strong>one</strong> time selector — either <code>timestamps</code> or <code>startDate</code>/<code>endDate</code> — not both. </p>
</blockquote>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code class="language-json">{
  "networks": ["ethereum", "bitcoin"],
  "symbols": ["ETH", "USDC", "BTC"],
  "timestamps": ["2026-06-01T00:00:00.000Z"],
  "startDate": "2026-06-01T00:00:00.000Z",
  "endDate": "2026-06-08T23:59:59.999Z",
  "sources": ["fireblocks", "coinbase"],
  "limit": 1000,
  "offset": 0,
  "groupBy": "symbol"
}

</code></pre>
<h2 id="notes-on-groupby">Notes on groupBy</h2>
<ul>
<li><p>Without <code>groupBy</code> you get one entry per token holding (network + symbol + source).</p>
</li>
<li><p>With <code>groupBy</code> (e.g. <code>"symbol"</code>) entries with the same group value on the same date are summed into a single total — useful for "total USDC per day" style views.</p>
</li>
</ul>
<h2 id="example-response-no-groupby">Example response (no groupBy)</h2>
<p>Amounts are returned as strings to preserve precision.</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code class="language-json">{
  "results": [
    {
      "network": "ethereum",
      "symbol": "USDC",
      "tokenAddress": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
      "timestamp": "2026-06-01T00:00:00.000Z",
      "amount": "1500000000",
      "fiatValue": 1500.0,
      "unitFiatPrice": 1.0,
      "source": "fireblocks",
      "custodianName": "Fireblocks",
      "isOffchain": false
    }
  ],
  "limit": 1000,
  "offset": 0,
  "total": 42
}

</code></pre>
<h2 id="example-response-with-groupby-symbol">Example response (with groupBy: "symbol")</h2>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code class="language-json">{
  "results": [
    {
      "symbol": "USDC",
      "timestamp": "2026-06-01T00:00:00.000Z",
      "isOffchain": false,
      "amount": "3500000000",
      "fiatValue": 3500.0
    }
  ],
  "limit": 1000,
  "offset": 0,
  "total": 8
}

</code></pre>
<h2 id="response-fields">Response fields</h2>
<div class="click-to-expand-wrapper is-table-wrapper"><table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>results</code></td>
<td>The matching balances (token-level rows, or grouped totals when <code>groupBy</code> is used).</td>
</tr>
<tr>
<td><code>total</code></td>
<td>Total number of matching results available — use with <code>limit</code>/<code>offset</code> to page through them.</td>
</tr>
<tr>
<td><code>limit</code></td>
<td>Echoes back the limit applied.</td>
</tr>
<tr>
<td><code>offset</code></td>
<td>Echoes back the offset applied.</td>
</tr>
<tr>
<td><code>isOffchain</code></td>
<td>Indicates whether the balance is from an off-chain source.</td>
</tr>
</tbody>
</table>
</div>

**Auth:** bearer

**Request body:**
```json
{
    "startDate": "2026-01-01T00:00:00.000Z",
    "endDate": "2026-06-01T00:00:00.000Z"
}
```

## Find Account Positions

`POST {{backend}}/pof/find-account-positions`

**Auth:** bearer

**Request body:**
```json
{
    "networks": [
        "ethereum"
    ],
    "symbols": [
        "ETH",
        "MATIC"
    ],
    "timestamps": [
        1735689600000,
        1761955200000
    ],
    "tokenAddresses": [
        "native",
        "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0"
    ],
    "validatorAddresses": ["0x0000000000"],
    "offset": 0,
    "limit": 100
}
```

## Query Account Positions

`POST {{backend}}/pof/aggregate-account-positions`

**Auth:** bearer

**Request body:**
```json
{
    "pipeline": [
        {
            "$match": {
                "network": "ethereum"
            }
        },
        {
            "$limit": 100
        }
    ]
}
```

## Enable/Disable Networks

`POST {{backend}}/pof/enable-disable-networks`

**Auth:** bearer

**Request body:**
```json
{
    "networks": [
        "bitcoin",
        "ethereum"
    ],
    "enable": true
}
```

## Get Network Status

`POST {{backend}}/pof/network-status`

**Auth:** bearer

**Request body:**
```json
{
    "networks": [
        "ethereum",
        "bitcoin",
        "ripple",
        "dash",
        "cardano"
    ]
}
```

## Snapshot Status

`POST {{backend}}/pof/snapshot-status`

<h2 id="snapshot-status">Snapshot Status</h2>
<p>Returns the snapshot completion status for one or more Unix timestamps. Use this endpoint to check whether all networks have finished processing their snapshots for the given timestamps.</p>
<hr />
<h3 id="request-body">Request Body</h3>
<div class="click-to-expand-wrapper is-table-wrapper"><table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>timestamps</code></td>
<td>array of numbers</td>
<td>Yes</td>
<td>A list of Unix timestamps in milliseconds to check the snapshot status for (e.g. <code>[1762300800000]</code>)</td>
</tr>
</tbody>
</table>
</div><hr />
<h3 id="authentication">Authentication</h3>
<p>This endpoint requires a <strong>Bearer token</strong>. The token is sourced from the <code>{{access_token}}</code> variable.</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>Authorization: Bearer {{access_token}}

</code></pre><hr />
<h3 id="expected-response">Expected Response</h3>
<p><strong><code>200 OK</code></strong> — The request was successful.</p>
<p>Returns a <code>snapshots</code> object keyed by timestamp. Each entry contains:</p>
<div class="click-to-expand-wrapper is-table-wrapper"><table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>networksCompleted</code></td>
<td>array of strings</td>
<td>List of networks that have completed the snapshot</td>
</tr>
<tr>
<td><code>networksInProgress</code></td>
<td>array of strings</td>
<td>List of networks still processing the snapshot</td>
</tr>
<tr>
<td><code>isCompleted</code></td>
<td>boolean</td>
<td>Whether all networks have completed the snapshot for that timestamp</td>
</tr>
</tbody>
</table>
</div>

**Auth:** bearer

**Request body:**
```json
{
    "timestamps": [
       1762300800000,
       1769644800000
    ]
}
```

**Sample response (200):**
```json
{"snapshots":{"1762300800000":{"networksCompleted":["abstract","algorand","arbitrum","astar","avax","base","berachain","binance","bitcoin","bitcoin_cash","cardano","celestia","celo","near","optimism","osmosis","polkadot","polygon","ripple","sei","solana","sonic","stellar","sui","tezos","ton","tron"],"networksInProgress":[],"isCompleted":true},"1769644800000":{"networksCompleted":["abstract","algorand","arbitrum","astar","avax","axelar","base","berachain","binance","bitcoin","bitcoin_cash","canton","cardano","celestia","celo","near","optimism","osmosis","polkadot","polygon","ripple","sei","solana","soneium","sonic","sui","tezos"],"networksInProgress":["ethereum","tron"],"isCompleted":false}}}
```

## Fetch Token Policy

`GET {{backend}}/pof/network-token-policy?networks=ethereum,base&tokenAddress=0x123`

<h2 id="fetch-token-policy">Fetch Token Policy</h2>
<p>Retrieves the token policy for one or more networks and a specific token contract address. Use this endpoint to look up policy configuration associated with a given token across the specified networks.</p>
<hr />
<h3 id="query-parameters">Query Parameters</h3>
<div class="click-to-expand-wrapper is-table-wrapper"><table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>networks</code></td>
<td>string</td>
<td>Yes</td>
<td>Comma-separated list of network names (e.g. <code>ethereum,base</code>)</td>
</tr>
<tr>
<td><code>tokenAddress</code></td>
<td>string</td>
<td>Yes</td>
<td>The token contract address to fetch the policy for (e.g. <code>0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48</code>). Use <code>native</code> to fetch the policy for the native token of the network.</td>
</tr>
</tbody>
</table>
</div><hr />
<h3 id="authentication">Authentication</h3>
<p>This endpoint requires a <strong>Bearer token</strong>. The token is sourced from the <code>{{access_token}}</code> variable.</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>Authorization: Bearer {{access_token}}

</code></pre><hr />
<h3 id="expected-response">Expected Response</h3>
<p><strong><code>200 OK</code></strong> — The request was successful and the token policy data is returned in the response body.</p>

**Auth:** bearer

**Sample response (200):**
```json
{"networks": [{"network": "ethereum", "tokenAddress": "0x123", "isFound": false}, {"network": "base", "tokenAddress": "0x123", "isFound": false}]}
```

## Update Token Policy

`POST {{backend}}/pof/network-token-policy`

<h2 id="update-token-policy">Update Token Policy</h2>
<p>Creates or updates the token policy for a specific network and token contract address. Use this endpoint to configure policy settings associated with a given token on the specified network.</p>
<hr />
<h3 id="body-parameters">Body Parameters</h3>
<div class="click-to-expand-wrapper is-table-wrapper"><table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>network</code></td>
<td>string</td>
<td>Yes</td>
<td>The network name (e.g. <code>ethereum</code>)</td>
</tr>
<tr>
<td><code>tokenAddress</code></td>
<td>string</td>
<td>Yes</td>
<td>The token contract address to set the policy for (e.g. <code>0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48</code>). Use <code>native</code> for the native token of the network.</td>
</tr>
</tbody>
</table>
</div><hr />
<h3 id="authentication">Authentication</h3>
<p>This endpoint requires a <strong>Bearer token</strong>. The token is sourced from the <code>{{access_token}}</code> variable.</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>Authorization: Bearer {{access_token}}

</code></pre><hr />
<h3 id="expected-response">Expected Response</h3>
<p><strong><code>200 OK</code></strong> — The request was successful and the token policy has been created or updated.</p>

**Auth:** bearer

**Request body:**
```json
{
    "network": "ethereum",
    "tokenAddress": "0x123"
}
```

**Sample response (200):**
```json
{"success": true, "network": "ethereum", "tokenAddress": "0x123"}
```

## Delete Token Policy

`DELETE {{backend}}/pof/network-token-policy/ethereum/0x123`

<h2 id="delete-token-policy">Delete Token Policy</h2>
<p>Deletes the token policy for a specific network and token contract address. Use this endpoint to remove the policy configuration associated with a given token on the specified network.</p>
<hr />
<h3 id="path-parameters">Path Parameters</h3>
<div class="click-to-expand-wrapper is-table-wrapper"><table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>network</code></td>
<td>string</td>
<td>Yes</td>
<td>The network name (e.g. <code>ethereum</code>)</td>
</tr>
<tr>
<td><code>tokenAddress</code></td>
<td>string</td>
<td>Yes</td>
<td>The token contract address to delete the policy for (e.g. <code>0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48</code>). Use <code>native</code> to delete the policy for the native token of the network.</td>
</tr>
</tbody>
</table>
</div><hr />
<h3 id="authentication">Authentication</h3>
<p>This endpoint requires a <strong>Bearer token</strong>. The token is sourced from the <code>{{access_token}}</code> variable.</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code>Authorization: Bearer {{access_token}}

</code></pre><hr />
<h3 id="expected-response">Expected Response</h3>
<p><strong><code>200 OK</code></strong> — The request was successful and the token policy has been deleted.</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code class="language-json">{
    "success": true,
    "network": "ethereum",
    "tokenAddress": "0x123",
    "isDeleted": true
}

</code></pre>

**Auth:** bearer

**Sample response (200):**
```json
{"success": true, "network": "ethereum", "tokenAddress": "0x123"}
```

## Register Network Accounts

`PUT {{backend}}/pof/accounts`

**Auth:** bearer

**Request body:**
```json
{
    "accounts": [
        {
            "accountAddress": "0xdadB0d80178819F2319190D340ce9A924f783711",
            "network": "ethereum"
        },
        {
            "accountAddress": "0xdadB0d80178819F2319190D340ce9A924f783711",
            "network": "arbitrum"
        }
    ]
}
```

## Query Registered Accounts

`POST {{backend}}/pof/accounts`

**Auth:** bearer

**Request body:**
```json
{
    "filter": {
        "$or": [
         {"network": "ethereum"}
        ]
    },
    "offset": 1000
}
```

## Delete Network Accounts

`DELETE {{backend}}/pof/accounts`

**Auth:** bearer

**Request body:**
```json
{
    "network": "arbitrum",
    "accountAddresses": [
        "0xdadB0d80178819F2319190D340ce9A924f783711"
    ]
}
```
