'''
1x1 -> True
2x2 -> True
3x3 -> False 
4x4 -> True
5x5 -> True

. . . . .
. . . . .
. . . . .
. . . . .
'''

def adaSchool(N,M):
    if (N*M) % 2 == 0:
        return "YES"
    else:
        return "NO"

num_cases = int(input())
for case in range(1, num_cases + 1):
    N, M = [int(s) for s in input().split(" ")]
    ans = adaSchool(N,M)
    print(ans)