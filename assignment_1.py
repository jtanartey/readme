import random

roll = random.randint(1,6)
print (roll)

question = input('Would you like to roll the dice [y/n]?\n')

while question != 'n':
    if question == 'y':
        die = random.randint(1, 6)
        print(die)
        question = input('Would you like to roll the dice [y/n]?\n')
    else:
        print('Invalid response. Please type "y" or "n".')
        question = input('Would you like to roll the dice [y/n]?\n')        

print('Good-bye!')