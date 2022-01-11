import random

secret = random.randint(1,21)
guess = ''
print('I am thinking of a number between 1 and 20.')
print('Take a guess.')
numberOfGuesses = 0
while guess != secret:
    guess = int(input())
    numberOfGuesses += 1
    if guess < secret:
        print("Your guess is too low.")
    elif guess > secret:
        print("Your guess is too high.")
    else:
        print("Good job! You guessed my number in %s guesses!" % numberOfGuesses)
        break
    print("Take a guess.")


