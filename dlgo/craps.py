from numpy import random
import sys

def getDice():
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    print('You rolled a ' + str(n1) + ' and a ' + str(n2))
    return n1 + n2


result = getDice()

if result == 7 or result == 11:
    print('You Win')
    sys.exit()

elif result == 2 or result == 3 or result == 12:
    print('You Lose!')
    sys.exit()

point = result

while result != 7 and result != point:
    result = getDice()

if result == 7:
    print('You Lose')
else:
    print('You Win')
