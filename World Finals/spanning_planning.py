# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem C. Spanning Planning
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/000000000020187a
#
# Time:  O(R * N^3), R is the times of random, which may be up to 2*10^5
# Space: O(N^2),     N is the empirical number of nodes, which could be 13
#

from random import randint, seed
from operator import mul

def determinant(matrix):
    N = len(matrix)
    sign = 1
    for d in xrange(N):  # turn laplacian matrix into upper triangle form by Gaussian elimination
        for i in xrange(d, N):
            if matrix[i][d] > EPS:
                break
        else:
            break
        if i != d:
            matrix[i], matrix[d] = matrix[d], matrix[i]
            sign *= -1  # interchange
        for i in xrange(d+1, N): 
            scalar = matrix[i][d]/matrix[d][d]
            for j in xrange(N):
                matrix[i][j] -= scalar*matrix[d][j]
    return int(round(sign*reduce(mul, (matrix[d][d] for d in xrange(N)))))

def minor(matrix, r, c):
    return determinant([[v for j, v in enumerate(row) if j+1 != c] 
                           for i, row in enumerate(matrix) if i+1 != r])

def cofactor(matrix, r, c):
    return (-1)**((r+c)%2) * minor(matrix, r, c)

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
        if laplacian_matrix[i][i] == 0.0:
            return 0
    return cofactor(laplacian_matrix, 1, 1)

def spanning_planning():
    K = input()
    if K <= MAX_N:
        N = K
        adj = [[int(abs(i-j) in (1, N-1)) for j in xrange(N)] for i in xrange(N)]
    else:
        N = EXP_N
        adj = [[0]*N for _ in xrange(N)]
        for i in xrange(N):
            for j in xrange(i+1, N):
                adj[i][j] = adj[j][i] = int(randint(1, P_INV) == 1)
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
EXP_N = 13
P_INV = 4
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, spanning_planning())
