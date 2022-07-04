import requests
import json

url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

querystring = None

headers = {
    "X-RapidAPI-Key": "85e9aede11msh899612f060efb10p1a01eajsn38f2dfa623d2",
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

# print((get_data('aquarius', 'today')))


def get_attribute(data, attribute):
    return data[attribute]


data = get_data('ksajd', 'jkdsas')


# print(data)
# print(type(data))

'''
{'date_range': 'Mar 21 - Apr 20', 'current_date': 'July 4, 2022', 'description': "Someone who's totally unlike anyone you've ever known will suddenly cross your path, and you won't be shy about letting them know just how unusual they are. The good news is that they'll find you equally interesting.",
    'compatibility': 'Capricorn', 'mood': 'Charming', 'color': 'Sky Blue', 'lucky_number': '35', 'lucky_time': '6am'}
'''
