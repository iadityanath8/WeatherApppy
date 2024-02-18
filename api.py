from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

secret_key = os.getenv("SECRET_KEY")

url=f"https://api.weatherapi.com/v1/current.json?key={secret_key}"


def getcity_name(name):
    global url
    url += f"&q={name}"

    print(url)

    response = requests.get(url)
    
    if response.status_code == 200:
        a = response.json()
        url = f"https://api.weatherapi.com/v1/current.json?key={secret_key}"
        return a
    else:
        print(f"Error with status code {response.status_code}")
        url = f"https://api.weatherapi.com/v1/current.json?key={secret_key}"
        return json.dumps({'message':"cannot fetch",'code':'false'})   