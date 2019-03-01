'''
Author: James Nicholson
Date: 6/25/2018
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
'''

#New game
new_game = ""

print('''Please pick one:
        rock
        paper
        sissors''')

while new_game != "yes" and new_game != "Yes":
    game_dict = {'rock': 1, 'sissors': 2, 'paper': 3}
    player_1 = str(input("Player 1: "))
    player_2 = str(input("Player 2: "))
    a = game_dict.get(player_1)
    b = game_dict.get(player_2)
    dif = a - b

    if dif in [-1, 2]:
        print('Player 1 wins!')
        if str(input('Do you want to play another game, yes or no\n'))=='yes':
            continue
        else: 
            print('GAME OVER!')
            break
    elif dif in [-2, 1]:
        print('Player 2 wins!')
        if str(input('Do you want to play another game, yes or no\n'))=='yes':
            continue
        else: 
            print('GAME OVER!')
            break
    else:
        print('Draw. Plesae contine')
        print('')
    
new_game = input('Do you want to play another game, yes or no\n')

#End Script
