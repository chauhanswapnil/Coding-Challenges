def solution(x, n):
    mistakes = 0
    for i in range(0,n-1):
        if x[i] > x[i+1]:
            mistakes +=1
        if i < n-2 and x[i] > x[i+2]:
            mistakes+=1
        if mistakes > 1:
            break
    if mistakes > 1:
        return "NO"
    else:
        return "YES"

num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    x = [int(s) for s in input().split(" ")]
    ans = solution(x,n)
    print(ans)