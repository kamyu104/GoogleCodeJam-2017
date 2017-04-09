# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Qualification Round - Problem A. Oversized Pancake Flipper
# https://code.google.com/codejam/contest/3264486/dashboard#s=p0
#
# Time:  O(K * S)
# Space: O(S)
#

def flip(stack, i, j):
    for k in xrange(i, j):
        stack[k] = '+' if stack[k] == '-' else '-'

def oversized_pancake_flipper():
    stack, K = raw_input().strip().split()
    stack, K = list(stack), int(K)
    count = 0
    for i in xrange(len(stack)-K+1):
        if stack[i] == '-':
            flip(stack, i, i+K)
            count += 1
    return count if '-' not in stack else "IMPOSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, oversized_pancake_flipper())
