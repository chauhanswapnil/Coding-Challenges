def solution(x,y):
    return x*3 if x*3 < y*2 else y*2

num_cases = int(input())
for case in range(1, num_cases + 1):
    x,y = [int(s) for s in input().split(" ")]
    ans = solution(x,y)
    print(ans)