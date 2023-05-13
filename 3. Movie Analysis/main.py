import pymongo
import time
import os
import re
import sys
import colorama
from colorama import Fore, Back
import pandas as pd


class movieanal:
    def __init__(self):
        self.year = 0
        self.name = ""
        self.rate = 0
        self.valid_input = False
        self.valid_input_name = False
        self.valid_input_rate = False
        self.sleep_1 = time.sleep(1)
        self.sleep_2= time.sleep(2)
        self.db_name = "LetterBox"
        self.db_collection = "rating"
        self.myurl = 'mongodb://localhost:27017/'
        self.client = pymongo.MongoClient(self.myurl)
        
    def Connection(self):
        db = self.client[self.db_name]
        collection = db[self.db_collection]
        return collection
        
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  # Loop over the message
            # Print the one charecter, flush is used to force python to print the char
            print(i, end="", flush=True)
            time.sleep(speed)  # Sleep a little before the next one
            if newLine:  # Check if the newLine argument is set to True
                print()               
    def main_logo(self):
        print("""
              
        ███╗░░░███╗░█████╗░██╗░░░██╗██╗███████╗  ░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
        ████╗░████║██╔══██╗██║░░░██║██║██╔════╝  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
        ██╔████╔██║██║░░██║╚██╗░██╔╝██║█████╗░░  ╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
        ██║╚██╔╝██║██║░░██║░╚████╔╝░██║██╔══╝░░  ░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
        ██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░██║███████╗  ██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
        ╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚══════╝  ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
                                        \033[22;34;41m Made By Jayesh Vegda \033[0m                                      """)
    def logo(self):
            self.Connection()
            print("""
                
            ███╗░░░███╗░█████╗░██╗░░░██╗██╗███████╗  ░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
            ████╗░████║██╔══██╗██║░░░██║██║██╔════╝  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
            ██╔████╔██║██║░░██║╚██╗░██╔╝██║█████╗░░  ╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
            ██║╚██╔╝██║██║░░██║░╚████╔╝░██║██╔══╝░░  ░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
            ██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░██║███████╗  ██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
            ╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚══════╝  ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝""")
    def start_logo(self):
        os.system("cls")
        self.logo()
        self.sleep_1        
    def movie_year_search(self):
        while True:
            try:
                os.system("cls")
                self.logo()
                self.year = input("\nEnter the year of movie you wanna search (1800-2023) : ")
                self.slowType("Searching.........", .03, newLine=False)
                sys.stdout.flush()
                time.sleep(1)
                count = 0
                if int(self.year) >= 1800 and int(self.year) <= 2023:
                    print("\r\033[1;31mHere is your result\n\033[1;32m")
                    print(f"Result of Year : {self.year}")
                    movie_count = 0
                    for i in self.Connection().find({"Year": int(self.year)}):
                        movie_count = movie_count + 1
                        name = i.get("Name", "Not Avalible")
                        year = i.get("Year", "Not Avalible")
                        rate = i.get("Rating", "Not Avalible")
                        # print(f"Name: {name} \nYear: {year} \nRating: {rate} \n")
                        print(f"{name} ({year}) - Rating: {rate}")
                    print(f"\n\033[1;34mYou Have Watched {movie_count} in Year {self.year}")
                    see = input("\n\033[0mPress Enter to Search or Write 'quit' to return : ")
                    
                    if see.strip() == "":
                        pass
                    elif see == "quit" or see == "exit":
                        break
                    else:
                        print("Error Occure")
                        time.sleep(2)
                        break
                else:
                    print("\r\033[1;31mEnter Year Between 1800 to 2023 only\033[0m")
                    time.sleep(2)
                    self.movie_year_search()
                    count += 1
                    if count >= 3:
                        print("\r\033[1;31mToo many invalid inputs. Exiting.\033[0m")
                        break
                    break
            except ValueError:
                print("\r\033[1;31mInvalid Input\033[0m")
                time.sleep(2)
                self.movie_year_search()
                break

        
        # valid_input = False
        
        # while not valid_input:
        #     try: 
        #         if int(self.year) > 1800 and int(self.year) < 2024:
        #             print(f"Result of Year : {self.year}")
        #             movie_count = 0
        #             for x in self.Connection().find({"Year": int(self.year)}):
        #                 movie_count = movie_count + 1
        #                 name = x["Name"]
        #                 print(f"{movie_count}. {name}")
                        
        #             print(f"\nYou Have Watch Total {movie_count} in Year {self.year}")
                    
        #         else:
        #             print("Enter Year Between 1800 to 2024 only")
        #             time.sleep(1)
        #             self.movie_year_search()
        #     except ValueError:
        #         print("Invalid Input")
        #         time.sleep(1)
        #         self.movie_year_search()
    def movie_search_by_name(self):
        while True:
            try:
                os.system("cls")
                self.logo()
                self.sleep_1
                self.name = input("\nEnter the Name of movie : ")
                self.slowType("Searching.........", .03, newLine=False)
                sys.stdout.flush()
                time.sleep(1)
                pattern = re.compile(f".*{self.name}.*", re.IGNORECASE)
                results = self.Connection().find({ "Name": pattern })
                check = list(results)
                time.sleep(1)
                count = 0
                movie_count = 0
                if not check :
                    print("\r\033[1;31mSorry We Cound't Found Your Movie")
                    time.sleep(2)
            
                elif check:
                    pattern = re.compile(f".*{self.name}.*", re.IGNORECASE)
                    results = self.Connection().find({ "Name": pattern})
                    print("\r\033[1;31mHere is your result\n\033[1;32m")
                   
                    
                    for result in results:
                        movie_count = movie_count + 1
                        name = result["Name"]
                        year = result.get("Year", "Not Avaliable")
                        rate = result.get("Rating", "Not Avaliable")
                        print(f"{movie_count}. {name} ({year}) - Rating: {rate}")
                    
                    see = input("\n\033[0mPress Enter to Search or Write 'quit' to return : ")
                    sys.stdout.flush()
                    if see.strip() == "":
                        pass
                    elif see == "quit" or see == "exit":
                        self.slowType("\r\033[1;31mReturning to the main menu....\033[0m", 0.1, newLine=False)
                        time.sleep(1)
                        self.main_menu()
                        break
                    else:
                        print("Error Occure")
                        time.sleep(2)
                        break
                                    
                else:
                    print("\r\033[1;31mSorry We Could't Found Your Movie\033[0m")
                    time.sleep(2)
                                
            except ValueError:
                print("\r\033[1;31mInvalid Input\033[0m")
                time.sleep(1)
                break

        
        
        
        # name = input("Enter Name that you want to search : ")
        # print("Searching....")
        # check = list(name)
        # valid = True
        # while True:
        #     try: 
        #         valid = True
        #        for result in results:
        #             name = result["Name"]
        #             year = result["Year"]
        #             rating = result["Rating"]
        #         
        #             print(f"Name: {name}, Year: {year}, Rating: {rating}")
        #         i = input("Click Enter")  
        #         if i.strip() == "":
        #             break 
        #         else:
        #             self.movie_search_by_name()                 
        #     except:
        #         valid = False
        #         print("Sorry We Cound't Found Your Movie")
        #         print("Please Try Again.....")
        #         time.sleep(2)
        #         self.movie_search_by_name()   
    def movie_search_by_rating(self):
        while True:
            try:
                os.system("cls")
                self.logo()
                self.sleep_1
                self.rate = float(input("Enter the Rating You want Search : "))
                self.slowType("Searching.........", .03, newLine=False)
                sys.stdout.flush()
                time.sleep(1)
                if self.rate == int(self.rate) or self.rate % 1 == 0.5:
                    if 1 <= self.rate <= 5:
                        print("\r\033[1;31mHere is your result\n\033[1;32m")
                        result = self.Connection().find({"Rating": self.rate})
                        for i in result:
                            name = i.get("Name", "Not Avalible")
                            year = i.get("Year", "Not Avalible")
                            rate = i.get("Rating", "Not Avalible")
                            # print(f"Name: {name} \nYear: {year} \nRating: {rate} \n")
                            print(f"{name} ({year}) - Rating: {rate}")
                        see = input("\n\033[0mPress Enter to Search or Write 'quit' to return : ")
                        if see.strip() == "":
                            pass
                        elif see == "quit" or see == "exit":
                            break
                        else:
                            print("Error Occure")
                            time.sleep(2)
                            break

                    else:
                        print("\rNumber out of range. Please enter a number between 1 and 5.")
                        time.sleep(2)
                        
                else:
                    print("Invalid input. Please enter an integer or a float with .5 as decimal in 1 to 5.")
                    time.sleep(2)                  
            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(2)
    def main_menu(self):
        os.system("cls")
        self.main_logo()
        time.sleep(2)
        print("\033[22;35m\nSelect Any One Option from below : \033[0m")
        print("1. Movie Advance Search")
        print("2. Import Your Data")
        print("3. Modify Settings")
        print("4. Credits")
        print("5. Exit the Program")
        
        choise = int(input("Choise Any one : "))
        
        if choise == 1:
            self.movie_search_by_name()
        elif choise == 2:
            self.imp_data()
        elif choise == 3:
            self.my_setting()
        elif choise == 4:
            self.credit()
        elif choise == 5:
            exit()
        else:
            print("Error Occure")
            time.sleep(2)
    def imp_data(self):
        self.start_logo()
        print("\nMake Sure that your file name is 'rating.csv' in MovieAnalysis Folder !")
        see = input("- Are you sure to Continue (y/n) : " )
        if see == "y" or see == "Y" or see == "yes" or see == "YES":
            csv_file = os.path.dirname(os.path.abspath(__file__))
            p = pd.read_csv(f'{csv_file}/ratings.csv')
            ask_db = input("1. Enter Your Database name : ")
            ask_col = input("2. Enter Your Collection Name : ")
            self.db_name = ask_db
            self.db_collection = ask_col
            data = p.to_dict('records')
            self.Connection().insert_many(data)
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client.list_database_names()
            if self.db_name in db:
                print(f"- {self.db_name} is Created Succesfully !")
            else:
                print(f"- ERROR : {self.db_name} is Unsucessfull !")
        else:
            pass
    def movie_menu(self):
        self.start_logo()
        print("\n\033[22;35mSelect Any One Option from below : \033[0m")
        print("1. Movie Search by Name")
        print("2. Movie Search by Year")
        print("3. Movie Search by Rating")
        print("4. Return to Main Menu")
        
        choise = int(input("Choise Any one : "))
        
        while True:
            if choise == 1:
                self.movie_search_by_name()
                break
            elif choise == 2:
                self.movie_year_search()
                break
            elif choise == 3:
                self.movie_search_by_rating()
                break
            elif choise == 4:
                self.main_menu()
                break
            else:
                print(Fore.RED + "Please Enter The Valid Input ! " + Fore.RESET)
                time.sleep(2)
                self.movie_menu()
        
    def my_setting(self):
        self.start_logo()
        print("\n\033[22;35mSelect Any One Option from below : \033[0m")
        print("1. Configure Database")
        print("2. Exit the Program")
        
        choise = int(input("Choise Any one : "))
        
        if choise == 1:
            try:
                self.start_logo()

                ask_client = input("\n\033[0m1. Enter Your Only MongoDB Link (enter to default): ")
                if ask_client.strip() == "":
                    self.myurl = "mongodb://localhost:27017/"
                    print(f"\033[1;32m- {self.myurl} link has been successfully connected.\033[0m")
                elif ask_client != "":
                    self.myurl = ask_client
                    print("\033[1;32m- Your client link has been successfully connected.\033[0m")
                else:
                    print(Back.RED + "Error Occure" + Back.RESET)
                    time.sleep(2)
                    self.my_setting()
                    
                    
                while True:
                    ask_db = input("\n\033[0m2. Enter Your Database Name : ")
                    if ask_db.strip() == "":
                        print("\033[1;31m- Error : Please Provide Valid Name\033[0m")
                    elif ask_db.strip() != "":
                        self.db_name = ask_db
                        print(f"\033[1;32m- {self.db_name} Database Name has been successfully established.\033[0m")
                        break
                    else:
                        print(Back.RED + "Error Occure" + Back.RESET)
                        time.sleep(2)
                        self.my_setting()
                    
                while True:
                    ask_collection = input("\n3. Enter Your Collection Name : ")
                    if ask_collection.strip() == "":
                        print("\033[1;31m- Error : Please Provide Valid Name\033[0m")
                    elif ask_collection.strip() != "":
                        self.db_collection = ask_collection
                        print(f"\033[1;32m- {self.db_collection} Collection Name has been successfully established.\033[0m")
                        break
                    else:
                        print(Back.RED + "Error Occure" + Back.RESET)
                        time.sleep(2)
                        self.my_setting()
                
                print(F"\n- Your configuration has successfully established.")
                input("Please Enter to return Main Menu....")
                self.main_menu()
            except:
                print(Back.RED + "Error Occure" + Back.RESET)
                time.sleep(2)
                self.my_setting()
    
    def credit(self):
        self.start_logo()
        print("""\n- Created By: Jayesh Vegda \n- Github: https://github.com/Jayesh.Vegda \n- Email: Jayeshvegda@gmail.com \n- Twitter: https://twitter.com/Jayesh.Vegda \n- Instagram: https://www.instagram.com/Zayu.Vegda \n""")
        input("\nPlease Enter to Return to Main Menu: ")
        self.main_menu()
       
if __name__ == "__main__":
    
    obj = movieanal()
    obj.movie_menu()