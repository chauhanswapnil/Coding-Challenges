def luckyNumberGame(n,a,b,l):    
    ca = 0
    cb = 0
    cc = 0
    for i in range(n):
        if l[i] % a == 0 and l[i] % b == 0:
            cc+=1
        if l[i] % a == 0:
            ca+=1
        if l[i] % b == 0:
            cb+=1
    if cb + min(cc,1) > ca:
        return "BOB"
    else:
        return "ALICE"
        
    
num_cases = int(input())
for case in range(1, num_cases + 1):
    n,a,b = [int(s) for s in input().split(" ")]
    l = [int(s) for s in input().split(" ")]
    ans = luckyNumberGame(n,a,b,l)
    print(ans)
    
# print(luckyNumberGame(3,2,4,[4,6,8]))