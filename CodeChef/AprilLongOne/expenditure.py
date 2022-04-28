def party(n):
    c = n // 4
    if  n % 4 == 0:
        return c
    else:
        return c+1
    

num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    ans = str(party(n))
    print(ans)