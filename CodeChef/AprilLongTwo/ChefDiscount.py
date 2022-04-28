def solution(x):
    return 100 if int(x*0.1) < 100 else int(x*0.1)

num_cases = int(input())
for case in range(1, num_cases + 1):
    x = int(input())
    ans = solution(x)
    print(ans)