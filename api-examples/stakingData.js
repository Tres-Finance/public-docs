#!/usr/bin/env node
/**
 * Script to fetch Staking Yield Options from TRES API
 * Flow: Login → Fetch stakingYieldOptions using JWT
 *
 * Similar to tres_api_org_specific Python scripts.
 */

const { join } = require("path");

const GRAPHQL_ENDPOINT = "https://api.tres.finance/graphql";

/** Start date for staking data requests (YYYY-MM-DD) */
const START_DATE = "2026-01-01";

const CLIENT_ID = "";
const CLIENT_SECRET = "";

const LOGIN_MUTATION = `
  mutation LoginMutation($clientId: String!, $clientSecret: String!) {
    getApiKey(clientId: $clientId, clientSecret: $clientSecret) {
      token
    }
  }
`;

const STAKING_YIELD_OPTIONS_QUERY = `
  query StakingYieldOptions($resolveStatus: Boolean) {
    stakingYieldOptions(resolveStatus: $resolveStatus) {
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
`;

const STAKING_DATA_QUERY = `
  query getStakingData(
    $platform: Platform!,
    $identifier: String!,
    $start: Date!,
    $end: Date!,
    $excludeZeroRewards: Boolean,
    $yieldType: StakingYieldType,
    $ignoreMissingDataErrors: Boolean,
    $asset: String
  ) {
    stakingData(
      platform: $platform,
      identifier: $identifier,
      assetIdentifier: $asset,
      start: $start,
      end: $end,
      excludeZeroRewards: $excludeZeroRewards,
      yieldType: $yieldType,
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
          unlocking
          validatorIdentifier
          stakingLedger {
            timestamp
            type
            tx {
              identifier
              methodId
              blockNumber
              classification {
                action
              }
            }
            amount
            balanceFactor
            sender {
              identifier
            }
            recipient {
              identifier
            }
            originalSender {
              identifier
            }
            originalRecipient {
              identifier
            }
          }
        }
      }
    }
  }
`;

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function escapeCsvField(value) {
  if (value === null || value === undefined) return "";
  const str = String(value);
  if (str.includes(",") || str.includes('"') || str.includes("\n")) {
    return `"${str.replace(/"/g, '""')}"`;
  }
  return str;
}

function toCsv(rows) {
  if (rows.length === 0) return "";
  const headers = Object.keys(rows[0]);
  const lines = [
    headers.map(escapeCsvField).join(","),
    ...rows.map((row) =>
      headers.map((h) => escapeCsvField(row[h])).join(",")
    ),
  ];
  return lines.join("\n");
}

function flattenYieldOptions(options) {
  const rows = [];
  for (const opt of options) {
    for (const assetOpt of opt.assetOptions || []) {
      for (const iaOpt of assetOpt.internalAccountOptions || []) {
        rows.push({
          platform: opt.platform,
          yieldType: opt.yieldType,
          assetName: assetOpt.asset?.name,
          assetIdentifier: assetOpt.asset?.identifier,
          internalAccountName: iaOpt.internalAccount?.name,
          internalAccountId: iaOpt.internalAccount?.id,
          internalAccountIdentifier: iaOpt.internalAccount?.identifier,
          earliest: iaOpt.earliest,
          latest: iaOpt.latest,
          status: iaOpt.status,
        });
      }
    }
  }
  return rows;
}

