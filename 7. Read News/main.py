import os
import requests
import random
import json
import os
import time


class newpaper:
    def __init__(self):
        self.api_key = "5486b438363b4124842d7325f4c69198"
        self.country = "in"
        self.categories = ""
        self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
        
        
    def logo(self):
        print(""" 
              
        /$$   /$$                                         /$$$$$$$$ /$$                        
        | $$$ | $$                                        |__  $$__/|__/                        
        | $$$$| $$  /$$$$$$  /$$  /$$  /$$  /$$$$$$$         | $$    /$$ /$$$$$$/$$$$   /$$$$$$ 
        | $$ $$ $$ /$$__  $$| $$ | $$ | $$ /$$_____/         | $$   | $$| $$_  $$_  $$ /$$__  $$
        | $$  $$$$| $$$$$$$$| $$ | $$ | $$|  $$$$$$          | $$   | $$| $$ \ $$ \ $$| $$$$$$$$
        | $$\  $$$| $$_____/| $$ | $$ | $$ \____  $$         | $$   | $$| $$ | $$ | $$| $$_____/
        | $$ \  $$|  $$$$$$$|  $$$$$/$$$$/ /$$$$$$$/         | $$   | $$| $$ | $$ | $$|  $$$$$$$
        |__/  \__/ \_______/ \_____/\___/ |_______/          |__/   |__/|__/ |__/ |__/ \_______/
                                                                                                """)
    
    
    def settings(self):
        while True:
            os.system("cls")
            self.logo()
            print("Select any option from below")
            print("1. Change Country")
            print("2. Cutomize Categories")
            print("3. Modify API Key")
            print("4. Return Main Menu")
            choice = input("Enter You Choice : ")
            
            if choice == '1':
                self.select_country()
                break
            elif choice == '2':
                self.select_categories()
                break
            elif choice == '3':
                api = input("\n- Enter Your API Key : ")
                self.api_key = api
                print("- Your Api Key has been Succesfully Changed!")
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                time.sleep(2)
                self.main_menu()
                
            elif choice == '4':
                self.main_menu()
                break
            else:
                print("Invalid Input")

       
    def select_country(self):
        os.system('cls')
        self.logo()
        country_codes = {
            'United States': 'us',
            'Canada': 'ca',
            'United Kingdom': 'uk',
            'Australia': 'au',
            'Germany': 'de',
            'France': 'fr',
            'Italy': 'it',
            'China': 'cn',
            'India': 'in',
            'Brazil': 'br',
            'Mexico': 'mx',
            'Russia': 'ru',
            'United Arab Emirates': 'ae',
            'Argentina': 'ar',
            'Aruba': 'aw',
            'Bulgaria': 'bg',
            'Botswana': 'bw',
            'Costa Rica': 'cr',
            'Czech Republic': 'cz',
            'Denmark': 'dk',
            'Egypt': 'eg',
            'France': 'fr',
            'United Kingdom': 'gb',
            'Greece': 'gr',
            'Hong Kong': 'hk',
            'Indonesia': 'id',
            'Ireland': 'ie',
            'Israel': 'il',
            'India': 'in',
            'Japan': 'jp',
            'South Korea': 'kr',
            'Lithuania': 'lt',
            'Latvia': 'lv',
            'Maldives': 'mv',
            'Mexico': 'mx',
            'Malaysia': 'my',
            'Nigeria': 'ng',
            'Netherlands': 'nl',
            'New Zealand': 'nz',
            'Philippines': 'ph',
            'Poland': 'pl',
            'Portugal': 'pt',
            'Puerto Rico': 'pr',
            'Romania': 'ro',
            'Russia': 'ru',
            'Saudi Arabia': 'sa',
            'Sweden': 'se',
            'Singapore': 'sg',
            'Slovakia': 'sk',
            'Thailand': 'th',
            'Turkey': 'tr',
            'Taiwan': 'tw',
            'Ukraine': 'ua',
            'United States': 'us',
            'Venezuela': 've',
            'South Africa': 'za'
        }

        country_list = list(country_codes.items())

        count = 0
        for key in country_codes:
            count = count + 1
            print(f"{count}. {key}")
            
        select = int(input("Enter country Number : "))
        # Accessing by index
        index = select - 1
        while True:
            if index < len(country_list):
                country_name, country_code = country_list[index]
                print("\n- Selected Country : ", country_name)
                self.country = country_code
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                time.sleep(2)
                self.settings()
            else:
                print("Invalid index!")
                break
                self.select_country()
 
    def select_categories(self):        
        while True:
            os.system("cls")
            print("Select any option from below")
            print("1. All")
            print("2. Business")
            print("3. Entertainment")
            print("4. Genral")
            print("5. Health")
            print("6. Science")
            print("7. Sports")
            print("8. Technology")
            choice = input("Enter You Choice : ")
            if choice == '1':
                self.categories = ""
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                print("\n- Your Category Changed to all")
                time.sleep(1)
                self.main_menu()
                break
            elif choice == '2':
                self.categories = "business"
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                print("\n- Your Category Changed to Business")
                time.sleep(1)
                self.main_menu()
                break
            elif choice == '3':
                self.categories = "entertainment"
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                print("\n- Your Category Changed to Entertainment")
                time.sleep(1)
                self.main_menu()
                break
            elif choice == '4':
                self.categories = "general"
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                print("\n- Your Category Changed to Genral")
                time.sleep(1)
                self.main_menu()
                break
            elif choice == '5':
                self.categories = "health"
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                print("\n- Your Category Changed to Health")
                time.sleep(1)
                self.main_menu()
                break
            elif choice == '6':
                self.categories = "science"
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                print("\n- Your Category Changed to Science")
                time.sleep(1)
                self.main_menu()
                break
            elif choice == '7':
                self.categories = "sports"
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                print("\n- Your Category Changed to Sports")
                time.sleep(1)
                self.main_menu()
                break
            elif choice == '8':
                self.categories = "technology"
                self.base_url = f"https://newsapi.org/v2/top-headlines?country={self.country}&category={self.categories}&apiKey={self.api_key}"
                print("\n- Your Category Changed to Technology")
                time.sleep(1)
                self.main_menu()
                break
            else:
                print("Invalid Input")
                time.sleep(2)
                                    
        
        
    def main_menu(self):
        while True:
            os.system("cls")
            self.logo()
            print("Welcome to the News API")
            print("1. Get News")
            print("2. Settings")
            print("3. Exit")
            choice = input("Enter your choice : ")
            if choice == '1':
                self.get_news()
                break
            elif choice == '2':
                self.settings()
                break
            elif choice == '3':
                exit()
                break
            else:
                time.sleep(2)
    
    def get_news(self):
        url = self.base_url.format(self=self)
        res = requests.get(url)
        s = res.text
        found = json.loads(s)
        os.system("cls")
        self.logo()
        if not found['articles']:
            print("\nError Occure \n- Check Your Internet Connection\n - Check Your Api Key ")
        else:
            print("We have Found Total", found['totalResults'], "For You!")
        time.sleep(3)
        change = True
        while True:
            os.system("cls")
            print(url)
            print(self.base_url)
            print(self.categories)
            self.logo()
            if not found['articles']:
                print("No more articles available.")
                time.sleep(2)
                self.main_menu()
                break
            if change == True:
                i = random.choice(found['articles'])
            else: 
                pass
            
            i_title = i['title']
            i_description = i['description']
            i_url = i['url']
            print(f"\n- {i_title}\n- {i_description}\n")
            ask = input("Do You Want To Continue? (y/n) : ")
            if ask == 'y' or ask == 'Y':
                found['articles'].remove(i)
                change = True
            elif ask == 'n' or ask == 'N':
                self.main_menu()
                break
            else:
                print("invalid input")
                change = False
                time.sleep(21)
                
if __name__ == '__main__':
    n = newpaper()
    n.main_menu()