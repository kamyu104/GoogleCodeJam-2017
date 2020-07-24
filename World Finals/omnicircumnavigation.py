# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2017 Word Finals - Problem D. Omnicircumnavigation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/000000000020190a
#
# Time:  O(N^2), pass in PyPy2 but Python2
# Space: O(N)
#

def inner_product(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def outer_product(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def omnicircumnavigation():
    points = [tuple(map(int, raw_input().strip().split())) for _ in xrange(input())]
    p = []
    for i in xrange(len(points)):
        for j in xrange(i+1, len(points)):
            if outer_product(points[i], points[j]) == (0, 0, 0):  # colinear
                if inner_product(points[i], points[j]) < 0:  # angle between line [(0, 0), points[i]] and line [(0, 0), points[j]] is 180 degrees
                    return "YES"
                else:
                    break
        else:
            p.append(points[i])
    for i in xrange(len(p)):
        k = -1
        for j in xrange(len(p)):
            if j in (i, k):
                continue
            # rotate a plane with [(0, 0), p[i]] as the axis to cover each point,
            # if the points are inside the semi-sphere,
            # there should exist two plane boundaries and the angle between them is less than 180 degrees and all points are inside them
            if k == -1 or inner_product(outer_product(p[i], p[k]), p[j]) > 0:
                k = j  # find the leftmost point where the left plane boundary is
        for j in xrange(len(p)):
            if j in (i, k):
                continue
            coplanar = inner_product(outer_product(p[i], p[k]), p[j])
            if coplanar == 0:  # coplanar
                if inner_product(outer_product(p[i], p[k]), outer_product(p[i], p[j])) < 0:  # angle between plane [(0, 0), p[i], p[k]] and plane [(0, 0), p[i], p[k]] is 180 degrees
                    break
            elif coplanar > 0:  # the left plane boundary doesn't exist, thus the points are not inside the semisphere
                break
        else:
            return "NO"  # all points are inside the semisphere
    return "YES"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, omnicircumnavigation())
