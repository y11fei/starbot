import requests


def get_adv():
    response = requests.get('https://api.adviceslip.com/advice')
    data = response.json()['slip']['advice']
    return data
