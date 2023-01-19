import random
from colorama import Fore, Back, Style

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

your_total_score = 0
computer_total_score = 0
general_winner = ''
games = 11
while games > 0:
    games -= 1
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

    print(Fore.LIGHTBLUE_EX + f"The computer chose {computer_move}.")



    if computer_move == player_move:
        print(Fore.YELLOW + f'Draw!')
    elif (computer_move == rock and player_move == scissors) or (computer_move == paper and player_move == rock or
                                                                 computer_move == scissors and player_move == paper):
        print(Fore.RED + f'You lose!')
        computer_total_score += 1
    else:
        print(Fore.GREEN + f'You win!')
        your_total_score += 1
print(Fore.CYAN + f'Computer score: {computer_total_score}')
print(Fore.LIGHTGREEN_EX + f'Your score: {your_total_score}')
if computer_total_score > your_total_score:
    print('General winner is COMPUTER!')
elif your_total_score > computer_total_score:
    print('General winner are You!')
else:
    print('No general winner!')
    