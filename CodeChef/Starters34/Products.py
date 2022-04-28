def solution(n,arr):
    cp=0
    cn=0
    for i in range(n):
        if arr[i] > 0:
            cp+=1
        if arr[i] < 0:
            cn+=1
    
    cpc = (cp * (cp-1)) // 2
    cpn = (cn * (cn-1)) // 2
    
    return cpc + cpn
    
num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    ans = solution(n,arr)
    print(ans)
    
print(solution(5,[0,-3,0,0,-1]))