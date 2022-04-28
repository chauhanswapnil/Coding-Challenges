def solution(a, n):
    return n

num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    ans = solution(a,n)
    print(ans)