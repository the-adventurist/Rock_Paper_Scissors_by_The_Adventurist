import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Choose [r]ock, [p]aper, [s]ciossors: ')

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid input. Try again...')

computer_random_number = random.randint(1, 3)
computer_move = ''
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

if computer_move == player_move:
    print('Draw!')
elif (computer_move == rock and player_move == scissors) or (computer_move == paper and player_move == rock or
                                                             computer_move == scissors and player_move == paper):
    print('You lose!')
else:
    print('You win!')
