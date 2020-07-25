# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem E. Stack Management
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/00000000002017fd
#
# Time:  O((N * C) * logN)
# Space: O(N)
#

from collections import defaultdict
from heapq import heappush, heappop

def preprocess(stks):  # Time: O((N * C) * logN), Space: O(N)
    min_heaps, s = defaultdict(list), []
    for i, stk in enumerate(stks):
        value, suite = stk[-1]
        heappush(min_heaps[suite], (value, i))
        if len(min_heaps[suite]) > 1:
            s.append(suite)
    while s:
        suite = s.pop()
        _, i = heappop(min_heaps[suite])
        stks[i].pop()
        if not stks[i]:
            continue
        value, suite = stks[i][-1]
        heappush(min_heaps[suite], (value, i))
        if len(min_heaps[suite]) > 1:
            s.append(suite)

def dfs(edges, source, targets):  # Time: O(N), Space: O(N)
    s, lookup = [source], set([source])
    while s:
        u = s.pop()
        if u in targets:
            return True
        if u not in edges:
            continue
        for v in edges[u]:
            if v in lookup:
                continue
            lookup.add(v)
            s.append(v)
    return False

def stack_management():
    N, C = map(int, raw_input().strip().split())
    stks = map(lambda x: STKS[x][:], map(int, raw_input().strip().split()))
    preprocess(stks)  # remove all cards if possible 
    for stk in stks:
        if len(stk) > 1:
            break
    else:
        return "POSSIBLE"
    suite_to_values = defaultdict(list)
    for i, stk in enumerate(stks):  # Time: O((N * C) * log2), Space: O(N)
        for idx, (value, suite) in enumerate(stk):
            heappush(suite_to_values[suite], value)
            if len(suite_to_values[suite]) == 3:
                heappop(suite_to_values[suite])
            elif len(suite_to_values) > len(stks):
                return "IMPOSSIBLE"  # early return
    if len(suite_to_values) < len(stks):
        return "POSSIBLE"
    for stk in stks:
        if not stk:
            break
    else:
        return "IMPOSSIBLE"  # no empty stack

    sources, targets, edges = [], [], defaultdict(list)
    for i, stk in enumerate(stks):  # Time: O(R * C)
        if not stk:
            continue
        ace_value, ace_suite = stk[0]
        if ace_value != suite_to_values[ace_suite][-1]:
            continue
        if len(suite_to_values[ace_suite]) == 1:
            sources.append(ace_suite)
        for value, suite in stk:
            if suite == ace_suite:
                continue
            if value == suite_to_values[suite][-1]:
                targets.append(ace_suite)
            if len(suite_to_values[suite]) >= 2 and value == suite_to_values[suite][-2]:
                edges[ace_suite].append(suite)
    for source in sources:
        if dfs(edges, source, targets):
            break
    else:
        return "IMPOSSIBLE"
    return "POSSIBLE"

P = input()
STKS = []
for _ in xrange(P):
    V_S = map(int, raw_input().strip().split())
    STKS.append([(V_S[2*i+1], V_S[2*i+2]) for i in reversed(xrange((len(V_S)-1)//2))])
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, stack_management())
