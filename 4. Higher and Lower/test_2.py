import import_imdb
import os

client = "mongodb://localhost:27017"
db = input("Enter the name of the database: ")
collection = input("Enter the name of the collection: ")
oath = input("Enter the name of the csv file: ")
oa = os.path.dirname(os.path.abspath(__file__))
go_path = os.path.join(oa, oath + ".csv")
import_imdb.import_data(import_imdb.import_imdb(client, db, collection), go_path)

