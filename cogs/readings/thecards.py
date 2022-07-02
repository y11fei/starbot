import json
import random

with open('cogs/readings/cards.json') as cards_data:
    cards = json.load(cards_data)

directions = ['light', 'shadow']


def get_card():
    return random.choice(cards)


def get_direction():
    return random.choice(directions)


def card_name(card):
    return card['name']


def card_meanings(card, direction):
    return '\n'.join(card['meanings'][direction])


def card_keywords(card):
    return '\n'.join(card['keywords'])


def get_image(card):
    return card['img']


def get_questions(card):
    return '\n'.join(card['Questions to Ask'])


def get_fortunes(card):
    return '\n'.join(card['fortune_telling'])


def card_description(card):
    return card['description']


def get_3cards():
    cards = {}
    for i in range(3):
        cards[f'card{i}'] = get_card()
    return cards


def yes_no(cards):
    count = 0
    for i in range(3):
        if "Ace" in cards[f'card{i}']['name']:
            count += 1
        else:
            continue
    return count


def get_attribute(cards, attribute):
    newList = []
    for i in range(len(cards)):
        newList.append(cards[f'card{i}'][attribute])
    if attribute == "name":
        return '\n'.join(newList)
    return newList
