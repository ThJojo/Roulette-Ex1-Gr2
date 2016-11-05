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

# Listing 2 from "Ex-1_simple_roulette.pdf" used for float format
print('\n' + 'Your budget is {:.2f}'.format(budget) + '\n') # May remove for final version

# Implementing the different bet types
# http://stackoverflow.com/a/2184764
single = list(range(37))       # creates a list with the numbers  0..36
manque = list(range(1,19))     #                                  1..18
passe = list(range(19,37))     #                                 19..36

# https://en.wikipedia.org/wiki/Roulette#Roulette_wheel_number_sequence
# http://stackoverflow.com/a/13959555
rouge = list(range(1,11,2)) \
        + list(range(12,19,2)) \
        + list(range(19,29,2)) \
        + list(range(30,37,2)) # list of "rouge" numbers
                               # odd numbers   1..10 and 19..28
                               # even numbers 11..18 and 29..36

# http://stackoverflow.com/a/2070734
noir = list(range(1,37))       # creates a list with the numbers  1..36
for x in rouge:
    noir.remove(x)             # removing all entries, which are already present in "rouge"

pair = list(range(2,37,2))     # even numbers between 1..36
impair = list(range(1,37,2))   # odd numbers between  1..36
dozen1 = list(range(1,13))     # creates a list with the numbers  1..12
dozen2 = list(range(13,25))    #                                 13..24
dozen3 = list(range(25,37))    #                                 25..36
column1 = list(range(1,37,3))  # column1: 1, 4, 7, 10, .. , 34
column2 = list(range(2,37,3))  # column2: 2, 5, 8, 11, .. , 35
column3 = list(range(3,37,3))  # column3: 3, 6, 9, 12, .. , 36


# ----------------------------------- TASK 3 -----------------------------------
# Asking the player for the bet
# https://wiki.python.org/moin/WhileLoop
# http://stackoverflow.com/a/4138231
# http://stackoverflow.com/a/4730961
while True:
    bet = input('How big is your bet for this game? ') # may add the name of the game as soon as task 2 is implemented
    try:
        bet = float(bet)
        if bet <= 0:
            print('\n' + 'Your bet must be greater than zero!')
        elif bet > budget:
            print('\n' + 'Your bet must not exceed your budget!')
        else:
            break
    except ValueError:
        print('\n' + 'Only Arabic numerals are accepted as input!')

# May ask here to confirm the bet. If not confirmed, ask if player wants to quit, or bet a different amount.

# calculate budget = budget-bet+(+win or -loss) later --> maybe only in task 4
