def solution(r,a,b):
    sa = 0
    k = 1
    while (r != 0):
        area = (22/7) * (r*r)
        sa += area
        if k % 2 == 0:
            r = r//b
        else:
            r = r * a
            print(r)
        k+=1
    return sa

num_cases = int(input())
for case in range(1, num_cases + 1):
    r,a,b = [int(s) for s in input().split(" ")]
    ans = str(solution(r,a,b))
    print('Case #{}: {}'.format(case, ans))