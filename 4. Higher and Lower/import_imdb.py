import pymongo as pm 
import csv

def connection(client_name, db_name, collection_name):
    client = pm.MongoClient(client_name)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def import_data(client_name, db_name, collection_name, path):
    collection = connection(client_name, db_name, collection_name)
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['rank', 'imdb_rating', 'year', 'duration'])
        next(reader)  # Skip header row

        # Iterate over rows and insert documents into MongoDB
        for row in reader:
            try:
                imdb_rating = float(row['imdb_rating'])
            except ValueError:
                imdb_rating = None

            document = {
                'rank': int(row['rank']),
                'imdb_rating': imdb_rating,
                'duration': int(row['duration'])
            }
            collection.insert_one(document)

    return collection
