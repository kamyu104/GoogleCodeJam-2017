# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem F. Teleporters
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/000000000020184b
#
# Time:  O(N^3 * logM), pass in PyPy2 but Python2
# Space: O(N^2 * logM)
#

from itertools import izip, islice

def dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

def vector_mult(A, B):  # Time: O(N^2), A is a N-d vector, B is a N x N symmetric matrix
    result = [0]*len(B[0])
    B_T = B
    for i, B_T_i in enumerate(B_T):
        for j, (A_j, B_T_i_j) in enumerate(izip(A, B_T_i)):
            dist = A[j] + B_T_i[j]
            if dist > result[i]:
                result[i] = dist
    return result

def matrix_mult(A, B):  # Time: O(N^3), A, B are both N x N symmetric matrixs
    result = [[0]*len(B[0]) for _ in xrange(len(A))]
    B_T = B
    for i, (result_i, A_i) in enumerate(izip(result, A)):
        for j, (result_j, B_T_j) in enumerate(islice(izip(result, B_T), i, len(result)), i):
            for A_i_k, B_T_j_k in izip(A_i, B_T_j):
                dist = A_i_k + B_T_j_k
                if dist > result_i[j]:
                    result_i[j] = result_j[i] = dist  # result is also a symmetric matrix
    return result

def binary_search(left, right, check_fn, update_fn):  # find min x in (left, right) s.t. check(x) = true
    while right-left >= 2:
        mid = left + (right-left)//2
        found, new_U_vector = check_fn(mid-left)  # Time: O(N^2), Space: O(N)
        if found:
            right = mid
        else:
            left = mid
            update_fn(new_U_vector)  # Time: O(N), Space: O(N)
    return right

def teleporters():
    def check_fn(x):
        new_U_vector = vector_mult(U_vector, matrix_pow[log2[x]])  # Time: O(N^2), Space: O(N)
        return any(dist(Q, teleporters[i]) <= U for i, U in enumerate(new_U_vector)), new_U_vector

    def update_fn(new_U_vector):
        U_vector[:] = new_U_vector

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

    MAX_STEP_NUM = max(dist(Q, t) for t in teleporters)  # the farest reachable distance strictly increase at least 1 per step
    ceil_log2_MAX_STEP_NUM = (MAX_STEP_NUM-1).bit_length()
    left = 2-1  # extend binary search range from [2, MAX_STEP_NUM] to (1, 1+2**ceil_log2_MAX_STEP_NUM)
    right = left+2**ceil_log2_MAX_STEP_NUM
    U_vector = [dist(P, t) for t in teleporters]  # N-d vector
    matrix_pow = [[[dist(teleporters[i], teleporters[j]) for j in xrange(len(teleporters))] for i in xrange(len(teleporters))]]
    log2, base = {1:0}, 2
    for i in xrange(1, ceil_log2_MAX_STEP_NUM):  # Time: O(N^3 * logM)
        matrix_pow.append(matrix_mult(matrix_pow[-1], matrix_pow[-1]))
        log2[base] = i
        base <<= 1
    return binary_search(left, right, check_fn, update_fn)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, teleporters())
