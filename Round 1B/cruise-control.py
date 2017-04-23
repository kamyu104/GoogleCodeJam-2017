# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 1B - Problem A. Steed 2: Cruise Control
# https://code.google.com/codejam/contest/8294486/dashboard#s=p0
#
# Time:  O(N)
# Space: O(1)
#

def  cruise_control():
    D, N = map(int, raw_input().strip().split())
    max_time = 0
    for _ in xrange(N):
        K, S = map(int, raw_input().strip().split())
        max_time = max(max_time, float(D - K) / S)
    return D / max_time

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, cruise_control())
