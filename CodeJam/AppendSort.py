import math


def appendSort(N, L):
    count = 0
    prev = L[0]
    for i in range(1,N):
        curr = L[i]
        if prev >= curr:
            # We need to make curr bigger than previous
            if len(prev) == len(curr):
                curr = curr * 10 + 0
                count+=1
            else:
                k = len(prev) - len(curr)
                # new_curr = curr * math.pow(10,k)
                if prev < curr * math.pow(10,k):
                    prev = curr * math.pow(10,k)
                elif prev < curr * math.pow(10,):
                    

            last_digit = prev % 10
            if last_digit != 9:
                last_digit = last_digit + 1
            while prev >= curr:
                curr = curr * 10 + last_digit
                count+=1
        prev = curr
    return count

num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    L = [int(s) for s in input().split(" ")]
    ans = appendSort(N,L)
    print('Case #{}: {}'.format(case, str(ans)))
    
print(appendSort(3,[200,201,200]))

20, 199, 19