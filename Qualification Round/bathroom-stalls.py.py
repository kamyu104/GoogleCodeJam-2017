# Time:  O(logK)
# Space: O(1)

def max_min(n):
    return ((n+1)//2, n//2)

def bathroom_stalls():
    N, K = map(int, raw_input().strip().split())
    while K > 1:
        M, m = max_min(N-1)
        K -= 1
        N = M if K % 2 else m
        K = (K+1)//2
            
    return max_min(N-1)

for case in xrange(input()):
    print 'Case #{}: {} {}'.format(case+1, *bathroom_stalls())
