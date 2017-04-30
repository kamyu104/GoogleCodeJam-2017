# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 1C - Problem C. Core Training
# https://code.google.com/codejam/contest/3274486/dashboard#s=p2
#
# Time:  O(N^2 * K)
# Space: O(K)
#

def calc(probs, K):
    dp = [0.0 for _ in xrange(K+1)]
    dp[0] = 1.0
    for p in probs:
        prev_dp = dp
        dp = [(1.0-p)*prev_dp[i] + p*prev_dp[max(i-1, 0)] for i in xrange(K+1)]
    return dp[K]

def upfill(probs, U, start_index):
    for i in xrange(start_index, len(probs)):
        if i + 1 < len(probs):
            d = probs[i+1] - probs[i]
        else:
            d = 1.0 - probs[i]
        add = min(d, U / (i - start_index + 1))
        for k in xrange(start_index, i+1):
            probs[k] += add
            U -= add
        if U <= 0.0:
            break
    for i in reversed(xrange(start_index)):
        d = probs[i+1] - probs[i]
        if U > d:
            probs[i] = probs[i+1]
            U -= d
        else:
            probs[i] += U
            break
    found = (start_index-1 < 0 or probs[start_index-1] < probs[start_index])
    return found, probs


def core_training():
    N, K = map(int, raw_input().strip().split())
    U = float(input())
    Ps = map(float, raw_input().strip().split())
    Ps.sort()

    result = 0.0
    Ps.sort()
    for start_index in xrange(len(Ps)):
        found, tmp_probs = upfill(list(Ps), U, start_index)
        if found:
            result = max(result, calc(tmp_probs, K))
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, core_training())