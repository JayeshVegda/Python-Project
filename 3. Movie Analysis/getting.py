import pymongo
import time
import os
from PyMovieDb import IMDB
import json
import re
import pandas as pd

# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client['db_db']
# collection = db['db_collection']
# imdb =  IMDB()


# # asK_db = input("Enter Your Database Name : ")
# # asK_col = input("Enter Your Collection Name : ")
# p = pd.read_csv('3. Movie Analysis/ratings.csv')

# data_p = p.to_dict('records')
# collection.insert_many(data_p)


while True:
    ask_db = input("Enter The Name of DataBase : ")
    if ask_db.strip() == "":
        print("Plese provide a valid db name")
    elif ask_db.strip() != "":
        print(ask_db, "thnkxs u")
        break
    else:
        print("heart break")



# i = float(input("enter "))
# if i in range(6):
#     print(i, "is on range")
# else:
#     print("Not in range")

# while True:
#     try:
#         i = float(input("Enter a number: "))
#         if i == int(i) or i % 1 == 0.5:
#             if 1 <= i <= 5:
#                 print(i, "is valid.")
#                 break
#             else:
#                 print("Number out of range. Please enter a number between 1 and 5.")
#         else:
#             print("Invalid input. Please enter an integer or a float with .5 as decimal in 1 to 5.")
#     except ValueError:
#         print("Invalid input. Please enter a number.")



# # l = []
# # i = float(input("enter the : "))
# result = collection.find({"Rating": i})
# for i in result:
#     name = i.get("Name", "Not Avalible")
#     year = i.get("Year", "Not Avalible")
#     rate = i.get("Rating", "Not Avalible")
#     print(f"Name: {name}, Year: {year}, Rating: {rate}")


    
# l = []
# i = input("Enter the name of Movie : ")
# pattern = re.compile(f".*{i}.*", re.IGNORECASE)
# results = collection.find({ "Name": pattern })
# check = list(results)
# if not check:
#     print("Sorry Your movie is not in list")
# else:
#     for result in results:
#         name = result["Name"]
#         year = result["Year"]
#         rating = result["Rating"]
#         print(f"Name: {name}, Year: {year}, Rating: {rating}")

# get_year = x['Year']
# get_rating = x['Rating']

# print(f"\nMovie Name : {i} \nYear : {get_year} \nRating : {get_year}")


# get_name = collection.find()
# movie_list = []
# director_list = []

# for i in get_name:
#     name = i["Name"]
#     movie_list.append(name)
    
# for j in movie_list:
#     if director_list != "Bryan Singer":
#         get = imdb.get_by_name(j, tv=False)
#         data = json.loads(get)
#         try:
#             director = data['director'][0]['name']
#         except:
#             director = 'Null'
#         print(director)
#         director_list.append(director)
#     else:
#         print("oopps")
    
# for a in movie_list:
#     for b in director_list:
#         print(a)
#     print(b)




# if client.server_info():
#     pass
# else:
#     print("Connection Error")

# class movieanal:
    
#     def __init__(self):
#         self.year = 0
        
#     def movie_year_search(self):
#         os.system("cls")
#         self.year = int(input("Enter the year of movie you wanna search: "))
#         print("Searching... \n")
#         time.sleep(2)
        
#         print(f"This is list of Movie that Relased in {self.year} \n")
#         movie_count = 0
#         for x in collection.find({"Year": self.year}):
#             print(x["Name"])
#             movie_count = movie_count + 1
            
#         print("\nTotal Movie: ", movie_count)

#     def movie_search_by_director(self):
#         os.system("cls")
        
    
# if __name__ == "__main__":
#     obj = movieanal()
#     obj.movie_year_search()