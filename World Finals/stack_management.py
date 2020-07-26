# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem E. Stack Management
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/00000000002017fd
#
# Time:  O((N * C) * logN)
# Space: O(N * C)
#

from collections import defaultdict
from heapq import heappush, heappop

def preprocess(piles):  # Time: O((N * C) * logN), Space: O(N)
    min_heaps, stk = defaultdict(list), []
    for i, pile in enumerate(piles):
        value, suite = pile[-1]
        heappush(min_heaps[suite], (value, i))
        if len(min_heaps[suite]) > 1:
            stk.append(suite)
    while stk:
        suite = stk.pop()
        _, i = heappop(min_heaps[suite])
        piles[i].pop()
        if not piles[i]:
            continue
        value, suite = piles[i][-1]
        heappush(min_heaps[suite], (value, i))
        if len(min_heaps[suite]) > 1:
            stk.append(suite)

def dfs(adj, source, targets):  # Time: O(N), Space: O(N)
    stk, lookup = [source], set([source])
    while stk:
        u = stk.pop()
        if u in targets:
            return True
        if u not in adj:
            continue
        for v in adj[u]:
            if v in lookup:
                continue
            lookup.add(v)
            stk.append(v)
    return False

def stack_management():
    N, C = map(int, raw_input().strip().split())
    piles = map(lambda x: PILES[x][:], map(int, raw_input().strip().split()))
    preprocess(piles)  # remove all cards if possible 
    for pile in piles:
        if len(pile) > 1:
            break
    else:
        return "POSSIBLE"
    suite_to_max_two_values = defaultdict(list)
    for i, pile in enumerate(piles):  # Time: O((N * C) * log2), Space: O(N)
        for idx, (value, suite) in enumerate(pile):
            heappush(suite_to_max_two_values[suite], value)
            if len(suite_to_max_two_values[suite]) == 3:
                heappop(suite_to_max_two_values[suite])
            elif len(suite_to_max_two_values) > len(piles):
                return "IMPOSSIBLE"  # early return
    if len(suite_to_max_two_values) < len(piles):
        return "POSSIBLE"
    for pile in piles:
        if not pile:
            break
    else:
        return "IMPOSSIBLE"  # no empty stack

    vertices = {pile[0][1] for pile in piles if pile and pile[0][0] == suite_to_max_two_values[pile[0][1]][-1]}  # Time: O(N)
    sources, targets, adj = [], set(), defaultdict(list)
    for i, pile in enumerate(piles):  # Time: O(N * C)
        if not pile:
            continue
        ace_value, ace_suite = pile[0]
        if ace_value != suite_to_max_two_values[ace_suite][-1]:
            continue
        if len(suite_to_max_two_values[ace_suite]) == 1:
            sources.append(ace_suite)
        for value, suite in pile:
            if suite == ace_suite:
                continue
            if value == suite_to_max_two_values[suite][-1]:
                targets.add(ace_suite)
            elif suite in vertices and len(suite_to_max_two_values[suite]) == 2 and value == suite_to_max_two_values[suite][-2]:
                adj[ace_suite].append(suite)
    for source in sources:  # total - Time: O(N), Space: O(N)
        if dfs(adj, source, targets):
            break
    else:
        return "IMPOSSIBLE"
    return "POSSIBLE"

P = input()
PILES = []
for _ in xrange(P):
    V_S = map(int, raw_input().strip().split())
    PILES.append([(V_S[2*i+1], V_S[2*i+2]) for i in reversed(xrange((len(V_S)-1)//2))])
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, stack_management())
