class Player:
    def __init__(self, name="Default"):
        self.name = name
        self.hand = []
        self.score = 0
        self.bid = 0
        self.tricks = 0

    def draw(self, card):
        if card:
            self.hand.append(card)

    def play(self, pos):
        card = self.hand[pos]
        self.hand.remove(card)
        return card

    def add_score(self, points):
        self.score = self.score + points

    def bid(self, bid):
        self.bid = bid

    def win_trick(self):
        self.tricks = self.tricks + 1

    def clear(self):
        self.hand = []
        self.bid = 0
        self.tricks = 0

    def reset(self):
        self.clear()
        self.score = 0
