# compute prob that if you have x (5,6,7) of a suit, it is the common suit
# P(common | 5) = P(5 | common) P(common) / (P(5 | common) P(common) + P(5 | not common) P(not common))

from math import comb
from itertools import permutations
from prettytable import PrettyTable
import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})


def conditional_x(x, total):
    return comb(total, x) * comb(40-total, 8-x) / comb(40, 8)

def find_prob(x):
    x_and_common = 0.25 * conditional_x(x, 12)
    return x_and_common / (x_and_common + 0.5 * conditional_x(x, 10) + 0.25 * conditional_x(x, 8))

t = PrettyTable(["Num cards", "Prob common suit"])
for i in range(9):
    t.add_row([i, f"{find_prob(i):.3f}"])
print(t)

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


# combo is of the form [1,2,2,3],
def conditional(combo, total):
    res = 1
    for i in range(len(combo)):
        res *= comb(total[i], combo[i])
    return res / comb(40, 8)

# we return a 4-element array indicating the probs they are the common suit
def find_probs(combo):
    res = []
    for pos in range(4):
        combo_and_common = 0
        combo_and_not_common = 0
        for total in possibles:
            if total[pos] == 12:
                combo_and_common += conditional(combo, total) / 12
            else:
                combo_and_not_common += conditional(combo, total) / 12
        res.append(combo_and_common / (combo_and_common + combo_and_not_common))
    return res

def combo_prob(combo):
    res = 0
    for total in possibles:
        res += conditional(combo, total) / 12
    perms = []
    for perm in permutations(combo):
        if perm not in perms:
            perms.append(perm)
    return len(perms) * res

# Enumerate combos
combos = []
for a in range(9):
    for b in range(9):
        for c in range(9):
            if a + b + c <= 8:
                d = 8 - (a + b + c)
                combo = sorted([a,b,c,d])
                if combo not in combos:
                    combos.append(combo)

combo_probs = []
for combo in combos:
    combo_probs.append([combo, combo_prob(combo), np.array(find_probs(combo))])
combo_probs = sorted(combo_probs, key=lambda x:-x[1])

t = PrettyTable(['Prob of combo', 'Combo', 'Prob of each suit common'])
for x in combo_probs:
    t.add_row([f"{x[1]:.3f}", x[0], x[2]])
print(t)

