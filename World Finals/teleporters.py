# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem F. Teleporters
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/000000000020184b
#
# Time:  O(N^3 * logM), pass in PyPy2 (sometimes TLE) but Python2
# Space: O(N^2 * logM)
#

def dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

def matrix_mult(A, B):  # Time: O(I * K * J)
    result = [[0]*len(B[0]) for _ in xrange(len(A))]
    for i in xrange(len(A)): 
        for j in xrange(len(B[0])): 
            for k in xrange(len(B)): 
                result[i][j] = max(result[i][j], A[i][k]+B[k][j]) 
    return result

def binary_search(left, right, check_fn, update_fn):  # find min x in (left, right) s.t. check(x) = true
    while right-left >= 2:
        mid = left + (right-left)//2
        found, new_U_matrix = check_fn(mid-left)  # Time: O(N^2), Space: O(N)
        if found:
            right = mid
        else:
            left = mid
            update_fn(new_U_matrix)  # Time: O(N), Space: O(N)
    return right

def teleporters():
    def check_fn(x):
        new_U_matrix = matrix_mult(U_matrix, matrix_pow[log2[x]])  # Time: O(N^2), Space: O(N)
        return any(dist(Q, teleporters[i]) <= U for i, U in enumerate(new_U_matrix[0])), new_U_matrix
    
    def update_fn(new_U_matrix):
        U_matrix[:] = new_U_matrix

    N = input()
    P, Q = [map(int, raw_input().strip().split()) for _ in xrange(2)]
    teleporters = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    if any(dist(P, t) == dist(Q, t) for t in teleporters):
        return 1
    if N == 1:
        return "IMPOSSIBLE"
    if all(dist(P, t) < dist(Q, t) for t in teleporters):
        pass  # P is the closer point
    elif all(dist(P, t) > dist(Q, t) for t in teleporters):
        P, Q = Q, P
    else:
        return 2

    MAX_STEP_NUM = max(dist(Q, t) for t in teleporters)  # each step strictly increase at least one distance
    left = 2-1  # extend binary search range from [2, MAX_RANGE] to (1, 1+2**(MAX_RANGE-1).bit_length())
    right = left+2**(MAX_STEP_NUM-1).bit_length()
    U_matrix = [[dist(P, t) for t in teleporters]]  # 1 x N matrix
    matrix_pow = [[[dist(teleporters[i], teleporters[j]) for j in xrange(len(teleporters))] for i in xrange(len(teleporters))]]
    log2, base = {1:0}, 2
    for i in xrange(1, (MAX_STEP_NUM-1).bit_length()):  # Time: O(N^3 * logM)
        matrix_pow.append(matrix_mult(matrix_pow[-1], matrix_pow[-1]))
        log2[base] = i
        base <<= 1
    return binary_search(left, right, check_fn, update_fn)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, teleporters())
