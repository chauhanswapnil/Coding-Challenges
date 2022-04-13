def pairwiseXor(n):
    if n%2 != 0:
        return -1
    if (n & (n-1) == 0) and n != 0:
        return -1
    else:
        c = n & ~(n-1)
        return (0, n//2, (n-c)//2 )


num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    ans = pairwiseXor(n)
    if ans == -1:
        print(-1)
    else:
        a,b,c = ans
        print(str(a) + " " + str(b) + " " + str(c))

# print(pairwiseXor(50))


def pairwiseXor(n):
    a = 0
    b = 10
    c = 8
    
    return (a^b) + (b^c) + (c^a)

print(pairwiseXor(50))