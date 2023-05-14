import pymongo
import time
import os
import re
import sys
import colorama
from colorama import Fore, Back
import pandas as pd
import ctypes

class game_hl:
    def __init__(self):
        pass
    
    def get_data(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["game"]
        col = db["hl"]
        return col.find_one()