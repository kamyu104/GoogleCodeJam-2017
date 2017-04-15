# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 1A - Problem B. Ratatouille
# https://code.google.com/codejam/contest/5304486/dashboard#s=p1
#
# Time:  O(N^2 * P^2)
# Space: O(N * P)
#

def ratatouille():
    N, P = map(int, raw_input().strip().split())
    R = map(int, raw_input().strip().split())
    Q = []
    for _ in xrange(N):
        Q.append(map(int, raw_input().strip().split()))

    choices = []
    for i in xrange(N):
        for j in xrange(P):
            q, r = Q[i][j], R[i]
            lower = max(1, (10 * q + 11 * r - 1) // (11 * r))
            upper = (10 * q) // (9 * r)
            if lower > upper: continue
            choices.append((lower, False, i, q))
            choices.append((upper, True, i, q))
    choices.sort()

    count = 0
    quantities = [[] for _ in xrange(N)]
    for (_, is_upper, i, q) in choices:
        if is_upper:
            if q in quantities[i]:
                quantities[i].remove(q)
        else:
            quantities[i].append(q)
            if all(quantities):
                count += 1
                for j in xrange(N):
                    del quantities[j][0]
    return count

for case in xrange(input()):
    print 'Case #%d: %d' % (case+1, ratatouille())
