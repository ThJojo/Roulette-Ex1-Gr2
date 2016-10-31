# 120.050 Introduction to Python programming for geoscience
# Exercise 1 - Group 2
# 2016 October and November

# Listing 1 from "Ex-1_simple_roulette.pdf"
# This snippet clears the screan of a terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Asking for the player's name
player = input('Welcome to Terminal Roulette!\n\n'
             + 'Please, enter your name: ')
print('\n' + 'Hello', player + '!' + '\n') # May remove for final version

# Asking the player for the budget
# https://wiki.python.org/moin/WhileLoop
# http://stackoverflow.com/a/4138231
# http://stackoverflow.com/a/4730961
while True:
    budget = input('How big is your budget for this game? ')
    try:
        budget = float(budget)
        if budget > 0:
            break
        else:
            print('\n' + 'Your input must be greater than zero!')
    except ValueError:
        print('\n' +'Only Arabic numerals are accepted as input!')
        False

# Listing 2 from "Ex-1_simple_roulette.pdf" used for float format
print('\n' + 'Your budget is {:.2f}'.format(budget) + '\n') # May remove for final version
