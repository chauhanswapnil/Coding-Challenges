from math import gcd


def primeSum(a,b):
    # diff = abs(b-a)
    # if a == 1 or b == 1:
    #     return -1
    # # if (a%diff )
    # if (a%2==0 and b%2==0) or b%a==0 or a%b==0 or (a%3==0 and b%3==0) or(diff % 2 == 0):
    #     return 0
    # else:
    #     return 1
    
    if a == 1 or b == 1:
        return -1
    
    if gcd(a,b) == 1:
        return 1
    else:
        return 0
# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     a,b = [int(s) for s in input().split(" ")]
#     ans = primeSum(a,b)
#     print(ans)
            
print(primeSum(21,28))