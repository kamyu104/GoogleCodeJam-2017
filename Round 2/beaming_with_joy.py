# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 2 - Problem C. Beaming with Joy
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/0000000000201876
#
# Time:  O(R * C)
# Space: O(R * C)
#

from sys import setrecursionlimit
from collections import defaultdict

# Template:
# https://github.com/kamyu104/GoogleCodeJam-2018/blob/master/World%20Finals/swordmaster.py
def strongly_connected_components(graph):  # Tarjan's Algorithm, Time: O(|V| + |E|), Space: O(|V|)
    def strongconnect(v, index_counter, index, lowlinks, stack, stack_set, result):
        index[v] = index_counter[0]
        lowlinks[v] = index_counter[0]
        index_counter[0] += 1
        stack_set.add(v)
        stack.append(v)
        for w in (graph[v] if v in graph else []):
            if w not in index:
                strongconnect(w, index_counter, index, lowlinks, stack, stack_set, result)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif w in stack_set:
                lowlinks[v] = min(lowlinks[v], index[w])
        if lowlinks[v] == index[v]:
            connected_component = []
            w = None
            while w != v:
                w = stack.pop()
                stack_set.remove(w)
                connected_component.append(w)
            result.append(tuple(connected_component))

    index_counter, index, lowlinks = [0], {}, {}
    stack, stack_set = [], set()
    result = []
    for v in graph:
        if v not in index:
            strongconnect(v, index_counter, index, lowlinks, stack, stack_set, result)
    return result

class TwoSat(object):
    def solve(self, __clauses):
        graph = defaultdict(list)
        for p, q in __clauses:
            graph[-p].append(q)
            graph[-q].append(p)
        sccs, assignments = strongly_connected_components(graph), set()
        for scc in sccs:
            scc_set = set(scc)
            if any(-v in scc_set for v in scc_set):
                break
        else:
            for scc in sccs:
                for v in scc:
                    if v not in assignments and -v not in assignments:
                        assignments.add(v)
        return assignments

class CNFEncoder(object):
    def __init__(self, cnf):
        self.__cnf = cnf
        self.__forward_map = {}
        self.__reverse_map = {}
        self.__clauses = []

    def add(self, o1, v1, o2, v2):
        self.__clauses.append((self.__encode(o1) * self.__sign(v1), self.__encode(o2) * self.__sign(v2)))
 
    def solve(self):
        return map(self.__decode, self.__cnf.solve(self.__clauses))

    def __encode(self, obj):
        if obj not in self.__forward_map:
            key = len(self.__forward_map)+1
            self.__forward_map[obj] = key
            self.__reverse_map[key] = obj
        return self.__forward_map[obj]

    def __decode(self, key):
        return self.__reverse_map[abs(key)], key > 0

    def __sign(self, val):
        return {True: 1, False: -1}[val]

def shoot(G, i, j, d):
    def dfs(G, i, j, di, dj, curr):
        ni, nj = i+di, j+dj
        if not (0 <= ni < len(G) and 0 <= nj < len(G[0])) or G[ni][nj] == '#':
            return curr
        elif G[ni][nj] == '.':
            curr.append((ni, nj))
            return dfs(G, ni, nj, di, dj, curr)
        elif G[ni][nj] == '/':
            return dfs(G, ni, nj, -dj, -di, curr)
        elif G[ni][nj] == '\\':
            return dfs(G, ni, nj, dj, di, curr)
        else:
            return None

    if d == '-':
        path_left, path_right = dfs(G, i, j, 0, -1, []), dfs(G, i, j, 0, 1, [])
        return None if path_right is None or path_left is None else path_right+path_left
    elif d == '|':
        path_up, path_down = dfs(G, i, j, -1, 0, []), dfs(G, i, j, 1, 0, [])
        return None if path_up is None or path_down is None else path_up+path_down

def beaming_with_joy():
    R, C = map(int, raw_input().strip().split())
    G = [list(raw_input().strip()) for _ in xrange(R)]
    shooters, empties = set(), {}
    for i, r in enumerate(G):
        for j, c in enumerate(r):
            if c in "-|":
                shooters.add((i, j))
            elif c == '.':
                empties[(i, j)] = []
    cnf = CNFEncoder(TwoSat())
    for s in shooters:
        choice_mask = 0
        for i, d in enumerate("-|", 1):
            path = shoot(G, s[0], s[1], d)
            if path is None:
                continue
            choice_mask |= i
            for cell in path:
                empties[cell].append((s, d))
        if not choice_mask:
            return "IMPOSSIBLE"
        elif choice_mask == 1:
            cnf.add(s, False, s, False)
        elif choice_mask == 2:
            cnf.add(s, True, s, True)
    for choices in empties.itervalues():
        if not choices:
            return "IMPOSSIBLE"
        elif len(choices) == 1:
            cnf.add(choices[0][0], choices[0][1] == '|', choices[0][0], choices[0][1] == '|')
            continue
        elif len(choices) == 2:
            cnf.add(choices[0][0], choices[0][1] == '|', choices[1][0], choices[1][1] == '|')
    result = cnf.solve()
    if not result:
        return "IMPOSSIBLE"
    for (i, j), is_vertical in result:
        G[i][j] = "-|"[is_vertical]
    return "POSSIBLE\n{}".format("\n".join(map(lambda x: "".join(x), G)))

MAX_R, MAX_C = 50, 50
BASE = 3
setrecursionlimit(BASE + (1+2*MAX_R*MAX_C))
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, beaming_with_joy())
