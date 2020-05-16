# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 3 - Problem B. Good News and Bad News
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201902/0000000000201846
#
# Time:  O(P)
# Space: O(P)
#

from sys import setrecursionlimit
from collections import defaultdict
from itertools import imap

def dfs(G, prev_id, u, stk, lookup, result):
    for i, v in G[u]:
        if ~i == prev_id:
            continue
        if v not in lookup:
            lookup[v] = len(lookup)+1
            stk.append((i, v))
            dfs(G, i, v, stk, lookup, result)
            stk.pop()
            continue
        if lookup[v] >= lookup[u]:
            continue
        result[i if i >= 0 else ~i] += 1 if i >= 0 else -1
        for j, t in reversed(stk):
            if t == v:
                break
            result[j if j >= 0 else ~j] += 1 if j >= 0 else -1

def good_news_and_bad_news():
    F, P = map(int, raw_input().strip().split())
    G = defaultdict(list)
    for i in xrange(P):
        A, B = map(int, raw_input().strip().split())
        G[A].append((i, B))
        G[B].append((~i, A))
    result, lookup, stk = [0]*P, {}, []
    for u in G.iterkeys():
        if u in lookup:
            continue
        lookup[u] = len(lookup)+1
        stk.append((None, u))
        dfs(G, None, u, stk, lookup, result)
        stk.pop()
    if any(x == 0 for x in result):
        return "IMPOSSIBLE"
    return " ".join(imap(str, result))

BASE = 3
MAX_F = 1000
setrecursionlimit(BASE+(1+MAX_F))
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, good_news_and_bad_news())
