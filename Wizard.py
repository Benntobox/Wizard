import random


class Deck:
    def __init__(self):
        self.deck = []
        self.suits = ['s', 'd', 'c', 'h']
        self.reset()

    def draw(self):
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


class Player:
    def __init__(self, name="Default"):
        self.name = name
        self.hand = []
        self.current_score = 0
        self.current_bid = 0
        self.current_tricks = 0

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

    def win_trick(self):
        self.current_tricks = self.current_tricks + 1

    def clear(self):
        self.hand = []
        self.current_bid = 0
        self.current_tricks = 0


class Wizard:
    def __init__(self, player_count=3, turn=1):
        self.deck = Deck()
        self.deck.shuffle()
        self.trump_suit = 'z'

        self.turn = turn if 0 < turn < (60 / player_count) else 1

        self.players = []
        for p in range(player_count):
            self.players.append(Player("Player " + str(p + 1)))

    def deal(self):
        for player in self.players:
            for _ in range(self.turn):
                player.draw(self.deck.draw())

    def bids(self):
        if self.turn != 60 / len(self.players):
            trump = self.deck.draw()
            if trump[0] == 15:
                self.trump_suit = input("Enter the letter of trump suit:")
            elif trump[0] != 1:
                self.trump_suit = trump[1]
        print("Trump is", "none" if self.trump_suit == 'z' else self.trump_suit)
        for player in self.players:
            print("Trump is", self.trump_suit)
            print(player.name + " Hand")
            print(player.hand)
            curr_bid = int(input("Enter your bid: \n"))
            player.current_bid = curr_bid

    def play(self):
        for rounds in range(self.turn):
            best = None
            winner = None
            for player in self.players:
                print("Trump is", self.trump_suit)
                print(player.hand)
                choice = int(input("Choose a card to play, " + player.name + "\n"))
                card = player.play(choice)
                if self.find_winner(best, card, self.trump_suit) == card:
                    best = card
                    winner = player
                print("Current leading card is ", best)

            winner.win_trick()
            print("The winner of this round was: ", winner.name, "\n")

    def score(self):
        for player in self.players:
            if player.current_bid == player.current_tricks:
                player.score(20 + 10 * player.current_bid)
            else:
                player.score(-(abs(player.current_bid - player.current_tricks) * 10))
        for player in self.players:
            print(player.name, "score is :" + str(player.current_score))

    def end(self):
        for player in self.players:
            player.clear()
        self.deck.reset()
        self.trump_suit = 'z'
        self.turn = self.turn + 1

    def game(self):
        while self.turn <= 60 / len(self.players):
            self.deal()
            self.bids()
            self.play()
            self.score()
            self.end()

    @staticmethod
    def find_winner(lead_card, played_card, trump_suit):
        if not lead_card:
            return played_card

        lead_val, lead_suit = lead_card[0], lead_card[1]
        played_val, played_suit = played_card[0], played_card[1]

        if lead_val == 15 or played_val == 1:
            return lead_card
        if played_val == 15 or lead_val == 1:
            return played_card
        if lead_suit != played_suit:
            return played_card if played_suit == trump_suit else lead_card
        if lead_val >= played_val:
            return lead_card
        return played_card


if __name__ == "__main__":
    wizard = Wizard(4, 3)
    wizard.game()
    print("GAME OVER ")