function flattenStakingData(results) {
  const rows = [];
  for (const result of results) {
    const req = result.request;
    if (result.error) {
      rows.push({
        platform: req.platform,
        yieldType: req.yieldType,
        assetIdentifier: req.assetIdentifier,
        internalAccountName: req.internalAccountName,
        requestIdentifier: req.identifier,
        error: result.error,
        start: "",
        end: "",
        totalCount: "",
        validatorIdentifier: "",
        claimable: "",
        generatedRewards: "",
        locked: "",
        apr: "",
        unlocking: "",
        ledgerTimestamp: "",
        ledgerType: "",
        ledgerAmount: "",
        ledgerBalanceFactor: "",
        txIdentifier: "",
        slot: "",
        txMethodId: "",
        txBlockNumber: "",
        txAction: "",
        senderIdentifier: "",
        recipientIdentifier: "",
        originalSenderIdentifier: "",
        originalRecipientIdentifier: "",
      });
      continue;
    }

    const sd = result.data;
    if (!sd) continue;

    for (const validator of sd.data?.byValidator || []) {
      const ledgerEntries = validator.stakingLedger || [];
      if (ledgerEntries.length === 0) {
        rows.push({
          platform: sd.platform,
          yieldType: validator.yieldType,
          assetIdentifier: sd.assetIdentifier,
          internalAccountName: sd.internalAccountName,
          requestIdentifier: sd.identifier,
          error: "",
          start: validator.start,
          end: validator.end,
          totalCount: sd.totalCount,
          validatorIdentifier: validator.validatorIdentifier,
          claimable: validator.claimable,
          generatedRewards: validator.generatedRewards,
          locked: validator.locked,
          apr: validator.apr,
          unlocking: validator.unlocking,
          ledgerTimestamp: "",
          ledgerType: "",
          ledgerAmount: "",
          ledgerBalanceFactor: "",
          txIdentifier: "",
          slot: "",
          txMethodId: "",
          txBlockNumber: "",
          txAction: "",
          senderIdentifier: "",
          recipientIdentifier: "",
          originalSenderIdentifier: "",
          originalRecipientIdentifier: "",
        });
      }
      for (const entry of ledgerEntries) {
        rows.push({
          platform: sd.platform,
          yieldType: validator.yieldType,
          assetIdentifier: sd.assetIdentifier,
          internalAccountName: sd.internalAccountName,
          requestIdentifier: sd.identifier,
          error: "",
          start: validator.start,
          end: validator.end,
          totalCount: sd.totalCount,
          validatorIdentifier: validator.validatorIdentifier,
          claimable: validator.claimable,
          generatedRewards: validator.generatedRewards,
          locked: validator.locked,
          apr: validator.apr,
          unlocking: validator.unlocking,
          ledgerTimestamp: entry.timestamp,
          ledgerType: entry.type,
          ledgerAmount: entry.amount,
          ledgerBalanceFactor: entry.balanceFactor,
          txIdentifier: entry.tx?.identifier,
          slot: entry.tx?.identifier?.includes("_") ? entry.tx.identifier.split("_")[1] : "",
          txMethodId: entry.tx?.methodId,
          txBlockNumber: entry.tx?.blockNumber,
          txAction: entry.tx?.classification?.action,
          senderIdentifier: entry.sender?.identifier,
          recipientIdentifier: entry.recipient?.identifier,
          originalSenderIdentifier: entry.originalSender?.identifier,
          originalRecipientIdentifier: entry.originalRecipient?.identifier,
        });
      }
    }
  }
  return rows;
}

