import pymongo as pm 
import time
import pandas as pd
import csv


def import_imdb(client_name, db_name, collection_name):
    client = pm.MongoClient(client_name)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def import_data(import_imdb, path):
    
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['id', 'imdb_rating', 'duration'])
        next(reader)  # Skip header row

    # Iterate over rows and insert documents into MongoDB
    for row in reader:
        document = {
            'id': int(row['id']),
            'imdb_rating': float(row['imdb_rating']),
            'duration': int(row['duration'])
        }
        import_imdb().insert_one(document)
    # data = pd.read_csv(path)
    # data = data.to_dict('records')
    # import_data.insert_many(data)
    return import_data