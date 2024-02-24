#import random

#counter = 0

#def Bingo ():
  #for i in range(8):
    #x = random.randint(1,90)
    #return x

#card = [[Bingo(), Bingo(), Bingo()], [Bingo(), "BINGO", Bingo()], [Bingo(), Bingo(), Bingo()]]

#y = int(random.randint(0,2))
#x = int(random.randint(0,2))
#print(y, x)

#print(card[y][x])

import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()