def axnodrBrute(N):
    B = 1 
    for i in range(2,N+1):
        if i % 2 == 0:
            B = B ^ i
        else:
            B = B & i
    return B

print(axnodrBrute(69))


def axnodr(N):
    if N % 4 == 3 or N % 4 == 2:
        return 3
    elif N % 4 == 0:
        return 3+N
    else:
        return N
    
num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    ans = axnodr(N)
    print(ans)

print(axnodr(10000000000000000))
            