import random


class Hand:
    hand = []

    def add(self, card):
        self.hand.append(card)

    def play(self, pos):
        return self.hand[pos]

    def contains(self, c):
        for card in self.hand:
            if card == c:
                return True
        return False

    def print(self):
        print("HAND:")
        for card in self.hand:
            print(card)
        print("ENDOHAND")


class Deck:
    deck = []

    def __init__(self):
        for val in range(1, 14):
            for i in range(4):
                suit = Card.suits[i]
                card = Card(val, suit)
                self.deck.append(card)

    def draw(self):
        card = self.deck[0]
        deck.remove(card)
        return card

    def shuffle(self, shuffle_count=15):
        for j in range(shuffle_count):
            for i in range(len(self.deck)):
                rand = random.randrange(len(self.deck))
                self.deck[i], self.deck[rand] = self.deck[rand], self.deck[i]

    def contains(self, c):
        for card in self.deck:
            if card == c:
                return True
        return False

    def remove(self, card):
        self.deck.remove(card)

    def print(self):
        print("FULL DECK: ")
        for card in self.deck:
            print(card)
        print("FINISHED")


class Card:
    value = 0
    suit = ''
    suits = ['s', 'd', 'c', 'h']

    def __init__(self, value=0, suit='z'):
        self.value = value if value != 0 else random.randrange(1, 13)
        self.suit = suit if suit != 'z' else self.suits[random.randrange(0, 3)]

    def __str__(self):
        return str(self.value) + " of " + self.suit

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit


if __name__ == "__main__":
    deck = Deck()

    print("First")
    deck.print()
    testcard = Card(4, 's')
    if deck.contains(testcard):
        print("AHAHA")
    deck.shuffle()
    print("And then")
    deck.print()

    newcard = deck.draw()
    print("OF COURSE")
    print(newcard)
    print("AND OF COURSE")

    deck.print()

    newcard = deck.draw()
    print("OF COURSE")
    print(newcard)
    print("AND OF COURSE")
