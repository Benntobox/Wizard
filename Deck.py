import random


class Deck:
    def __init__(self):
        self.deck = []
        self.suits = ['s', 'd', 'c', 'h']
        self.reset()

    def draw(self):
        if len(self.deck) == 0:
            return None
        card = self.deck[0]
        self.deck.remove(card)
        return card

    def shuffle(self):
        random.shuffle(self.deck)

    def reset(self):
        self.deck = []
        for val in range(1, 16):
            for i in range(4):
                suit = self.suits[i]
                card = (val, suit)
                self.deck.append(card)
