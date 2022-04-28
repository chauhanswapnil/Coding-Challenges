'''
https://www.codechef.com/problems/BSCOST

'''
def bscost(N,X,Y,B):
    cost = 0
    if "1" in B and "0" in B:
        if X > Y:
            cost = Y
        else:
            cost = X        
    return cost

num_cases = int(input())
for case in range(1, num_cases + 1):
    N, X, Y = [int(s) for s in input().split(" ")]
    B = input()
    ans = bscost(N,X,Y,B)
    print(str(ans))

