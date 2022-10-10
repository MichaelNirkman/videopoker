import random
from var.constants import bcolors as c, ranks, suits

class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.rank_str = ranks[rank]["text"]
        self.suit = suit
        self.suit_str = suits[suit]["icon"]
        self.high = ranks[rank]["high"]
    
    def __str__(self):
        color = c.BOLD
        return f"{color}{self.rank_str}{self.suit_str}{c.ENDC}"

class deck:
    def __init__(self, shuffle):
        self.cards = generate_standard_deck(shuffle)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def pick_card(self, amount=1):
        if amount == 1:
            chosen_card = self.cards.pop(0)
            return chosen_card
        elif amount > 1:
            chosen_cards = []
            for i in range(0, amount):
                chosen_cards.append(self.cards.pop(i))
            return chosen_cards
        else:
            return None
    
    def restore(self):
        self.cards = generate_standard_deck()
    
    def replace_cards(self, hand, keeps):
        keeps_list = []
        if keeps == "all":
            keeps_list = ["1", "2", "3", "4", "5"]
        else:
            keeps_list = [*keeps]
        for i in range(0, len(hand)):
            if str(i+1) not in keeps_list:
                hand[i] = self.cards.pop(0)
        return hand

def generate_standard_deck(shuffle=False):
    cards = []
    for i in range(0, len(ranks)):
        for u in range(0, len(suits)):
            cards.append(card(i, u))
    if shuffle:
        random.shuffle(cards)
    else:
        cards.sort(key=lambda x: x.suit)
    return cards