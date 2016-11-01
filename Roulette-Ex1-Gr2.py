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

# Implementing the different bet types
# http://stackoverflow.com/a/2184764
single = list(range(37))     # creates a list with the numbers  0..36
manque = list(range(1,19))   #                                  1..18
passe = list(range(19,37))   #                                 19..36
rouge = [ 1,  3,  5,  7,  9, 12,
         14, 16, 18, 19, 21, 23,
         25, 27, 30, 32, 34, 36] # list of "rouge" numbers
                                 # logical explanation for distribution not yet found!
noir = [ 2,  4,  6,  8, 10, 11,
        13, 15, 17, 20, 22, 24,
        26, 28, 29, 31, 33, 35] # list of "rouge" numbers
                                # logical explanation for distribution not yet found!
pair = list(range(2,37,2))   # even numbers between 1..36
impair = list(range(1,37,2)) # odd numbers between  1..36
dozen1 = list(range(1,13))   # creates a list with the numbers  1..12
dozen2 = list(range(13,25))  #                                 13..24
dozen3 = list(range(25,37))  #                                 25..36
