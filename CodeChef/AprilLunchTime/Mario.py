def solution(x):
    if x % 3 == 1:
        return "HUGE"
    if x % 3 == 2:
        return "SMALL"
    if x % 3 == 0:
        return "NORMAL"

num_cases = int(input())
for case in range(1, num_cases + 1):
    x = int(input())
    ans = solution(x)
    print(ans)