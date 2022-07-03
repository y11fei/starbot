import json
import random

with open('cogs/readings/cards.json') as cards_data:
    cards = json.load(cards_data)

directions = ['Upright', 'Reversed']


def get_card():
    return random.choice(cards)


def get_direction():
    return random.choice(directions)


def card_name(card):
    return card['name']


def card_meanings(card, direction):
    return '\n'.join(card['meanings'][direction.lower()])


def card_keywords(card):
    return '\n'.join(card['keywords'])


def get_image(card):
    return card['img']


def get_affirmation(card):
    return card['Affirmation']


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
    for x in cards:
        if cards[x] == "Upright":
            count += 1
        else:
            continue
    return count


def get_attribute(cards, attribute):
    newList = []
    for i in range(len(cards)):
        newList.append(cards[f'card{i}'][attribute])
    return newList


def get_shapes(cards):
    answers = {}
    for i in cards:
        answers[i] = random.choice(directions)
    return answers


def helper(cards):
    newList = []
    for x in cards:
        newList.append(f'{x} ({cards[x]})')
    return '\n'.join(newList)


def find_card(card):
    answer = None
    for i in cards:
        if i['name'].lower() == card.lower():
            answer = i
            break
        else:
            answer = "Not a valid Tarot Card, sorry \N{confounded face}. Please try again."
            continue
    return answer


def arcana_cards(suit):
    list = []
    for i in cards:
        if i['suit'] == suit:
            list.append(i['name'])
    return '\n'.join(list)
