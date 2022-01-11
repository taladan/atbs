# Traditional game of Rock Paper Scissors
import random
import sys

wins = 0
losses = 0
ties = 0
moves = {'r':'Rock', 'p':'Paper', 's':'Scissors'}


def picker():
    options = ["r", "p", "s"]
    return random.choice(options)

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    player_choice = ''
    computer_choice = picker()

# Player input loop
    while True:
        print('Enter your move: (r)ock, (p)aper), (s)cissors, or (q)uit.')
        player_choice = input()
        if player_choice in ['r', 'p', 's']:
            break # Break out of player input loop
        elif player_choice == 'q':
            sys.exit()
        else:
            print("Invalid choice, please pick (r)ock, (p)aper, (s)cissors, or (q)uit")

    print("%s versus..." % moves[player_choice])
    print("%s" % moves[computer_choice])

    if player_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif player_choice == 'r' and computer_choice == 's':
        print('You win!')
        wins += 1
    elif player_choice == 's' and computer_choice == 'p':
        print('You win!')
        wins += 1
    elif player_choice == 'p' and computer_choice == 'r':
        print('You win!')
        wins += 1
    elif player_choice == 'r' and computer_choice == 'p':
        print('You lose!')
        losses += 1
    elif player_choice == 's' and computer_choice == 'r':
        print('You lose!')
        losses += 1
    elif player_choice == 'p' and computer_choice == 's':
        print('You lose!')
        losses += 1
