def taxi(n,a):
    # a = set(a)
    for i in range(n):
        diff = abs(a[i] - a[i+1])
        if diff > 2:
            return len(a) + 1
    return len(a)
    

num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    ans = taxi(n,a)
    print(ans)