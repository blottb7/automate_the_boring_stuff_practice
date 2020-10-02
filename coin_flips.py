#Practice problem number 2 in Chapter 4

import random
numberOfStreaks = 0
for experimentNumber in range(1):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = []
    for flip in range(100):
        coin_flips.append(random.randint(0,1))
        #print(coin_flips[flip-1])
    #print(flip)
    #print(coin_flips)
    #print(len(coin_flips))
    #print(type(coin_flips))
    #print(coin_flips[flip-1])
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1
    #while streak < 6:
    for flip in range(len(coin_flips)):
        #print(coin_flips)
        #print(coin_flips[flip])
        if coin_flips[flip] == coin_flips[flip-1]:
            streak += 1
                #print(streak)
                #print(coin_flips[flip])
        else:
            streak = 1
        print(streak)

#print('Chance of streak: %s%%' % (numberOfStreaks / 100))
