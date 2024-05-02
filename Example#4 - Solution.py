# Example 4 - Guessing Game - Correct Solution

import random

num = random.randrange(1, 101)

guess= int(input(f'Guess a number between 1 and 100: '))

while guess != num:
    if guess > num:
        print('Number is too high, try again')

    else:
        print('Number is too low, try again')
    guess = int(input(f'Take a guess: '))

print('Congradulations')