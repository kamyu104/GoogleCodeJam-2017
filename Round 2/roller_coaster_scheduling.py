# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 2 - Problem B. Roller Coaster Scheduling
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/0000000000201845
#
# Time:  O(N + M)
# Space: O(N + M)
#

from collections import defaultdict

def ceil(a, b):
    return (a-1)//b+1

def roller_coaster_scheduling():
    N, C, M = map(int, raw_input().strip().split())
    seat_count, customer_count = defaultdict(int), defaultdict(int)
    for _ in xrange(M):
        P, B = map(int, raw_input().strip().split())
        seat_count[P] += 1
        customer_count[B] += 1
    min_ride, accu = max(customer_count.itervalues()), 0
    for k in xrange(1, N+1):
        if k not in seat_count:
            continue
        accu += seat_count[k]
        min_ride = max(min_ride, ceil(accu, k))
    min_promote = 0
    for k in xrange(1, N+1):
        if k not in seat_count:
            continue
        min_promote += max(seat_count[k]-min_ride, 0)
    return "{} {}".format(min_ride, min_promote)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, roller_coaster_scheduling())
