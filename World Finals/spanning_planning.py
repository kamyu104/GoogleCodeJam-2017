# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem B. Operation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/000000000020184a
#
# Time:  O(R * 22^3), R is the times of random, R may be up to 10^6, TLE in both Python2 / PyPy2, but pass in C++
# Space: O(22^2)
#

from random import randint, seed
from operator import mul

# https://www.geeksforgeeks.org/total-number-spanning-trees-graph/
def kirchhoff_matrix_tree_theorem(adj):
    N = len(adj)
    laplacian_matrix = [[0.0]*N for _ in xrange(N)]
    for i in xrange(N):
        for j in xrange(N):
            if not adj[i][j]:
                continue
            laplacian_matrix[i][i] += 1
            laplacian_matrix[i][j] -= adj[i][j]
    for d in xrange(N-1):  # make laplacian matrix upper triangle form
        for i in xrange(d, N-1):
            if laplacian_matrix[i][d] > EPS:
                break
        else:
            break
        laplacian_matrix[i], laplacian_matrix[d] = laplacian_matrix[d], laplacian_matrix[i]
        for i in xrange(d+1, N-1): 
            coef = -laplacian_matrix[i][d]/laplacian_matrix[d][d]
            for j in xrange(N-1):
                laplacian_matrix[i][j] += coef*laplacian_matrix[d][j]
    return int(round(reduce(mul, (laplacian_matrix[d][d] for d in xrange(N-1)))))

def spanning_planning():
    K = input()
    N = min(K, MAX_N)
    adj = [[0]*N for _ in xrange(N)]
    if K <= MAX_N:
        for i in xrange(N):
            for j in xrange(N):
                adj[i][j] = int(abs(i-j) == 1 or abs(i-j) == N-1)
    else:
        while True:
            number_of_spanning_tree = kirchhoff_matrix_tree_theorem(adj)
            if number_of_spanning_tree > K:
                while True:
                    i, j = randint(0, N-1), randint(0, N-1)
                    if i != j and adj[i][j]:
                        adj[i][j] = adj[j][i] = 0
                        break
            elif number_of_spanning_tree < K:
                while True:
                    i, j = randint(0, N-1), randint(0, N-1)
                    if i != j and not adj[i][j]:
                        adj[i][j] = adj[j][i] = 1
                        break
            else:
                break
    return "%s\n%s" % (N, "\n".join("".join(map(str, row)) for row in adj))

seed(0)
EPS = 0.1
MAX_N = 22
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, spanning_planning())
