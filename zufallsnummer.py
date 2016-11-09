print("Drücken sie S um das Roulette Rad zu starten")

dictPlay = {'s' : 'spin the wheel',
            'x' : 'one level up',
            'q' : 'quit'}

def printDictSorted(dictPlay):
    for key, value in sorted(dictPlay.items()):
        print("{} = {}".format(key, value))


bet= 17
budget = 30
einsatz = 5
import random
roulette = random.randint(0,36)
print("ergebnis", roulette)
if roulette != bet:
    budget = budget-einsatz
    print("Sie haben leider falsch getippt")
    print('\n' + 'Your new budget is {:.2f}'.format(budget) + '\n')
else:
    budget += einsatz
    print("Sie haben richtig getippt")
    print('\n' + 'Your new budget is {:.2f}'.format(budget) + '\n')
