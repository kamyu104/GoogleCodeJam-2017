# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 1B - Problem B. Stable Neigh-bors
# https://code.google.com/codejam/contest/8294486/dashboard#s=p1
#
# Time:  O(N)
# Space: O(1)
#

def stable_neighbors():
    N, R, O, Y, G, B, V = map(int, raw_input().strip().split())
    result = None
    if R == G != 0:
        result = "RG" * R if N == R + G else "IMPOSSIBLE"
    elif Y == V != 0:
        result = "YV" * Y if N == Y + V else "IMPOSSIBLE"
    elif B == O != 0: 
        result = "BO" * B if N == B + O else "IMPOSSIBLE"
    else:
        sort = sorted(((R - G, "R"), (Y - V, "Y"), (B - O, "B")))
        if sort[2][0] <= sort[1][0] + sort[0][0]:
            result = (sort[2][1] + sort[1][1] + sort[0][1]) * (sort[1][0] + sort[0][0] - sort[2][0]) + \
                    (sort[2][1] + sort[1][1]) * (sort[2][0] - sort[0][0]) + \
                    (sort[2][1] + sort[0][1]) * (sort[2][0] - sort[1][0])
            if G:
                result = result.replace("R", "R" + "GR" * G, 1)
            if V:
                result = result.replace("Y", "Y" + "VY" * V, 1)
            if O:
                result = result.replace("B", "B" + "OB" * O, 1)
        else:
            result = "IMPOSSIBLE"
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, stable_neighbors())
