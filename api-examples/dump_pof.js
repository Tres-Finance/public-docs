/*
    1. Install the required node packages mongodb and json2csv by running: 
    `npm install mongodb json2csv`
    2. Update the mongoUrl with your connection string
    3. Set the fields dates, network and symbols with the required parameters of the balance you want to export.
    You can specify 0, 1 or more values in each field
*/
const mongodb = require('mongodb');
const json2csv = require('json2csv').Parser;
const fs = require('fs');

let mongoClient
const mongoUrl = 'ENTER CONNECTION STRING';
const dates = ["2024-07-01", "2024-06-01"] // Enter dates
const networks = ["ethereum"] // Enter networks
const symbols = ["ETH"] // Enter token symbols
const DB_NAME = "my-pof" // Enter db name

exportFromMongo(dates, networks, symbols)

async function exportFromMongo(dates = [], networks = [], symbols = []) {
    try {
        if (!dates.length && !networks.length && !symbols.length) {
            console.error("You must provide at least one parameter out of dates, networks and symbols")
            return
        }

        // MongoDB client
        mongoClient = new mongodb.MongoClient(mongoUrl);
        await mongoClient.connect()
        console.log('Connected to MongoDB');
        const db = mongoClient.db(DB_NAME);
        const collection = db.collection('accountBalances');

        console.log(`Fetching balances for dates: ${dates} networks: ${networks} and symbols: ${symbols}`)
        const aggregationPipeline = buildAggregationPipeline(dates, networks, symbols)
        const docs = await collection.aggregate(aggregationPipeline).toArray();

        const outputFilePath = `TRES Exported Balances ${getFormattedDate()}.csv`;
        console.log(`Exporting ${docs.length} balances to ${outputFilePath}`)
        const fields = Object.keys(docs[0] || {});
        const json2csvParser = new json2csv({ fields });
        const csv = json2csvParser.parse(docs);
        fs.writeFileSync(outputFilePath, csv);
        console.log(`CSV file exported to ${outputFilePath}`);

        // Close the MongoDB connection
        mongoClient.close();
    } catch (err) {
        console.error(`Failed to export from MongoDB: ${err}`)
        if (mongoClient) {
            mongoClient.close()
        }
    }
}

function getFormattedDate() {
    const currentDate = new Date();
    const year = currentDate.getFullYear();
    const month = String(currentDate.getMonth() + 1).padStart(2, '0');
    const day = String(currentDate.getDate()).padStart(2, '0');
    const hours = String(currentDate.getHours()).padStart(2, '0');
    const minutes = String(currentDate.getMinutes()).padStart(2, '0');

    const formattedDate = `${year}-${month}-${day} ${hours}:${minutes}`;
    return formattedDate
}

function buildAggregationPipeline(dates, networks, symbols) {
    const aggregationPipeline = []

    if ((dates && dates.length) || (networks && networks.length)) {
        let match = {}

        if (dates && dates.length) {
            match = {
                timestamp: {
                    $in: dates.map(date => new Date(`${date}T00:00:00.000Z`))
                }
            }
        }

        if (networks && networks.length) {
            match = {
                ...match, network: {
                    $in: networks
                }
            }
        }

        aggregationPipeline.push({
            $match: match
        })
    }

    aggregationPipeline.push({
        $unwind: "$balances",
    })

    if (symbols && symbols.length) {
        aggregationPipeline.push({
            $match: {
                "balances.symbol": {
                    $in: symbols
                }
            }
        })
    }

    aggregationPipeline.push({
        $project: {
            "Asset Platform": "$network",
            "Wallet Address": "$accountAddress",
            "Historical Balance (T)": {
                $toString: "$balances.amount"
            },
            "Asset Symbol": "$balances.symbol",
            "Asset Address": "$balances.tokenAddress",
            Timestamp: "$timestamp",
            "Block Number": "$blockNumber",
            "Block Timestamp": "$blockTimestamp",
        }
    })

    return aggregationPipeline
}