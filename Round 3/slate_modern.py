# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 3 - Problem D. Slate Modern
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201902/0000000000201903
#
# Time:  O(N^2)
# Space: O(N^2)
#

# divide submatrix into 4 parts, each part would be either a rectangle, triangle,
# ladder-shaped, or rectangle excluding triangle, generalized as follows:
#  +-------- c+1 --------+
#  |b...............b+D*c|
#  |.                   .|
#  |.            b+D*anti+
# r+1                  ./
#  |.          b+D*anti/
#  |.                ./
#  |b+D*r....b+D*anti/
#  +----------------+
def f(b, r, c, anti, D):
    def rectangle(b, r, c, D):
        return b*(r+1)*(c+1) + D*(r+c)*(r+1)*(c+1)//2

    def triangle(b, anti, D):
        return (b-D)*anti*(anti+1)//2 + D*anti*(anti+1)*(2*anti+1)//6

    r, c, anti = min(r, anti), min(c, anti), min(anti, r+c)
    return rectangle(b, r, c, D) - triangle(b+D*(r+c), (r+c)-anti, -D)

def coordinate_compression(R, C, D, fixeds):
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
    return rows, cols, [[[dp[i][j][0], dp[i+1][j][1], dp[i][j+1][2], dp[i+1][j+1][3]] for j in xrange(len(cols)-1)] for i in xrange(len(rows)-1)]

def slate_modern():
    R, C, N, D = map(int, raw_input().strip().split())
    fixeds = [map(int, raw_input().strip().split()) for i in xrange(N)]
    if any(abs(b1-b2) > D*(abs(r1-r2)+abs(c1-c2)) for r1, c1, b1 in fixeds for r2, c2, b2 in fixeds):
        return "IMPOSSIBLE"
    rows, cols, min_manhattan_dist_dp = coordinate_compression(R, C, D, fixeds)
    result = 0
    for i in xrange(len(rows)-1):
        for j in xrange(len(cols)-1):
            r0, c0, r1, c1 = rows[i], cols[j], rows[i+1], cols[j+1]
            m0, m1, m2, m3 = min_manhattan_dist_dp[i][j]  # tl, bl, tr, br
            min_r, max_r = r0, min(r1-1, (m1-m0)/(2*D))
            min_c, max_c = c0, min(c1-1, (m2-m0)/(2*D))
            min_anti, max_anti = r0+c0, min((r1-1)+(c1-1), (m3-m0)/(2*D))
            if (min_r <= max_r) and (min_c <= max_c) and (min_anti <= max_anti):
                # b0 = min(b + D*(r0-r + c0-c)) = min(b+D*(-r-c)) + D*(min_r+min_c)
                result = (result + f(m0+D*min_anti, max_r-min_r, max_c-min_c, max_anti-min_anti, D))%MOD
            min_r, max_r = max(r0, (m1-m0)/(2*D)+1), r1-1
            min_diag, max_diag = c0-(r1-1), min((c1-1)-r0, (m2-m1)/(2*D))
            min_c, max_c = c0, min(c1-1, (m3-m1)/(2*D))
            if (min_r <= max_r) and (min_c <= max_c) and (min_diag <= max_diag):
                # b1 = min(b + D*(r-(r1-1) + c0-c)) = min(b+D*(r-c)) + D*(-max_r+min_c)
                result = (result + f(m1+D*min_diag, max_r-min_r, max_c-min_c, max_diag-min_diag, D))%MOD
            min_c, max_c = max(c0, (m2-m0)/(2*D)+1), c1-1
            min_diag, max_diag = max(c0-(r1-1), (m2-m1)/(2*D)+1), (c1-1)-r0
            min_r, max_r = r0, min(r1-1, (m3-m2)/(2*D))
            if (min_r <= max_r) and (min_c <= max_c) and (min_diag <= max_diag):
                # b2 = min(b + D*(r0-r + c-(c1-1))) = min(b+D*(-r+c)) + D*(min_r-max_c)
                result = (result + f(m2+D*(-max_diag), max_r-min_r, max_c-min_c, max_diag-min_diag, D))%MOD
            min_anti, max_anti = max(r0+c0, (m3-m0)/(2*D)+1), (r1-1)+(c1-1)
            min_c, max_c = max(c0, (m3-m1)/(2*D)+1), c1-1
            min_r, max_r = max(r0, (m3-m2)/(2*D)+1), r1-1
            if (min_r <= max_r) and (min_c <= max_c) and (min_anti <= max_anti):
                # b3 = min(b + D*(r-(r1-1)+ c-(c1-1))) = min(b+D*(r+c)) + D*(-max_r-max_c)
                result = (result + f(m3+D*(-max_anti), max_r-min_r, max_c-min_c, max_anti-min_anti, D))%MOD
    return result

MOD = 10**9+7
DIRECTIONS = [lambda x: x, lambda x:reversed(x)]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, slate_modern())
