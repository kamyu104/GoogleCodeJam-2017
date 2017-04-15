# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 1A - Problem A. Alphabet Cake
# https://code.google.com/codejam/contest/5304486/dashboard#s=p0
#
# Time:  O(R * C)
# Space: O(1)
#

def paint_non_empty_row(cake, r, c):
    for j in reversed(xrange(0, c)):
        if cake[r][j] == '?':
            cake[r][j] = cake[r][j+1]
        else:
            break
    for j in xrange(c+1, len(cake[r])):
        if cake[r][j] == '?':
            cake[r][j] = cake[r][j-1]
        else:
            break
    return

def paint_empty_row(cake, r, c):
    for i in reversed(xrange(0, r)):
        if cake[i][c] == '?':
            cake[i] = cake[i+1]
        else:
            break
    for i in xrange(r+1, len(cake)):
        if cake[i][c] == '?':
           cake[i] = cake[i-1]
        else:
            break
    return

def alphabet_cake():
    R, C = map(int, raw_input().strip().split())
    cake, initials = [], []
    for i in xrange(R):
        cake.append(list(raw_input().strip()))
        for j in xrange(C):
            if cake[i][j] != '?':
                initials.append((i, j))
    for p in initials:
        paint_non_empty_row(cake, *p)
    for p in initials:
        paint_empty_row(cake, *p)
    return cake

for case in xrange(input()):
    print 'Case #%d:' % (case+1)
    for row in alphabet_cake():
        print "".join(row)
