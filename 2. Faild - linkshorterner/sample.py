import requests
import json

api = "B6HJ4IHCIA1edpBKC7vy02R3NbJPSZi8kgm1hEIe8xHu2zTiIHKyibqXZifMB4xl"
url = "https://t.ly/api/v1/link/shorten?Y249YB4EXAst3VjeIoRwct2kylO9s62Uta4OzvJoTa4WwbDt36GXb9PLpaxO"


long_url = input("Enter the long url: ")

data = {"long_url": long_url}
head = { "Content-Type": "application/json"}

req = requests.post(url, data=json.dumps(data), headers=head)
print(req.text)