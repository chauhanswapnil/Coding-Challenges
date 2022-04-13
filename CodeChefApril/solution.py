def solve(X,Y):
    if Y % X != 0:
        return Y // X
    else:
        return (Y//X)-1
    
num_cases = int(input())
for case in range(1, num_cases + 1):
    X,Y = [int(s) for s in input().split(" ")]
    ans = solve(X,Y)
    print(ans)

from math import gcd
def solve(a,b):
    # minn = 999999999
    # ai = -1
    # aj = -1
    # for i in range(a,b+1):
    #     for j in range(a,b+1):
    #         if i != j:
    #             g = gcd(i,j)
    #             if g>1 and (i+j)<minn:
    #                 minn = i+j
    #                 ai = i
    #                 aj = j
    # if ai == -1:
    #     return (-1,-1)
    # else:
    #     return (ai,aj)
    if a % 2 == 0:
        if a+2 > b:
            return (-1,-1)
        else:
            return (a,a+2)
    elif a%3 ==0:
        if a+3 > b:
            return (-1,-1)
        else:
            return (a,a+3)
    else:
        if a+3 > b:
            return (-1,-1)
        else:
            return (a+1,a+3)
            
num_cases = int(input())
for case in range(1, num_cases + 1):
    a,b = [int(s) for s in input().split(" ")]
    i,j = solve(a,b)
    if i == -1 or j == -1:
        print("-1")
    else:
        print(str(i) + " " + str(j))