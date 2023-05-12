import pymongo

# create a client object
client = pymongo.MongoClient("mongodb://localhost:27017/")

# create a database object
db = client["mydatabase"]

# create a collection object
collection = db["mycollection"]

# create a document with null value for name field
document = {"name": None}

# insert the document into the collection
collection.insert_one(document)
