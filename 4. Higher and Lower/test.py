import pymongo
import time
import os
import re
import sys
import colorama
from colorama import Fore, Back
import pandas as pd
import ctypes
import json
import random

os.system("cls")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["imdb"]
collection = db["top_250"]


class ran:
    def __init__(self):
        self.name_1 = ""
        self.rank_1 = 0
        self.year_1 = 0
        self.duration_1 = 0
        self.rate_1 = 0
        self.name_2 = ""
        self.rank_2 = 0
        self.year_2 = 0
        self.duration_2 = 0
        self.rate_2 = 0
        
    def random_choise_1(self):
        call = list(collection.find({}))
        random_data = random.choices(population=call, k=1)
        self.name_1 = random_data[0]['name']
        self.rank_1 = random_data[0]['rank']
        self.year_1 = random_data[0]['year']
        self.duration_1 = random_data[0]['duration']
        self.rate_1 = random_data[0]['imdb_rating']


    def random_choise_2(self):
        call = list(collection.find({}))
        random_data = random.choices(population=call, k=1)
        self.name_2 = random_data[0]['name']
        self.rank_2 = random_data[0]['rank']
        self.year_2 = random_data[0]['year']
        self.duration_2 = random_data[0]['duration']
        self.rate_2 = random_data[0]['imdb_rating']
        
    def call(self):
        self.random_choise_1()
        self.random_choise_2()
        print(f"{self.name_1} Rating is {self.rank_1} ")
        print(f"{self.name_2} Rating will be higher or lower ?")
        i = input("Choise 'h' or 'l' :" )
        if self.rank_1 > self.rank_2:
            print(f"{self.name_1} rank {self.rank_1} is more higher then {self.name_2} rank which is {self.rank_2}")
        elif self.rank_2 > self.rank_2:
            print(f"{self.name_2} rank {self.rank_2} is more higher then {self.name_1} rank which is {self.rank_1}")
        elif self.rank_1 == self.rank_2:
            print("Both rank is same")
        else:
            print("invalid input")
r = ran()
r.call()
