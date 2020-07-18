# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem B. Operation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/000000000020184a
#
# Time:  O(11*2^11 * (N * D^2)), D is the max number of input digits
# Space: O(2^11 * (N * D))
#

from fractions import Fraction
from operator import add, sub, mul, div

def operation():
    S, C = map(int, raw_input().strip().split())
    adds, subs, mulps, mulzs, mulns, divps, divns = [[] for _ in xrange(7)]
    for i in xrange(C):
        op, v = raw_input().strip().split()
        v = int(v)
        if op == '-':
            v *= -1
            op = '+'
        if op == '+':
            if v > 0:
                adds.append(v)
            elif v < 0:
                subs.append(-v)
        elif op == '*':
            if v > 0:
                mulps.append(v)
            elif v < 0:
                mulns.append(v)
            else:
                mulzs.append(0)
        else:
            if v > 0:
                divps.append(v)
            elif v < 0:
                divns.append(v)
    ops = []
    if adds:
        ops.append(('+', sum(adds)))
    if subs:
        ops.append(('-', sum(subs)))
    if mulps:
        ops.append(('*', reduce(lambda x, y: x*y, mulps)))
    if mulzs:
        ops.append(('*', 0))
    if divps:
        ops.append(('/', reduce(lambda x, y: x*y, divps)))
    for _ in xrange(min(len(mulns), 2)):
        i = mulns.index(max(mulns))
        mulns[-1], mulns[i] = mulns[i], mulns[-1]
        ops.append(('*', mulns.pop()))
    if mulns:
        ops.append(('*', reduce(lambda x, y: x*y, mulns)))
    for _ in xrange(min(len(divns), 2)):
        i = divns.index(max(divns))
        divns[-1], divns[i] = divns[i], divns[-1]
        ops.append(('/', divns.pop()))
    if divns:
        ops.append(('/', reduce(lambda x, y: x*y, divns)))
    max_dp, min_dp = [float("-inf") for i in xrange(2**len(ops))], [float("inf") for i in xrange(2**len(ops))]
    max_dp[0], min_dp[0] = Fraction(S), Fraction(S)
    for i in xrange(1, len(max_dp)):
        mask = 1
        for op, v in ops:
            if i&mask:
                m, M = LOOKUP[op](max_dp[i^mask],v), LOOKUP[op](min_dp[i^mask],v)
                max_dp[i], min_dp[i] = max(max_dp[i], m, M), min(min_dp[i], m, M)
            mask <<= 1
    return "%s %s" % (max_dp[-1].numerator, max_dp[-1].denominator)

LOOKUP = {'+':add, '-':sub, '*':mul, '/':div}
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, operation())

