import json


def card():
    with open('cards.json') as cards_data:
        cards = json.load(cards_data)
    return cards[0]['fortune_telling'][0]
