import requests
import json
import urllib
from tqdm import tqdm
import string
from pathlib import Path
import os
import time


base_url = "https://api.ytbvideoly.com/api/thirdvideo/parse"
ab_path = Path(__file__).parent.absolute()
clean = 'cls' if os.name == 'nt' else 'clear'

class yt_downloader:
    
    def __init__(self):
        self.name = ""
        self.link = ""
        self.vi_list = []
        self.res = 0
        
        
    def logo(self):
         
        print("""              
            ██████╗  ██████╗ ██╗    ██╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
            ██╔══██╗██╔═══██╗██║    ██║████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
            ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  
            ██║  ██║██║   ██║██║███╗██║██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  
            ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║   ██║   ╚██████╔╝██████╔╝███████╗
            ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
                                                                                
              """)
        
    def get_link(self):
        os.system(clean)
        self.logo()
        link = input("\n- Enter the link of video: ")
        self.link = urllib.parse.quote(link)
        time.sleep(1)
        self.download()
    
    def download(self):
        os.system(clean)
        form = f"link={self.link}&from=videodownloaded"
        r = requests.post(base_url, data=form)
        parse = json.loads(r.text)
        if parse['errno'] :
            print(parse['show_msg'])
            print("Please enter the valid url")
            time.sleep(2)
            self.get_link()
        else:
            self.name = parse['data']['title']
            mp4 = parse['data']['videos']['mp4']
            id = 0 
            self.vi_list = []
            for video in mp4:
                video_dict = {}
                id = id + 1 
                video_dict['id'] = id
                video_dict['resolution'] = video['resolution']
                final_s =  video['size']//1000000
                video_dict['size'] = str(final_s) + " MB"
                video_dict['url'] = video['url']
                self.vi_list.append(video_dict)
            self.choise()
        
            
    
    def choise(self):
        os.system(clean)
        count = 0
        self.logo()
        for i in range(len(self.vi_list)):
            count = count + 1
            print(f"{self.vi_list[i]['id']}. {self.vi_list[i]['resolution']} - {self.vi_list[i]['size']}")
        
        choice = int(input("\n- Enter your choice: "))
        print(i)
        while True:
            if choice == 1:
                self.res = 0
                break
            elif choice == 2:
                self.res = 1
                break
            else:
                print("Invalid choice")
        self.downloader()
        
    def downloader(self):
        os.system(clean)
        try: 
            url = self.vi_list[self.res]['url']
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 KB
            
            download_path = f"{ab_path}\download"
            full_path = f"{download_path}\{self.name} _ {self.res}.mp4"

            if not os.path.exists(download_path):
                os.makedirs(download_path)


            see = full_path
            print(" ")
            with open(see, "wb") as f:
                progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    f.write(data)

            progress_bar.close()
        except Exception as e:
            print(e)
            print("Error")
            time.sleep(2)
            self.mainmenu()
        
        ask = input("Do You want to continue? (y/n) ")
        if ask == "y":
            self.get_link()
        elif ask == "n":
            self.mainmenu()
        else:
            print("Invalid choice")
            time.sleep(2)
            self.mainmenu()
    
    def mainmenu(self):
        os.system(clean)
        self.logo()
        print("\n1. Download Video")
        print("2. Exit")
        choice = int(input("\n- Enter your choice: "))
        if choice == 1:
            self.get_link()
        elif choice == 2:
            exit()
        else:
            print("Invalid choice")
            self.mainmenu()

if __name__ == "__main__":
    m = yt_downloader()
    m.mainmenu()