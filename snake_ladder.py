"""#1. First Declare the grid of 10 by 10. And current position of player in the Grid equals to 0."""
"""#2. Declare Snake dictionary"""
"""#3. Declare ladder dictionary"""
"""#4. Roll the dice. """
"""#5. Get the current position of the player and add with the dice value, say new value."""
"""#6. check the following:"""
"""#a. verify new value greater than 100"""
"""#b. verify value available in snake dictionary. if available, Get the value and set current position to that value."""
"""#c.verify value available in snake dictionary. if available, Get the value and set current position to that value. """
"""#7. check new position equals 100. if yes, player won the Game. """

import random
import sys

""" First Declare the grid of 10 by 10. And current position of player in the Grid equals to 0."""

game_grid = list()
game_grid = range(1,101)


"""# Initialize the snake dictionary"""

snake_dict = dict()
snake_dict = {'16:6', '47:26' ,'48:11' , '62:19','64:60','56:53','93:24','95:75','98:78'}

"""# Initialize the Ladder dictionary"""

ladder_dict = dict()
ladder_dict = {'5:14','9:31','1:38','21:42','28:84','36:44','51:67','71:91','80:100'}

"""# Player position"""

player1_pos = 0
win_position = 100


def roll_the_dice():
    return random.randint(1,7)

""" Roll the dice"""
print('Enter 0 to quit.')
print("Enter 1 to Roll Dice")

player = int(input('Enter no of player'))

game_play = 'TRUE'

while game_play == 'TRUE':
    x = int(input("Enter Your choice 0 or 1:   "))
    if x == 0:
        game_play = 'FALSE'
    else:
        value = roll_the_dice()

        """Get the current position."""
        player1_pos = player1_pos + value

        if player1_pos == win_position:
            print('Player Won the Game')
            game_play = 'FALSE'
        else:
            """ Find the player1_pos value in snake dict"""
            snake_box = 'FALSE'
            for key, value in snake_dict.items():
                if player1_pos == key:
                    player1_pos = value
                    snake_box = 'TRUE'
                    break

            if snake_box == 'FALSE':
                for key, value in ladder_dict.items():
                    if player1_pos == key:
                        player1_pos = value

            if player1_pos == win_position:
                print('Player Won the Game')
                game_play = 'FALSE'
            else:
                print('player 1 moved to the location {}'.format(player1_pos))

print('Bye.Game over. Have Fun !')

