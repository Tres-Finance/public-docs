from core.graphql_functions import *
from data.demo import *
from datetime import datetime
from core.models import *
from core.csv import *
def main():

    # Login
    graphql_client = get_graphql_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    
    platform = Platform.ETHEREUM2

    sub_transactions = get_all_sub_transactions(
        graphql_client, datetime(2020, 1, 1), datetime(2023, 8, 31), platform, None,
        ['8b91d99620ca493e73d6651cbe3b27066d2e1aa21d8d8cb6815432ab6f6a4546b2ca0ff4dd7abfa98f908a7c1aaf744f', 'b9e73395d717ea26169cb5734dc33f7b220d93d0ef7a69e244ce2058e1eaecaa41024a0d666ccb80c10f17d430b9a01d', '8840a4a761478dd664a2b286d0df79304119f87ab0f0890b53e1bb53a017287317a15ebaf7d8be4d318c6458d2298727']
    )

    print(sub_transactions)
    write_output(sub_transactions)

if __name__ == "__main__":
    main()