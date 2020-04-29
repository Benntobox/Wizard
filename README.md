# Wizard

* A simple text based version of the card game Wizard

* Each player is dealt a hand, bids on number of wins, then plays out rounds to win tricks
* Scoring is based on how close to the bid they guessed and the tricks won match
* Deck entity creates a list of the cards of the game, as tuples of (value, suit) 
* Player entity manages score, current cards, current bids, and current tricks won
* Wizard game class creates players, then deals, runs bids, runs game loop, then closes down and scores
