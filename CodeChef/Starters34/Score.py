def solution(a,b,c,d):
    if c < a or d < b:
        return "Impossible"
    else:
        return "Possible"

num_cases = int(input())
for case in range(1, num_cases + 1):
    a,b = [int(s) for s in input().split(" ")]
    c,d = [int(s) for s in input().split(" ")]
    ans = solution(a,b,c,d)
    print(ans)