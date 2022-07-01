def maxBalancedSubStrings(L,R):
    if L == 0 or R == 0:
        return 0
    if L == 1 or R == 1:
        return 1
    return min(L,R) + 1

num_cases = int(input())
for case in range(1, num_cases + 1):
    L, R = [int(s) for s in input().split(" ")]
    ans = maxBalancedSubStrings(L,R)
    print('Case #{}: {}'.format(case, ans))
    
    
    (((()))