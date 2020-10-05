#Practice problem number 2 in Chapter 4:
#https://automatetheboringstuff.com/2e/chapter4/

import random
numberOfStreaks = 0
long_streak_list = []
number_of_trials = 10000
for experimentNumber in range(number_of_trials):

    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = []
    for flip in range(100):
        coin_flips.append(random.randint(0,1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1
    long_streak = False

    for flip in range(len(coin_flips)):
        
        if coin_flips[flip] == coin_flips[flip-1]:
            streak += 1

            if streak == 6:
                long_streak = True
                long_streak_list.append(True)
                break

        else:
            streak = 1

    numberOfStreaks = len(long_streak_list)

print('Chance of streak: ' + str(100 * numberOfStreaks / number_of_trials) + "%")
