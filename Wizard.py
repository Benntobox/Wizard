import random


class Hand:
    hand = []

    def add(self, card):
        self.hand.append(card)

    def play(self, pos):
        card = self.hand[pos]
        self.hand.remove(card)
        return card

    def contains(self, c):
        for card in self.hand:
            if card == c:
                return True
        return False

    def print(self):
        for card in self.hand:
            print(card)


class Deck:
    deck = []

    def __init__(self):
        for val in range(1, 16):
            for i in range(4):
                suit = Card.suits[i]
                card = Card(val, suit)
                self.deck.append(card)

    def draw(self):
        card = self.deck[0]
        self.deck.remove(card)
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
        for card in self.deck:
            print(card)
        print("\n")


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


class Player:
    name = ""
    hand = Hand()
    score = 0
    current_bid = 0
    current_tricks_won = 0

    def __init__(self, name="Default"):
        self.name = name

    def draw(self, card):
        self.hand.add(card)

    def play(self, pos):
        return self.hand.play(pos)

    def score(self, points):
        self.score = self.score + points

    def bid(self, guess):
        self.current_bid = guess

    def win(self):
        self.current_tricks_won = self.current_tricks_won + 1

    def clear(self):
        self.hand = Hand()
        self.current_bid = 0
        self.current_tricks_won = 0


class Wizard:
    players = []
    current_hand = []
    current_turn = 1
    deck = Deck()

    def __init__(self, player_count=2, start=1):
        if start < 60 / player_count:
            self.current_turn = start
        for p in range(player_count):
            self.players.append(Player("Player " + str(p + 1)))

    def deal(self):
        for player in self.players:
            player.draw(self.deck.draw())

    def bids(self):
        for player in self.players:
            print(player.name + " Hand")
            player.hand.print()
            curr_bid = int(input("Enter your bid: "))
            player.current_bid = curr_bid

    def play(self):
        best = Card(0, 'z')
        winner = Player()
        for player in self.players:
            choice = int(input("Choose a card to play"))
            card = player.play(choice)
            if best.suit == 'z':
                best = card
                winner = player
            elif card.suit == best.suit and card.value > best.value:
                best = card
                winner = player

        winner.win()

    def end(self):
        for player in self.players:
            player.clear()

    def score(self):
        for player in self.players:
            if player.current_bid == player.current_tricks_won:
                player.score(20 + 10 * player.current_bid)
            else:
                player.score(-(abs(player.current_bid - player.current_tricks_won)))

    def game(self):
        while self.current_turn <= 60 / len(self.players):

            deck = Deck()
            deck.shuffle(30)

            print("current turn " + str(self.current_turn))
            print("p1 hand")
            self.players[0].hand.print()

            self.deal()

            print("p1 hand")
            self.players[0].hand.print()
            print("p2 hand")
            self.players[1].hand.print()

            self.bids()

            for rounds in range(self.current_turn):
                self.play()

            self.score()

            self.current_turn = self.current_turn + 1


if __name__ == "__main__":
    game = Wizard(3, 3)

    game.game()
