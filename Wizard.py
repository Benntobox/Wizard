from Deck import Deck
from Player import Player


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
        print("Current turn is", self.turn)
        for player in self.players:
            for _ in range(self.turn):
                player.draw(self.deck.draw())

    def bids(self):
        if self.turn != 60 / len(self.players):
            trump = self.deck.draw()
            if not trump or trump[0] == 1:
                self.trump_suit = 'z'
            elif trump[0] == 15:
                self.trump_suit = input("Enter the letter of trump suit:")
            else:
                self.trump_suit = trump[1]

        for player in self.players:
            print("Trump is", "none" if self.trump_suit == 'z' else self.trump_suit)
            print(player.name + " Hand")
            print(player.hand)
            curr_bid = int(input("Enter your bid: \n"))
            player.bid = curr_bid

    def play(self):
        for _ in range(self.turn):
            best = None
            winner = None
            lead = None
            for player in self.players:
                choice = -1
                while 0 > choice or choice > len(player.hand) - 1:
                    print("Trump is", self.trump_suit)
                    print("Current leading card is", best if best else "none")
                    print(player.hand)
                    choice = int(input("Choose a card to play, " + player.name + "\n"))
                card = player.play(choice)
                if not lead:
                    lead = card
                if self.find_winner(best, card, self.trump_suit) == card:
                    best = card
                    winner = player

            winner.win_trick()
            print("The winner of this round was: ", winner.name, "\n")

    def score(self):
        for player in self.players:
            if player.bid == player.tricks:
                player.add_score(20 + 10 * player.bid)
            else:
                player.add_score(-(abs(player.bid - player.tricks) * 10))
        for player in self.players:
            print(player.name, "score is :" + str(player.score))

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

