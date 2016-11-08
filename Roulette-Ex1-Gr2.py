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

# Defining multiple dictionaries for the selection of the bet type
dictBetType = {1  : 'single [0..36]',
               2  : 'manque [1..18]',
               3  : 'passe [19..36]',
               4  : 'color',
               5  : 'pair or impair',
               6  : 'dozen',
               7  : 'column',
              'q' : 'quit'}

dictColor = {1  : 'rouge',
             2  : 'noir',
            'x' : 'one level up',
            'q' : 'quit'}

dictImPair = {1  : 'pair',
              2  : 'impair',
             'x' : 'one level up',
             'q' : 'quit'}

dictDozen = {1  : '1st dozen [1..12]',
             2  : '2nd dozen [13..24]',
             3  : '3rd dozen [25..36]',
            'x' : 'one level up',
            'q' : 'quit'}

dictColumn = {1  : '1st column [1, 4, 7, .. 34]',
              2  : '2nd column [2, 6, 8, .. 35]',
              3  : '3rd column [3, 5, 9, .. 36]',
             'x' : 'one level up',
             'q' : 'quit'}

# Defining other dictonaries to translate the selection
dictTransBetType = {'single [0..36]' : single,
                    'manque [1..18]' : manque,
                    'passe [19..36]' : passe}

dictTransColor = {'rouge' : rouge,
                 'noir'   : noir}

dictTransImPair = {'pair'    : pair,
                   'impair' : impair}

dictTransDozen = {'1st dozen [1..12]'  : dozen1,
                  '2nd dozen [13..24]' : dozen2,
                  '3rd dozen [25..36]' : dozen3}

dictTransColumn = {'1st column [1, 4, 7, .. 34]' : column1,
                   '2nd column [2, 6, 8, .. 35]' : column2,
                   '3rd column [3, 5, 9, .. 36]' : column3}

# This function prints all elements of a dictonary (sorted)
# http://stackoverflow.com/a/18219242
def printDictSorted(x):
    for key, value in sorted(x.items()):
        print("{} = {}".format(key, value))

# This function prints all elements of a dictonary
def printDict(x):
    for key, value in x.items():
        print("{} = {}".format(key, value))

# This function is used for the selection of the game.
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
                print('\n' + 'Wrong input!')

# The following function is used for the games single, manque, and passe
# The player has to select a number from the printed list
# Optional, the player can go one level up, or quit the game.
def selectBetNumber(bet):
    print('\n')
    print(bet)
    print('x = one level up' '\n' + 'q = quit')
    while True:
        numberSelected = input('\n' + 'Please select from list: ')
        try:
            numberSelected = int(numberSelected)
            if numberSelected in bet:
                return numberSelected
                break
            else:
                print('\n' + 'Wrong inupt!')
        except ValueError:
            if numberSelected is 'x':
                print('One level up!')
                return numberSelected
            elif numberSelected is 'q':
                confirmQuit = input('Do you really want to quit? ')
                while True:
                    if confirmQuit == 'y':
                        quit()
                    else:
                        break
            else:
                print('\n' + 'Wrong input!')

# trial outputs
# https://bytebaker.com/2008/11/03/switch-case-statement-in-python/
switch = 0
while True:
    if switch == 0:
        main = selectBetType(dictBetType, len(dictBetType)-1)
        if main in range(1,4,1):
            selection = selectBetNumber(dictTransBetType[dictBetType[main]])
            if selection in dictTransBetType[dictBetType[main]]:
                break
        else:
            switch += 1
    else: # Maybe this if/elif selection can be also realized with a dictonary.
        if main == 4:
            sub = selectBetType(dictColor, len(dictBetType)-2)
            dictNumToBet = {'color'          : dictColor[sub]}
        elif main == 5:
            sub = selectBetType(dictImPair, len(dictBetType)-2)
            dictNumToBet = {'pair or impair' : dictImPair[sub]}
        elif main == 6:
            sub = selectBetType(dictDozen, len(dictBetType)-2)
            dictNumToBet = {'dozen'          : dictDozen[sub]}
        elif main == 7:
            sub = selectBetType(dictColumn, len(dictBetType)-2)
            dictNumToBet = {'column'         : dictColumn[sub]}
        if sub is not 'x':
            selection = dictNumToBet[dictBetType[main]]
            break
        else:
            switch -=1
            continue

print('\n' + selection + '\n')
