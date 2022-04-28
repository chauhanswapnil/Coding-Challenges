def solution(t):
    return "YES" if (t>=1 and t<=4) else "NO"

num_cases = int(input())
for case in range(1, num_cases + 1):
    t = int(input())
    ans = solution(t)
    print(ans)