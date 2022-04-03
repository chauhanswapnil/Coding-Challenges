'''
CodeJam 2022 Qualification Round
d1000000

'''
def d1000000(N, D):
    j = 0
    k = 0
    for i in sorted(D):
        if i>j:
            k+=1 
            j+=1 
    return k

num_cases = int(input())
for case in range(1, num_cases + 1):
    N = input()
    D = [int(s) for s in input().split(" ")]
    ans = d1000000(N,D)
    print('Case #{}: {}'.format(case, str(ans)))



