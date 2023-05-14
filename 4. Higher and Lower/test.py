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
from art import *

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
        self.score = 0
    
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  # Loop over the message
            # Print the one charecter, flush is used to force python to print the char
            print(i, end="", flush=True)
            time.sleep(speed)  # Sleep a little before the next one
            if newLine:  # Check if the newLine argument is set to True
                print()   
                
    def logo(self):
       Art=text2art("HoL",font='block',chr_ignore=True) # Return ASCII text with block font
       print(Art)
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
        
    def game_ranking(self):
        score = 0
        call = True
        while True:
            os.system("cls")
            self.logo()
            if call == True:
                self.random_choise_1()
                self.random_choise_2()
            else:
                pass
            
            print(f"\n{self.name_1} Ranking is {self.rank_1} ")
            print(f"{self.name_2} Ranking will be higher or lower ?")
            i = input("Choise 'h' or 'l' :" )
            try:
                if i == "h":
                    if self.rank_1 > self.rank_2:
                        print(f"You Win, {self.name_2} Ranking is {self.rank_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    else:
                        print("You lose")
                        print(f"{self.name_2} Ranking is {self.rank_2}")
                        time.sleep(1)
                        print(f"\nYour score is {score}")
                        time.sleep(2)
                        break
                        
                elif i == "l":
                    if self.rank_1 < self.rank_2:
                        print("You win")
                        print(f"You Win, {self.name_2} Ranking is {self.rank_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    else:
                        print("You lose")
                        print(f"{self.name_2} Ranking is {self.rank_2}")
                        time.sleep(1)
                        print(f"\nYour score is {score}")
                        time.sleep(2)
                        break
                else:
                    print("Wrong choise")
                    call = False
                    time.sleep(2)
            except:
                print("Error Occure ! ")
                call = False
                time.sleep(2)
                break
    
    def game_rating(self):
        score = 0
        call = True
        while True:
            os.system("cls")
            self.logo()
            if call == True:
                self.random_choise_1()
                self.random_choise_2()
            else:
                pass
            
            print(f"\n{self.name_1} Rating is {self.rate_1} ")
            print(f"{self.name_2} Rating will be higher or lower ? {self.rate_2}")
            i = input("Choise 'h' or 'l' :" )
            try:
                if i == "h":
                    if float(self.rate_1) == float(self.rate_2):
                        print(f"Same rating, {self.name_2} Rating is {self.rate_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    elif self.rate_1 < self.rate_2:
                        print(f"You Win, {self.name_2} Ranking is {self.rate_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r{self.name_2} Ranking is {self.rate_2}")
                        time.sleep(1)
                        print(f"\nYour score is {score}")
                        time.sleep(2)
                        break
                        
                elif i == "l":
                    if self.rate_1 == self.rate_2:
                        print(f"Same rating, {self.name_2} Rating is {self.rate_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    elif self.rate_1 > self.rate_2:
                        print("You win")
                        print(f"You Win, {self.name_2} Ranking is {self.rate_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r{self.name_2} Ranking is {self.rate_2}")
                        time.sleep(1)
                        os.system("cls")
                        self.logo()
                        print(f"\nYour score is {score}")
                        time.sleep(2)
                        break
                else:
                    print("Wrong choise")
                    call = False
                    time.sleep(2)
            except:
                print("Error Occure ! ")
                call = False
                time.sleep(2)
                break
    
    def game_duration(self):
        score = 0
        call = True
        while True:
            os.system("cls")
            self.logo()
            if call == True:
                self.random_choise_1()
                self.random_choise_2()
            else:
                pass
            
            print(f"\n{self.name_1} Rating is {self.duration_1} ")
            print(f"{self.name_2} Rating will be higher or lower ? {self.duration_2}")
            i = input("Choise 'h' or 'l' :" )
            try:
                if i == "h":
                    if self.duration_1 == self.duration_2:
                        print(f"Same rating, {self.name_2} Rating is {self.duration_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    elif self.duration_1 < self.duration_2:
                        print(f"You Win, {self.name_2} Ranking is {self.duration_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    else:
                        print("You lose")
                        print(f"{self.name_2} Ranking is {self.duration_2}")
                        time.sleep(1)
                        print(f"\nYour score is {score}")
                        time.sleep(2)
                        break
                        
                elif i == "l":
                    if self.duration_1 == self.duration_2:
                        print(f"Same rating, {self.name_2} Rating is {self.duration_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    elif self.duration_1 > self.duration_2:
                        print("You win")
                        print(f"You Win, {self.name_2} Ranking is {self.duration_2}")
                        score = score + 1
                        time.sleep(1)
                        call = True
                    else:
                        print("You lose")
                        print(f"{self.name_2} Ranking is {self.duration_2}")
                        time.sleep(1)
                        print(f"\nYour score is {score}")
                        time.sleep(2)
                        break
                else:
                    print("Wrong choise")
                    call = False
                    time.sleep(2)
            except:
                print("Error Occure ! ")
                call = False
                time.sleep(2)
                break

    def mod_test(self):
            os.system("cls")
            i = int(input("score : "))
            if i == 69:
                exit()
            else:
                self.score = i
                print(self.score)
                self.myscore()
            
    def myscore(self):
        if self.score == 0:
            print("\n\033[2;31mBetter Luck Next Time !\033[1;0m")
            print(f"Your Total Score is \033[1;32m{self.score}\033[1;0m")
        elif self.score >= 1 and self.score < 5:
            print("\n\033[22;32mVery Good !\033[1;0m")
            print(f"Your Total Score is \033[1;32m{self.score}\033[1;0m")
        elif self.score >= 5 and self.score < 10:
            print("\n\033[22;34mExcellent !\033[1;0m")
            print(f"Your Total Score is \033[1;32m{self.score}\033[1;0m")
        elif self.score >= 10 and self.score < 20:
            print("\n\033[22;34mOutstanding !\033[1;0m")
            print(f"Your Total Score is \033[1;32m{self.score}\033[1;0m")
        elif self.score >= 20 and self.score < 30:
            print("\n\033[22;30;47mUnbelievable !\033[1;0m")
            print("You are a Genius ! ")
            print(f"Your Total Score is \033[1;32m{self.score}\033[1;0m")
        else:
            print("\n\033[22;32mYou are a Cheater ! ")
            print(f"Your Total Score is \033[1;32m{self.score}\033[1;0m")
        
        time.sleep(2)
        self.mod_test()
        
   
                
r = ran()
r.mod_test()
