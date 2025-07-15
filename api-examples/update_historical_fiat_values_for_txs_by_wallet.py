from data.stateless_demo import CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN
from core.graphql_functions import get_graphql_client, execute_grahpql_query
from pydantic import BaseModel
from datetime import datetime, timezone
import csv
import os

class WalletAssetPair(BaseModel):
    wallet_address: str
    fiat_currency: str
    fiat_price: float
    platform: str
    asset_identifier: str

    @property
    def asset_id(self):
        return self.platform + "_" + self.asset_identifier.lower()

# --------------------------
# CONFIGURATION
# --------------------------
graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        access_token=ACCESS_TOKEN
    )

END_DATE = datetime(2025, 1, 1, tzinfo=timezone.utc).isoformat()
START_DATE = datetime(2018, 1, 1, tzinfo=timezone.utc).isoformat()
def graphql_request(payload):
    result = execute_grahpql_query(graphql_client, payload["query"], payload["variables"])
    return result

def get_sub_transactions(wallet_identifier  , asset_id):
    query = {
        "operationName": "readTxsQuery1",
        "variables": {
            "limit": 100,
            "offset": 0,
            "timestamp_Lt": END_DATE,
            "timestamp_Gt": START_DATE,
            "belongsTo_Identifier_In": [wallet_identifier],
            "asset_In": [str(asset_id)]
        },
        "query": """
            query GetSubTransactionByInternalAccountIdentifier(
            $limit: Int, 
            $offset: Int, 
            $timestamp_Gt: DateTime,  
            $timestamp_Lt: DateTime, 
            $platform: String, 
            $tx_Id: String
            $tx_DecodedFunctionName: String ,
            $tx_DecodedFunctionNameIn: [String],
            $belongsTo_Identifier_In: [String],  
            $balanceFactor: Float,
            $tag: [String]
            $asset_In: [ID],
            $tx_Identifier_In: [String]) {
            subTransaction(
            balanceFactor: $balanceFactor,    
            limit: $limit, 
            offset: $offset, 
            tx_Id: $tx_Id,
            timestamp_Gt: $timestamp_Gt, 
            platform: $platform, 
            timestamp_Lt: $timestamp_Lt, 
            tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
            belongsTo_Identifier_In: $belongsTo_Identifier_In, 
            tx_DecodedFunctionName: $tx_DecodedFunctionName,
            tags_Overlap: $tag,
            tx_Identifier_In: $tx_Identifier_In 
            asset_In: $asset_In
            ) {
                results {
                    id
                    platform
                    amount
                    balanceFactor
                    type
                    tx {
                        decodedFunctionName
                        methodId
                        blockNumber
                        identifier
                    }
                    timestamp
                    sender {
                        identifier
                    }
                    recipient {
                        identifier
                    }
                    createdAt
                    updatedAt
                }
            }
            }
        """
    }

    response = graphql_request(query)
    children = []
    for sbx in response["data"]["subTransaction"]["results"]:
        children.append(sbx["id"])
    return children


def batch_update_fiat_value(sub_tx_ids, price, currency):
    if not sub_tx_ids:
        print("⚠ No sub-transactions to update.")
        return False

    mutation = {
        "operationName": "SetBatchManualFiatValue",
        "variables": {
            "ids": sub_tx_ids,
            "newUnitValue": price,
            "currency": currency
        },
        "query": """
        mutation SetBatchManualFiatValue($ids: [String]!, $newUnitValue: Float!, $currency: String) {
          setBatchManualFiatValue(ids: $ids, newUnitValue: $newUnitValue, currency: $currency) {
            success
          }
        }
        """
    }

    try:
        result = graphql_request(mutation)
        success = result["data"]["setBatchManualFiatValue"]["success"]
        if success:
            print(f"✅ Successfully updated {len(sub_tx_ids)} sub-transactions to {price} {currency.upper()}")
        else:
            print("❌ Batch update failed.")
        return success
    except Exception as e:
        print(f"❌ Error during batch update: {e}")
        return False    


def update_wallet_asset_fiat(wallet_asset_list: list[WalletAssetPair]):
    for wallet_asset in wallet_asset_list:
        print(f"\n===== Wallet: {wallet_asset.wallet_address} | Asset ID: {wallet_asset.asset_id} =====")
        try:
            sub_ids = get_sub_transactions(wallet_asset.wallet_address, wallet_asset.asset_id)

            print(f"🔍 Total sub-transactions to update: {len(sub_ids)}")
            batch_update_fiat_value(sub_ids, wallet_asset.fiat_price, wallet_asset.fiat_currency)
        except Exception as e:
            print(f"❌ Error for wallet {wallet_asset.wallet_address}: {e}")


# -----------------------------------
# Example Execution
# -----------------------------------
if __name__ == "__main__":
    
    def load_wallet_asset_pairs_from_csv(csv_file_path: str) -> list[WalletAssetPair]:
        """Load wallet asset pairs from CSV file"""
        wallet_asset_pairs = []
        
        if not os.path.exists(csv_file_path):
            print(f"❌ CSV file not found: {csv_file_path}")
            return wallet_asset_pairs
            
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    try:
                        wallet_asset_pair = WalletAssetPair(
                            wallet_address=row['wallet_address'],
                            platform=row['platform'],
                            asset_identifier=row['asset_identifier'],
                            fiat_price=float(row['fiat_price']),
                            fiat_currency=row['fiat_currency']
                        )
                        wallet_asset_pairs.append(wallet_asset_pair)
                    except (KeyError, ValueError) as e:
                        print(f"⚠️  Skipping invalid row: {row} - Error: {e}")
                        continue
                        
            print(f"✅ Loaded {len(wallet_asset_pairs)} wallet asset pairs from CSV")
            return wallet_asset_pairs
            
        except Exception as e:
            print(f"❌ Error reading CSV file: {e}")
            return wallet_asset_pairs

    # Load wallet asset pairs from CSV
    csv_file_path = "wallet_asset_pairs.csv"
    wallet_asset_pairs = load_wallet_asset_pairs_from_csv(csv_file_path)
    
    if wallet_asset_pairs:
        update_wallet_asset_fiat(wallet_asset_pairs)
    else:
        print("❌ No wallet asset pairs loaded. Please check the CSV file.")