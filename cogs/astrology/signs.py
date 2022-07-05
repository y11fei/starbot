import os
import requests
import json
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'))

api_key = os.getenv("API_KEY")

url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
}


def get_data(user_sign, user_day):
    querystring = {'sign': user_sign, 'day': user_day}
    response = requests.request(
        "POST", url, headers=headers, params=querystring)
    if 'Wrong sign or day' in response.text:
        return response.text
    else:
        data = json.loads(response.text)
        return data


# print(get_data('aquarius', 'today'))
