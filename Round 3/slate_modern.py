# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 3 - Problem D. Slate Modern
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201902/0000000000201903
#
# Time:  O(N^2)
# Space: O(N^2)
#

def formula(a, b, c, k):
    return a*k + b*k*(k-1)//2 + c*k*(k-1)*(2*k-1)//6

def formula_from_i_to_j(a, b, c, i, j):
    return formula(a, b, c, j)-formula(a, b, c, i) if i < j else 0

#  +-------- c+1 --------+
#  |b . . . . . . . b+D*c|
#  |.                .   |
#  |.                .   |
#  |.            b+D*anti+
# r+1               .   /
#  |.          b+D*anti/
#  |.             .   /
#  |b+D*r .  b+D*anti/
#  +----------------+
def f(b, r, c, anti, D):
    return formula_from_i_to_j((2*b+D*anti)*(anti+1), D-2*b, -D, max(0, (anti-r)+1), min(anti, c)+1)//2 + \
           formula_from_i_to_j(b*(r+1)+D*r*(r+1)//2, D*(r+1), 0, 0, min(c, anti-r)+1)

def slate_modern():
    R, C, N, D = map(int, raw_input().strip().split())
    fixeds = [map(int, raw_input().strip().split()) for i in xrange(N)]
    if any(abs(b1-b2) > D*(abs(r1-r2)+abs(c1-c2)) for r1, c1, b1 in fixeds for r2, c2, b2 in fixeds):
        return "IMPOSSIBLE"
    rows, cols = sorted(set([1, R+1]+[r for r, _, _ in fixeds])), sorted(set([1, C+1]+[c for _, c, _ in fixeds]))
    lookup_r, lookup_c = {x:i for i, x in enumerate(rows)}, {x:i for i, x in enumerate(cols)}
    dp = [[[float("inf")]*4 for _ in xrange(len(cols))] for _ in xrange(len(rows))]
    for r, c, b in fixeds:
        dp[lookup_r[r]][lookup_c[c]] = [b+D*(-r-c), b+D*(r-c), b+D*(-r+c), b+D*(r+c)]
    for d1, direction1 in enumerate(DIRECTIONS):
        for i in direction1(xrange(len(rows))):
            for d2, direction2 in enumerate(DIRECTIONS):
                for j in direction2(xrange(len(cols))):
                    if 0 <= i+2*d1-1 < len(rows):
                        dp[i][j][d2*2+d1] = min(dp[i][j][d2*2+d1], dp[i+2*d1-1][j][d2*2+d1])
                    if 0 <= j+2*d2-1 < len(cols):
                        dp[i][j][d2*2+d1] = min(dp[i][j][d2*2+d1], dp[i][j+2*d2-1][d2*2+d1])
    new_dp = [[[dp[i][j][0], dp[i+1][j][1], dp[i][j+1][2], dp[i+1][j+1][3]] for j in xrange(len(cols)-1)] for i in xrange(len(rows)-1)]
    result = 0
    for i in xrange(len(rows)-1):
        for j in xrange(len(cols)-1):
            r0, c0, r1, c1 = rows[i], cols[j], rows[i+1], cols[j+1]
            b0, b1, b2, b3 = new_dp[i][j]
            min_r, max_r = r0, min(r1-1, (b1-b0)/(2*D))
            min_c, max_c = c0, min(c1-1, (b2-b0)/(2*D))
            min_anti, max_anti = r0+c0, min(r1+c1-2, (b3-b0)/(2*D))
            if (min_r <= max_r) and (min_c <= max_c) and (min_anti <= max_anti):
                # assigned_b0 = min(b + D*(r0-r + c0-c)) = min(b+D*(-r-c)) + D*(min_r+min_c)
                result = (result + f(b0+D*(min_r+min_c), max_r-min_r, max_c-min_c, max_anti-(min_r+min_c), D))%MOD
            min_r, max_r = max(r0, (b1-b0)/(2*D)+1), r1-1
            min_diag, max_diag = c0-(r1-1), min((b2-b1)/(2*D), (c1-1)-r0)
            min_c, max_c = c0, min(c1-1, (b3-b1)/(2*D))
            if (min_r <= max_r) and (min_c <= max_c) and (min_diag <= max_diag):
                # assigned_b1 = min(b + D*(r-(r1-1) + c0-c)) = min(b+D*(r-c)) + D*(-max_r+min_c)
                result = (result + f(b1+D*(-max_r+min_c), max_r-min_r, max_c-min_c, max_diag-(-max_r+min_c), D))%MOD
            min_c, max_c = max(c0, (b2-b0)/(2*D)+1), c1-1
            min_diag, max_diag = max(c0-(r1-1), (b2-b1)/(2*D)+1), (c1-1)-r0
            min_r, max_r = r0, min(r1-1, (b3-b2)/(2*D))
            if (min_r <= max_r) and (min_c <= max_c) and (min_diag <= max_diag):
                # assigned_b2 = min(b + D*(r0-r + c-(c1-1))) = min(b+D*(-r+c)) + D*(min_r-max_c)
                result = (result + f(b2+D*(min_r-max_c), max_r-min_r, max_c-min_c, -(min_r-max_c)-min_diag, D))%MOD
            min_anti, max_anti = max(r0+c0, (b3-b0)/(2*D)+1), r1+c1-2
            min_c, max_c = max(c0, (b3-b1)/(2*D)+1), c1-1
            min_r, max_r = max(r0, (b3-b2)/(2*D)+1), r1-1
            if (min_r <= max_r) and (min_c <= max_c) and (min_anti <= max_anti):
                # assigned_b3 = min(b + D*(r-(r1-1)+ c-(c1-1))) = min(b+D*(r+c)) + D*(-max_r-max_c)
                result = (result + f(b3+D*(-max_r-max_c), max_r-min_r, max_c-min_c, -(-max_r-max_c)-min_anti, D))%MOD
    return result

DIRECTIONS = [lambda x: x, lambda x:reversed(x)]
MOD = 10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, slate_modern())
