import os, time, requests, json
from instagrapi import Client

insta = Client()
insta.photo_download_by_url("https://www.instagram.com/p/CrCpfpVt3Zq/")

