def solution(a, n):
    pos = 0
    neg = 0
    for i in a:
        if i == 1:
            pos+=1
        else:
            neg+=1
    if abs(pos-neg) < 2:
        return "YES"
    elif abs(pos-neg) == 2 and pos%2==0 and neg%2==0:
        return "YES"
    else:
        return "NO"

num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    ans = solution(a,n)
    print(ans)