async function graphqlRequest(query, variables = {}, token = null) {
  const headers = {
    "Content-Type": "application/json",
  };
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const response = await fetch(GRAPHQL_ENDPOINT, {
    method: "POST",
    headers,
    body: JSON.stringify({ query, variables }),
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  }

  const data = await response.json();

  if (data.errors && data.errors.length > 0) {
    throw new Error(
      `GraphQL errors: ${data.errors.map((e) => e.message).join("; ")}`
    );
  }

  return data;
}

async function login() {
  console.log("🔐 Authenticating...");

  const data = await graphqlRequest(LOGIN_MUTATION, {
    clientId: CLIENT_ID,
    clientSecret: CLIENT_SECRET,
  });

  const accessToken = data?.data?.getApiKey?.token?.access_token;
  if (!accessToken) {
    throw new Error("Login failed: no access_token in response");
  }

  console.log("✅ Authentication successful");
  return accessToken;
}

async function fetchStakingYieldOptions(accessToken, resolveStatus = true) {
  console.log("\n📊 Fetching staking yield options...");

  const data = await graphqlRequest(
    STAKING_YIELD_OPTIONS_QUERY,
    { resolveStatus },
    accessToken
  );

  const options = data?.data?.stakingYieldOptions;
  if (options === undefined) {
    throw new Error("Response missing stakingYieldOptions");
  }

  return options;
}

async function fetchStakingData(accessToken, params) {
  const { platform, identifier, start, end, yieldType, asset } = params;

  const variables = {
    platform,
    identifier,
    start,
    end,
    excludeZeroRewards: true,
    yieldType: yieldType || null,
    ignoreMissingDataErrors: true,
    asset: asset || null,
  };

  const data = await graphqlRequest(STAKING_DATA_QUERY, variables, accessToken);
  return data?.data?.stakingData;
}

async function main() {
  console.log("=".repeat(60));
  console.log("TRES Staking Yield Options + Staking Data");
  console.log("=".repeat(60));

  try {
    const accessToken = await login();
    const options = await fetchStakingYieldOptions(accessToken);

    console.log(`\n✅ Retrieved ${options?.length ?? 0} staking yield option(s)`);

    const fs = require("fs");
    const optionsPath = join(__dirname, "staking_yield_options.json");
    fs.writeFileSync(optionsPath, JSON.stringify(options, null, 2));
    console.log(`📁 Options saved to: ${optionsPath}`);

    const optionsCsvPath = join(__dirname, "staking_yield_options.csv");
    const optionsRows = flattenYieldOptions(options);
    fs.writeFileSync(optionsCsvPath, toCsv(optionsRows));
    console.log(`📁 Options CSV saved to: ${optionsCsvPath} (${optionsRows.length} rows)`);

    // Collect all (option, assetOption, internalAccountOption) for staking data
    const requests = [];
    for (const option of options) {
      for (const assetOpt of option.assetOptions || []) {
        for (const iaOpt of assetOpt.internalAccountOptions || []) {
          requests.push({
            platform: option.platform,
            yieldType: option.yieldType,
            assetIdentifier: assetOpt.asset?.identifier,
            internalAccountName: iaOpt.internalAccount?.name,
            identifier: iaOpt.internalAccount?.identifier,
            end: iaOpt.latest,
          });
        }
      }
    }

    console.log(`\n📊 Fetching staking data in ${requests.length} requests...`);
    console.log(`   Start: ${START_DATE}`);

    const stakingDataResults = [];
    for (let i = 0; i < requests.length; i++) {
      const r = requests[i];
      process.stdout.write(
        `   [${i + 1}/${requests.length}] ${r.platform} / ${r.yieldType} / ${r.internalAccountName}... `
      );
      try {
        const data = await fetchStakingData(accessToken, {
          platform: r.platform,
          identifier: r.identifier,
          start: START_DATE,
          end: r.end,
          yieldType: r.yieldType,
          asset: r.assetIdentifier,
        });
        stakingDataResults.push({ request: r, data });
        console.log("✓");
      } catch (err) {
        console.log(`✗ ${err.message}`);
        stakingDataResults.push({ request: r, error: err.message });
      }
      if (i < requests.length - 1) await sleep(500);
    }

    const dataPath = join(__dirname, "staking_data_results.json");
    fs.writeFileSync(dataPath, JSON.stringify(stakingDataResults, null, 2));
    console.log(`\n📁 Staking data saved to: ${dataPath}`);

    const dataCsvPath = join(__dirname, "staking_data_results.csv");
    const dataRows = flattenStakingData(stakingDataResults);
    fs.writeFileSync(dataCsvPath, toCsv(dataRows));
    console.log(`📁 Staking data CSV saved to: ${dataCsvPath} (${dataRows.length} rows)`);
  } catch (err) {
    console.error("\n❌ Error:", err.message);
    process.exit(1);
  }
}

main();
