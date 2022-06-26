import csv
import os
import random


print(os.getcwd())
play = 'y'

index = random.randint(0, 51)
print(index)
while play == 'y':

    #draw = input('Draw?')

    with open('pythonpractice/cards.csv', newline='') as csvfile:
        GAME = csv.reader(csvfile,delimiter=' ',quotechar='|')
        headers = next(GAME)
        for row in GAME:
            card = row(index)
        print(card)
