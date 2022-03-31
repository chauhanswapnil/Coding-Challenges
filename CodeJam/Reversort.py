'''
Reversort
Google CodeJam 2021 Qualifying Round

'''

def reversort(L):
    cost = 0
    for i in range(0, len(L)-1):
        j = L.index(min(L[i:len(L)+1]))
        L[i:j+1] = reversed(L[i:j+1])
        cost += (j-i+1)
    return cost
    
    
num_cases = int(input())
for case in range(1, num_cases + 1):
    N = input()
    L = [int(s) for s in input().split(" ")]
    ans = reversort(L)
    print('Case #{}: {}'.format(case, str(ans)))