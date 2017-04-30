# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 1C - Problem A. Ample Syrup
# https://code.google.com/codejam/contest/3274486/dashboard#s=p0
#
# Time:  O((A_C + A_J) * log(A_C + A_J))
# Space: O(A_C + A_J)
#

def parenting_partnering():
    A_C, A_J = map(int, raw_input().strip().split())
    intervals = []
    for _ in xrange(A_C):
        C, D = map(int, raw_input().strip().split())
        intervals.append((C, D, 0))
    for _ in xrange(A_J):
        J, K = map(int, raw_input().strip().split())
        intervals.append((J, K, 1))
    intervals.sort()
    
    exchange, charged_time, gaps = 0, [0] * 2, [[] for _ in xrange(2)]
    for interval in intervals:
        charged_time[interval[2]] += interval[1] - interval[0]
    for i in xrange(len(intervals)-1):
        if intervals[i][2] == intervals[i+1][2]:
            gaps[intervals[i][2]].append(intervals[i+1][0] - intervals[i][1])
        else:
            exchange += 1
    if intervals[-1][2] == intervals[0][2]:
        gaps[intervals[-1][2]].append(1440 + intervals[0][0] - intervals[-1][1])
    else:
        exchange += 1
    
    for i in xrange(2):
        gaps[i].sort(reverse=True)
        while gaps[i] and charged_time[i] + gaps[i][-1] <= 720:  # merge from the smallest gap
            charged_time[i] += gaps[i][-1]
            gaps[i].pop()
        exchange += 2 * len(gaps[i])
    return exchange

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, parenting_partnering())