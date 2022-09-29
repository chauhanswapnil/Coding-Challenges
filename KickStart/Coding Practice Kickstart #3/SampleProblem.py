def solution(N,arr, M):
    totalCandies = sum(arr)
    return totalCandies - (totalCandies // M) * M

num_cases = int(input())
for case in range(1, num_cases + 1):    
    N, M = [int(s) for s in input().split(" ")]
    arr = [int(s) for s in input().split(" ")]
    ans = solution(N, arr, M)
    print('Case #{}: {}'.format(case, ans))