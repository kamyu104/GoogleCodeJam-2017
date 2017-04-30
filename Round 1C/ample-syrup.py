# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 1C - Problem A. Ample Syrup
# https://code.google.com/codejam/contest/3274486/dashboard#s=p0
#
# Time:  O(NlogK)
# Space: O(K)
#

from math import pi
from heapq import heappush, heappop

def ample_syrup():
    N, K = map(int, raw_input().strip().split())
    Ps = []
    for i in xrange(N):
        Ps.append(map(int, raw_input().strip().split()))
    Ps.sort()

    result, min_heap = 0, []
    for P in Ps:
        if len(min_heap) == K-1:
            result = max(result, P[0] * P[0] + 2 * P[0] * P[1] + sum(min_heap))
        heappush(min_heap, 2 * P[0] * P[1])
        if len(min_heap) >= K:
            heappop(min_heap)
    return result * pi

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, ample_syrup())
