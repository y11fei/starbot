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
