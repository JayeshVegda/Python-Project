import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the LetterBox database and collections
db = client["LetterBox"]
rating_collection = db["rating"]
imdb_collection = db["imdb"]

# Define the aggregation pipeline
pipeline = [
    {
        "$lookup": {
            "from": "imdb",
            "let": { "name": "$Name" },
            "pipeline": [
                { "$match": { "$expr": { "$eq": [ "$Title", "$$name" ] } } },
                { "$limit": 1 }
            ],
            "as": "matching_docs"
        }
    },
    {
        "$match": {
            "matching_docs": { "$eq": [] }
        }
    },
    {
        "$project": {
            "_id": 0,
            "Name": 1
        }
    }
]

# Execute the aggregation pipeline on the rating collection
result = rating_collection.aggregate(pipeline)

# Print the non-matching names
for doc in result:
    print(doc["Name"])
