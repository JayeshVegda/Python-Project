import import_imdb
import os
import json
import string
import random
import csv

# client = "mongodb://localhost:27017"
# db = input("Enter the name of the database: ")
# collection = input("Enter the name of the collection: ")
# oath = input("Enter the name of the csv file: ")
# oa = os.path.dirname(os.path.abspath(__file__))
# go_path = os.path.join(oa, oath + ".csv")

# import_imdb.import_data(client_name=client, db_name=db, collection_name=collection, path=go_path)
absolute_path = os.path.dirname(__file__)
relative_path = "movies.csv"
full_path = os.path.join(absolute_path, relative_path)

i = full_path.replace("\\", "/")
print(i)


import csv

with open(i, encoding='latin-1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
