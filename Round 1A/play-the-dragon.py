# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Round 1A - Problem C. Play The Dragon
# https://code.google.com/codejam/contest/5304486/dashboard#s=p2
#
# Time:  O(sqrt(N))
# Space: O(1)
#

from math import ceil

# Hd - i * (Ak - d * D) >= 1
# 1. given d, find max of i s.t. i <= (Hd-1)/(Ak-d*D)
#    i = (Hd-1)//(Ak-d*D)
# 2. given i, find min of d s.t. d >= (i*Ak - (Hd-1))/(i*D)
#    d = ceil((i*Ak - (Hd-1))/(i*D)) = (i*Ak - Hd + 1 + i*D-1)//(i*D)
def possible_d_with_c_period(Hd, Ak, D):
    yield 0, (Hd-1)//Ak
    if D == 0:
        return
    cur_Hd, c, prev_Ak = Hd, 0, Ak
    prev_d, d = 0, 1
    while d < (Ak+D-1)//D:
        i = (Hd-1)//(Ak-d*D)
        if i == 0: # lose
            return
        yield d, i
        i += 1
        prev_d = d
        d = (i*Ak - Hd+1 + i*D-1)//(i*D)
        if d - prev_d > 1 and i == 2:
            return
    yield (Ak+D-1)//D, float("inf")

def cure_time_for_debuff_without_optimization(Hd, Ak, D, cur_Hd, pre_d, d, c_period):
    if d == 0 or c_period == float("inf"):
        return 0, cur_Hd
    c = 0
    while pre_d < d:
        pre_d += 1
        if cur_Hd - (Ak - pre_d * D) > 0:
            cur_Hd -= (Ak - pre_d * D)
        else:
            pre_d -= 1
            c += 1
            cur_Hd = Hd - (Ak - pre_d * D)
    return c, cur_Hd

def cure_turn_for_debuff(Hd, Ak, D, cur_Hd, pre_d, d, c_period):
    if d == 0 or c_period == float("inf"):
        return 0, cur_Hd

    # |x|period-1|period-1|period-1|y|

    # x part
    a = Ak - (pre_d+1) * D
    if cur_Hd - (Ak - (pre_d+1) * D) <= 0:
        x = pre_d
    elif D*D + 4*a*a + 4*a*D - 8*cur_Hd*D >= 0:
        x = min(d, int(ceil((2*Ak - D - (D*D + 4*a*a + 4*a*D - 8*cur_Hd*D) ** 0.5) / (2*D)) - 1))
        cur_Hd -= (a + Ak-x*D) * ((a - Ak+x*D)/D+1) / 2
        if x+1 <= d and cur_Hd - (Ak - (x+1) * D) > 0:  # adjust x for inaccuracy of big float number
            cur_Hd -= Ak - (x+1) * D
            x += 1
        if x == d:
            return 0, cur_Hd
    else:
        return 0, cur_Hd - (a + Ak-d*D) * ((a - Ak+d*D)/D+1) / 2

    # periodical part
    c, c_period, cur_Hd, y = 1, (Hd-1) // (Ak-x*D), Hd - (Ak-x*D), x
    if 2 <= c_period <= (d-x):
        c += (d-x-1-1)//(c_period-1)
        y += (d-x-1-1)//(c_period-1) * (c_period-1)
        if (d-x-1-1)//(c_period-1) > 0:
            cur_Hd = Hd - (Ak-y*D)
        
    # y part, at most c_period debuff, possibly required curing
    a = Ak - (y+1) * D
    if cur_Hd - (a + Ak-d*D) * ((a - Ak+d*D)/D+1) / 2 <= 0:
        c += 1
        cur_Hd = Hd - (Ak-(d-1)*D) - (Ak-d*D)
    else:
        cur_Hd -= (a + Ak-d*D) * ((a - Ak+d*D)/D+1) / 2
    return c, cur_Hd

def play_the_dragon():
    Hd, Ad, Hk, Ak, B, D = map(int, raw_input().strip().split())
    min_b_a = float("inf")
    i = 0
    while True:  # O(sqrt(N))
        turn = i + (Hk + (Ad + i*B)-1) // (Ad + i*B)
        if turn > min_b_a: break
        min_b_a = turn
        i += 1
    min_d_c_b_a = float("inf")
    c_for_d = 0
    pre_d, cur_Hd = 0, Hd
    for d, c_period in possible_d_with_c_period(Hd, Ak, D): # O(sqrt(N))
        cur_c_for_d, cur_Hd = cure_turn_for_debuff(Hd, Ak, D, cur_Hd, pre_d, d, c_period)
        c_for_d += cur_c_for_d
        c_for_min_b_a = 0
        # first cure and periodical cure
        # |(cur_Hd-1)//(Ak-d*D)| min_b_a-1 - (cur_Hd-1)//(Ak-d*    D)       | 1 |
        # |                    | c_period-1 | c_period-1 | ... | c_period-1 |   |
        #                                                         (no cure)
        if (Ak-d*D) > 0 and min_b_a-1 > (cur_Hd-1)//(Ak-d*D):
            if c_period <= 1:
                pre_d = d
                continue
            c_for_min_b_a = 1 + (min_b_a-1 - (cur_Hd-1)//(Ak-d*D) - 1)//(c_period-1)

        turn = d + c_for_d + min_b_a + c_for_min_b_a
        min_d_c_b_a = min(min_d_c_b_a, turn)
        pre_d = d
    return min_d_c_b_a if min_d_c_b_a != float("inf") else "IMPOSSIBLE"
     
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, play_the_dragon())
