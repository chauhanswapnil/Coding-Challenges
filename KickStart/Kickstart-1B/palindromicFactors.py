from functools import reduce

def solution(n):    
    count = 0
    facts = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
    for f in facts:
        if str(f) == str(f)[::-1]:
            count +=1
    
    return count

num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    ans = str(solution(n))
    print('Case #{}: {}'.format(case, ans))

