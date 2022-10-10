from lib.assets import card, deck

def generate_straight():
    cards = []
    cards.append(card(3, 2))
    cards.append(card(4, 0))
    cards.append(card(5, 2))
    cards.append(card(6, 3))
    cards.append(card(7, 2))
    return cards

def generate_flush():
    cards = []
    cards.append(card(3, 2))
    cards.append(card(4, 2))
    cards.append(card(10, 2))
    cards.append(card(6, 2))
    cards.append(card(2, 2))
    return cards

def generate_pair_of_jacks():
    cards = []
    cards.append(card(9, 3))
    cards.append(card(4, 2))
    cards.append(card(9, 2))
    cards.append(card(6, 2))
    cards.append(card(2, 2))
    return cards

def generate_pair():
    cards = []
    cards.append(card(9, 3))
    cards.append(card(10, 0))
    cards.append(card(1, 3))
    cards.append(card(1, 1))
    cards.append(card(12, 2))
    return cards