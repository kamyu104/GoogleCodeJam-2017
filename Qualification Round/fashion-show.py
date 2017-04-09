# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Qualification Round - Problem D. Fashion Show
# https://code.google.com/codejam/contest/3264486/dashboard#s=p3
#
# Time:  O(N^2)
# Space: O(N)
#

def fashion_show():
    N, M = map(int, raw_input().strip().split())
    stage, row, col, diag, anti = set(), set(), set(), set(), set()
    for _ in xrange(M):
        style, i, j = raw_input().strip().split()
        i, j = int(i), int(j)
        stage.add((i, j))
        if style != '+':
            row.add(i)
            col.add(j)
        if style != 'x':
            diag.add(i-j)
            anti.add(i+j)

    modles = []
    for i in xrange(1,N+1):
        for p in [(i,j) for j in xrange(i,N+1)]+[(j,i) for j in xrange(i+1,N+1)]:
            addTimes, addPlus = False, False
            if (p[0] not in row) and (p[1] not in col):
                addTimes = True
                row.add(p[0])
                col.add(p[1])
            if  (p[0]-p[1] not in diag) and (p[0]+p[1] not in anti):
                addPlus = True
                diag.add(p[0]-p[1])
                anti.add(p[0]+p[1])
            if (addTimes and addPlus) or ((addTimes or addPlus) and p in stage):
                modles.append(('o',p[0],p[1]))
            elif addTimes:
                modles.append(('x',p[0],p[1]))
            elif addPlus:
                modles.append(('+',p[0],p[1]))
    return len(row)+len(diag), modles
   
for case in xrange(input()):
    points, modles = fashion_show()
    print 'Case #%d: %d %d' % (case+1, points, len(modles))
    for style, i, j in modles:
        print style, i, j
    
