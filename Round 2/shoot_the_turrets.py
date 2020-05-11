# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 2 - Problem D. Shoot the Turrets
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/0000000000201901
#
# Time:  build G with BFSes:   O(S * R * C)
#        bipartite matching:   O((S * T) * sqrt(S + T))
#        build G's with BFSes: O(S * R * C + T * S * (R + C))
#        build Hs:             O(T * (S * T))
#        total:                O(S * R * C + S * T^2 + T * S * (R + C))
# Space: build G with BFSes:   O(R * C)
#        bipartite matching:   O(S + T)
#        build G's with BFSes: O(R * C)
#        build Hs:             O(S * T)
#        total:                O(S * R * C)
#
# PyPy2 always pass in large dataset, but Python2 sometimes fails (the time is very tight)
#

from collections import Counter, defaultdict, deque

# Time:  O(E * sqrt(V))
# Space: O(V)
# Source code from http://code.activestate.com/recipes/123641-hopcroft-karp-bipartite-matching/
# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002
def bipartiteMatch(graph):
    '''Find maximum cardinality matching of a bipartite graph (U,V,E).
    The input format is a dictionary mapping members of U to a list
    of their neighbors in V.  The output is a triple (M,A,B) where M is a
    dictionary mapping members of V to their matches in U, A is the part
    of the maximum independent set in U, and B is the part of the MIS in V.
    The same object may occur in both U and V, and is treated as two
    distinct vertices if this happens.'''
    
    # initialize greedy matching (redundant, but faster than full search)
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break
    
    while 1:
        # structure residual graph into layers
        # pred[u] gives the neighbor in the previous layer for u in U
        # preds[v] gives a list of neighbors in the previous layer for v in V
        # unmatched gives a list of unmatched vertices in final layer of V,
        # and is also used as a flag value for pred[u] when u is in the first layer
        preds = {}
        unmatched = []
        pred = dict([(u,unmatched) for u in graph])
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)
        
        # repeatedly extend layering structure by another pair of layers
        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v,[]).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)
        
        # did we finish layering without finding any alternating paths?
        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return (matching,list(pred),list(unlayered))

        # recursively search backward through layers to find alternating paths
        # recursion returns true if found path, false otherwise
        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0

        for v in unmatched: recurse(v)

def group_T(G, T_inv):  # Time: O(R * C), Space: O(R * C)
    H_T, V_T = defaultdict(set), defaultdict(set)
    H, V = [[0]*len(G[0]) for _ in xrange(len(G))], [[0]*len(G[0]) for _ in xrange(len(G))]
    for i in xrange(len(G)):
        H_T[len(H_T)+1] = set()
        for j in xrange(len(G[0])):
            if G[i][j] == '#':
                H_T[len(H_T)+1] = set()
                continue
            H[i][j] = len(H_T)
            if G[i][j] == 'T':
                H_T[len(H_T)].add(T_inv[i, j])
    for j in xrange(len(G[0])):
        V_T[len(V_T)+1] = set()
        for i in xrange(len(G)):
            if G[i][j] == '#':
                V_T[len(V_T)+1] = set()
                continue
            V[i][j] = len(V_T)
            if G[i][j] == 'T':
                V_T[len(V_T)].add(T_inv[i, j])
    return H, V, H_T, V_T

def remove_T(H, V, H_T, V_T, T, t):  # Time: O(1), Space: O(1)
    r, c = T[t]
    H_T[H[r][c]].remove(t)
    V_T[V[r][c]].remove(t)

def find_T(h, h_t, r, c):  # Time: O(1), Space: O(1)
    return h_t[h[r][c]]

def bfs(G, M, T_inv, H, V, H_T, V_T, q, lookup):  # Time: O(R * C), Space: O(R * C)
    result, pending = set(), deque()
    while q:
        r, c, step = q.popleft()
        if (r, c) in lookup and lookup[r, c] < step:
            continue
        can_move = True
        for h, h_t in [(H, H_T), (V, V_T)]:
            ts = find_T(h, h_t, r, c)
            if not ts:
                continue
            can_move = False
            for t in ts:
                result.add(t)
        if not can_move:
            pending.append((r, c, step))
            continue
        if step+1 > M:
            continue
        step += 1
        for dr, dc in DIRECTIONS:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < len(G) and 0 <= nc < len(G[0]) and
                    G[nr][nc] != "#" and
                    ((nr, nc) not in lookup or lookup[nr, nc] > step)):
                continue
            lookup[nr, nc] = step
            q.append((nr, nc, step))
    return result, pending

def find_max_bipartite_matching(G, M, S, T, T_inv):
    E = defaultdict(list)
    for i, (r, c) in S.iteritems():  # Time: O(S * R * C)
        H, V, H_T, V_T = group_T(G, T_inv)
        pending, lookup = deque([(r, c, 0)]), {}
        while pending:
            ts, pending = bfs(G, M, T_inv, H, V, H_T, V_T, pending, lookup)
            for t in ts:
                E[t].append(i)
                remove_T(H, V, H_T, V_T, T, t)
    match, _, _ = bipartiteMatch(E)  # Time: O((S * T) * sqrt(S + T)), Space: O(S + T)
    return match

def find_cycle(E, i, match):  # Time: O(T), Space: O(T)
    if i in match:
        return i
    for j in E[i]:
        match[i] = j
        start = find_cycle(E, j, match)
        if start != 0:
            return start
    assert(False)
        
def find_alternate_matching(G, M, S, T, T_inv, match):
    H, V, H_T, V_T = group_T(G, T_inv)
    result = []
    pending, lookup = {}, {}
    for i in match.iterkeys():
        r, c = S[i]
        pending[i], lookup[i] = deque([(r, c, 0)]), {}
    while match:  # Time: O(S * (R * C + T) + T * S * (R + C) + T)), each time add at least one valid edge, at most len(match)
        E = defaultdict(list)
        T_set = set(match.itervalues())
        for i in match.iterkeys():  # Time: O(S * (R * C + T) + T * S * (R + C))
            r, c = S[i]
            ts, pending[i] = bfs(G, M, T_inv, H, V, H_T, V_T, pending[i], lookup[i])
            for t in ts:  # Time: O(R * C)
                if t not in T_set:  # exchange with a valid edge
                    result.append((i, t))
                    remove_T(H, V, H_T, V_T, T, t)
                    match.pop(i)
                    break
                E[i].append(-t)
            else:
                E[-match[i]].append(i)
                continue
            break
        else:  # Time: O(T)
            new_match = {}
            i = start = find_cycle(E, i, new_match)  # start from any s, there should exist a cycle (the start may not be in the cycle)
            while True:  # exchange with valid edges (forward edges) in the cycle
                if i > 0:
                    result.append((i, -new_match[i]))
                    remove_T(H, V, H_T, V_T, T, -new_match[i])
                    match.pop(i)
                i = new_match[i]
                if i == start:
                    break
    return result

def shoot_the_turrets():
    C, R, M = map(int, raw_input().strip().split())
    G, S, T, T_inv = [], {}, {}, {}
    for r in xrange(R):
        G.append(raw_input().strip())
        for c in xrange(C):
            if G[r][c] == 'S':
                S[len(S)+1] = (r, c)
            elif G[r][c] == 'T':
                T[len(T)+1] = (r, c)
                T_inv[(r, c)] = len(T_inv)+1

    match = find_max_bipartite_matching(G, M, S, T, T_inv)
    if not match:
        return 0
    result = find_alternate_matching(G, M, S, T, T_inv, match)
    return "{}\n{}".format(len(result), "\n".join(map(lambda x: "{} {}".format(*x), result)))

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, shoot_the_turrets())
