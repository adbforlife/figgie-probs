import random
import numpy as np


possibles = []
for i in range(4):
    for j in range(i+1, 4):
        possible1 = [10,10,10,10]
        possible2 = [10,10,10,10]
        possible1[i] = 12
        possible1[j] = 8
        possible2[i] = 8
        possible2[j] = 12
        possibles.append(possible1)
        possibles.append(possible2)

# Randomly sample a deck, return something like [12,10,8,10]
def get_deck():
    return random.choice(possibles)

# Return 4 players' cards like
# [[3,1,2,4],
#  [5,2,1,2],
#  [1,0,5,4],
#  [3,5,2,0]]
def shuffle(deck):
    perm = np.random.permutation(40)
    res = []
    for pos in range(4):
        cards = perm[10*pos:10*(pos+1)]
        suits = [0,0,0,0]
        for card in cards:
            if card < deck[0]:
                suits[0] += 1
            elif card < deck[0] + deck[1]:
                suits[1] += 1
            elif card < deck[0] + deck[1] + deck[2]:
                suits[2] += 1
            else:
                suits[3] += 1
        res.append(suits)
    return res

''' This is for testing probability of combos.
num1 = 0
num2 = 0
total = 0
for i in range(1000000):
    deck = get_deck()
    res = shuffle(deck)
    combo = sorted(res[0])
    if combo == [2,2,3,3]:
        num1 += 1
    elif combo == [1,2,3,4]:
        num2 += 1
    total += 1
    if i % 1000 == 0:
        print(f"{num1 / total:.3f}, {num2 / total:.3f}")
'''

''' This is for testing probability of common suit given number of cards in suit
num = 0
total = 0
for i in range(1000000):
    deck = get_deck()
    res = shuffle(deck)
    combo = sorted(res[0])
    if sorted(combo)[3] == 5:
        ind = res[0].index(5)
        total += 1
        if res[0][ind] + res[1][ind] + res[2][ind] + res[3][ind] == 12:
            num += 1
    if i % 1000 == 0 and total > 0:
        print(f"{num/total:.3f}")
'''
