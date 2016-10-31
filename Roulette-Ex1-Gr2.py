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
print('\n' + 'Hello', player + '!' , '\n')
