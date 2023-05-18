import json
import requests
import os

def path():
    cwd = os.path.dirname(os.path.realpath(__file__))
    return cwd + "/settings.json"

p = path()
print(p)
