def solution(n,d,l):
    c0 = 0
    c1 = 0
    for i in l:
        if i == 0:
            c0+=1
        if i == 1:
            c1+=1
    if c1 > c0:
        ans = c0 + 1
    else:
        ans = c1 + 1        
    return ans


print (solution(6,2,[1,1,1,0,0,1]))
# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     n,d = [int(s) for s in input().split(" ")]
#     l = [int(s) for s in input().split(" ")]
#     ans = str(solution(n,d,l))
#     print('Case #{}: {}'.format(case, ans))