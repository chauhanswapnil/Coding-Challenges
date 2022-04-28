def solution(x,y):
    fst = x * 10
    snd = y * 5
    if fst == snd:
        return "ANY"
    return "FIRST" if fst > snd else "SECOND"

num_cases = int(input())
for case in range(1, num_cases + 1):
    x,y = [int(s) for s in input().split(" ")]
    ans = solution(x,y)
    print(ans)