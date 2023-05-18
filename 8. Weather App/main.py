import json
import requests
import os
from colorama import Fore, Back, Style

class stater:
    def __init__(self):
        self.logo = ""
    
    def set_logo(self):
        print(""" 
        __        __         _   _                    _                
        \ \      / /__  __ _| |_| |__   ___ _ __     / \   _ __  _ __  
         \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|   / _ \ | '_ \| '_ \ 
          \ V  V /  __/ (_| | |_| | | |  __/ |     / ___ \| |_) | |_) |
           \_/\_/ \___|\__,_|\__|_| |_|\___|_|    /_/   \_\ .__/| .__/ 
                                                          |_|   |_|    
        """)
        
    def logo_settings(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.set_logo()
        print("")
    
    def Credits(self):
        self.logo_settings()
        print(Fore.BLUE + "Author : " + Style.RESET_ALL + "Jayesh Vegda")            
        print(Fore.BLUE + "Email : " + Style.RESET_ALL + "Jayeshvegda198@gmail.com")            
        print(Fore.BLUE + "GitHub : " + Style.RESET_ALL + "https://github.com/Jayesh.Vegda")            
        print(Fore.BLUE + "Twitter : " + Style.RESET_ALL + "https://twitter.com/Jayesh.Vegda")            
        print(Fore.BLUE + "Instagram : " + Style.RESET_ALL + "https://instagram.com/Zayu.Vegda")                      

class main(stater):
    def __init__(self):
        self.name = ""
        self.api_key = "61907108014d4a438e491401231705"
        self.location = "Jamnagar"
        self.base_url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.location}&aqi=yes"
    
    def main_menu(self):
        while True:
            stater().logo_settings()
            print(Fore.CYAN + "Select any one option from below:" + Style.RESET_ALL)
            print("1. Check the Weather")
            print("2. Change Preferences")
            print("3. Credits")
            print("4. Exit The Program")
            
            choice = input(Fore.CYAN + "Enter Your Choice: " + Style.RESET_ALL)
            if choice == "1":
                self.check_weather()
                break
            elif choice == "2":
                self.change_preferences()
                break
            elif choice == "3":
                self.credits()
                break
            elif choice == "4":
                exit()
                break
            else:
                print("Invalid Choice. Please Try")           
    
    def fatch_data(self):
        try:
            r = requests.get(self.base_url)
            data = json.loads(r.text)
            return data
        except:
            print("Invalid URL. Please Try Again")
            self.fatch_data()
            
    def check_weather(self):
        found = self.fatch_data()
        self.logo_settings()
        
        name = found["location"]["name"]
        region = found["location"]["region"]
        country = found["location"]["country"]
        timezone = found["location"]["tz_id"]
        locatime = found["location"]["localtime"]
        temp_c = found["current"]["temp_c"]
        temp_f = found["current"]["temp_f"]
        humidity = found["current"]["humidity"]
        feelslike_c = found["current"]["feelslike_c"]
        feelslike_f = found["current"]["feelslike_f"]
        condition = found["current"]["condition"]['text']

        stater = f"in, its a {condition} Day here temprature is {temp_c} and it feels like {feelslike_c}"
        another = f"The Weather is {condition} in {name}, {region}, {country} \nThe temperature here is {temp_c} degrees, but it feels like {feelslike_c}."
        print(another)
        
        
    def change_preferences(self):
        pass
    def credits(self):
        stater().logo_settings()
        input("Please Enter to Return to Main Menu: ")
        self.main_menu()

if __name__ == "__main__":
    i = main()
    i.main_menu()