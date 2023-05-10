import requests
import json
import time
import os

class Link_shortener:
    
    def __init__(self):
        self.api = "Y249YB4EXAst3VjeIoRwct2kylO9s62Uta4OzvJoTa4WwbDt36GXb9PLpaxO"
        self.url = f"https://t.ly/api/v1/link/shorten?{self.api}"
    
    
    def logo(self):
        print(""" 
        ███╗░░░███╗██╗░░░██╗  ░██████╗██╗░░██╗░█████╗░██████╗░████████╗███╗░░██╗███████╗██████╗░
        ████╗░████║╚██╗░██╔╝  ██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝████╗░██║██╔════╝██╔══██╗
        ██╔████╔██║░╚████╔╝░  ╚█████╗░███████║██║░░██║██████╔╝░░░██║░░░██╔██╗██║█████╗░░██████╔╝
        ██║╚██╔╝██║░░╚██╔╝░░  ░╚═══██╗██╔══██║██║░░██║██╔══██╗░░░██║░░░██║╚████║██╔══╝░░██╔══██╗
        ██║░╚═╝░██║░░░██║░░░  ██████╔╝██║░░██║╚█████╔╝██║░░██║░░░██║░░░██║░╚███║███████╗██║░░██║
        ╚═╝░░░░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝""")

    def shorten(self):
        os.system("cls")
        self.logo()
        print("\n1. Enter the URL to shorten the below !")
        long_url = input("Enter the URL: ")
        input("Press Enter to Grenate a short Link")
        print(self.url)
        data = {
        "long_url": long_url
        }

        head = {
        "Content-Type": "application/json"
        }

        
        req = requests.post(self.url, data=data, headers=head)
        dump = req.json()
        result = dump["short_url"]
        print(f"Your Short Link is: {result}")
                
        
    
    def setting(self):
        pass
    
    def credit(self):
        pass
    
    def leave(self):
        pass
    
    def start(self):
        self.logo()
        print("\nSelect any one Option from below")
        print("1. Genrate a short Link")
        print("2. Modify Settings")
        print("3. Credits")
        print("4. Exit the program")
        start_input = int(input("Enter your choice: "))
        
        if start_input == 1:
            self.shorten()
        elif start_input == 2:
            self.setting()
        elif start_input == 3:
            self.credit()
        elif start_input == 4:
            self.leave()
        else:
            print("Invalid Input")
        



base_url = "https://t.ly/api/v1/link/shorten?api_token=Y249YB4EXAst3VjeIoRwct2kylO9s62Uta4OzvJoTa4WwbDt36GXb9PLpaxO"

data = {
    "long_url": "https://github.com/logicguy1/Discord-Nitro-Generator-and-Checker/blob/main/main.py"
}

head = {
    "Content-Type": "application/json"
}

c = Link_shortener()
c.start()
