import random
from itertools import groupby
from collections import Counter
numStreak = 0

for experimentNumber in range (10000):
    flips = []
    for toss in range(100): #code that creates list of 100 'heads' or 'tails' values
        if random.randint(0,1) == 0:
            flips.append('H')
        else:
            flips.append('T')
    #code that checks if there is a streak of 6 heads or tails in a row
    streak_threshold = 6
    grps_by_streak = [grp_id for grp_id, grp in groupby(flips) if len(list(grp)) >=streak_threshold]
    #print(grps_by_streak)
    cc = Counter(grps_by_streak)
    #print(cc)
    numStreak = sum(cc.values())
    #print(numStreak)
print ('Chance of streak: %s%%' % (numStreak / 100))