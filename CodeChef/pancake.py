def pancake(n):
    return n//2 + 1

num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    ans = str(pancake(n))
    print(ans)