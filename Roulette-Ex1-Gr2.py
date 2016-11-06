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
print('\n' + 'Your budget is {:.2f}'.format(budget)) # May remove for final version

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

# ----------------------------------- TASK 2 -----------------------------------
# Ask player for the game

# Defining a dictonary with integer keys and name values
# dictGames = {1: 'single',
#             2: 'manque',
#             3: 'passe',
#             4: 'rouge',
#             5: 'noir',
#             6: 'pair',
#             7: 'impair',
#             8: 'dozen1',
#             9: 'dozen2',
#            10: 'dozen3',
#            11: 'column1',
#            12: 'column2',
#            13: 'column3'}

# Defining multiple dictionaries for the selection of the bet type
dictBetType = {1: 'single [0..36]',
               2: 'manque [1..18]',
               3: 'passe [19..36]',
               4: 'color',
               5: 'pair or impair',
               6: 'dozen',
               7: 'column',
              'q': 'quit'}

dictColor = {1: 'rouge',
             2: 'noir',
            'x': 'one level up',
            'q': 'quit'}

dictImPair = {1: 'pair',
              2: 'impair',
             'x': 'one level up',
             'q': 'quit'}

dictDozen = {1: '1st dozen [1..12]',
             2: '2nd dozen [13..24]',
             3: '3rd dozen [25..36]',
            'x': 'one level up',
            'q': 'quit'}

dictColumn = {1: '1st column [1, 4, 7, .. 34]',
              2: '2nd column [2, 6, 8, .. 35]',
              3: '3rd column [3, 5, 9, .. 36]',
             'x': 'one level up',
             'q': 'quit'}

# Defining another dictonary to translate the selection
dictTranslate = {'single [0..36]' : single,
                 'manque [1..18]' : manque,
                 'passe [19..36]' : passe,
                 'rouge'          : rouge,
                 'noir'           : noir,
                 'pair'           : pair,
                 'impair'         : impair,
                 '1st dozen [1..12]'  : dozen1,
                 '2nd dozen [13..24]' : dozen2,
                 '3rd dozen [25..36]' : dozen3,
                 '1st column [1, 4, 7, .. 34]' : column1,
                 '2nd column [2, 6, 8, .. 35]' : column2,
                 '3rd column [3, 5, 9, .. 36]' : column3}

# This function prints all elements of a dictonary
# http://stackoverflow.com/a/18219242
def printDictSorted(x):
    for key, value in sorted(x.items()):
        print("{} = {}".format(key, value))

def printDict(x):
    for key, value in x.items():
        print("{} = {}".format(key, value))

def selectBetType(dictBet, itemsInList):
    print('\n')
    printDict(dictBet)
    while True:
        itemBet = input('\n' + 'Please select from list: ')
        try:
            itemBet = int(itemBet)
            if itemBet in range(1,itemsInList+1,1):
                return itemBet # http://stackoverflow.com/questions/354883/how-do-you-return-multiple-values-in-python
                break
            else:
                print('\n' + 'Wrong input!')
        except ValueError:
            if itemBet is 'x' and 'x' in dictBet:
                print('One level up!')
                return itemBet
            elif itemBet is 'q':
                confirmQuit = input('Do you really want to quit? ')
                while True:
                    if confirmQuit == 'y':
                        quit()
                    else:
                        break
            else:
                print('\n' + 'Wrong input! except')

# trial outputs
# https://bytebaker.com/2008/11/03/switch-case-statement-in-python/
switch = 0
while True:
    if switch == 0:
        level_0 = selectBetType(dictBetType, 7)
        if level_0 in range(1,4,1):
            break
        else:
            switch += 1
    if level_0 == 4:
        level_1a = selectBetType(dictColor, 2)
        if level_1a is not 'x':
            break
        else:
            switch -=1
            continue
    if level_0 == 5:
        level_1b = selectBetType(dictImPair, 2)
        if level_1b is not 'x':
            break
        else:
            switch -=1
            continue
    if level_0 == 6:
        level_1c = selectBetType(dictDozen, 3)
        if level_1c is not 'x':
            break
        else:
            switch -=1
            continue
    if level_0 == 7:
        level_1d = selectBetType(dictColumn, 3)
        if level_1d is not 'x':
            break
        else:
            switch -=1
            continue

# https://docs.python.org/3/library/stdtypes.html?highlight=dict#dict
#print('\n' + 'Available games:' + '\n')
#printDict(dictGames)
#while True:
#    gameSelected = input('\n' + 'Your choice: ')
#    try:
#        gameSelected = int(gameSelected)
#        if gameSelected in dictTranslate:
#            print('Selected game:', dictTranslate[gameSelected]) # May edit later
#            break
#        else:
#            print('Only integers between', list(dictGames.keys())[0], 'and', list(dictGames.keys())[-1], 'are accepted as input!')
#    except ValueError:
#        print('Only integers between', list(dictGames.keys())[0], 'and', list(dictGames.keys())[-1], 'are accepted as input!')
#
#print(dictNumbers[dictGames[gameSelected]])

# How to program a switch using python
# http://stackoverflow.com/a/60211
# http://stackoverflow.com/a/103081
