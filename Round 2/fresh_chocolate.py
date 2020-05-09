# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 2 - Problem A. Fresh Chocholate
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/00000000002017f4
#
# Time:  O(1)
# Space: O(1)
#

from collections import Counter

def ceil(a, b):
    return (a-1)//b+1

def floor(a, b):
    return a//b

def fresh_chocolate():
    N, P = map(int, raw_input().strip().split())
    G = map(lambda x: int(x)%P, raw_input().strip().split())
    lookup = Counter(G)
    if P == 2:
        return lookup[0] + ceil(lookup[1], 2)
    if P == 3:
        return lookup[0] + min(lookup[1], lookup[2]) + ceil(abs(lookup[1]-lookup[2]), 3)
    if P == 4:
        return lookup[0] + floor(lookup[2], 2) + min(lookup[1], lookup[3]) + ceil(2*(lookup[2]%2) + abs(lookup[1]-lookup[3]), 4)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fresh_chocolate())
