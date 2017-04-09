# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Qualification Round - Problem D. Fashion Show
# https://code.google.com/codejam/contest/3264486/dashboard#s=p3
#
# Time:  O(N^2)
# Space: O(N^2)
#

from collections import Counter, defaultdict
    
def add(style, i, j, val, row, col, diag, anti):
    row[style][i] += val
    col[style][j] += val
    diag[style][i-j] += val
    anti[style][i+j] += val

def update(old, style, i, j, row, col, diag, anti):
    add(old, i, j, -1, row, col, diag, anti)
    add(style, i, j, 1, row, col, diag, anti)
    
def is_valid(i, j, row, col, diag, anti):
    if row['o'][i] + row['x'][i] > 1 or \
       col['o'][j] + col['x'][j] > 1 or \
       diag['o'][i-j] + diag['+'][i-j] > 1 or \
       anti['o'][i+j] + anti['+'][i+j] > 1:
        return False
    return True

def fill_stage(stage, i, j, row, col, diag, anti, points, result):
    for style in ('o', '+', 'x'):
        if (stage[i][j] == '.') or \
           (stage[i][j] in ('+', 'x') and style == 'o'):
            old = stage[i][j]
            stage[i][j] = style
            points += 1 if stage[i][j] != 'o' else 2
            update(old, style, i, j, row, col, diag, anti)
            if is_valid(i, j, row, col, diag, anti):
                 result.append((style, i, j))
                 break
            update(style, old, i, j, row, col, diag, anti)
            points -= 1 if stage[i][j] != 'o' else 2
            stage[i][j] = old
    else:
        points += stage[i][j] != '.' if stage[i][j] != 'o' else 2
    return points

def fashion_show():
    N, M = map(int, raw_input().strip().split())
    stage = [['.' for _ in xrange(N)] for _ in xrange(N)]
    row, col = defaultdict(Counter), defaultdict(Counter)
    diag, anti = defaultdict(Counter), defaultdict(Counter)
    for _ in xrange(M):
        style, i, j = raw_input().strip().split()
        i, j = int(i)-1, int(j)-1
        stage[i][j] = style
        add(style, i, j, 1, row, col, diag, anti)
    
    points, result = 0, []
    left, right, top, bottom = 0, N-1, 0, N-1        
    while left <= right and top <= bottom: # spiral order
        for j in xrange(left, right + 1):
            points = fill_stage(stage, top, j, row, col, diag, anti, points, result)
        for i in xrange(top + 1, bottom):
            points = fill_stage(stage, i, right, row, col, diag, anti, points, result)
        for j in reversed(xrange(left, right + 1)):
            if top < bottom:
                points = fill_stage(stage, bottom, j, row, col, diag, anti, points, result)
        for i in reversed(xrange(top + 1, bottom)):
            if left < right:
                points = fill_stage(stage, i, left, row, col, diag, anti, points, result)
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return points, result
   
for case in xrange(input()):
    points, result = fashion_show()
    print 'Case #%d: %d %d' % (case+1, points, len(result))
    for style, i, j in result:
        print style, i+1, j+1
    
