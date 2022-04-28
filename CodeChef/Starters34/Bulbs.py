def solution(n,x,arr):
    ans = n * x - sum(arr)
    if ans < n*x:
        return 0
    else:
        return ans

num_cases = int(input())
for case in range(1, num_cases + 1):
    n,x = [int(s) for s in input().split(" ")]
    arr = [int(s) for s in input().split(" ")]
    ans = solution(n,x,arr)
    print(ans)