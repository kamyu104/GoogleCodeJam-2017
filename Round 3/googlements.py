# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 3 - Problem A. Googlements
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201902/00000000002017f6
#
# Time:  O(L * (H(L + 1, L) - 1)) = O(L * (C((L + 1) + (L - 1), L) - 1)) = O(L * ((2L)!/L!/L!-1)) = O(9 * (18!/9!/9!-1)) = O(9 * 48619)
# Space: O(L * (H(L + 1, L) - 1)) = O(L * (C((L + 1) + (L - 1), L) - 1)) = O(L * ((2L)!/L!/L!-1)) = O(9 * (18!/9!/9!-1)) = O(9 * 48619)
#

def nCr(n, r):
    if n-r < r:
        return nCr(n, n-r)
    c = 1
    for k in xrange(1, r+1):
        c *= n-k+1
        c //= k
    return c

def nextPermutation(nums):
    if len(nums) == 1:
        return False
    k, l = -1, 0
    for i in reversed(xrange(len(nums)-1)):
        if nums[i] < nums[i+1]:
            k = i
            break
    else:
        nums.reverse()
        return False

    for i in reversed(xrange(k+1, len(nums))):
        if nums[i] > nums[k]:
            l = i
            break
    nums[k], nums[l] = nums[l], nums[k]
    nums[k+1:] = nums[:k:-1]
    return True

def backtracking(G):
    if sum(G) > len(G):
        return 1
    new_G = []
    for i in reversed(xrange(len(G))):
        new_G.extend([i+1]*G[i])
    new_G.extend([0]*(len(G)-len(new_G)))
    new_G = new_G[::-1]
    if sum(new_G) > len(new_G):
        result, n = 1, len(G)
        for i in G:
            result *= nCr(n, i)
            n -= i
        return 1+result
    result = 0
    while True:
        result += backtracking(new_G) if new_G != G else 0
        if not nextPermutation(new_G):
            break
    return 1+result

def googlements():
    G = map(int, list(raw_input().strip()))
    return backtracking(G)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, googlements())
