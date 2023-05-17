import os
import requests
import random
import json
import os


class newpaper:
    def __init__(self):
        self.api_key = "5486b438363b4124842d7325f4c69198"
        self.country = "in"
        self.base_url = "https://newsapi.org/v2/top-headlines?country={self.country}&apiKey={self.api_key}"

    def get_news(self):
        url = self.base_url.format(self=self)
        res = requests.get(url)
        s = res.text
        found = json.loads(s)
        print("We have Found Total", found['totalResults'], "For You!")
        
        while True:
            i = random.choice(found['articles'])
            i_title = i['title']
            i_description = i['description']
            i_url = i['url']
            print(f"\n- {i_title}\n- {i_description}\n")
            i = input("Yes or no")
            if i == 'yes':
                pass
            elif i == 'no':
                break
            else:
                print("invalid input")
        

    def main_menu(self):
        os.system("cls")
        print("Welcome to the News API")
        print("1. Get News")
        print("2. Settings")
        print("3. Exit")
        print("Enter your choice")
        choice = input()
        while True:
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
                print("invalid input")