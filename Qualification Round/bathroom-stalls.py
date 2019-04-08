# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Qualification Round - Problem C. Bathroom Stalls
# https://code.google.com/codejam/contest/3264486/dashboard#s=p2
#
# Time:  O(logK)
# Space: O(1)
#

# 1. after the first person chooses the mid stall of the single row,
#    the stalls are split into left and right groups. 
#
# 2. by intuition, the following people would choose a stall from each group alternatively
#    and can always find a vacant block with non-increasing size. 
#    this could be easily proved by the mathematical induction, and we skip here.
# 
# 3. hence, we can check if the number of remaining people is odd or even
#    to find the last vacant block entered by the last person.
#
# 4. by conclusion, we can reduce the problem by the following rules:
#    - bathroom_stalls(2N+2, 2K+2) = bathroom_stalls(N+1, K+1)
#    - bathroom_stalls(2N+3, 2K+2) = bathroom_stalls(N+1, K+1)
#    - bathroom_stalls(2N+2, 2K+3) = bathroom_stalls(N,   K+1)
#    - bathroom_stalls(2N+3, 2K+3) = bathroom_stalls(N+1, K+1)
#    - bathroom_stalls(2N+2,    1) = (N+1, N)
#    - bathroom_stalls(2N+1,    1) = (N,   N)

def max_min(n):
    return ((n+1)//2, n//2)

def bathroom_stalls2():  # implemented by conclusion
    N, K = map(int, raw_input().strip().split())
    while K > 1:
        if N % 2 == 0 and K % 2 == 1:
            N -= 1
        N, K = N//2, K//2

    return max_min(N-1)

def bathroom_stalls():  # implemented by intuition
    N, K = map(int, raw_input().strip().split())
    while K > 1:
        M, m = max_min(N-1)
        K -= 1
        N, K = (M if K % 2 == 1 else m), (K+1)//2

    return max_min(N-1)

for case in xrange(input()):
    print 'Case #{}: {} {}'.format(case+1, *bathroom_stalls())
