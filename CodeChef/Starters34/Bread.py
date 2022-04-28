def solution(a,b,c,d):
    if c < a or d < b:
        return "Yes"
    else:
        return "No"

num_cases = int(input())
for case in range(1, num_cases + 1):
    N, M, K = [int(s) for s in input().split(" ")]
    ans = solution(N,M,K)
    print(ans)