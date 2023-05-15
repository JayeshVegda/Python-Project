import requests
import json
import urllib
from tqdm import tqdm
import string
from pathlib import Path
import os

base_url = "https://api.ytbvideoly.com/api/thirdvideo/parse"
form = """link=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DOVLI6jWma9M&from=videodownloaded"""
ab_path = Path(__file__).parent.absolute()

r = requests.post(base_url, data=form)
j = json.loads(r.text)

my_title = j['data']['title']
mp4_videos = j['data']['videos']['mp4']
video_list = []
    
id = 0
for video in mp4_videos:
    video_dict = {}
    id = id + 1 
    video_dict['id'] = id
    video_dict['resolution'] = video['resolution']
    final_s =  video['size']//1000000
    video_dict['size'] = str(final_s) + " MB"
    video_dict['url'] = video['url']
    video_list.append(video_dict)

  
url = video_list[0]["url"]
response = requests.get(url, stream=True)

total_size = int(response.headers.get('content-length', 0))
block_size = 1024  # 1 KB
progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

download_path = f"{ab_path}\download"
full_path = f"{download_path}\{my_title}.mp4"

if not os.path.exists(download_path):
    os.makedirs(download_path)


print(full_path)
with open(full_path, "wb") as f:
    for data in response.iter_content(block_size):
        progress_bar.update(len(data))
        f.write(data)

progress_bar.close()