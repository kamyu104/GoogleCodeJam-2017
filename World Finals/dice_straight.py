# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem A. Dice Straight
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/00000000002017fc
#
# Time:  O(N^2), pass in PyPy2 but Python2
# Space: O(N)
#

from collections import defaultdict

# Ford-Fulkerson Algorithm
# Time:  O(V * E)
# Space: O(V)
from functools import partial

class BipartiteMatching:
    def __init__(self, graph):
        self.graph = graph
        self.match = {}
        self.match_r = {}

    def augment(self, u):
        def divide(u):
            if u not in self.graph:
                return
            for v in self.graph[u]:
                if v not in self.match_r:  # early return
                    self.match[u] = v
                    self.match_r[v] = u
                    ret[0] = True
                    return
            stk.append(partial(conquer, u, iter(self.graph[u])))

        def conquer(u, it):
            for v in it:
                if v in lookup:
                    continue
                lookup.add(v)
                stk.append(partial(postprocess, u, v, it))
                stk.append(partial(divide, self.match_r[v]))
                return

        def postprocess(u, v, it):
            if not ret[0]:
                stk.append(partial(conquer, u, it))
                return
            self.match[u] = v
            self.match_r[v] = u

        ret, stk, lookup = [False], [], set()
        stk.append(partial(divide, u))
        while stk:
            stk.pop()()
        return ret[0]

def dice_straight():
    N = input()
    D = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    nums_set = set()
    graph = defaultdict(list)
    for i, dice in enumerate(D):
        for dij in dice:
            graph[dij].append(i)
            nums_set.add(dij)
    nums = sorted(nums_set)
    bipartite_matching = BipartiteMatching(graph)
    result, right = 0, -1
    for left in xrange(len(nums)):
        if (len(nums)-1)-left+1 <= result:  # early return
            break
        while right+1 != len(nums) and (right+1 == left or nums[right]+1 == nums[right+1]) and \
              bipartite_matching.augment(nums[right+1]):
            right += 1
        result = max(result, right-left+1)
        bipartite_matching.match_r.pop(bipartite_matching.match.pop(nums[left]))
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, dice_straight())
