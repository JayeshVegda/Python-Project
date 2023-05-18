import json
import requests
import os



key = ""
country = "France"
with open("8. Weather App/settings.json", "r") as json_file:
    data = json.load(json_file)
    key = data["api"]



url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={country}&aqi=yes"
res = requests.get(url)
found = json.loads(res.text)

os.system("cls")
# print(found)
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