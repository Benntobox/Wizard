from Wizard import Wizard

if __name__ == "__main__":
    wizard = Wizard(3, 3)
    wizard.game()
    print("GAME OVER ")

'''
Current turn is 3
Trump is d
Player 1 Hand
[(1, 's'), (9, 'h'), (7, 's')]
Enter your bid: 
1
Trump is d
Player 2 Hand
[(4, 'h'), (14, 'h'), (3, 'h')]
Enter your bid: 
1
Trump is d
Player 3 Hand
[(10, 'h'), (7, 'd'), (2, 'd')]
Enter your bid: 
0
Trump is d
Current leading card is none
[(1, 's'), (9, 'h'), (7, 's')]
Choose a card to play, Player 1
1
Trump is d
Current leading card is (9, 'h')
[(4, 'h'), (14, 'h'), (3, 'h')]
Choose a card to play, Player 2
1
Trump is d
Current leading card is (14, 'h')
[(10, 'h'), (7, 'd'), (2, 'd')]
Choose a card to play, Player 3
0
The winner of this round was:  Player 2 

Trump is d
Current leading card is none
[(1, 's'), (7, 's')]
Choose a card to play, Player 1
1
Trump is d
Current leading card is (7, 's')
[(4, 'h'), (3, 'h')]
Choose a card to play, Player 2
1
Trump is d
Current leading card is (7, 's')
[(7, 'd'), (2, 'd')]
Choose a card to play, Player 3
0
The winner of this round was:  Player 3 

Trump is d
Current leading card is none
[(1, 's')]
Choose a card to play, Player 1
0
Trump is d
Current leading card is (1, 's')
[(4, 'h')]
Choose a card to play, Player 2
0
Trump is d
Current leading card is (4, 'h')
[(2, 'd')]
Choose a card to play, Player 3
0
The winner of this round was:  Player 3 

Player 1 score is :-10
Player 2 score is :30
Player 3 score is :-20
Current turn is 4
Trump is s
Player 1 Hand
[(1, 's'), (1, 'd'), (1, 'c'), (1, 'h')]
Enter your bid: 
'''