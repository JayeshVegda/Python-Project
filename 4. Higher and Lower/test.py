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
import string

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
        self.local_data = True
        self.file_name = "top-250"
        
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  # Loop over the message
            # Print the one charecter, flush is used to force python to print the char
            print(i, end="", flush=True)
            time.sleep(speed)  # Sleep a little before the next one
            if newLine:  # Check if the newLine argument is set to True
                print()   
    def lets_quit(self):
        self.slowType("\r\033[1;31mReturning to the main menu....\033[0m", 0.1, newLine=False)
        time.sleep(1)
        self.main_menu()
                    
    def logo(self):
       Art=text2art("HoL",font='block',chr_ignore=True) # Return ASCII text with block font
       print(Art)
    def random_choise_1(self):
        if self.local_data == True:
            oa = os.path.dirname(os.path.abspath(__file__))
            go_path = os.path.join(oa, self.file_name + ".json")
            i = go_path.replace("\\", "/")
            with open(i, 'r') as file:
                data = json.load(file)
            # Parse the duration field
            random_data = random.choice(data)
            if random_data == "Your Rating":
                self.name_1 = random_data['Title']
            else:
                self.name_1 = random_data['name']
            if random_data == "Your Rating":
                self.rank_1 = 0
            else:
                self.rank_1 = random_data['rank']

            if random_data == "Your Rating":
                self.year_1 = random_data['Year']
            else:
                self.year_1 = random_data['year']
            if random_data == "Your Rating":
                self.duration_1 = random_data['Runtime (mins)']
            else:
                self.duration_1 = random_data['duration']
            if random_data == "Your Rating":
                self.rate_1 = random_data['IMDb Rating']
            else:
                self.rate_1 = random_data['imdb_rating']
                
        elif self.local_data == False:
            call = list(collection.find({}))
            random_data = random.choices(population=call, k=1)
            if random_data == "Your Rating":
                self.name_1 = random_data[0]['Title']
            else:
                self.name_1 = random_data[0]['name']
                
            if random_data == "Your Rating":
                self.rank_1 = 0
            else:
                self.rank_1 = random_data[0]['rank']
                
            if random_data == "Your Rating":
                self.year_1 = random_data[0]['Year']
            else:
                self.year_1 = random_data[0]['year']
                
            if random_data == "Your Rating":
                self.duration_1 = random_data[0]['Runtime (mins)']
            else:
                self.duration_1 = random_data[0]['duration']
                
            if random_data == "Your Rating":
                self.rate_1 = random_data[0]['IMDb Rating']
            else:
                self.rate_1 = random_data[0]['imdb_rating']
        else:
            print(Fore.WHITE + Back.RED + "Modify Settigs"+ Fore.RESET + Back.RESET)
            time.sleep(2)
            self.main_menu()


    def random_choise_2(self):
        if self.local_data == True:
            oa = os.path.dirname(os.path.abspath(__file__))
            go_path = os.path.join(oa, self.file_name + ".json")
            i = go_path.replace("\\", "/")
            with open(i, 'r') as file:
                data = json.load(file)
            # Parse the duration field
            random_data = random.choice(data)
            if random_data == "Your Rating":
                self.name_2 = random_data['Title']
            else:
                self.name_2 = random_data['name']
            if random_data == "Your Rating":
                self.rank_2 = 0
            else:
                self.rank_2 = random_data['rank']

            if random_data == "Your Rating":
                self.year_2 = random_data['Year']
            else:
                self.year_2 = random_data['year']
            if random_data == "Your Rating":
                self.duration_2 = random_data['Runtime (mins)']
            else:
                self.duration_2 = random_data['duration']
            if random_data == "Your Rating":
                self.rate_2 = random_data['IMDb Rating']
            else:
                self.rate_2 = random_data['imdb_rating']
                
        elif self.local_data == False:
            call = list(collection.find({}))
            random_data = random.choices(population=call, k=1)
            if random_data == "Your Rating":
                self.name_2 = random_data[0]['Title']
            else:
                self.name_2 = random_data[0]['name']
                
            if random_data == "Your Rating":
                self.rank_2 = 0
            else:
                self.rank_2 = random_data[0]['rank']
                
            if random_data == "Your Rating":
                self.year_2 = random_data[0]['Year']
            else:
                self.year_2 = random_data[0]['year']
                
            if random_data == "Your Rating":
                self.duration_2 = random_data[0]['Runtime (mins)']
            else:
                self.duration_2 = random_data[0]['duration']
                
            if random_data == "Your Rating":
                self.rate_2 = random_data[0]['IMDb Rating']
            else:
                self.rate_2 = random_data[0]['imdb_rating']
        else:
            print(Fore.WHITE + Back.RED + "Modify Settigs"+ Fore.RESET + Back.RESET)
            time.sleep(2)
            self.main_menu()
        
    def game_ranking(self):
        score = 0
        call = True
        while True:
            os.system("cls")
            self.logo()
            print("\nGame Mode : Ranking")
            if call == True:
                self.random_choise_1()
                self.random_choise_2()
            else:
                pass
            
            print(f"\n\033[2;36m{self.name_1}\033[1;0m Ranking is \033[2:37m{self.rank_1}\033[1;0m")
            print(f"\033[2;36m{self.name_2}\033[1;0m Ranking will be Higher or Lower ? ")
            i = input("Choise 'h' or 'l' (q for quit) : " )
            try:
                if i == "h" or i == "H":
                    if self.rank_1 < self.rank_2:
                        print(f"\n\033[2;32mYou Win\033[1;0m \n- {self.name_2} Ranking is {self.rank_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r{self.name_2} Ranking is {self.rank_2}")
                        time.sleep(2)
                        os.system("cls")
                        self.logo()
                        self.myscore()
                        time.sleep(2)
                        break
                        
                elif i == "l":
                    if self.rank_1 > self.rank_2:
                        print(f"\n\033[2;32mYou Win\033[1;0m \n-{self.name_2} Ranking is {self.rank_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r- {self.name_2} Ranking is {self.rank_2}")
                        time.sleep(2)
                        os.system("cls")
                        self.logo()
                        self.myscore()
                        time.sleep(2)
                        break
                else:
                    print(Fore.WHITE + Back.RED + "Wrong choise"+ Fore.RESET + Back.RESET)
                    call = False
                    time.sleep(2)
            except:
                print(Fore.WHITE + Back.RED + "ERROR ERROR ERROR"+ Fore.RESET + Back.RESET)
                call = False
                time.sleep(2)
                break
    
    def game_rating(self):
        self.score = 0
        call = True
        while True:
            os.system("cls")
            self.logo()
            print("\nGame Mode : Rating")
            if call == True:
                self.random_choise_1()
                self.random_choise_2()
            else:
                pass
            
            print(f"\n\033[2;36m{self.name_1}\033[1;0m Rate is \033[2:37m{self.rate_1}\033[1;0m")
            print(f"\033[2;36m{self.name_2}\033[1;0m Rate will be Higher or Lower ? ")
            i = input("Choise 'h' or 'l' (q for quit) : " )
            try:
                if i == "h" or i == "H":
                    if float(self.rate_1) == float(self.rate_2):
                        print(f"\n\033[2;36mSame rating\033[1;0m \n- {self.name_2} Rating is {self.rate_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    elif self.rate_1 < self.rate_2:
                        print(f"\n\033[2;32mYou Win\033[1;0m \n- {self.name_2} Ranking is {self.rate_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r{self.name_2} Ranking is {self.rate_2}")
                        time.sleep(2)
                        os.system("cls")
                        self.logo()
                        self.myscore()
                        time.sleep(2)
                        break
                        
                elif i == "l" or i == "L":
                    if self.rate_1 == self.rate_2:
                        print(f"\n\033[2;36mSame rating\033[1;0m{self.name_2} Rating is {self.rate_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    elif self.rate_1 > self.rate_2:
                        print(f"\n\033[2;32mYou Win\033[1;0m \n- {self.name_2} Ranking is {self.rate_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r\033[22;31m{self.name_2} Ranking is {self.rate_2}\033[1;m")
                        time.sleep(2)
                        os.system("cls")
                        self.logo()
                        self.myscore()
                        time.sleep(2)
                        break
                elif i == "q" or i == "Q":
                    self.lets_quit()
                    break
                
                else:
                    print(Fore.WHITE + Back.RED + "Wrong choise"+ Fore.RESET + Back.RESET)
                    call = False
                    time.sleep(2)
                
            except:
                print(Fore.WHITE + Back.RED + "ERROR ERROR ERROR"+ Fore.RESET + Back.RESET)
                call = False
                time.sleep(2)
                break
    
    def game_duration(self):
        self.score = 0
        call = True
        while True:
            os.system("cls")
            self.logo()
            print("\nGame Mode : Duaration")
            if call == True:
                self.random_choise_1()
                self.random_choise_2()
            else:
                pass
            
            print(f"\n\033[2;36m{self.name_1}\033[1;0m Duration is \033[2:37m{self.duration_1}\033[1;0m")
            print(f"\033[2;36m{self.name_2}\033[1;0m Duration will be Higher or Lower ? {self.duration_2}")
            i = input("Choise 'h' or 'l' (q for quit) : " )
            try:
                if i == "h":
                    if self.duration_1 == self.duration_2:
                        print(f"\n\033[2;36mSame rating\033[1;0m \n- {self.name_2} Rating is {self.duration_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    elif self.duration_1 < self.duration_2:
                        print(f"\n\033[2;32mYou Win\033[1;0m \n- {self.name_2} Ranking is {self.duration_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r{self.name_2} Ranking is {self.duration_2}")
                        time.sleep(2)
                        os.system("cls")
                        self.logo()
                        self.myscore()
                        time.sleep(2)
                        break
                        
                elif i == "l":
                    if self.duration_1 == self.duration_2:
                        print(f"\n\033[2;36mSame rating\033[1;0m{self.name_2} Rating is {self.duration_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    elif self.duration_1 > self.duration_2:
                        print(f"\n\033[2;32mYou Win\033[1;0m \n- {self.name_2} Ranking is {self.duration_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r\033[22;31m{self.name_2} Ranking is {self.duration_2}\033[1;m")
                        time.sleep(2)
                        os.system("cls")
                        self.logo()
                        self.myscore()
                        time.sleep(2)
                        break
                else:
                    print(Fore.WHITE + Back.RED + "Wrong choise"+ Fore.RESET + Back.RESET)
                    call = False
                    time.sleep(2)
            except:
                print(Fore.WHITE + Back.RED + "ERROR ERROR ERROR"+ Fore.RESET + Back.RESET)
                call = False
                time.sleep(2)
                break

    def game_year(self):
        self.score = 0
        call = True
        while True:
            os.system("cls")
            self.logo()
            print("\nGame Mode : Year")
            if call == True:
                self.random_choise_1()
                self.random_choise_2()
            else:
                pass
            
            print(f"\n\033[2;36m{self.name_1}\033[1;0m Released in  \033[2:37m{self.year_1}\033[1;0m")
            print(f"\033[2;36m{self.name_2}\033[1;0m Released year will be Higher or Lower ? ")
            i = input("Choise 'h' or 'l' (q for quit) : " )
            try:
                if i == "h":
                    if self.year_1 == self.year_2:
                        print(f"\n\033[2;36mSame Year Released\033[1;0m \n- {self.name_2} Released in {self.year_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    elif self.year_1 < self.year_2:
                        print(f"\n\033[2;32mYou Win\033[1;0m \n- {self.name_2} Released in {self.year_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r{self.name_2} Released in {self.year_2}")
                        time.sleep(2)
                        os.system("cls")
                        self.logo()
                        self.myscore()
                        time.sleep(2)
                        break
                        
                elif i == "l":
                    if self.year_1 == self.year_2:
                        print(f"\n\033[2;36mSame rating\033[1;0m{self.name_2} Released in {self.year_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    elif self.year_1 > self.year_2:
                        print(f"\n\033[2;32mYou Win\033[1;0m \n- {self.name_2} Released in {self.year_2}")
                        self.score = self.score + 1
                        time.sleep(1)
                        call = True
                    else:
                        self.slowType("\r\n\033[1;31mYou lose......\033[1;m", 0.1, newLine=False)
                        print(f"\r\033[22;31m{self.name_2} Released in {self.year_2}\033[1;m")
                        time.sleep(2)
                        os.system("cls")
                        self.logo()
                        self.myscore()
                        time.sleep(2)
                        break
                else:
                    print(Fore.WHITE + Back.RED + "Wrong choise"+ Fore.RESET + Back.RESET)
                    call = False
                    time.sleep(2)
            except:
                print(Fore.WHITE + Back.RED + "ERROR ERROR ERROR"+ Fore.RESET + Back.RESET)
                call = False
                time.sleep(2)
                break

    def settings_menu(self):
        os.system("cls")
        self.logo()
        time.sleep(2)
        print("\033[22;35m\nSelect Any One Option from below : \033[0m")
        print("1. Modify Database Type : ")
        print("2. Change Name of local Database")
        print("3. Credits")
        print("4. Exit the Program")
        
        choise = input("Choise Any one : ")
        while True:
            time.sleep(1)
            if choise == "1":
                i = input("""\n- Write "local" or "Mongo" : """)
                if i == "local":
                    self.local_data = True
                    print("- Database Switched to local Succesfully")
                    time.sleep(2)
                    self.main_menu()
                    break
                    
                elif i == "Mongo":
                    
                    self.local_data = False
                    print("- Database Switched to MongoDB Succesfully")
                    time.sleep(2)
                    self.main_menu() 
                    break
                else:
                    print("Please Enter the Valid Input : ")
            elif choise == "2":
                pass
            elif choise == "3":
                pass
            elif choise == "4":
                pass
            elif choise == "5":
                self.slowType("\033[1;31mExiting.......\033[0m", 0.03, newLine=False)
                os.system("cls")
                exit()
                
            else:
                print(Fore.RED + "Please Enter The Valid Input ! " + Fore.RESET)
                time.sleep(2)
                self.main_menu()
    def main_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        if os.name == "nt":  # If the system is windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Movie Analysis - Made by Jayesh Vegda")  # Change the
        else:  # Or if it is unix
            print(f'\33]0;Movie Analysis - Made by Jayesh Vegda\a',
                  end='', flush=True)  # Update title of command prompt
        os.system("cls")
        self.logo()
        time.sleep(2)
        print("\033[22;35m\nSelect Any One Option from below : \033[0m")
        print("1. Lets Play Game")
        print("2. Modify Settings")
        print("3. Credits")
        print("4. Exit the Program")
        
        choise = input("Choise Any one : ")
        while True:
            time.sleep(1)
            if choise == "1":
                self.game_menu()
                break
            elif choise == "2":
                self.settings_menu()
                break
            elif choise == "3":
          
                break
            elif choise == "4":
           
                break
            elif choise == "5":
                self.slowType("\033[1;31mExiting.......\033[0m", 0.03, newLine=False)
                os.system("cls")
                exit()
                
            else:
                print(Fore.RED + "Please Enter The Valid Input ! " + Fore.RESET)
                time.sleep(2)
                self.main_menu()

    def game_menu(self):
        os.system("cls")
        self.logo()
        if self.local_data == True:
            print("\n\033[22;35mSelect Any One Option from below : \033[0m")
            print("1. Game by Rating")
            print("2. Game by Duration")
            print("3. Game by Year")
            print("4. Return to Main Menu")
            choise = input("Choise Any one : ")
        
            while True:
                time.sleep(1)
                if choise == "1":
                    self.game_rating()
                    break
                elif choise == "2":
                    self.game_duration()
                    break
                elif choise == "3":
                    self.game_year()
                    break
                elif choise == "4":
                    self.main_menu()
                    break
                else:
                    print(Fore.RED + "Please Enter The Valid Input ! " + Fore.RESET)
                    time.sleep(2)
                    self.game_menu()
        else:
            print("\n\033[22;35mSelect Any One Option from below : \033[0m")
            print("1. Game by Ranking")
            print("2. Game by Rating")
            print("3. Game by Duration")
            print("4. Game by Year")
            print("5. Return to Main Menu")
                
            choise = input("Choise Any one : ")
            
            while True:
                time.sleep(1)
                if choise == "1":
                    self.game_ranking()
                    break
                elif choise == "2":
                    self.game_rating()
                    break
                elif choise == "3":
                    self.game_duration()
                    break
                elif choise == "4":
                    self.game_year()
                    break
                elif choise == "5":
                    self.main_menu()
                    break
                else:
                    print(Fore.RED + "Please Enter The Valid Input ! " + Fore.RESET)
                    time.sleep(2)
                    self.game_menu()
                
    def myscore(self):
        if self.score == 0:
            print("\n\033[2;31mBetter Luck Next Time !\033[1;0m")
            print(f"\033[1;32mYour Total Score is \033[1;32m{self.score}\033[1;0m")
            input("\nPlease Press enter to return Main Menu : ")
            time.sleep(1)
            self.main_menu()
        elif self.score >= 1 and self.score < 5:
            print("\n\033[22;32mVery Good !\033[1;0m")
            print(f"\033[1;32mYour Total Score is \033[1;32m{self.score}\033[1;0m")
            input("\nPlease Press enter to return Main Menu : ")
            time.sleep(1)
            self.main_menu()
        elif self.score >= 5 and self.score < 10:
            print("\n\033[22;34mExcellent !\033[1;0m")
            print(f"\033[1;32mYour Total Score is \033[1;32m{self.score}\033[1;0m")
            input("\nPlease Press enter to return Main Menu : ")
            time.sleep(1)
            self.main_menu()
        elif self.score >= 10 and self.score < 20:
            print("\n\033[22;34mOutstanding !\033[1;0m")
            print(f"\033[1;32mYour Total Score is \033[1;32m{self.score}\033[1;0m")
            input("\nPlease Press enter to return Main Menu : ")
            time.sleep(1)
            self.main_menu()
        elif self.score >= 20 and self.score < 30:
            print("\n\033[22;30;47mUnbelievable !\033[1;0m")
            print("You are a Genius ! ")
            print(f"\033[1;32mYour Total Score is {self.score}\033[1;0m")
            input("\nPlease Press enter to return Main Menu : ")
            time.sleep(1)
            self.main_menu()
        else:
            print("\n\033[22;32mYou are a Cheater ! ")
            print(f"\033[1;32mYour Total Score is \033[1;32m{self.score}\033[1;0m")
            input("\nPlease Press enter to return Main Menu : ")
            time.sleep(1)
            self.main_menu()
        time.sleep(2)
        
   
                
r = ran()
r.main_menu()
