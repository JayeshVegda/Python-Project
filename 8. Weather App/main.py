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
        self.api_key = self.accss_setting()['api']
        self.location = self.accss_setting()['location']
        self.base_url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.location}&aqi=yes"
    
    def path(self):
        cwd = os.path.dirname(os.path.realpath(__file__))
        return cwd + "/settings.json"

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
        condition = found["current"]['condition']['text']

        wind_mph = found["current"]['wind_mph']
        wind_kph = found["current"]['wind_kph']
        wind_degree = found["current"]['wind_degree']
        wind_dir = found["current"]['wind_dir']
        pressure_mb = found["current"]['pressure_mb']
        pressure_in = found["current"]['pressure_in']
        precip_mm = found["current"]['precip_mm']
        precip_in = found["current"]['precip_in']
        pressure_mb = found["current"]['pressure_mb']
        humidity = found["current"]['humidity']
        cloud = found["current"]['cloud']
        uv = found["current"]['uv']

        # Air Quality

        co = found["current"]['air_quality']['co']
        no2 = found["current"]['air_quality']['no2']
        o3 = found["current"]['air_quality']['o3']
        so2 = found["current"]['air_quality']['so2']
        pm2_5 = found["current"]['air_quality']['pm2_5']
        pm10 = found["current"]['air_quality']['pm10']
        us = found["current"]['air_quality']['us-epa-index']
        uk = found["current"]['air_quality']['gb-defra-index']

        stater = f"in, its a {condition} Day here temprature is {temp_c} and it feels like {feelslike_c}"
        another = f"The Weather is {condition} in {name}, {region}, {country} \nThe temperature here is {temp_c} degrees, but it feels like {feelslike_c}."
        print(another)
        choice = input("Do You Want to more info (y/n) ? : ")
        if choice == "y":
            self.logo_settings()
            print(Fore.CYAN + "Location" + Style.RESET_ALL)
            print("- City :", name)
            print("- State :", region)
            print("- Country :", country)

            print(Fore.CYAN + "\nTime Zone" + Style.RESET_ALL)
            print("- Time :", locatime)
            print("- Time-Zone  :", timezone)

            print(Fore.CYAN + "\nTemperature" + Style.RESET_ALL)
            print("- Weather :", condition)
            print("- Temperature (Celsius) :", temp_c)
            print("- Temperature (Fahrenheit)   :", temp_f)
            print("- Feel like Temperature (Celsius) :", feelslike_c)
            print("- Feel Temperature (Fahrenheit)   :", feelslike_f)

            print(Fore.CYAN + "\nWind Force" + Style.RESET_ALL)
            print("- Wind Direction :", wind_dir)
            print("- Wind Degree :", wind_degree)
            print("- Wind Force (kPH) :", wind_kph)
            print("- Wind Force (mPH) :", wind_mph)
            
            print(Fore.CYAN + "\nPressure" + Style.RESET_ALL)
            print("- Preesure (mb) :", pressure_mb)
            print("- Preesure (in) :", pressure_in)

            print(Fore.CYAN + "\nSky Report" + Style.RESET_ALL)
            print("- Cloud :", cloud)
            print("- Chance of Rain :", precip_in)
            print("- Humidity :", humidity)
            print("- UV Rays :", uv)

            print(Fore.CYAN + "\nAir Quality" + Style.RESET_ALL)
            print("- Carbon  :", co)
            print("- Nitrogen :", no2)
            print("- Ozone :", o3)
            print("- Particulate Matter :", pm2_5)
            print("- US Index Quality :", us)
            print("- GB Index Quality :", uk)
            input("\nPress Enter To return Main Menu : ")
            self.main_menu()
        elif choice == "n":
            self.main_menu()
        else:
            print("Invalid Input")
            self.check_weather()

    def accss_setting(self):
        p = self.path()
        with open(p, "r") as file:
            data = json.load(file)
            self.api_key = data["api"]
            self.location = data["location"]
            self.base_url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.location}&aqi=yes"
        return data 
        
    def change_preferences(self):
        self.logo_settings()
        print(Fore.CYAN + "Select any one option from below:" + Style.RESET_ALL)
        print("1. Set Default Location")
        print("2. Change Api Key")
        print("3. Return To Main Menu")
        choice = input(Fore.CYAN + "Enter Your Choice : " + Style.RESET_ALL)
        if choice == "1":
            p = self.path()
            self.logo_settings()
            new_location = input("Enter Your New Location : ")
            ok = self.accss_setting()
            ok["location"] = new_location
            with open(p, "w") as file:
                json.dump(ok, file)
                print(Fore.CYAN + "Location Changed Successfully" + Style.RESET_ALL)
            input("\nPress Enter To Return To Main Menu : ")
            self.main_menu()

        elif choice == "2":
            pass
        elif choice == "3":
            self.main_menu()
        else:
            print("Invalid Choice. Please Try Again")
            self.change_preferences()

    def credits(self):
        stater().Credits()
        input("Please Enter to Return to Main Menu: ")
        self.main_menu()


if __name__ == "__main__":
    i = main()
    i.main_menu()