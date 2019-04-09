# Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Qualification Round - Problem C. Bathroom Stalls
# https://code.google.com/codejam/contest/3264486/dashboard#s=p2
#
# Time:  O(logK)
# Space: O(1)
#

# 1. by intuition, after the first person chooses the mid stall of the single row,
#    the remaining stalls are split into left and right groups.
#    the following people would choose a stall from each group alternatively
#    and can always find a vacant block with non-increasing size. 
#    this could be easily proved by the mathematical induction, and we skip here.
#
# 2. another way is to think a stall as a node in balanced binary search tree, 
#    where the number of nodes in left subtree of each node is at most 1 more than
#    the number of right subtree of that node.
#    people visit the root of the balanced BST first and then visit the left and right subtree of the root alternatively
#    and can always find a subtree with non-increasing number of nodes in this rule.
#    the answer is the number of nodes in left and right subtree of the last visited node.
#
# 3. hence, we can check if the number of the remaining people is odd or even
#    to find the last vacant block or subtree entered by the last person.
#    
# 4. by conclusion, we can reduce the problem by the following rules (N >= 0, K >= 0): 
#    - bathroom_stalls(2N+2, 2K+2) = bathroom_stalls(N+1, K+1)
#    - bathroom_stalls(2N+3, 2K+2) = bathroom_stalls(N+1, K+1)
#    - bathroom_stalls(2N+2, 2K+3) = bathroom_stalls(N,   K+1)
#    - bathroom_stalls(2N+3, 2K+3) = bathroom_stalls(N+1, K+1)
#    - bathroom_stalls(2N+2,    1) = (N+1, N)
#    - bathroom_stalls(2N+1,    1) = (N,   N)

def bigger_smaller(n):
    return ((n+1)//2, n//2)

def bathroom_stalls3():  # simplified by bit operation of bathroom_stalls2
    N, K = map(int, raw_input().strip().split())
    return bigger_smaller((N-K) // 2**(K.bit_length()-1))

def bathroom_stalls2():  # implemented by conclusion
    N, K = map(int, raw_input().strip().split())
    while K > 1:  # K.bit_length()-1 times
        if N % 2 == 0 and K % 2 == 1:  # it's like bit operation of N-K, could be simplified to bathroom_stalls3
            N -= 1
        N, K = N//2, K//2

    return bigger_smaller(N-1)

def bathroom_stalls():  # implemented by intuition
    N, K = map(int, raw_input().strip().split())
    while K > 1:
        bigger_N, smaller_N = bigger_smaller(N-1)
        bigger_K, smaller_K = bigger_smaller(K-1)
        N, K = (bigger_N, bigger_K) if (K-1) % 2 == 1 else (smaller_N, smaller_K)

    return bigger_smaller(N-1)

for case in xrange(input()):
    print 'Case #{}: {} {}'.format(case+1, *bathroom_stalls3())
