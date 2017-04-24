# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 1B - Problem C. Pony Express
# https://code.google.com/codejam/contest/8294486/dashboard#s=p2
#
# Time:  O(N^3)
# Space: O(1)
#

def floyd_warshall(N, D):
    for j in xrange(N):
        for i in xrange(N):
            for k in xrange(N):
                D[i][k] = min(D[i][k], D[i][j]+D[j][k])

def pony_express():
    N, Q = map(int, raw_input().strip().split())
    E, S = [], []
    for _ in xrange(N):
        Ei, Si = map(int, raw_input().strip().split())
        E.append(Ei)
        S.append(Si)
    D = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    U_V = [map(int, raw_input().strip().split()) for _ in xrange(Q)]

    D = [[float("inf") if k == -1 else float(k) for k in D[i]] for i in xrange(N)]
    floyd_warshall(N, D) # find min distance
    D = [[float("inf") if k > E[i] else float(k)/S[i] for k in D[i]] for i in xrange(N)]
    floyd_warshall(N, D) # find min time
    result = [D[U-1][V-1] for (U,V) in U_V]

    return " ".join(str(i) for i in result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, pony_express())
