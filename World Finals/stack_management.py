# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem E. Stack Management
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/00000000002017fd
#
# Time:  O((N * C) * log(N * C))
# Space: O(N * C)
#

from collections import defaultdict
from heapq import heappush, heappop

def preprocess(stks):
    q = []
    min_heaps = defaultdict(list)
    for i in xrange(len(stks)):
        value, suite = stks[i][-1]
        heappush(min_heaps[suite], (value, i))
        q.append(suite)
    while q:
        suite = q.pop()
        if len(min_heaps[suite]) == 1:
            continue
        _, i = heappop(min_heaps[suite])
        stks[i].pop()
        if not stks[i]:
            continue
        value, suite = stks[i][-1]
        heappush(min_heaps[suite], (value, i))
        q.append(suite)

def dfs(edges, source, targets):
    stk, lookup = [source], set([source])
    while stk:
        u = stk.pop()
        if u in targets:
            return True
        if u not in edges:
            continue
        for v in edges[u]:
            if v in lookup:
                continue
            lookup.add(v)
            stk.append(v)
    return False

def stack_management():
    N, C = map(int, raw_input().strip().split())
    stks = map(lambda x: STACKS[x][:], map(int, raw_input().strip().split()))
    preprocess(stks)
    suite_to_values = defaultdict(list)
    for i, stk in enumerate(stks):
        for idx, (value, suite) in enumerate(stk):
            suite_to_values[suite].append(value)
    if len(suite_to_values) < len(stks):
        return "POSSIBLE"
    if len(suite_to_values) > len(stks):
        return "IMPOSSIBLE"
    for stk in stks:
        if len(stk) > 1:
            break
    else:
        return "POSSIBLE"
    for stk in stks:
        if not stk:
            break
    else:
        return "IMPOSSIBLE" 
    for values in suite_to_values.itervalues():
        values.sort()
    stk_to_last_ace_suite, stk_to_king_suites = {}, defaultdict(list)
    for i, stk in enumerate(stks):
        if not stk:
            continue
        value, suite = stk[0]
        if value == suite_to_values[suite][-1]:
            stk_to_last_ace_suite[i] = suite
        for j, (value, suite) in enumerate(stk):
            if len(suite_to_values[suite]) >= 2 and value == suite_to_values[suite][-2]:
                stk_to_king_suites[i].append(suite)
    
    vertex = {suite for suite in stk_to_last_ace_suite.itervalues()}
    sources = {suite for suite in stk_to_last_ace_suite.itervalues() if len(suite_to_values[suite]) == 1}
    targets = {suite for i, suite in stk_to_last_ace_suite.iteritems() for (value2, suite2) in stks[i] if suite2 != suite and suite_to_values[suite2][-1] == value2}
    edges = defaultdict(list)
    for i, ace_suite in stk_to_last_ace_suite.iteritems():
        if i not in stk_to_king_suites:
            continue
        for king_suite in stk_to_king_suites[i]:
            if king_suite not in vertex or ace_suite == king_suite:
                continue
            edges[ace_suite].append(king_suite)
    for source in sources:
        if dfs(edges, source, targets):
            break
    else:
        return "IMPOSSIBLE"
    return "POSSIBLE"

P = input()
STACKS = []
for _ in xrange(P):
    V_S = map(int, raw_input().strip().split())
    STACKS.append([(V_S[2*i+1], V_S[2*i+2]) for i in reversed(xrange((len(V_S)-1)//2))])
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, stack_management())
