import random


class Deck:
    def __init__(self):
        self.deck = []
        suits = ['s', 'd', 'c', 'h']
        for val in range(1, 16):
            for i in range(4):
                suit = suits[i]
                card = (val, suit)
                self.deck.append(card)

    def draw(self):
        if len(self.deck) == 0:
            print("Empty Deck")
            return None
        card = self.deck[0]
        self.deck.remove(card)
        return card

    def shuffle(self, shuffle_count=15):
        for j in range(shuffle_count):
            for i in range(len(self.deck)):
                rand = random.randrange(len(self.deck))
                self.deck[i], self.deck[rand] = self.deck[rand], self.deck[i]


class Player:
    def __init__(self, name="Default"):
        self.name = name
        self.hand = []
        self.current_score = 0
        self.current_bid = 0
        self.current_tricks_won = 0

    def draw(self, card):
        self.hand.append(card)

    def play(self, pos):
        card = self.hand[pos]
        self.hand.remove(card)
        return card

    def score(self, points):
        self.current_score = self.current_score + points

    def bid(self, bid):
        self.current_bid = bid

    def win(self):
        self.current_tricks_won = self.current_tricks_won + 1

    def clear(self):
        self.hand = []
        self.current_bid = 0
        self.current_tricks_won = 0

    def print(self):
        for card in self.hand.hand:
            print(card)


class Wizard:
    players = []
    current_hand = []
    current_turn = 1

    def __init__(self, player_count=2, start=1):
        self.deck = Deck()
        self.deck.shuffle(30)
        if start < 60 / player_count:
            self.current_turn = start
        for p in range(player_count):
            self.players.append(Player("Player " + str(p + 1)))

    def deal(self):
        for player in self.players:
            for _ in range(self.current_turn):
                player.draw(self.deck.draw())

    def bids(self):
        for player in self.players:
            print(player.name + " Hand")
            player.hand.print()
            curr_bid = int(input("Enter your bid: "))
            player.current_bid = curr_bid

    def play(self):
        best = Card(0, 'z')
        winner = self.players[0]
        for player in self.players:
            player.print()
            choice = int(input("Choose a card to play, " + player.name))
            card = player.play(choice)
            if best.suit == 'z':
                best = card
                winner = player
            elif card.suit == best.suit and card.value > best.value:
                best = card
                winner = player

        winner.win()
        print("The winner of this round was: ", winner.name)

    def end(self):
        for player in self.players:
            player.clear()

    def score(self):
        for player in self.players:
            if player.current_bid == player.current_tricks_won:
                player.score(20 + 10 * player.current_bid)
            else:
                player.score(-(abs(player.current_bid - player.current_tricks_won) * 10))

    def game(self):
        while self.current_turn <= 60 / len(self.players):

            self.deck = Deck()
            self.deck.shuffle(30)

            self.deal()

            self.bids()

            for rounds in range(self.current_turn):
                self.play()

            self.score()

            for player in self.players:
                print(player.name, "score is :" + str(player.current_score))

            self.current_turn = self.current_turn + 1


if __name__ == "__main__":
    game = Wizard(3, 3)

    game.game()
