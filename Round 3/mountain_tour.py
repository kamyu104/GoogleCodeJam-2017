# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 3 - Problem C. Mountain Tour
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201902/0000000000201877
#
# Time:  O(C * log*(C))
# Space: O(C)
#

# Template:
# https://github.com/kamyu104/FacebookHackerCup-2019/blob/master/Final%20Round/temporal_revision.py
class UnionFind(object):  # Time: (N * log*(N)), Space: O(N)
    def __init__(self, n):
        self.set = range(n)

    def get_id(self):
        self.set.append(len(self.set))
        return len(self.set)-1

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression.
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True

def time_to_arrive(a, b):
    return (a+b)%24

def time_to_leave(a, b):
    return (b-a)%24

def mountain_tour():
    C = input()
    tours = map(lambda x: (x[0]-1, x[1], x[2]), [map(int, raw_input().strip().split()) for _ in xrange(2*C)])
    prev_camps = [[] for _ in xrange(C)]
    for i, (E, _, _) in enumerate(tours):
        prev_camps[E].append(i)
    result = sum(D for _, _, D in tours)
    next_camps, costs = [0]*(2*C), [0]*C
    for i, (prev_a, prev_b) in enumerate(prev_camps):
        (_, prev_a_l, prev_a_d), (_, prev_b_l, prev_b_d) = tours[prev_a], tours[prev_b]
        if not i:
            ta = min(time_to_leave(time_to_arrive(prev_a_l, prev_a_d), tours[2*i][1]) + tours[2*i+1][1],
                     time_to_leave(time_to_arrive(prev_b_l, prev_b_d), tours[2*i+1][1]) + tours[2*i][1])
            tb = min(time_to_leave(time_to_arrive(prev_a_l, prev_a_d), tours[2*i+1][1]) + tours[2*i][1],
                     time_to_leave(time_to_arrive(prev_b_l, prev_b_d), tours[2*i][1]) + tours[2*i+1][1])
        else:
            ta = time_to_leave(time_to_arrive(prev_a_l, prev_a_d), tours[2*i][1]) + \
                 time_to_leave(time_to_arrive(prev_b_l, prev_b_d), tours[2*i+1][1])
            tb = time_to_leave(time_to_arrive(prev_a_l, prev_a_d), tours[2*i+1][1]) + \
                 time_to_leave(time_to_arrive(prev_b_l, prev_b_d), tours[2*i][1])
            assert(abs(ta-tb) in (0, 24))
        if ta < tb:
            result += ta
            next_camps[prev_a], next_camps[prev_b] = 2*i, 2*i+1
            costs[i] = tb-ta
        else:
            result += tb
            next_camps[prev_a], next_camps[prev_b] = 2*i+1, 2*i
            costs[i] = ta-tb
    union_find = UnionFind(2*C)
    for i in xrange(2*C):
        union_find.union_set(i, next_camps[i])
    for i, c in enumerate(costs):
        if not c:  # first, union camps with 0 hr
            union_find.union_set(2*i, 2*i+1)
    # second, union camp1 if its tours are disjoint cycles, which has the smallest union costs in the rest of disjoint cycles
    # finally, union other camps which costs are all 24 hrs
    return result + sum(c for i, c in enumerate(costs) if union_find.union_set(2*i, 2*i+1))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, mountain_tour())
